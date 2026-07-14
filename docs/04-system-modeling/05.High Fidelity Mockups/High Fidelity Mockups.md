# Entregable 5 (D5): High-Fidelity Mockups

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Alcance:** Global
**Estado:** Aprobado

---

### 1. Renders Finales (Pantallas Clave)

**Pantalla 01: Home Page (Marketplace)**
- *Screenshot: `[Mockup_Home_Desktop.png]`*
- *Screenshot: `[Mockup_Home_Mobile.png]`*

**Pantalla 02: Detalles de Propiedad (Property Page)**
- *Screenshot: `[Mockup_Property_Desktop.png]`*
- *Screenshot: `[Mockup_Property_Mobile.png]`*

---

### 2. Especificaciones Visuales Aplicadas (Dev Handoff)

**Pantalla: Home Page B2C**
- **Hero Image:** Aplicado Overlay (40% negro) para contraste.
- **Hero H1 Title ("Encuentra tu refugio"):** Aplicado token tipografico `Epilogue` (Display-lg 48px), color Blanco `#ffffff`.
- **Search Bar (Buscador Global):** Aplicada forma de pildora (Pill) con esquinas 100% redondeadas. Fondo `#ffffff`, borde interno invisible, boton primario en `Deep Forest (#1B3022)` con texto `Be Vietnam Pro`.
- **Fondo General de la Grilla (Grid Background):** Aplicado token `Surface (#f9faf6)` para ambiente organico y nula fatiga visual.

**Pantalla: Property Page (Modulo MOD-PROP)**
- **Property Title:** Inyeccion de dato real ("Hacienda El Paraiso Cafetero"). Tipografia `Epilogue` en color oscuro `On-Surface (#1a1c1a)`.
- **Etiqueta de Precio:** Inyeccion de dato real ("$850.000 COP"). Tipografia `Epilogue`, color de acento `Clay Terracotta (#BC6C25)`.
- **Descripcion Larga:** Tipografia `Be Vietnam Pro` (Body-md 16px) asegurando legibilidad maxima.
- **Property Cards (Tarjetas Similares):** Fondo `#ffffff`, esquinas redondeadas `0.5rem (8px)`, sombra base ambiental de 15% opacidad color `Deep Forest`.

---

### 3. Estados Interactivos y Micro-interacciones

**Hover States (Navegacion Desktop)**
- **Property Cards:** Al pasar el raton, la tarjeta crece un 1% (escala 1.01) y la sombra ambiental (Tonal Layering) pasa de 15% a 25% de opacidad para dar retroalimentacion fisica sin parecer que "flota" artificialmente.
- **Botones Primarios (Deep Forest):** Se aclara u oscurece sutilmente la luminosidad del boton (Filter Brightness).

**Edge Cases & Errores (Checkout MOD-PAY)**
- **Validacion Fallida (Terminos Legales):** Si el usuario omite el checkbox, el contenedor estalla con un borde rojo solido (`#ba1a1a` Error Token), y un texto de ayuda inferior en `Be Vietnam Pro` rojo alerta aparece inmediatamente bajo la caja.
- **Modales Activos (Ej. Date Picker):** El fondo del portal se difumina (Glassmorphism) para aislar la accion, manteniendo los colores vivos de las fincas parcialmente visibles de fondo.
