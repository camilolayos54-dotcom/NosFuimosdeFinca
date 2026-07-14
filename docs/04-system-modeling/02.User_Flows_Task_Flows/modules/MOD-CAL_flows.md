# User Flows: MOD-CAL (Calendario y Disponibilidad)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-CAL
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Basado en los requerimientos de la Fase 3, evaluamos cómo los conceptos de "Soft-Lock" y "Hard-Lock" se traducen en acciones humanas en el Frontend.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Bloqueo Manual de Fechas (B2B)** | **Task Flow** | El Finquero selecciona fechas y oprime "Bloquear". Es un flujo lineal de administración sin decisiones sistémicas complejas. | Finquero |
| **Selección de Fechas B2C (Soft-Lock)** | **User Flow** | El Turista elige fechas. El sistema debe evaluar disponibilidad real (evitando Double-Booking) y asegurar el "Soft-Lock" por 90 min. | Turista |

---

## 2. Screen Mapping (Cruce Topológico)

Mapeo de los flujos contra los Nodos del Sitemap (D1).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Bloqueo Manual B2B** | `/dashboard/calendario` | **Toast Notification:** "Fechas Bloqueadas Exitosamente". |
| **Selección Soft-Lock B2C** | `/finca/[slug]` -> `/checkout/[id]` | **Modal/Alert:** "Fechas ocupadas temporalmente por otro usuario". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. Task Flow: Bloqueo Manual de Calendario (Finquero)
El camino administrativo donde el dueño decide cerrar su finca para mantenimiento o uso personal. Es lineal y ocurre completamente dentro del Hub Protegido.

```mermaid
flowchart TD
    %% Nodos UI
    DashboardUI[Tablero Calendario B2B<br>Ruta: /dashboard/calendario]
    ConfirmModalUI[Modal de Confirmación<br>'¿Desea bloquear estos días?']
    ToastUI[Toast Success<br>'Días Bloqueados']
    
    %% Nodos Asíncronos
    DB((PostgreSQL DB<br>Estado: HARD_LOCK))
    
    %% Flujo Administrativo
    DashboardUI --> |Selecciona Fechas| ConfirmModalUI
    ConfirmModalUI --> |Clic 'Bloquear'| DB
    
    DB -.-> ToastUI
    ToastUI --> DashboardUI
```

### 3.2. User Flow: Selección de Fechas y Soft-Lock (Turista)
El flujo crítico Anti-Overbooking. El turista no puede simplemente "elegir" una fecha; el sistema debe asegurar (Locking) los días exclusivamente para él en la base de datos antes de permitirle ir a la pasarela de pagos.

```mermaid
flowchart TD
    %% Nodos UI
    FincaUI[Perfil Público de Finca<br>Ruta: /finca/slug]
    WidgetUI[Widget Selector Fechas<br>Componente Anidado]
    CheckoutUI[Wizard de Reserva<br>Ruta: /checkout/id]
    ErrorToastUI[Componente Error<br>Fechas No Disponibles]
    
    %% Nodos Asíncronos
    DB((PostgreSQL DB<br>Validación Transaccional))
    LockCron((Redis / CronJob<br>Timer de 90 Min))
    
    %% Decisiones
    AvailabilityCheck{¿Las fechas<br>están libres?}

    %% Flujo Turista
    FincaUI --> WidgetUI
    WidgetUI --> |Elige Check-in/out<br>Clic 'Reservar'| DB
    
    %% Respuesta Backend
    DB -.-> AvailabilityCheck
    
    %% Unhappy Path (Alguien le ganó la reserva milisegundos antes)
    AvailabilityCheck -- No (Ocupado) --> ErrorToastUI
    ErrorToastUI --> FincaUI
    
    %% Happy Path (Se otorgan los 90 minutos)
    AvailabilityCheck -- Sí (Libre) --> |Inicia SOFT_LOCK| LockCron
    LockCron -.-> |Genera ID| CheckoutUI
```
