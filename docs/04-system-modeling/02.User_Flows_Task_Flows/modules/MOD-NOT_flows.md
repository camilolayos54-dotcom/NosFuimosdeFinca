# User Flows: MOD-NOT (Notificaciones y Alertas Asincronas)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-NOT
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Extraemos las formas en que el Sistema interrumpe o informa al usuario sobre eventos que sucedieron en segundo plano (WebSockets) o mientras no estaba logueado.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **In-App Notification Center** | **Task Flow** | El usuario abre la "campanita", lee sus alertas historicas y las marca como leidas. Es un flujo lineal de lectura. | Finquero / Agencia |
| **Toast de Tiempo Real (WebSocket)** | **User Flow** | Un evento externo asincrono (Ej. "Turista pago la reserva") empuja un Toast UI a la pantalla del Finquero de la nada, con un boton de accion rapida para redirigirlo a los detalles. | Finquero / Agencia |

---

## 2. Screen Mapping (Cruce Topologico)

Las notificaciones son componentes "Flotantes" que no tienen una URL propia, pero pueden dispararse en cualquier parte del ecosistema protegido B2B.

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Centro de Notificaciones** | Barra de Navegacion B2B (`/dashboard/*`) | **Dropdown View:** Se despliega un panel sobre la pantalla actual. |
| **Toast en Tiempo Real** | Global B2B (Cualquier ruta) | **Componente Toast:** Desaparece a los 5 segundos (Auto-hide). |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. Task Flow: Buzon Historico (Centro de Notificaciones)
El usuario entra activamente a revisar que paso mientras no estaba conectado a la aplicacion.

```mermaid
flowchart TD
    %% Nodos UI
    NavbarUI[Barra Superior B2B<br>Icono de Campana]
    DropdownUI[Panel Desplegable<br>Lista de Notificaciones]
    EmptyStateUI[Estado Vacio<br>'Estas al dia']
    DetailUI[Pantalla de Detalles<br>Ruta Destino Especifica]
    
    %% Nodos Asincronos
    DB((PostgreSQL DB<br>Consultar Historial))
    
    %% Decisiones
    CountCheck{ Hay<br>Notificaciones?}

    %% Flujo Lineal
    NavbarUI --> |Clic 'Campana'| DB
    DB -.-> CountCheck
    
    CountCheck -- No (Array Vacio) --> EmptyStateUI
    CountCheck -- Si --> DropdownUI
    
    %% Accion posterior
    DropdownUI --> |Clic en una Alerta| DetailUI
```

### 3.2. User Flow: Interrupcion Asincrona (WebSocket Toast)
Este flujo modela un evento del sistema que es empujado al Frontend sin que el usuario haga absolutamente nada (Real-time). Exige que el Frontend este suscrito a un canal de Spring WebSocket.

```mermaid
flowchart TD
    %% Nodos Logicos/Asincronos
    ExternalTrigger((Evento Externo<br>Ej. Wompi Confirma Pago))
    SpringWebSocket((Spring WebSocket<br>Canal: 'host_alerts'))
    
    %% Nodos UI
    CurrentUI[Cualquier Pantalla B2B<br>Ej. /dashboard/calendario]
    ToastUI[Componente Toast Animado<br>' Nueva Reserva Pagada!']
    ActionBtnUI[Boton en Toast<br>'Ver Detalles']
    DestinationUI[Pantalla de Reserva<br>Ruta: /dashboard/reservas/id]
    
    %% Flujo Asincrono Hacia el Cliente
    ExternalTrigger -.-> |Dispara Evento DB| SpringWebSocket
    SpringWebSocket -.-> |Push Data al Cliente| ToastUI
    
    %% Interaccion del Usuario
    CurrentUI --> ToastUI
    ToastUI --> ActionBtnUI
    
    %% Decision del Usuario
    ActionBtnUI --> |Clickea Boton| DestinationUI
    ToastUI --> |Ignora por 5 Segundos| AutoClose(Se oculta automaticamente)
    AutoClose --> CurrentUI
```
