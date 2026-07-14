# Wireframe Specifications: `/onboarding/*` (Muro KYC)

**Ruta UI:** `/onboarding/docs`, `/onboarding/bank`, `/onboarding/pending`
**Requisitos Funcionales Inyectados:** `MOD-AUTH` (Proceso de Verificacion KYC y Estados Bloqueantes).

---

# RESULTADOS
![Onboarding - Banco (Wireframe Desktop).png](Onboarding%20-%20Banco%20%28Wireframe%20Desktop%29.png)
![Onboarding - Banco (Wireframe Mobile).png](Onboarding%20-%20Banco%20%28Wireframe%20Mobile%29.png)
![Onboarding - Documentos (Wireframe Desktop).png](Onboarding%20-%20Documentos%20%28Wireframe%20Desktop%29.png)
![Onboarding - Documentos (Wireframe Mobile).png](Onboarding%20-%20Documentos%20%28Wireframe%20Mobile%29.png)
![Onboarding - Pendiente (Wireframe Desktop).png](Onboarding%20-%20Pendiente%20%28Wireframe%20Desktop%29.png)
![Onboarding - Pendiente (Wireframe Mobile).png](Onboarding%20-%20Pendiente%20%28Wireframe%20Mobile%29.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El finquero acaba de crear su cuenta. Quiere publicar su finca ya mismo, pero lo obligamos a subir documentos legales pesados (RUT, Cedula). Esto genera altisima friccion y abandono.
- **Patron Principal:** `Progressive Disclosure Wizard` (Paso a Paso).
  - En lugar de mostrar un formulario intimidante de 30 campos legales, dividimos el proceso en pantallas diminutas (Una pantalla para el RUT, otra pantalla para la Cuenta Bancaria). Esto reduce la carga cognitiva.
  - Al final del tunel de captura de datos, debe haber un patron de **Empty State Ilusorio (Pending State)** que le indique al dueno que humanos estan revisando sus papeles.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar el Muro KYC:

### A. Atomos
- `ProgressStepper`: Barra de progreso superior (Ej. "Paso 1 de 3: Identidad").
- `FileUploadArea` **(Obligatorio por MOD-AUTH)**: Caja punteada grande para arrastrar y soltar el archivo PDF (RUT).
- `SecurityLockIcon`: Icono de un candado amigable o un escudo.

### B. Moleculas
- `DocumentUploadCard` **(Obligatorio por MOD-AUTH)**: Une (`FileUploadArea` + Texto descriptivo "Sube el PDF de tu RUT" + Enlace para descargar guia).
- `PendingIllustration` **(Obligatorio por MOD-AUTH)**: Ilustracion vectorial grande de un reloj de arena, un candado o una lupa de revision.

### C. Organismos
- `OnboardingWizardStep` **(Obligatorio por MOD-AUTH)**: Une (`ProgressStepper` + Titulo + `DocumentUploadCard` o Formulario Bancario + Boton `PrimaryButton` "Guardar y Continuar").
- `PendingReviewBlock` **(Obligatorio por MOD-AUTH)**: Une (`PendingIllustration` + Titulo "Estamos validando tus datos" + Texto explicando que el proceso tarda 24h).

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Aislamiento Total (Muro):**
   - Esta pantalla es un Muro. El Sidebar o Navbar del Dashboard principal (`/dashboard`) NO debe ser visible. El usuario esta literalmente "atrapado" aqui hasta que termine o se le apruebe el KYC.
2. **Carga Cognitiva en Subida de Archivos:**
   - El `FileUploadArea` debe ser el elemento mas prominente del Paso 1. Debe incluir indicaciones claras de los limites tecnicos exigidos por `MOD-AUTH` (Ej. "Formato PDF o JPG. Maximo 5MB").
3. **Gestion de la Ansiedad (Pending State):**
   - Una vez el finquero envia los datos, el servidor asincrono los pone en estado `PENDING_VERIFICATION`. La pantalla `/onboarding/pending` debe verse profesional y amigable para no asustarlo (No usar colores rojos ni alertas rojas, usar colores azules/neutros de "Procesamiento").

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/onboarding/*`:

### Pantallas Base del Wizard (Happy Path)
- `[ ]` **Paso 1 - Documentos (`/onboarding/docs`) (Obligatorio por MOD-AUTH):** Dibuja el wizard mostrando el `DocumentUploadCard` pidiendo el RUT.
- `[ ]` **Paso 2 - Financiero (`/onboarding/bank`) (Obligatorio por MOD-AUTH):** Dibuja el wizard pidiendo los datos bancarios para pagarle las reservas (Banco, Tipo de cuenta, Numero).

### Estado Transitorio Final (Bloqueante)
- `[ ]` **Estado de Revision (`/onboarding/pending`) (Obligatorio por MOD-AUTH):** Dibuja la pantalla final de bloqueo. Utiliza el `PendingReviewBlock` con la ilustracion. Esta pantalla no tiene botones de accion, solo un texto indicando "Te notificaremos por correo electronico cuando tu cuenta este aprobada".

### Excepciones Legales (Unhappy Paths)
- `[ ]` **Rechazo de Archivo MIME (Obligatorio por MOD-AUTH):** Dibuja la pantalla del Paso 1 en donde el usuario intento subir un archivo `.exe` o un PDF corrupto. El `FileUploadArea` debe tener bordes rojos y un toast debe indicar "Formato de archivo no soportado. Sube un PDF valido".
