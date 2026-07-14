# User Flows: MOD-AUTH (Identidad y Seguridad)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-AUTH
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Basado en los requerimientos de la Fase 3, extraemos las interacciones humanas y las clasificamos bajo las reglas estrictas de UX.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Login B2B / Muro de Seguridad** | **User Flow** | Requiere maquina de estados. Tiene bifurcaciones criticas (JWT expirado, KYC pendiente, contrasena erronea). | Finquero / Turista |
| **Onboarding B2B (KYC)** | **User Flow** | Flujo condicional y asincrono. Sube documentos y debe esperar respuesta del Admin. Requiere vista transitoria (Pending). | Finquero |
| **Recuperar Contrasena** | **Task Flow** | Camino lineal atomico. Ingresa email, recibe link, cambia clave. No hay validaciones complejas de multiples actores. | Universal |

---

## 2. Screen Mapping (Cruce Topologico)

Las interfaces que sustentan los flujos de Autenticacion, cruzadas con el *Sitemap* (D1).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Login B2B** | `/host` -> `/login` -> `/dashboard` (Exito) | **Modal Toast:** "Credenciales Invalidas". |
| **Onboarding** | `/onboarding/docs` -> `/onboarding/bank` -> `/dashboard` | **Pending View:** `/onboarding/pending` (Revision manual). |
| **Recovery** | `/login` -> `/recuperar-password` -> `/reset-password` | **Modal Toast:** "Correo Enviado" / "Expirado". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Autenticacion Unificada B2B (`/login`)
El camino del usuario que intenta entrar al Portal B2B, con el "Unhappy Path" del error de credenciales y el Muro KYC.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Fisicas (Spring Boot (Java))
    LandingUI[Pantalla Landing B2B<br>Ruta: /host]
    LoginUI[Pantalla Login<br>Ruta: /login]
    ToastErrorUI[Componente Toast<br>Credenciales Invalidas]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    OnboardingUI[Pantalla de Bienvenida KYC<br>Ruta: /onboarding]
    
    %% Nodos Redondeados: Backend Asincrono
    SpringSecurityDB((Spring Security<br>Verificacion JWT))
    
    %% Rombos: Evaluaciones Logicas
    CredentialCheck{ Email y Clave<br>correctos?}
    KYCCheck{ El usuario tiene<br>KYC Aprobado?}

    %% Camino Feliz e Interaccion
    LandingUI --> |Clic 'Ingresar'| LoginUI
    LoginUI --> |Submit Form| SpringSecurityDB
    
    %% Respuesta de Base de Datos
    SpringSecurityDB -.-> CredentialCheck
    
    %% Unhappy Path (Credenciales)
    CredentialCheck -- No (401 Auth Error) --> ToastErrorUI
    ToastErrorUI --> |Reintenta| LoginUI
    
    %% Happy Path y Bifurcacion KYC
    CredentialCheck -- Si (200 OK) --> KYCCheck
    KYCCheck -- No (Usuario Nuevo) --> OnboardingUI
    KYCCheck -- Si (Usuario Verificado) --> DashboardUI
```

### 3.2. User Flow: Onboarding B2B (Muro Legal KYC)
El flujo estricto donde el Finquero debe subir su RUT y queda bloqueado hasta que el Administrador de la plataforma lo aprueba.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Fisicas
    DocsUI[Formulario de Documentos<br>Ruta: /onboarding/docs]
    BankUI[Formulario Cuenta Bancaria<br>Ruta: /onboarding/bank]
    ErrorMIMEUI[Componente Modal<br>Error: Archivo Invalido]
    PendingUI[Pantalla de Espera<br>Ruta: /onboarding/pending]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    
    %% Nodos Redondeados: Backend Asincrono
    S3Storage((AWS S3 Storage<br>Sube PDF/JPG))
    AdminApprove((Backoffice Admin<br>Revision Manual))
    
    %% Rombos: Evaluaciones Logicas
    FormatCheck{ MIME y Tamano<br>son validos?}
    AdminDecision{ El Admin<br>aprobo el RUT?}

    %% Flujo Turista
    DocsUI --> |Adjunta Archivo| FormatCheck
    FormatCheck -- No (Unhappy Path) --> ErrorMIMEUI
    ErrorMIMEUI --> DocsUI
    
    FormatCheck -- Si --> S3Storage
    S3Storage -.-> BankUI
    BankUI --> |Guardar| PendingUI
    
    %% Bloqueo Asincrono
    PendingUI -.-> |Webhook / Polling| AdminDecision
    AdminDecision -- Rechazado (Dato falso) --> DocsUI
    AdminDecision -- Aprobado --> DashboardUI
```

### 3.3. Task Flow: Recuperacion de Contrasena
Accion lineal y atomica sin decisiones de multiples actores.

```mermaid
flowchart TD
    %% Nodos Cuadrados: Pantallas Fisicas
    LoginUI[Pantalla Login<br>Ruta: /login]
    ReqFormUI[Formulario de Recuperacion<br>Ruta: /recuperar-password]
    ToastSuccessUI[Componente Toast<br>'Revisa tu email']
    ResetUI[Formulario Nueva Clave<br>Ruta: /reset-password?token=XYZ]
    DashboardUI[Hub Dashboard B2B<br>Ruta: /dashboard]
    
    %% Nodos Redondeados: Backend Asincrono
    EmailService((MOD-NOT<br>Magic Link Email))
    
    %% Flujo Lineal
    LoginUI --> |Clic 'Olvide mi clave'| ReqFormUI
    ReqFormUI --> |Ingresa Email| EmailService
    EmailService -.-> ToastSuccessUI
    
    %% Intervencion Externa del Usuario
    ToastSuccessUI -.-> |Clickea link en su Gmail| ResetUI
    ResetUI --> |Escribe clave nueva| DashboardUI
```
