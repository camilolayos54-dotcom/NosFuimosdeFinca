# User Flows: MOD-AUTH (Identidad y Seguridad)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-AUTH
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Basado en los requerimientos de la Fase 3, extraemos las interacciones humanas y las clasificamos bajo las reglas estrictas de UX.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Login B2B / Muro de Seguridad** | **User Flow** | Requiere máquina de estados. Tiene bifurcaciones críticas (JWT expirado, KYC pendiente, contraseña errónea). | Finquero / Turista |
| **Onboarding B2B (KYC)** | **User Flow** | Flujo condicional y asíncrono. Sube documentos y debe esperar respuesta del Admin. Requiere vista transitoria (Pending). | Finquero |
| **Recuperar Contraseña** | **Task Flow** | Camino lineal atómico. Ingresa email, recibe link, cambia clave. No hay validaciones complejas de múltiples actores. | Universal |

---

## 2. Screen Mapping (Cruce Topológico)

Las interfaces que sustentan los flujos de Autenticación, cruzadas con el *Sitemap* (D1).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Login B2B** | `/host` -> `/login` -> `/dashboard` (Éxito) | **Modal Toast:** "Credenciales Inválidas". |
| **Onboarding** | `/onboarding/docs` -> `/onboarding/bank` -> `/dashboard` | **Pending View:** `/onboarding/pending` (Revisión manual). |
| **Recovery** | `/login` -> `/recuperar-password` -> `/reset-password` | **Modal Toast:** "Correo Enviado" / "Expirado". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Autenticación Unificada B2B (`/login`)
El camino del usuario que intenta entrar al Portal B2B, con el "Unhappy Path" del error de credenciales y el Muro KYC.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Físicas (Spring Boot (Java))
    LandingUI[Pantalla Landing B2B<br>Ruta: /host]
    LoginUI[Pantalla Login<br>Ruta: /login]
    ToastErrorUI[Componente Toast<br>Credenciales Inválidas]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    OnboardingUI[Pantalla de Bienvenida KYC<br>Ruta: /onboarding]
    
    %% Nodos Redondeados: Backend Asíncrono
    SpringSecurityDB((Spring Security<br>Verificación JWT))
    
    %% Rombos: Evaluaciones Lógicas
    CredentialCheck{¿Email y Clave<br>correctos?}
    KYCCheck{¿El usuario tiene<br>KYC Aprobado?}

    %% Camino Feliz e Interacción
    LandingUI --> |Clic 'Ingresar'| LoginUI
    LoginUI --> |Submit Form| SpringSecurityDB
    
    %% Respuesta de Base de Datos
    SpringSecurityDB -.-> CredentialCheck
    
    %% Unhappy Path (Credenciales)
    CredentialCheck -- No (401 Auth Error) --> ToastErrorUI
    ToastErrorUI --> |Reintenta| LoginUI
    
    %% Happy Path y Bifurcación KYC
    CredentialCheck -- Sí (200 OK) --> KYCCheck
    KYCCheck -- No (Usuario Nuevo) --> OnboardingUI
    KYCCheck -- Sí (Usuario Verificado) --> DashboardUI
```

### 3.2. User Flow: Onboarding B2B (Muro Legal KYC)
El flujo estricto donde el Finquero debe subir su RUT y queda bloqueado hasta que el Administrador de la plataforma lo aprueba.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Físicas
    DocsUI[Formulario de Documentos<br>Ruta: /onboarding/docs]
    BankUI[Formulario Cuenta Bancaria<br>Ruta: /onboarding/bank]
    ErrorMIMEUI[Componente Modal<br>Error: Archivo Inválido]
    PendingUI[Pantalla de Espera<br>Ruta: /onboarding/pending]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    
    %% Nodos Redondeados: Backend Asíncrono
    S3Storage((AWS S3 Storage<br>Sube PDF/JPG))
    AdminApprove((Backoffice Admin<br>Revisión Manual))
    
    %% Rombos: Evaluaciones Lógicas
    FormatCheck{¿MIME y Tamaño<br>son válidos?}
    AdminDecision{¿El Admin<br>aprobó el RUT?}

    %% Flujo Turista
    DocsUI --> |Adjunta Archivo| FormatCheck
    FormatCheck -- No (Unhappy Path) --> ErrorMIMEUI
    ErrorMIMEUI --> DocsUI
    
    FormatCheck -- Sí --> S3Storage
    S3Storage -.-> BankUI
    BankUI --> |Guardar| PendingUI
    
    %% Bloqueo Asíncrono
    PendingUI -.-> |Webhook / Polling| AdminDecision
    AdminDecision -- Rechazado (Dato falso) --> DocsUI
    AdminDecision -- Aprobado --> DashboardUI
```

### 3.3. Task Flow: Recuperación de Contraseña
Acción lineal y atómica sin decisiones de múltiples actores.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Físicas
    LoginUI[Pantalla Login<br>Ruta: /login]
    ReqFormUI[Formulario de Recuperación<br>Ruta: /recuperar-password]
    ToastSuccessUI[Componente Toast<br>'Revisa tu email']
    ResetUI[Formulario Nueva Clave<br>Ruta: /reset-password?token=XYZ]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    
    %% Nodos Redondeados: Backend Asíncrono
    EmailService((MOD-NOT<br>Magic Link Email))
    
    %% Flujo Lineal
    LoginUI --> |Clic 'Olvidé mi clave'| ReqFormUI
    ReqFormUI --> |Ingresa Email| EmailService
    EmailService -.-> ToastSuccessUI
    
    %% Intervención Externa del Usuario
    ToastSuccessUI -.-> |Clickea link en su Gmail| ResetUI
    ResetUI --> |Escribe clave nueva| DashboardUI
```
