# Wireframe Specifications: `/search` (Resultados de Busqueda)

**Ruta UI:** `/search` (Catalogo Filtrado)
**Requisitos Funcionales Inyectados:** `MOD-SRCH` (Filtros, Ordenamiento y Paginacion Infinita).

---

# RESULTADOS
![search_page_desktop.png](search_page_desktop.png)
![search_page_mobile.png](search_page_mobile.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El usuario ya hizo una busqueda en el Home y ahora esta en modo "Evaluacion Comparativa". Su carga cognitiva es alta porque esta leyendo precios, comodidades y evaluando fotos. Debemos evitar que se sature visualmente.
- **Patron Principal:** `Sidebar Filters + Infinite Grid` (Desktop) / `Sticky Filter Bar + Modal` (Mobile).
  - **Desktop:** El clasico layout de e-commerce. Menu lateral fijo a la izquierda con todos los filtros de `MOD-SRCH` y una gran grilla a la derecha.
  - **Mobile:** Por falta de espacio, los filtros se esconden tras un boton flotante (`Sticky`) que despliega un modal de pantalla completa. La paginacion infinita reemplaza a los botones de "Siguiente pagina" para no romper el flujo de lectura (Requisito `CR-SRCH-03`).

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la pagina `/search`:

### A. Atomos
- `SortDropdown` **(Obligatorio por MOD-SRCH)**: Menu desplegable para ordenar (Menor precio, Mayor precio, Calificacion).
- `CheckboxGroup` **(Obligatorio por MOD-SRCH)**: Lista de checkboxes para seleccionar amenidades (Piscina, Mascotas). *Variantes: `Unchecked`, `Checked`, `Disabled`.*
- `PriceRangeSlider` **(Obligatorio por MOD-SRCH)**: Control deslizante con dos manijas (Minimo y Maximo).

### B. Moleculas
- `ActiveFilterPill`: Pequena pildora que muestra un filtro activo (Ej. "Con Piscina ") para que el usuario pueda removerlo rapidamente.
- `PaginationLoader` **(Obligatorio por MOD-SRCH)**: Un texto o icono animado ("Cargando mas fincas...") que aparece al final de la pagina.

### C. Organismos
- `FilterSidebar` **(Obligatorio por MOD-SRCH)**: Bloque vertical que agrupa el `PriceRangeSlider` y multiples `CheckboxGroup`.
- `MobileFilterModal` **(Obligatorio por MOD-SRCH)**: Version adaptada del Sidebar que se sobrepone a toda la pantalla en telefonos.
- `SearchResultsGrid` **(Obligatorio por MOD-PROP)**: Una cuadricula que recicla las `PropertyCard`s creadas en el Home.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Gestion de Memoria (Infinite Scroll):**
   - Para evitar que la vista colapse al cargar la pagina 10 de resultados, en Figma debes indicar que la grilla es dinamica (Paginacion Infinita). Al final de la grilla siempre debe haber un espacio reservado para el `PaginationLoader`.
2. **Ley de Proximidad (Filtros Activos):**
   - Las `ActiveFilterPill` deben renderizarse justo debajo del `SortDropdown` y arriba de la grilla de resultados. El usuario necesita ver de un vistazo rapido por que solo le aparecen 3 fincas (Ej. Ah, es que tengo marcado "Solo Mascotas").
3. **Carga Cognitiva (Mobile Sticky Bar):**
   - En Mobile, el boton de "Filtros" y "Ordenar" debe estar anclado en `Sticky Bottom` (Flotando abajo de la pantalla) para que el pulgar lo alcance instantaneamente sin importar cuanto *scroll* haya hecho el turista.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/search`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el layout de 2 columnas (`FilterSidebar` a la izquierda, `SearchResultsGrid` a la derecha).
- `[ ]` **Mobile (390px):** Dibuja la grilla de resultados ocupando el 100% y el boton de "Filtros" flotando abajo (`Sticky Bottom`).

### Mutaciones de Estado y Paginacion
- `[ ]` **Filtros Abiertos (Mobile) (Obligatorio por MOD-SRCH):** Dibuja el `MobileFilterModal` abierto, mostrando los sliders de precios y checkboxes.
- `[ ]` **Paginacion Infinita (Obligatorio por MOD-SRCH):** Dibuja el final de la pantalla mostrando el `PaginationLoader` justo cuando el usuario llega al final de las fincas cargadas.

### Excepciones (Unhappy Paths)
- `[ ]` **Zero Results (Cross-Selling) (Obligatorio por MOD-SRCH):** Pantalla donde el usuario aplico demasiados filtros. Dibuja el Empty State tolerante (Como en el Home) sugiriendo *"Borra el filtro de 'Piscina' para ver 40 resultados mas"*.
