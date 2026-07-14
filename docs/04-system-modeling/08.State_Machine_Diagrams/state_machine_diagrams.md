 # Entregable 8 (D8): State Machine Diagrams

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Alcance:** Global (Reservas, Propiedades, Pagos, Desembolsos)
**Estado:** Aprobado

---

## 1. Bookings (Reservas) State Machine

*Backlink a Fase 3:* Implementa las reglas de negocio estrictas de `[[PHASE_3_REQUIREMENTS_ENGINEERING/8.Business_Rules_and_Constraints.md]]` (especificamente la ventana de 15 min de pago y la ventana de 90 min de aprobacion B2B via WhatsApp).
*Construido a partir del ERD (D6).*

```mermaid
stateDiagram-v2
    [*] --> PENDING_PAYMENT : Checkout Iniciado

    PENDING_PAYMENT --> PENDING_APPROVAL : Webhook Wompi(Approve) [payment.amt == total_price] / CreateSoftLock(), SendWARequest()
    PENDING_PAYMENT --> CANCELLED : Cron(Timeout) [> 15 mins] / ReleaseLock()
    PENDING_PAYMENT --> CANCELLED : Webhook Wompi(Decline)

    PENDING_APPROVAL --> CONFIRMED : WA API(Approve) [< 90 mins] / CommitHardLock(), NotifyGuest()
    PENDING_APPROVAL --> CANCELLED : WA API(Reject) / ReleaseSoftLock(), TriggerRefund()
    PENDING_APPROVAL --> CANCELLED : Cron(Timeout) [> 90 mins] / ReleaseSoftLock(), TriggerRefund()

    CONFIRMED --> COMPLETED : System.Timer [now >= check_in] / GeneratePayout()
    CONFIRMED --> CANCELLED : API.Cancel(Reason) [valid_policy] / Refund()

    COMPLETED --> [*]
    CANCELLED --> [*]
```

---

## 2. Payouts (Desembolsos) State Machine

Maquina de estado financiera que gestiona el envio de fondos (menos la comision de plataforma) a la cuenta bancaria del Finquero.

```mermaid
stateDiagram-v2
    [*] --> PENDING : Booking.COMPLETED [bank_account != null]

    PENDING --> PROCESSING : Cron(Facturacion Diaria)
    
    PROCESSING --> PAID : BankAPI(Success) / SendHostAlert(Push)
    PROCESSING --> FAILED : BankAPI(Error) / SendHostAlert(WA)
    
    FAILED --> PROCESSING : User(UpdateBankAccount)
    
    PAID --> [*]
```

---

## 3. Payments (Pagos Entrantes) State Machine

Gestion del dinero que entra desde el turista via tarjeta de credito / PSE.

```mermaid
stateDiagram-v2
    [*] --> PENDING : Redirect to Wompi
    
    PENDING --> PAID : Webhook(Transaction.Approved)
    PENDING --> FAILED : Webhook(Transaction.Declined)
    
    PAID --> REFUNDED : Booking.CANCELLED [RefundPolicy==True] / Wompi.Void()
    
    FAILED --> [*]
    REFUNDED --> [*]
```

---

## 4. Properties (Inmuebles) State Machine

Ciclo de curaduria (KYC) antes de que una Finca pueda aparecer en el buscador publico.

```mermaid
stateDiagram-v2
    [*] --> DRAFT : Create Property
    
    DRAFT --> PENDING_REVIEW : Click(Publish) [fotos >= 5 & reglas_completas] / NotifyAdmin()
    
    PENDING_REVIEW --> PUBLISHED : Admin(Approve) / TriggerSEORevalidation()
    PENDING_REVIEW --> DRAFT : Admin(Reject) / NotifyHost(Reason)
    
    PUBLISHED --> SUSPENDED : Admin(Suspend) / HideFromSearch()
    SUSPENDED --> PUBLISHED : Admin(Reactivate) / TriggerSEORevalidation()
    
    PUBLISHED --> [*] : Soft Delete (is_active = false)
```

---

## Implicacion de Fase
- **D9 (API Conceptual Design):** Los endpoints mutacionales (ej. `PATCH /bookings/approve`) deben validar los *Guards* aqui documentados antes de ejecutar el cambio.
- **D10 (Notification Matrix):** Las *Actions* de estas maquinas de estado (ej. `SendWARequest()`, `NotifyAdmin()`) se consolidaran en la matriz final de notificaciones.

