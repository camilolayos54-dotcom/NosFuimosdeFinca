# Wireframe Specifications: `/dashboard/calendario` (Gestor de Fechas B2B)

**Ruta UI:** `/dashboard/calendario` (Calendario Maestro B2B)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (Mantener la navegacion lateral).
**Requisitos Funcionales Inyectados:** `MOD-CAL` (Bloqueos Manuales y Visor de Overbooking).

---

# RESULTADOS
![Calendario Maestro B2B - Wireframe Estricto Desktop.png](Calendario%20Maestro%20B2B%20-%20Wireframe%20Estricto%20Desktop.png)
![Calendario Maestro B2B - Wireframe Mobile.png](Calendario%20Maestro%20B2B%20-%20Wireframe%20Mobile.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El finquero necesita administrar su tiempo. Quiere saber que fin de semana esta vendido, cual esta libre, y quiere poder bloquear una fecha rapidamente si su familia decide ir a la finca.
- **Patron Principal:** `Full-Width Master Calendar`.
  - Un calendario interactivo inmenso que ocupa todo el espacio de trabajo disponible.
  - Al hacer clic en los dias (o arrastrar el raton), debe emerger un panel lateral o modal pequeno (`Action Drawer`) para ejecutar bloqueos.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar el Calendario B2B:

### A. Atomos
- `CalendarCell` **(Obligatorio por MOD-CAL)**: Celda diaria. *Debe tener variantes de color muy estrictas: Blanco (`Available`), Azul (`Hard_Lock` - Vendido), Gris oscuro (`Manual_Block` - Cerrado por el dueno), Naranja (`Soft_Lock` - Alguien esta pagando).*
- `PriceTagInput`: Un campo pequeno dentro del `CalendarCell` por si el dueno quiere cobrar mas caro un festivo.

### B. Moleculas
- `MonthGrid`: Cuadricula de 7x5 usando `CalendarCell`.
- `LegendBar`: Barra superior explicando los colores (Azul = Vendido, Gris = Bloqueado).

### C. Organismos
- `MasterCalendarView` **(Obligatorio por MOD-CAL)**: Une multiples `MonthGrid` (Vista anual o trimestral) con flechas de navegacion.
- `ActionDrawer`: Panel deslizante a la derecha que aparece al tocar unos dias libres, con un boton gigante que dice "Bloquear Fechas".

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Codificacion de Color (Regla Anti-Errores):**
   - Es critico que el Finquero no confunda un dia que el mismo bloqueo (`Manual_Block`) con un dia que le compro un turista (`Hard_Lock`). Usa colores semanticamente diferentes.
2. **Interaccion de Bloqueo (MOD-CAL):**
   - El `ActionDrawer` debe explicar explicitamente la accion. Si oprime "Bloquear", debe haber un pequeno subtitulo *"El turista no podra ver ni comprar estas fechas en la pagina principal"*.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/calendario`:

### Pantallas Base (Happy Path)
- `[ ]` **Vista Calendario B2B:** Dibuja el `MasterCalendarView` dentro del Layout del Dashboard. Asegurate de pintar algunos dias en azul, gris y blanco.
- `[ ]` **Drawer de Bloqueo (Obligatorio por MOD-CAL):** Simula que el usuario hizo clic en los dias 14 y 15. Dibuja el `ActionDrawer` abierto ofreciendo la opcion "Bloquear Fechas".

### Excepciones de Sincronizacion (Unhappy Paths)
- `[ ]` **Conflicto Soft-Lock (Obligatorio por MOD-CAL):** Imagina que el finquero hace clic en "Bloquear Fechas", pero justo en ese instante un turista en su casa esta metiendo la tarjeta de credito (Estado `Soft_Lock`). Dibuja un `ToastNotification` rojo de error B2B: *"No puedes bloquear estas fechas porque un turista esta en la pasarela de pagos. Intenta en 10 minutos"*.
