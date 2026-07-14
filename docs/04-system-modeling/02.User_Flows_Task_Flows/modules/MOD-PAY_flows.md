# User Flows: MOD-PAY (Motor Financiero y Pagos)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-PAY
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Este modulo dicta como el dinero fluye a traves de la aplicacion. Exige un control absoluto de "Unhappy Paths" para evitar fraudes, cobros dobles o multas por la norma PCI-DSS.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Procesamiento de Pago Wompi** | **User Flow** | Requiere el bloqueo de la Interfaz Grafica. Delega la seguridad de los datos de la tarjeta a un tercero (PCI-DSS) y reacciona a los declives bancarios. | Turista |
| **Proteccion de Idempotencia (Doble Clic)** | **Task Flow** | Regla estricta de UI: Evitar que la desesperacion del Turista cause un cobro doble en su tarjeta de credito. | Turista |

---

## 2. Screen Mapping (Cruce Topologico)

Las transacciones ocurren en el embudo del Checkout, con redirecciones obligatorias a ecosistemas externos (Banco).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Flujo Wompi PCI-DSS** | `/checkout/[id]` -> `Wompi UI` -> `/checkout/success` | **Redireccion Estricta:** Salida del dominio `nosfuimosdefinca.com`. |
| **Prevencion Idempotencia** | `/checkout/processing` | **Boton Bloqueado (`disabled=true`)**: Con Spinner de carga. |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Integracion Segura Wompi (PCI-DSS)
Este flujo grafica explicitamente como nuestro sistema jamas toca los numeros de la tarjeta del Turista (PAN/CVC). Toda la validacion asincrona ocurre en el ecosistema del proveedor.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutUI[Pantalla Wizard Checkout<br>Ruta: /checkout/id]
    WompiGateway((Widget o Redireccion Wompi<br>Pasarela Externa Segura))
    ModalErrorUI[Componente Error<br>'Fondos Insuficientes']
    SuccessUI[Pantalla Exito<br>Ruta: /checkout/success]
    
    %% Nodos Asincronos
    BackendAPI((API /api/pay<br>Genera Firma de Transaccion))
    WompiWebhook((Wompi Webhook<br>Notificacion Server-to-Server))
    
    %% Decisiones
    BankDecision{ Banco aprueba<br>transaccion?}

    %% Flujo Turista
    CheckoutUI --> |Clic 'Proceder al Pago'| BackendAPI
    BackendAPI -.-> |Devuelve Hash de Seguridad| WompiGateway
    
    %% Flujo ciego (El Turista ingresa su tarjeta en Wompi, NO en nuestra app)
    WompiGateway --> |El Turista paga| BankDecision
    
    %% Camino Triste (Declive)
    BankDecision -- No (Tarjeta rechazada) --> ModalErrorUI
    ModalErrorUI --> |Boton 'Usar otra tarjeta'| CheckoutUI
    
    %% Camino Feliz y Webhook
    BankDecision -- Si (Aprobado) --> SuccessUI
    
    %% Proceso en background (Invisible al Turista)
    BankDecision -.-> |Wompi dispara Webhook POST| WompiWebhook
    WompiWebhook -.-> |Actualiza Base de Datos a 'PAID'| BackendAPI
```

### 3.2. Task Flow: Prevencion Antifraude (Idempotencia en UI)
Modela el comportamiento milimetrico de la Interfaz Grafica cuando un usuario esta ansioso porque su internet esta lento y oprime el boton de pago 5 veces seguidas.

```mermaid
flowchart TD
    %% Nodos UI
    CheckoutUI[Pantalla de Pago<br>Boton 'Pagar']
    LockedButtonUI[Boton Mutado UI<br>'Procesando...' + disabled=true]
    ToastErrorUI[Componente Toast<br>'Por favor espere, procesando pago...']
    
    %% Nodos Asincronos
    FrontendState((Estado Local de React<br>isSubmitting = true))
    API_Call((Llamada de Red API))
    
    %% Decisiones
    IsLoadingCheck{ isSubmitting<br>es TRUE?}

    %% Flujo Clic Multiple
    CheckoutUI --> |Clic 'Pagar' 1ra vez| IsLoadingCheck
    
    %% Primer clic valido
    IsLoadingCheck -- No --> FrontendState
    FrontendState --> LockedButtonUI
    LockedButtonUI --> API_Call
    
    %% El usuario se desespera y hace clic 3 veces mas
    LockedButtonUI --> |Clic 'Pagar' 2da vez| IsLoadingCheck
    IsLoadingCheck -- Si --> ToastErrorUI
    
    %% El flujo muere aqui, protegiendo la Base de Datos
    ToastErrorUI -.-> |Ignora el clic| LockedButtonUI
```
