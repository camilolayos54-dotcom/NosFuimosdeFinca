# Wireframe Specifications: `/` (Home B2C)

**Ruta UI:** `/` (Landing Page Publica)
**Requisitos Funcionales Inyectados:** `MOD-SRCH` (Buscador y Tolerancia), `MOD-PROP` (Grilla de Propiedades Destacadas).

---

# RESULTADOS
![body.png](body.png)
![body_phone.png](body_phone.png)


- **Diagnostico:** Esta es la fachada comercial (Marketplace) del proyecto. El Turista B2C tiene una carga cognitiva baja inicial; quiere inspirarse (Ver fincas hermosas) pero tambien quiere utilidad inmediata (Buscar fechas disponibles).
- **Patron Principal:** `Hero Search + Edge-to-Edge Grid`. 
  - La mitad superior debe ser inmersiva: Una gran imagen de fondo (`Edge-to-Edge`) con el buscador (`MOD-SRCH`) superpuesto en el centro para captar la atencion inmediata.
  - La mitad inferior debe usar el patron `Infinite Card Grid`, mostrando una grilla de tarjetas visuales (`MOD-PROP`) sin distracciones de texto excesivo.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en tu Design System de Figma para ensamblar la pagina de Inicio:

### A. Atomos
- `HeroImage`: Fotografia panoramica de alta calidad de una finca (Asset estatico).
- `SearchInput` **(Obligatorio por MOD-SRCH)**: Campo de texto/numero. *Variantes: `DateRange`, `GuestCounter`, `PriceSlider`.*
- `FilterChip` **(Obligatorio por MOD-SRCH)**: Pildoras booleanas para amenidades. *Variantes: `Default`, `Selected` (Borde oscuro).*
- `PropertyImage`: Contenedor 4:3 para la foto de la finca. *Debe tener bordes redondeados (`border-radius: 12px`).*
- `PriceTag`: Tipografia en negrita para el precio por noche (Ej. "$500.000 COP / noche").

### B. Moleculas
- `SearchBar` **(Obligatorio por MOD-SRCH)**: Une (`SearchInput` Fechas + `SearchInput` Personas + Boton Primario "Buscar").
- `PropertyCard` **(Obligatorio por MOD-PROP)**: Une (`PropertyImage` + Titulo + Ubicacion + `PriceTag`).

### C. Organismos
- `HeroSection`: Une (`HeroImage` de fondo + Titulo H1 Aspiracional + `SearchBar` flotando en el centro).
- `FilterDrawer` **(Obligatorio por MOD-SRCH)**: Un panel deslizable (Modal en Mobile, Horizontal en Desktop) que une todos los `FilterChip` y `PriceSlider`.
- `FeaturedGrid` **(Obligatorio por MOD-PROP)**: Une un grid de 12 a 20 `PropertyCard`s apiladas en columnas (1 en Mobile, 4 en Desktop).

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Ley de Fitts (Thumb Zone para Busqueda):**
   - En Mobile (390px), el `SearchBar` no debe ser un bloque gigante desplegado en el Hero. En su lugar, usa un `Sticky Top Pill` (una pildora pegada al tope que diga " Adonde vas?") que al tocarse abra un modal a pantalla completa para que el usuario use sus pulgares comodamente. En Desktop si debe ir extendido en el centro.
2. **Accesibilidad (a11y) y Legibilidad:**
   - La `HeroImage` obligatoriamente debe tener un `Overlay` (Capa negra con 40% de opacidad). Esto garantiza que el texto blanco del titulo H1 y el Buscador tengan un contraste superior a `4.5:1` frente a cualquier fotografia.
3. **Skeleton Loaders (Obligatorio por NFR-SRCH-01 - Percepcion de Velocidad):**
   - Para cumplir con el requerimiento de latencia (`LCP < 2.5s`), mientras el `MOD-PROP` consulta la Base de Datos, se deben pintar `Skeleton Cards` grises parpadeantes con la misma forma y tamano del `PropertyCard`.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el `HeroSection` completo (Imagen + Buscador) y debajo un `FeaturedGrid` con 4 columnas.
- `[ ]` **Mobile (390px):** Dibuja el Hero con la pildora de busqueda colapsada, y el `FeaturedGrid` en 1 columna.

### Estados Transitorios (Loaders)
- `[ ]` **Loading Grid (Obligatorio por MOD-SRCH):** Disena la pantalla de la grilla mostrando 4 `Skeleton Cards` mientras el sistema busca las fincas.

### Excepciones y Tolerancia Comercial (Unhappy Paths)
- `[ ]` **Empty State Cross-Selling (Obligatorio por MOD-SRCH):** Disena el estado cuando el turista filtra fincas imposibles (Ej. 50 personas a 1 peso). El sistema lanza `length === 0`. Dibuja un Organismo amigable con una ilustracion que diga *"No encontramos coincidencias exactas, pero mira estas opciones similares"*, seguido de una grilla de fincas tolerantes (Otras fechas u otro precio).
- `[ ]` **Drawer de Filtros Abierto (Obligatorio por MOD-SRCH):** Dibuja la vista donde el usuario expande el `FilterDrawer` para seleccionar amenidades (Piscina, Mascotas).
