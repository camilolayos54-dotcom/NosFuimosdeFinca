# Wireframe Specifications: `/onboarding/*` (Muro KYC)

**Ruta UI:** `/onboarding/docs`, `/onboarding/bank`, `/onboarding/pending`
**Requisitos Funcionales Inyectados:** `MOD-AUTH` (Proceso de Verificación KYC y Estados Bloqueantes).

---

# RESULTADOS
![Onboarding - Banco (Wireframe Desktop).png](<Onboarding - Banco (Wireframe Desktop).png>).png)
![Onboarding - Banco (Wireframe Mobile).png](<Onboarding - Banco (Wireframe Mobile).png>).png)
![Onboarding - Documentos (Wireframe Desktop).png](<Onboarding - Documentos (Wireframe Desktop).png>).png)
![Onboarding - Documentos (Wireframe Mobile).png](<Onboarding - Documentos (Wireframe Mobile).png>).png)
![Onboarding - Pendiente (Wireframe Desktop).png](<Onboarding - Pendiente (Wireframe Desktop).png>).png)
![Onboarding - Pendiente (Wireframe Mobile).png](<Onboarding - Pendiente (Wireframe Mobile).png>).png)


## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** El finquero acaba de crear su cuenta. Quiere publicar su finca ya mismo, pero lo obligamos a subir documentos legales pesados (RUT, Cédula). Esto genera altísima fricción y abandono.
- **Patrón Principal:** `Progressive Disclosure Wizard` (Paso a Paso).
  - En lugar de mostrar un formulario intimidante de 30 campos legales, dividimos el proceso en pantallas diminutas (Una pantalla para el RUT, otra pantalla para la Cuenta Bancaria). Esto reduce la carga cognitiva.
  - Al final del túnel de captura de datos, debe haber un patrón de **Empty State Ilusorio (Pending State)** que le indique al dueño que humanos están revisando sus papeles.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Muro KYC:

### A. Átomos
- `ProgressStepper`: Barra de progreso superior (Ej. "Paso 1 de 3: Identidad").
- `FileUploadArea` **(Obligatorio por MOD-AUTH)**: Caja punteada grande para arrastrar y soltar el archivo PDF (RUT).
- `SecurityLockIcon`: Icono de un candado amigable o un escudo.

### B. Moléculas
- `DocumentUploadCard` **(Obligatorio por MOD-AUTH)**: Une (`FileUploadArea` + Texto descriptivo "Sube el PDF de tu RUT" + Enlace para descargar guía).
- `PendingIllustration` **(Obligatorio por MOD-AUTH)**: Ilustración vectorial grande de un reloj de arena, un candado o una lupa de revisión.

### C. Organismos
- `OnboardingWizardStep` **(Obligatorio por MOD-AUTH)**: Une (`ProgressStepper` + Título + `DocumentUploadCard` o Formulario Bancario + Botón `PrimaryButton` "Guardar y Continuar").
- `PendingReviewBlock` **(Obligatorio por MOD-AUTH)**: Une (`PendingIllustration` + Título "Estamos validando tus datos" + Texto explicando que el proceso tarda 24h).

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Aislamiento Total (Muro):**
   - Esta pantalla es un Muro. El Sidebar o Navbar del Dashboard principal (`/dashboard`) NO debe ser visible. El usuario está literalmente "atrapado" aquí hasta que termine o se le apruebe el KYC.
2. **Carga Cognitiva en Subida de Archivos:**
   - El `FileUploadArea` debe ser el elemento más prominente del Paso 1. Debe incluir indicaciones claras de los límites técnicos exigidos por `MOD-AUTH` (Ej. "Formato PDF o JPG. Máximo 5MB").
3. **Gestión de la Ansiedad (Pending State):**
   - Una vez el finquero envía los datos, el servidor asíncrono los pone en estado `PENDING_VERIFICATION`. La pantalla `/onboarding/pending` debe verse profesional y amigable para no asustarlo (No usar colores rojos ni alertas rojas, usar colores azules/neutros de "Procesamiento").

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/onboarding/*`:

### ✅ Pantallas Base del Wizard (Happy Path)
- `[ ]` **Paso 1 - Documentos (`/onboarding/docs`) (Obligatorio por MOD-AUTH):** Dibuja el wizard mostrando el `DocumentUploadCard` pidiendo el RUT.
- `[ ]` **Paso 2 - Financiero (`/onboarding/bank`) (Obligatorio por MOD-AUTH):** Dibuja el wizard pidiendo los datos bancarios para pagarle las reservas (Banco, Tipo de cuenta, Número).

### ✅ Estado Transitorio Final (Bloqueante)
- `[ ]` **Estado de Revisión (`/onboarding/pending`) (Obligatorio por MOD-AUTH):** Dibuja la pantalla final de bloqueo. Utiliza el `PendingReviewBlock` con la ilustración. Esta pantalla no tiene botones de acción, solo un texto indicando "Te notificaremos por correo electrónico cuando tu cuenta esté aprobada".

### ✅ Excepciones Legales (Unhappy Paths)
- `[ ]` **Rechazo de Archivo MIME (Obligatorio por MOD-AUTH):** Dibuja la pantalla del Paso 1 en donde el usuario intentó subir un archivo `.exe` o un PDF corrupto. El `FileUploadArea` debe tener bordes rojos y un toast debe indicar "Formato de archivo no soportado. Sube un PDF válido".
