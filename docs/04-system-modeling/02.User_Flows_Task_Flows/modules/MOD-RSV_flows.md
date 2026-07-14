# User Flows: MOD-RSV (Gestion de Reservas)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-RSV
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Este modulo controla la columna vertebral del negocio: la intencion de compra del Turista y la aprobacion o rechazo del Finquero.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Wizard de Checkout (Cotizacion a Pago)** | **User Flow** | Extremadamente complejo. Cruza multiples estados: Resumen de Precios -> Carga de Huespedes -> Reglas Legales -> Delegacion a Wompi. | Turista |
| **Aprobar / Rechazar Reserva Entrante** | **Task Flow** | El Finquero visualiza la solicitud entrante y oprime "Aprobar" o "Rechazar" con una razon. Flujo lineal con validacion simple. | Finquero |

---

## 2. Screen Mapping (Cruce Topologico)

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Checkout Wizard** | `/checkout/[id]` | **Alert UI:** Timeout "Te quedan 15 minutos para pagar". |
| **Revision B2B** | `/dashboard/reservas` -> `/dashboard/reservas/[id]` | **Modal Confirmacion:** " Seguro que rechazas esta reserva?". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Wizard de Checkout (El Camino del Comprador)
Este flujo exige que el Frontend actue como un embudo (Wizard). El Turista no puede llegar al boton de pago de Wompi sin antes haber aceptado los Terminos Legales.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutInitUI[Resumen de Cotizacion<br>Ruta: /checkout/id]
    GuestFormUI[Formulario Huespedes<br>Componente Wizard]
    LegalTermsUI[Check de Terminos y Condiciones<br>Modal o Checkbox]
    WompiRedirectUI[Pantalla de Transicion<br>Ruta: /checkout/processing]
    
    %% Nodos Asincronos
    PricingDB((PostgreSQL DB<br>Calculo de Service Fee))
    WompiAPI((MOD-PAY<br>Motor Wompi))
    TimeoutCron((CronJob 90 min<br>Soft-Lock Timeout))
    
    %% Decisiones
    LegalCheck{ Acepto<br>las reglas?}
    TimeCheck{ Expiro<br>el tiempo?}

    %% Flujo Turista
    CheckoutInitUI --> |Solicita Precio Final| PricingDB
    PricingDB -.-> |Subtotal + Fee| GuestFormUI
    
    GuestFormUI --> LegalTermsUI
    LegalTermsUI --> LegalCheck
    
    LegalCheck -- No --> |Boton Deshabilitado| LegalTermsUI
    
    %% Condicion de Tiempo Real
    LegalCheck -- Si --> TimeCheck
    TimeCheck -- Si (Pasaron 90 min) --> ErrorToastUI[Toast Error<br>Tu sesion expiro]
    ErrorToastUI --> |Redireccion Forzada| CancelReturnUI[Perfil Finca<br>Ruta: /finca/slug]
    
    %% Camino Seguro a Pago
    TimeCheck -- No --> |Clic 'Pagar'| WompiRedirectUI
    WompiRedirectUI --> WompiAPI
    
    %% Timeout Cron Async (Invisible)
    TimeoutCron -.-> TimeCheck
```

### 3.2. Task Flow: Aprobacion / Rechazo B2B (Finquero)
El Finquero revisa quien se va a hospedar en su casa antes de aceptar la reserva (y el dinero).

```mermaid
flowchart TD
    %% Nodos UI
    InboxUI[Buzon de Reservas<br>Ruta: /dashboard/reservas]
    ResDetailUI[Detalle de Reserva<br>Ruta: /dashboard/reservas/id]
    RejectModalUI[Modal de Rechazo<br>Select: Razon de rechazo]
    SuccessToastUI[Toast Success<br>Accion Completada]
    
    %% Nodos Asincronos
    DB((PostgreSQL DB<br>Mutacion de Estado))
    EmailWorker((Notificador MOD-NOT<br>Avisa al Turista))
    
    %% Decisiones
    ApproveCheck{ Aprobar o<br>Rechazar?}

    %% Flujo Administrativo
    InboxUI --> |Clic en Fila| ResDetailUI
    ResDetailUI --> ApproveCheck
    
    %% Camino Triste (Rechazo)
    ApproveCheck -- Rechazar --> RejectModalUI
    RejectModalUI --> |Confirma Rechazo| DB
    DB -.-> |Dispara Email de Disculpa| EmailWorker
    
    %% Camino Feliz (Aprobacion)
    ApproveCheck -- Aprobar --> |Cambia a CONFIRMED| DB
    DB -.-> |Dispara Email de Bienvenida| EmailWorker
    
    %% Final
    EmailWorker -.-> SuccessToastUI
    SuccessToastUI --> InboxUI
```
