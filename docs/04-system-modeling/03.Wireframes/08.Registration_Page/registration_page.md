# Wireframe Specifications: `/registro`

**Ruta UI:** `/registro`
**Módulos Funcionales Inyectados:** `MOD-AUTH` (Autenticación e Identidad).

---

# RESULTADOS


- **Diagnóstico:** El usuario B2B o B2C necesita crear una cuenta de manera segura. Este paso tiene alta fricción, por lo que el diseño debe transmitir confianza y ser extremadamente claro.
- **Patrón Principal:** `Split-Screen (Pantalla Dividida)`. En Desktop, el 50% izquierdo contiene el formulario (fondo limpio para alta concentración) y el 50% derecho muestra una fotografía aspiracional de "Nos Fuimos de Finca". En Mobile, el formulario ocupa el 100% de la pantalla.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar la página de `/registro`:

### A. Átomos
- `AuthInput` **(Obligatorio por MOD-AUTH)**: Campo de texto. *Variantes: `Default`, `Focus`, `Error` (Borde rojo).*
- `DatePickerInput` **(Obligatorio para Cumpleaños)**: Variante de input para selección de fecha.
- `PrimaryButton`: Botón principal de acción ("Crear Cuenta").
- `BrandLogo`: Logo estático en la cabecera del formulario.

### B. Moléculas
- `RegistrationFormField`: Une (`Label` + `AuthInput` + `HelperText/ErrorText`).
- `DoubleFieldRow`: Une dos `RegistrationFormField` en una misma fila (Ej. para Nombres y Apellidos en Desktop).

### C. Organismos
- `RegistrationFormBlock` **(Obligatorio por MOD-AUTH)**: Une el Título H1 ("Crea tu cuenta") + Cuatro campos obligatorios (Nombres, Apellidos, Cédula, Fecha de Nacimiento) + `PrimaryButton`.

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Agrupación Lógica (Ley de Proximidad):**
   - Agrupa visualmente Nombres y Apellidos en la misma línea en pantallas Desktop. Cédula y Fecha de Nacimiento deben ir en líneas separadas por ser datos de naturaleza distinta.
2. **Accesibilidad (a11y) y Prevención de Errores:**
   - Si el usuario ingresa un formato de cédula inválido, la Molécula `RegistrationFormField` debe mostrar un `ErrorText` en rojo fuerte (`#ba1a1a`) y el borde del campo debe pintarse del mismo color.
3. **Flujo de Teclado:**
   - El orden de tabulación (Tab Order) debe seguir la lectura occidental estricta: Nombres -> Apellidos -> Cédula -> Fecha de Nacimiento -> Botón Submit.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/registro`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Layout Split-Screen con el formulario a la izquierda.
- `[ ]` **Mobile (390px):** Layout en 1 columna, apilado verticalmente.

### ✅ Estados Transitorios (Mutaciones Asíncronas)
- `[ ]` **Loading State:** Tras hacer clic en "Crear Cuenta", el botón pasa a estado `Disabled` y muestra un Spinner.

### ✅ Excepciones y Muros (Unhappy Paths)
- `[ ]` **Validation Error:** Muestra la pantalla con alertas rojas en los campos si se dejan vacíos o si la cédula ya existe.
