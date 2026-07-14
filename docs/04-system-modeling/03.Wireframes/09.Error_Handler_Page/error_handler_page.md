# Wireframe Specifications: `/error` (Global Error Handler)

**Ruta UI:** Dinamica (Intercepta errores 404, 500, 403 o fallas de red).
**Modulos Funcionales Inyectados:** Transversal a todos los modulos.

---

## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El usuario se ha topado con un muro tecnico (Ej. Se cayo la conexion, el servidor fallo o la pagina no existe). El nivel de frustracion es maximo. El diseno debe ser empatico, reducir la culpa del usuario y proveer salidas claras.
- **Patron Principal:** `Centered Focus (Foco Centrado)`. Una ilustracion amigable o icono de gran tamano en el centro, seguido de un mensaje claro y un boton de rescate (Call to Action) para devolver al usuario a una zona segura.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la pagina de Manejo de Errores:

### A. Atomos
- `HeroIcon / ErrorIllustration`: Asset grafico amigable (Ej. Un tractor varado o un mapa roto).
- `PrimaryButton`: Boton principal de rescate ("Volver al Inicio").
- `SecondaryButton`: Boton secundario ("Contactar Soporte").

### B. Moleculas
- `ErrorMessageGroup`: Une (Titulo H1 del Error + Parrafo explicativo Body-lg).
- `ActionRow`: Une (`PrimaryButton` + `SecondaryButton`) con espaciado uniforme.

### C. Organismos
- `ErrorStateBlock`: Une (`ErrorIllustration` + `ErrorMessageGroup` + `ActionRow`). Centrado vertical y horizontalmente en la pantalla.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Prevencion del Callejon sin Salida (No Dead-Ends):**
   - Todo layout de error DEBE incluir al menos un boton de navegacion visible que permita al usuario salir de esa pantalla.
2. **Claridad del Mensaje (Cero Jerga):**
   - El texto no debe decir "Error 500: Internal Server Exception". Debe decir "Ups, algo salio mal en nuestra granja" o un equivalente amigable.
3. **Accesibilidad (a11y):**
   - Los botones de rescate deben tener un tap target gigante (minimo 48px) para que en medio del estres, el usuario movil pueda tocarlos facilmente.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para el Manejo de Errores:

### Pantallas Base
- `[ ]` **Desktop (1440px):** Layout centrado, ocupando toda la pantalla (Full Height) sin Sidebar.
- `[ ]` **Mobile (390px):** Layout apilado verticalmente, botones ocupando 100% del ancho.

### Variantes Criticas de Mensajeria
- `[ ]` **Variante 404 (Not Found):** Pantalla donde el mensaje diga "Esta finca no existe" (Falla de URL).
- `[ ]` **Variante 500 (Server Error):** Pantalla donde el mensaje diga "Estamos experimentando problemas tecnicos".
- `[ ]` **Variante Offline (Network Error):** Pantalla indicando "Parece que te quedaste sin conexion a Internet".
