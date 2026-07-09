# Wireframe Specifications: `/error` (Global Error Handler)

**Ruta UI:** Dinámica (Intercepta errores 404, 500, 403 o fallas de red).
**Módulos Funcionales Inyectados:** Transversal a todos los módulos.

---

## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** El usuario se ha topado con un muro técnico (Ej. Se cayó la conexión, el servidor falló o la página no existe). El nivel de frustración es máximo. El diseño debe ser empático, reducir la culpa del usuario y proveer salidas claras.
- **Patrón Principal:** `Centered Focus (Foco Centrado)`. Una ilustración amigable o ícono de gran tamaño en el centro, seguido de un mensaje claro y un botón de rescate (Call to Action) para devolver al usuario a una zona segura.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar la página de Manejo de Errores:

### A. Átomos
- `HeroIcon / ErrorIllustration`: Asset gráfico amigable (Ej. Un tractor varado o un mapa roto).
- `PrimaryButton`: Botón principal de rescate ("Volver al Inicio").
- `SecondaryButton`: Botón secundario ("Contactar Soporte").

### B. Moléculas
- `ErrorMessageGroup`: Une (Título H1 del Error + Párrafo explicativo Body-lg).
- `ActionRow`: Une (`PrimaryButton` + `SecondaryButton`) con espaciado uniforme.

### C. Organismos
- `ErrorStateBlock`: Une (`ErrorIllustration` + `ErrorMessageGroup` + `ActionRow`). Centrado vertical y horizontalmente en la pantalla.

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Prevención del Callejón sin Salida (No Dead-Ends):**
   - Todo layout de error DEBE incluir al menos un botón de navegación visible que permita al usuario salir de esa pantalla.
2. **Claridad del Mensaje (Cero Jerga):**
   - El texto no debe decir "Error 500: Internal Server Exception". Debe decir "Ups, algo salió mal en nuestra granja" o un equivalente amigable.
3. **Accesibilidad (a11y):**
   - Los botones de rescate deben tener un tap target gigante (mínimo 48px) para que en medio del estrés, el usuario móvil pueda tocarlos fácilmente.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para el Manejo de Errores:

### ✅ Pantallas Base
- `[ ]` **Desktop (1440px):** Layout centrado, ocupando toda la pantalla (Full Height) sin Sidebar.
- `[ ]` **Mobile (390px):** Layout apilado verticalmente, botones ocupando 100% del ancho.

### ✅ Variantes Críticas de Mensajería
- `[ ]` **Variante 404 (Not Found):** Pantalla donde el mensaje diga "Esta finca no existe" (Falla de URL).
- `[ ]` **Variante 500 (Server Error):** Pantalla donde el mensaje diga "Estamos experimentando problemas técnicos".
- `[ ]` **Variante Offline (Network Error):** Pantalla indicando "Parece que te quedaste sin conexión a Internet".
