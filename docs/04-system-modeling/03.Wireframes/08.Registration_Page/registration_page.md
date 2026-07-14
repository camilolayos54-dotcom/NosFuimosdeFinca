# Wireframe Specifications: `/registro`

**Ruta UI:** `/registro`
**Modulos Funcionales Inyectados:** `MOD-AUTH` (Autenticacion e Identidad).

---

# RESULTADOS


- **Diagnostico:** El usuario B2B o B2C necesita crear una cuenta de manera segura. Este paso tiene alta friccion, por lo que el diseno debe transmitir confianza y ser extremadamente claro.
- **Patron Principal:** `Split-Screen (Pantalla Dividida)`. En Desktop, el 50% izquierdo contiene el formulario (fondo limpio para alta concentracion) y el 50% derecho muestra una fotografia aspiracional de "Nos Fuimos de Finca". En Mobile, el formulario ocupa el 100% de la pantalla.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la pagina de `/registro`:

### A. Atomos
- `AuthInput` **(Obligatorio por MOD-AUTH)**: Campo de texto. *Variantes: `Default`, `Focus`, `Error` (Borde rojo).*
- `DatePickerInput` **(Obligatorio para Cumpleanos)**: Variante de input para seleccion de fecha.
- `PrimaryButton`: Boton principal de accion ("Crear Cuenta").
- `BrandLogo`: Logo estatico en la cabecera del formulario.

### B. Moleculas
- `RegistrationFormField`: Une (`Label` + `AuthInput` + `HelperText/ErrorText`).
- `DoubleFieldRow`: Une dos `RegistrationFormField` en una misma fila (Ej. para Nombres y Apellidos en Desktop).

### C. Organismos
- `RegistrationFormBlock` **(Obligatorio por MOD-AUTH)**: Une el Titulo H1 ("Crea tu cuenta") + Cuatro campos obligatorios (Nombres, Apellidos, Cedula, Fecha de Nacimiento) + `PrimaryButton`.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Agrupacion Logica (Ley de Proximidad):**
   - Agrupa visualmente Nombres y Apellidos en la misma linea en pantallas Desktop. Cedula y Fecha de Nacimiento deben ir en lineas separadas por ser datos de naturaleza distinta.
2. **Accesibilidad (a11y) y Prevencion de Errores:**
   - Si el usuario ingresa un formato de cedula invalido, la Molecula `RegistrationFormField` debe mostrar un `ErrorText` en rojo fuerte (`#ba1a1a`) y el borde del campo debe pintarse del mismo color.
3. **Flujo de Teclado:**
   - El orden de tabulacion (Tab Order) debe seguir la lectura occidental estricta: Nombres -> Apellidos -> Cedula -> Fecha de Nacimiento -> Boton Submit.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/registro`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Layout Split-Screen con el formulario a la izquierda.
- `[ ]` **Mobile (390px):** Layout en 1 columna, apilado verticalmente.

### Estados Transitorios (Mutaciones Asincronas)
- `[ ]` **Loading State:** Tras hacer clic en "Crear Cuenta", el boton pasa a estado `Disabled` y muestra un Spinner.

### Excepciones y Muros (Unhappy Paths)
- `[ ]` **Validation Error:** Muestra la pantalla con alertas rojas en los campos si se dejan vacios o si la cedula ya existe.
