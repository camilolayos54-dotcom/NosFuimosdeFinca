# Wireframe Specifications: `/dashboard/reservas` (Buzón de Solicitudes)

**Ruta UI:** `/dashboard/reservas` (Buzón de Aprobación B2B)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (Es una vista interna).
**Requisitos Funcionales Inyectados:** `MOD-RSV` (Aprobación/Rechazo de Transacciones y Reembolsos).

---

## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** El dinero del turista ya está retenido por Wompi (`MOD-PAY`). Aquí el finquero entra como un "Juez" a revisar si el cliente le da confianza o no antes de aceptar la reserva.
- **Patrón Principal:** `Inbox / Split Master-Detail`.
  - Igual que un correo electrónico. La pantalla se divide en 2.
  - Columna Izquierda (Master): Lista de reservas ordenadas cronológicamente.
  - Columna Derecha (Detail): Los datos completos del Turista seleccionado (Nombre, edades de los huéspedes, precio) y dos botones gigantes: "Aprobar" o "Rechazar".

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Buzón de Reservas:

### A. Átomos
- `InboxAvatar`: Círculo con las iniciales del Turista.
- `DangerButton` **(Obligatorio por MOD-RSV)**: Botón con texto rojo y borde rojo (Rechazar).
- `ApproveButton` **(Obligatorio por MOD-RSV)**: Botón verde o primario sólido (Aprobar).

### B. Moléculas
- `InboxListItem`: Fila a la izquierda. Une (`InboxAvatar` + Nombre + Fechas de viaje). *Debe tener un punto naranja brillante si está "Pendiente de Aprobación"*.
- `TouristProfileBlock`: Bloque que agrupa los nombres y documentos de identidad de las 15 personas que van a ir a la finca (Exigido por `MOD-RSV`).

### C. Organismos
- `ReservationDetailCard` **(Obligatorio por MOD-RSV)**: El panel derecho. Une (`TouristProfileBlock` + Desglose de Dinero ganado + `ApproveButton` + `DangerButton`).
- `RejectionModal` **(Obligatorio por MOD-RSV)**: Modal crítico que aparece si se oprime "Rechazar".

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Gravedad de la Decisión (Rechazo B2B):**
   - Según el UC-RSV-04, rechazar a un turista implica que la plataforma le devolverá su dinero mediante un Reembolso Wompi y le enviará un correo triste.
   - Por esto, el botón "Rechazar" NUNCA puede ser una acción de 1 clic. Obligatoriamente debe abrir el `RejectionModal` pidiéndole al finquero que seleccione un motivo (Ej. "Mantenimiento imprevisto", "No cumples con las reglas") y confirme de nuevo.
2. **Carga Cognitiva (Legibilidad):**
   - En Mobile, el patrón Master-Detail no cabe. Se debe usar navegación Stack (Haz clic en la fila del inbox, y se abre una nueva pantalla completa con el detalle de la reserva).

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/reservas`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Inbox Desktop (1440px):** Layout dividido. A la izquierda la lista de turistas que ya pagaron, a la derecha el `ReservationDetailCard` esperando veredicto.
- `[ ]` **Inbox Mobile (390px):** Lista simple ocupando toda la pantalla.

### ✅ Mutaciones Transaccionales Críticas
- `[ ]` **Modal de Rechazo (Obligatorio por MOD-RSV):** Dibuja el `RejectionModal`. Ponle un texto de advertencia explícito: *"Si rechazas esta reserva, el dinero será reembolsado al turista de inmediato y las fechas quedarán libres"*.
- `[ ]` **Aprobación Exitosa:** El usuario oprimió Aprobar. Dibuja un `ToastNotification` verde que diga *"Reserva Confirmada. Le hemos enviado las instrucciones al turista"*.
