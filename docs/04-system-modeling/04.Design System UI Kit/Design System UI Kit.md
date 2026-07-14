# Design System & UI Kit

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Alcance:** Global
**Estado:** Aprobado
---
![Pasted image 20260709060236.png](Pasted%20image%2020260709060236.png)
### 1. Fundamentos Visuales (Tokens de Diseno)

**Tipografia (Brand: Rural Sanctuary)**
- Tipografia de Titulos (Display/Headlines): `Epilogue` (Sensacion geometrica, editorial y rustica).
- Tipografia de Cuerpo (Body/Labels): `Be Vietnam Pro` (Legibilidad alta, amigable y contemporanea).
- Escala: `Display-lg (48px)`, `Headline-lg (32px)`, `Body-lg (18px)`, `Label-md (12px)`.

**Paleta de Colores (Rural Sanctuary)**
- Primario (Deep Forest): `#1B3022` (Navegacion, botones primarios).
- Secundario (Clay Terracotta): `#BC6C25` (Acentos, etiquetas de precio).
- Terciario (Sage): `#2c3120` (Interacciones secundarias).
- Fondo/Superficie (Neutral): `#f9faf6` (Blanco humo calido para reducir fatiga visual).
- Superficie Interactiva (Tarjetas): `#ffffff` (Blanco puro con sombra difusa).
- Error: `#ba1a1a` (Rojo alerta).

**Cuadricula y Espaciado (Grid & Spacing)**
- Base Matematica: `8px`.
- Layout: Hibrido (Contenedor maximo de 1280px en Desktop, fluido en Mobile).
- Ritmo Vertical: `stack-sm (8px)`, `stack-md (16px)`, `stack-lg (32px)`.
- Border Radius (Global): Formas redondeadas `md (0.75rem / 12px)` para suavizar el aspecto clinico.

---

### 2. Biblioteca de Componentes (Diseno Atomico)

#### Atomos (Atoms)
**Boton Primario (Primary Button)**
- Fondo (BG): `Deep Forest (#1B3022)`.
- Texto: Blanco `#ffffff`, Tipografia: `Be Vietnam Pro (Label-lg)`.
- Border Radius: `0.75rem` (12px) o Forma de Pildora (Pill).

**Campo de Entrada de Texto (Input Field)**
- Fondo: `#f9faf6`.
- Borde: 1px solido `Sage (#2c3120)`.
- Estado Focus: Borde grueso en `Deep Forest`.
- Border Radius: `0.5rem` (8px).

**Etiqueta de Precio (Price Tag)**
- Tipografia: `Epilogue`.
- Color: `Clay Terracotta (#BC6C25)`.

#### Moleculas (Molecules)
**Tarjeta de Propiedad (Property Card)**
- Contiene: Imagen (Ratio 16:9) + Titulo (Epilogue) + Price Tag (Terracotta).
- Fondo: Blanco `#ffffff`.
- Esquinas: Redondeadas `0.5rem`.

#### Organismos (Organisms)
**Barra de Busqueda Global (Search Bar Pill)**
- Contenedor: Forma de pildora (Pill shape) destacada en el tope de la pantalla.
- Contiene: Inputs (Ubicacion, Fechas, Huespedes) + Boton Primario de Busqueda de alto contraste.

---

### 3. Reglas de Interactividad, Profundidad y Accesibilidad

- **Elevacion (Tonal Layering):** Cero elementos "flotantes". Las superficies se elevan mediante sombras ambientales muy suaves (15% de opacidad del color primario).
- **Interaccion Tactil (Hover):** Al pasar el cursor sobre un `Property Card`, la escala aumenta un 1% y la sombra se profundiza para brindar respuesta fisica.
- **Overlays (Modales y Fechas):** Utilizan desenfoque (Glassmorphism) para mantener visible la fotografia de la finca de fondo.
- **Contraste WCAG:** El fondo `Deep Forest` contrastado con texto blanco supera holgadamente el minimo de 4.5:1 exigido por WCAG AA.
