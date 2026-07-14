# User Flows: MOD-RSV (Gestión de Reservas)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-RSV
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Este módulo controla la columna vertebral del negocio: la intención de compra del Turista y la aprobación o rechazo del Finquero.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Wizard de Checkout (Cotización a Pago)** | **User Flow** | Extremadamente complejo. Cruza múltiples estados: Resumen de Precios -> Carga de Huéspedes -> Reglas Legales -> Delegación a Wompi. | Turista |
| **Aprobar / Rechazar Reserva Entrante** | **Task Flow** | El Finquero visualiza la solicitud entrante y oprime "Aprobar" o "Rechazar" con una razón. Flujo lineal con validación simple. | Finquero |

---

## 2. Screen Mapping (Cruce Topológico)

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Checkout Wizard** | `/checkout/[id]` | **Alert UI:** Timeout "Te quedan 15 minutos para pagar". |
| **Revisión B2B** | `/dashboard/reservas` -> `/dashboard/reservas/[id]` | **Modal Confirmación:** "¿Seguro que rechazas esta reserva?". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Wizard de Checkout (El Camino del Comprador)
Este flujo exige que el Frontend actúe como un embudo (Wizard). El Turista no puede llegar al botón de pago de Wompi sin antes haber aceptado los Términos Legales.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutInitUI[Resumen de Cotización<br>Ruta: /checkout/id]
    GuestFormUI[Formulario Huéspedes<br>Componente Wizard]
    LegalTermsUI[Check de Términos y Condiciones<br>Modal o Checkbox]
    WompiRedirectUI[Pantalla de Transición<br>Ruta: /checkout/processing]
    
    %% Nodos Asíncronos
    PricingDB((Supabase DB<br>Cálculo de Service Fee))
    WompiAPI((MOD-PAY<br>Motor Wompi))
    TimeoutCron((CronJob 90 min<br>Soft-Lock Timeout))
    
    %% Decisiones
    LegalCheck{¿Aceptó<br>las reglas?}
    TimeCheck{¿Expiró<br>el tiempo?}

    %% Flujo Turista
    CheckoutInitUI --> |Solicita Precio Final| PricingDB
    PricingDB -.-> |Subtotal + Fee| GuestFormUI
    
    GuestFormUI --> LegalTermsUI
    LegalTermsUI --> LegalCheck
    
    LegalCheck -- No --> |Botón Deshabilitado| LegalTermsUI
    
    %% Condición de Tiempo Real
    LegalCheck -- Sí --> TimeCheck
    TimeCheck -- Sí (Pasaron 90 min) --> ErrorToastUI[Toast Error<br>Tu sesión expiró]
    ErrorToastUI --> |Redirección Forzada| CancelReturnUI[Perfil Finca<br>Ruta: /finca/slug]
    
    %% Camino Seguro a Pago
    TimeCheck -- No --> |Clic 'Pagar'| WompiRedirectUI
    WompiRedirectUI --> WompiAPI
    
    %% Timeout Cron Async (Invisible)
    TimeoutCron -.-> TimeCheck
```

### 3.2. Task Flow: Aprobación / Rechazo B2B (Finquero)
El Finquero revisa quién se va a hospedar en su casa antes de aceptar la reserva (y el dinero).

```mermaid
flowchart TD
    %% Nodos UI
    InboxUI[Buzón de Reservas<br>Ruta: /dashboard/reservas]
    ResDetailUI[Detalle de Reserva<br>Ruta: /dashboard/reservas/id]
    RejectModalUI[Modal de Rechazo<br>Select: Razón de rechazo]
    SuccessToastUI[Toast Success<br>Acción Completada]
    
    %% Nodos Asíncronos
    DB((Supabase DB<br>Mutación de Estado))
    EmailWorker((Notificador MOD-NOT<br>Avisa al Turista))
    
    %% Decisiones
    ApproveCheck{¿Aprobar o<br>Rechazar?}

    %% Flujo Administrativo
    InboxUI --> |Clic en Fila| ResDetailUI
    ResDetailUI --> ApproveCheck
    
    %% Camino Triste (Rechazo)
    ApproveCheck -- Rechazar --> RejectModalUI
    RejectModalUI --> |Confirma Rechazo| DB
    DB -.-> |Dispara Email de Disculpa| EmailWorker
    
    %% Camino Feliz (Aprobación)
    ApproveCheck -- Aprobar --> |Cambia a CONFIRMED| DB
    DB -.-> |Dispara Email de Bienvenida| EmailWorker
    
    %% Final
    EmailWorker -.-> SuccessToastUI
    SuccessToastUI --> InboxUI
```
