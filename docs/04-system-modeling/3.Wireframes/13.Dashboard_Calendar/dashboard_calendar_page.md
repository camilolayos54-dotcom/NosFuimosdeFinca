# Wireframe Specifications: `/dashboard/calendario` (Gestor de Fechas B2B)

**Ruta UI:** `/dashboard/calendario` (Calendario Maestro B2B)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (Mantener la navegación lateral).
**Requisitos Funcionales Inyectados:** `MOD-CAL` (Bloqueos Manuales y Visor de Overbooking).

---

# RESULTADOS
![Calendario Maestro B2B - Wireframe Estricto Desktop.png](<Calendario Maestro B2B - Wireframe Estricto Desktop.png>)
![Calendario Maestro B2B - Wireframe Mobile.png](<Calendario Maestro B2B - Wireframe Mobile.png>)


## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** El finquero necesita administrar su tiempo. Quiere saber qué fin de semana está vendido, cuál está libre, y quiere poder bloquear una fecha rápidamente si su familia decide ir a la finca.
- **Patrón Principal:** `Full-Width Master Calendar`.
  - Un calendario interactivo inmenso que ocupa todo el espacio de trabajo disponible.
  - Al hacer clic en los días (o arrastrar el ratón), debe emerger un panel lateral o modal pequeño (`Action Drawer`) para ejecutar bloqueos.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Calendario B2B:

### A. Átomos
- `CalendarCell` **(Obligatorio por MOD-CAL)**: Celda diaria. *Debe tener variantes de color muy estrictas: Blanco (`Available`), Azul (`Hard_Lock` - Vendido), Gris oscuro (`Manual_Block` - Cerrado por el dueño), Naranja (`Soft_Lock` - Alguien está pagando).*
- `PriceTagInput`: Un campo pequeño dentro del `CalendarCell` por si el dueño quiere cobrar más caro un festivo.

### B. Moléculas
- `MonthGrid`: Cuadrícula de 7x5 usando `CalendarCell`.
- `LegendBar`: Barra superior explicando los colores (Azul = Vendido, Gris = Bloqueado).

### C. Organismos
- `MasterCalendarView` **(Obligatorio por MOD-CAL)**: Une múltiples `MonthGrid` (Vista anual o trimestral) con flechas de navegación.
- `ActionDrawer`: Panel deslizante a la derecha que aparece al tocar unos días libres, con un botón gigante que dice "Bloquear Fechas".

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Codificación de Color (Regla Anti-Errores):**
   - Es crítico que el Finquero no confunda un día que él mismo bloqueó (`Manual_Block`) con un día que le compró un turista (`Hard_Lock`). Usa colores semánticamente diferentes.
2. **Interacción de Bloqueo (MOD-CAL):**
   - El `ActionDrawer` debe explicar explícitamente la acción. Si oprime "Bloquear", debe haber un pequeño subtítulo *"El turista no podrá ver ni comprar estas fechas en la página principal"*.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/calendario`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Vista Calendario B2B:** Dibuja el `MasterCalendarView` dentro del Layout del Dashboard. Asegúrate de pintar algunos días en azul, gris y blanco.
- `[ ]` **Drawer de Bloqueo (Obligatorio por MOD-CAL):** Simula que el usuario hizo clic en los días 14 y 15. Dibuja el `ActionDrawer` abierto ofreciendo la opción "Bloquear Fechas".

### ✅ Excepciones de Sincronización (Unhappy Paths)
- `[ ]` **Conflicto Soft-Lock (Obligatorio por MOD-CAL):** Imagina que el finquero hace clic en "Bloquear Fechas", pero justo en ese instante un turista en su casa está metiendo la tarjeta de crédito (Estado `Soft_Lock`). Dibuja un `ToastNotification` rojo de error B2B: *"No puedes bloquear estas fechas porque un turista está en la pasarela de pagos. Intenta en 10 minutos"*.
