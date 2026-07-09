# Design System & UI Kit

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 — Modelado del Sistema
**Alcance:** Global
**Estado:** Aprobado
![[Pasted image 20260709060236.png]]
---

### 1. Fundamentos Visuales (Tokens de Diseño)

**Tipografía (Brand: Rural Sanctuary)**
- Tipografía de Títulos (Display/Headlines): `Epilogue` (Sensación geométrica, editorial y rústica).
- Tipografía de Cuerpo (Body/Labels): `Be Vietnam Pro` (Legibilidad alta, amigable y contemporánea).
- Escala: `Display-lg (48px)`, `Headline-lg (32px)`, `Body-lg (18px)`, `Label-md (12px)`.

**Paleta de Colores (Rural Sanctuary)**
- Primario (Deep Forest): `#1B3022` (Navegación, botones primarios).
- Secundario (Clay Terracotta): `#BC6C25` (Acentos, etiquetas de precio).
- Terciario (Sage): `#2c3120` (Interacciones secundarias).
- Fondo/Superficie (Neutral): `#f9faf6` (Blanco humo cálido para reducir fatiga visual).
- Superficie Interactiva (Tarjetas): `#ffffff` (Blanco puro con sombra difusa).
- Error: `#ba1a1a` (Rojo alerta).

**Cuadrícula y Espaciado (Grid & Spacing)**
- Base Matemática: `8px`.
- Layout: Híbrido (Contenedor máximo de 1280px en Desktop, fluido en Mobile).
- Ritmo Vertical: `stack-sm (8px)`, `stack-md (16px)`, `stack-lg (32px)`.
- Border Radius (Global): Formas redondeadas `md (0.75rem / 12px)` para suavizar el aspecto clínico.

---

### 2. Biblioteca de Componentes (Diseño Atómico)

#### Átomos (Atoms)
**Botón Primario (Primary Button)**
- Fondo (BG): `Deep Forest (#1B3022)`.
- Texto: Blanco `#ffffff`, Tipografía: `Be Vietnam Pro (Label-lg)`.
- Border Radius: `0.75rem` (12px) o Forma de Píldora (Pill).

**Campo de Entrada de Texto (Input Field)**
- Fondo: `#f9faf6`.
- Borde: 1px sólido `Sage (#2c3120)`.
- Estado Focus: Borde grueso en `Deep Forest`.
- Border Radius: `0.5rem` (8px).

**Etiqueta de Precio (Price Tag)**
- Tipografía: `Epilogue`.
- Color: `Clay Terracotta (#BC6C25)`.

#### Moléculas (Molecules)
**Tarjeta de Propiedad (Property Card)**
- Contiene: Imagen (Ratio 16:9) + Título (Epilogue) + Price Tag (Terracotta).
- Fondo: Blanco `#ffffff`.
- Esquinas: Redondeadas `0.5rem`.

#### Organismos (Organisms)
**Barra de Búsqueda Global (Search Bar Pill)**
- Contenedor: Forma de píldora (Pill shape) destacada en el tope de la pantalla.
- Contiene: Inputs (Ubicación, Fechas, Huéspedes) + Botón Primario de Búsqueda de alto contraste.

---

### 3. Reglas de Interactividad, Profundidad y Accesibilidad

- **Elevación (Tonal Layering):** Cero elementos "flotantes". Las superficies se elevan mediante sombras ambientales muy suaves (15% de opacidad del color primario).
- **Interacción Táctil (Hover):** Al pasar el cursor sobre un `Property Card`, la escala aumenta un 1% y la sombra se profundiza para brindar respuesta física.
- **Overlays (Modales y Fechas):** Utilizan desenfoque (Glassmorphism) para mantener visible la fotografía de la finca de fondo.
- **Contraste WCAG:** El fondo `Deep Forest` contrastado con texto blanco supera holgadamente el mínimo de 4.5:1 exigido por WCAG AA.
