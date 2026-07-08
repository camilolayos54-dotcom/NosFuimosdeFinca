# Wireframe Specifications: `/finca/[slug]` (Perfil de Propiedad)

**Ruta UI:** `/finca/[slug]` (Detalle Comercial de la Finca)
**Requisitos Funcionales Inyectados:** `MOD-PROP` (Galería Multimedia y Reglas de Negocio), `MOD-CAL` (Motor de Disponibilidad y Soft-Lock).

---

## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** Esta es la pantalla que **cierra la venta**. El turista ya hizo click, ahora quiere enamorarse de las fotos y confirmar si la finca está libre en sus fechas. La carga cognitiva debe dirigirse 100% a las imágenes y al precio.
- **Patrón Principal:** `Bento Grid Gallery + Sticky Sidebar Booking`.
  - **Desktop:** Usa un `Bento Grid` (Una cuadrícula asimétrica) en la parte superior para mostrar las 5 mejores fotos. Debajo, divide la pantalla en 2 columnas: 70% izquierda para leer la descripción, 30% derecha para un `Sticky Widget` (Un panel que baja contigo) que contiene el Calendario y el botón de reservar.
  - **Mobile:** Las fotos se convierten en un carrusel deslizable horizontalmente (Swipe). El botón de reservar se ancla en `Sticky Bottom` para que siempre esté al alcance del pulgar, ocultando el calendario hasta que el usuario lo toque.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Perfil de la Finca:

### A. Átomos
- `BentoImage` **(Obligatorio por MOD-PROP)**: Contenedor fotográfico con radios de borde variables dependiendo de su posición en la grilla.
- `RuleIcon` **(Obligatorio por MOD-PROP)**: Pequeño icono + texto para mostrar si aceptan mascotas o número de personas.
- `CalendarDay` **(Obligatorio por MOD-CAL)**: Celda del calendario. *Variantes: `Available`, `Selected`, `HardLocked` (Gris tachado), `SoftLocked` (Gris tachado).*

### B. Moléculas
- `HostProfileBadge`: Foto circular del dueño + Nombre y calificación.
- `CalendarMonth` **(Obligatorio por MOD-CAL)**: Grilla de 7x5 usando el átomo `CalendarDay`.
- `BookingSummary`: Desglose matemático (Ej. $500k x 2 noches = $1M).

### C. Organismos
- `HeroBentoGallery` **(Obligatorio por MOD-PROP)**: Agrupación de 5 `BentoImage`s formando un rectángulo perfecto.
- `FullscreenGalleryModal` **(Obligatorio por MOD-PROP)**: Modal oscuro a pantalla completa que permite ver las 50 fotos de la finca con flechas de navegación.
- `BookingWidget` **(Obligatorio por MOD-CAL)**: Tarjeta flotante que une (Precio + `CalendarMonth` + `BookingSummary` + Botón "Reservar").

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Jerarquía Visual LCP (Largest Contentful Paint):**
   - Según el NFR de rendimiento de `MOD-PROP`, las imágenes del `HeroBentoGallery` cargarán rapidísimo desde una CDN. Para evitar saltos en la pantalla (Cumulative Layout Shift), el componente debe tener un `aspect-ratio` fijo en CSS (Ej. 16:9 global).
2. **Ley de Fitts (Reserva Inmediata):**
   - En Mobile, el `BookingWidget` no cabe en la pantalla mientras se lee la descripción. Por tanto, debe estar encogido en un `Sticky Bottom Bar` que solo muestre el precio total y un botón brillante de "Reservar". Si el usuario lo toca, un `BottomSheet` emerge revelando el `CalendarMonth`.
3. **Carga Cognitiva (Feedback de Error):**
   - Si un usuario selecciona fechas en el calendario que están tachadas (`HardLocked`), el botón de "Reservar" debe mutar a estado `Disabled` de inmediato para prevenir un viaje en vano hacia el servidor.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/finca/[slug]`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el layout de 2 columnas. A la derecha, el `BookingWidget` debe verse claramente pegado (`sticky`) mientras haces scroll en la columna izquierda.
- `[ ]` **Mobile (390px):** Dibuja el carrusel de imágenes superior y la barra inferior pegajosa (`Sticky Bottom`) con el botón de reserva.

### ✅ Mutaciones de Estado y Módulos
- `[ ]` **Galería Expandida (Obligatorio por MOD-PROP):** Dibuja el `FullscreenGalleryModal` abierto, mostrando cómo el turista navega foto por foto en pantalla completa.
- `[ ]` **Selección de Fechas (Obligatorio por MOD-CAL):** Dibuja el `BookingWidget` reaccionando a la selección: El usuario tocó dos días (Check-in y Check-out). Debe aparecer el `BookingSummary` mostrando la multiplicación matemática del total a pagar.

### ✅ Excepciones y Barreras (Unhappy Paths)
- `[ ]` **Overbooking Collision (Obligatorio por MOD-CAL):** Imagina que el turista da clic en "Reservar", pero justo 1 milisegundo antes, otro turista bloqueó esas mismas fechas. Dibuja la pantalla donde el sistema rechaza la acción mostrando un Toast rojo que diga *"Lo sentimos, alguien más acaba de reservar estas fechas. Por favor, selecciona otras"*.
