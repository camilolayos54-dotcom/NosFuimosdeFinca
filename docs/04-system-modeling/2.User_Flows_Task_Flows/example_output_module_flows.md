# User Flows: MOD-RSV (Reservas)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-RSV
**Status:** Approved

---

## 1. Flow Inventory

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Descripción UX | Actor Principal |
| :--- | :--- | :--- | :--- |
| **UC-RSV-01: Wizard de Checkout** | User Flow | Camino largo desde que elige fechas hasta que paga con Wompi o sufre un Timeout. | Turista |
| **UC-RSV-02: Aprobar Reserva B2B** | Task Flow | Acción rápida del Finquero al aceptar un huésped en su panel. | Finquero |

---

## 2. Screen Mapping & Flow Modeling

### 2.1. User Flow 1: El Camino Crítico del Checkout (Turista)
**Trigger:** Turista selecciona fechas disponibles en el Widget del Perfil de Finca e inicia el checkout.
**Pantallas (Nodos D1):** `/finca/[slug]` -> `/checkout/[id]` -> `/checkout/processing` -> `Wompi Gateway` -> `/checkout/success`.

```mermaid
flowchart TD
    %% Nodos UI
    Start(Perfil Finca:<br>Selecciona Fechas)
    CheckoutUI[Pantalla Wizard Checkout<br>Ingresa Email y Subtotal]
    Spinner[Pantalla Transaccional<br>/checkout/processing]
    Wompi((Pasarela Externa<br>Wompi))
    Success[Pantalla Éxito<br>Muestra Recibo]
    Timeout[Pantalla Error 410<br>Tiempo Expirado]
    
    %% Decisiones
    LockCheck{¿Soft-Lock<br>Aprobado?}
    TimeCheck{¿Tardó más de<br>90 Minutos?}
    PayCheck{¿Pago Wompi<br>Aprobado?}

    %% Flujo
    Start --> LockCheck
    LockCheck -- No (Ocupado) --> Start
    LockCheck -- Sí --> CheckoutUI
    CheckoutUI --> TimeCheck
    
    TimeCheck -- Sí --> Timeout
    Timeout --> Start
    
    TimeCheck -- No --> Spinner
    Spinner --> Wompi
    
    Wompi --> PayCheck
    PayCheck -- No (Rechazado) --> CheckoutUI
    PayCheck -- Sí (Aprobado) --> Success
```

### 2.2. Task Flow 1: Aprobación B2B (Finquero)
**Trigger:** El Finquero revisa su lista de reservas entrantes y decide aprobar a un grupo.
**Pantallas (Nodos D1):** `/dashboard/reservas`.

```mermaid
flowchart TD
    %% Nodos UI
    Dashboard(Panel de Reservas B2B<br>/dashboard/reservas)
    ModalConfirm[Modal de Confirmación<br>'¿Seguro que aprueba?']
    ToastSuccess[Notificación Toast<br>Reserva Aprobada]
    
    %% Flujo Lineal (Task Flow)
    Dashboard --> |Click 'Aprobar'| ModalConfirm
    ModalConfirm --> |Click 'Confirmar'| ToastSuccess
    ToastSuccess --> Dashboard
```
