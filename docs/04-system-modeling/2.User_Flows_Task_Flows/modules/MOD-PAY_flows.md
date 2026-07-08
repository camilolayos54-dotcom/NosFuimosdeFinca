# User Flows: MOD-PAY (Motor Financiero y Pagos)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-PAY
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Este módulo dicta cómo el dinero fluye a través de la aplicación. Exige un control absoluto de "Unhappy Paths" para evitar fraudes, cobros dobles o multas por la norma PCI-DSS.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Procesamiento de Pago Wompi** | **User Flow** | Requiere el bloqueo de la Interfaz Gráfica. Delega la seguridad de los datos de la tarjeta a un tercero (PCI-DSS) y reacciona a los declives bancarios. | Turista |
| **Protección de Idempotencia (Doble Clic)** | **Task Flow** | Regla estricta de UI: Evitar que la desesperación del Turista cause un cobro doble en su tarjeta de crédito. | Turista |

---

## 2. Screen Mapping (Cruce Topológico)

Las transacciones ocurren en el embudo del Checkout, con redirecciones obligatorias a ecosistemas externos (Banco).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Flujo Wompi PCI-DSS** | `/checkout/[id]` -> `Wompi UI` -> `/checkout/success` | **Redirección Estricta:** Salida del dominio `nosfuimosdefinca.com`. |
| **Prevención Idempotencia** | `/checkout/processing` | **Botón Bloqueado (`disabled=true`)**: Con Spinner de carga. |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Integración Segura Wompi (PCI-DSS)
Este flujo grafica explícitamente cómo nuestro sistema jamás toca los números de la tarjeta del Turista (PAN/CVC). Toda la validación asíncrona ocurre en el ecosistema del proveedor.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutUI[Pantalla Wizard Checkout<br>Ruta: /checkout/id]
    WompiGateway((Widget o Redirección Wompi<br>Pasarela Externa Segura))
    ModalErrorUI[Componente Error<br>'Fondos Insuficientes']
    SuccessUI[Pantalla Éxito<br>Ruta: /checkout/success]
    
    %% Nodos Asíncronos
    BackendAPI((API /api/pay<br>Genera Firma de Transacción))
    WompiWebhook((Wompi Webhook<br>Notificación Server-to-Server))
    
    %% Decisiones
    BankDecision{¿Banco aprueba<br>transacción?}

    %% Flujo Turista
    CheckoutUI --> |Clic 'Proceder al Pago'| BackendAPI
    BackendAPI -.-> |Devuelve Hash de Seguridad| WompiGateway
    
    %% Flujo ciego (El Turista ingresa su tarjeta en Wompi, NO en nuestra app)
    WompiGateway --> |El Turista paga| BankDecision
    
    %% Camino Triste (Declive)
    BankDecision -- No (Tarjeta rechazada) --> ModalErrorUI
    ModalErrorUI --> |Botón 'Usar otra tarjeta'| CheckoutUI
    
    %% Camino Feliz y Webhook
    BankDecision -- Sí (Aprobado) --> SuccessUI
    
    %% Proceso en background (Invisible al Turista)
    BankDecision -.-> |Wompi dispara Webhook POST| WompiWebhook
    WompiWebhook -.-> |Actualiza Base de Datos a 'PAID'| BackendAPI
```

### 3.2. Task Flow: Prevención Antifraude (Idempotencia en UI)
Modela el comportamiento milimétrico de la Interfaz Gráfica cuando un usuario está ansioso porque su internet está lento y oprime el botón de pago 5 veces seguidas.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutUI[Pantalla de Pago<br>Botón 'Pagar']
    LockedButtonUI[Botón Mutado UI<br>'Procesando...' + disabled=true]
    ToastErrorUI[Componente Toast<br>'Por favor espere, procesando pago...']
    
    %% Nodos Asíncronos
    FrontendState((Estado Local de React<br>isSubmitting = true))
    API_Call((Llamada de Red API))
    
    %% Decisiones
    IsLoadingCheck{¿isSubmitting<br>es TRUE?}

    %% Flujo Clic Múltiple
    CheckoutUI --> |Clic 'Pagar' 1ra vez| IsLoadingCheck
    
    %% Primer clic válido
    IsLoadingCheck -- No --> FrontendState
    FrontendState --> LockedButtonUI
    LockedButtonUI --> API_Call
    
    %% El usuario se desespera y hace clic 3 veces más
    LockedButtonUI --> |Clic 'Pagar' 2da vez| IsLoadingCheck
    IsLoadingCheck -- Sí --> ToastErrorUI
    
    %% El flujo muere aquí, protegiendo la Base de Datos
    ToastErrorUI -.-> |Ignora el clic| LockedButtonUI
```
