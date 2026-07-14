# Wireframe Specifications: `/dashboard/reservas` (Buzon de Solicitudes)

**Ruta UI:** `/dashboard/reservas` (Buzon de Aprobacion B2B)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (Es una vista interna).
**Requisitos Funcionales Inyectados:** `MOD-RSV` (Aprobacion/Rechazo de Transacciones y Reembolsos).

---

# RESULTADOS
![Buzon de Reservas - Split View Wireframe Desktop.png](Buz%C3%B3n%20de%20Reservas%20-%20Split%20View%20Wireframe%20Desktop.png)
![Buzon de Reservas - Wireframe Mobile (Optimized).png](Buz%C3%B3n%20de%20Reservas%20-%20Wireframe%20Mobile%20%28Optimized%29.png)
![Modal de Rechazo - Wireframe Mobile.png](Modal%20de%20Rechazo%20-%20Wireframe%20Mobile.png)
![MODAL OVERLAY.png](MODAL%20OVERLAY.png)
![BACKGROUND_ Reservation Inbox Split View (Dimmed).png](BACKGROUND_%20Reservation%20Inbox%20Split%20View%20%28Dimmed%29.png)




## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El dinero del turista ya esta retenido por Wompi (`MOD-PAY`). Aqui el finquero entra como un "Juez" a revisar si el cliente le da confianza o no antes de aceptar la reserva.
- **Patron Principal:** `Inbox / Split Master-Detail`.
  - Igual que un correo electronico. La pantalla se divide en 2.
  - Columna Izquierda (Master): Lista de reservas ordenadas cronologicamente.
  - Columna Derecha (Detail): Los datos completos del Turista seleccionado (Nombre, edades de los huespedes, precio) y dos botones gigantes: "Aprobar" o "Rechazar".

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar el Buzon de Reservas:

### A. Atomos
- `InboxAvatar`: Circulo con las iniciales del Turista.
- `DangerButton` **(Obligatorio por MOD-RSV)**: Boton con texto rojo y borde rojo (Rechazar).
- `ApproveButton` **(Obligatorio por MOD-RSV)**: Boton verde o primario solido (Aprobar).

### B. Moleculas
- `InboxListItem`: Fila a la izquierda. Une (`InboxAvatar` + Nombre + Fechas de viaje). *Debe tener un punto naranja brillante si esta "Pendiente de Aprobacion"*.
- `TouristProfileBlock`: Bloque que agrupa los nombres y documentos de identidad de las 15 personas que van a ir a la finca (Exigido por `MOD-RSV`).

### C. Organismos
- `ReservationDetailCard` **(Obligatorio por MOD-RSV)**: El panel derecho. Une (`TouristProfileBlock` + Desglose de Dinero ganado + `ApproveButton` + `DangerButton`).
- `RejectionModal` **(Obligatorio por MOD-RSV)**: Modal critico que aparece si se oprime "Rechazar".

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Gravedad de la Decision (Rechazo B2B):**
   - Segun el UC-RSV-04, rechazar a un turista implica que la plataforma le devolvera su dinero mediante un Reembolso Wompi y le enviara un correo triste.
   - Por esto, el boton "Rechazar" NUNCA puede ser una accion de 1 clic. Obligatoriamente debe abrir el `RejectionModal` pidiendole al finquero que seleccione un motivo (Ej. "Mantenimiento imprevisto", "No cumples con las reglas") y confirme de nuevo.
2. **Carga Cognitiva (Legibilidad):**
   - En Mobile, el patron Master-Detail no cabe. Se debe usar navegacion Stack (Haz clic en la fila del inbox, y se abre una nueva pantalla completa con el detalle de la reserva).

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/reservas`:

### Pantallas Base (Happy Path)
- `[ ]` **Inbox Desktop (1440px):** Layout dividido. A la izquierda la lista de turistas que ya pagaron, a la derecha el `ReservationDetailCard` esperando veredicto.
- `[ ]` **Inbox Mobile (390px):** Lista simple ocupando toda la pantalla.

### Mutaciones Transaccionales Criticas
- `[ ]` **Modal de Rechazo (Obligatorio por MOD-RSV):** Dibuja el `RejectionModal`. Ponle un texto de advertencia explicito: *"Si rechazas esta reserva, el dinero sera reembolsado al turista de inmediato y las fechas quedaran libres"*.
- `[ ]` **Aprobacion Exitosa:** El usuario oprimio Aprobar. Dibuja un `ToastNotification` verde que diga *"Reserva Confirmada. Le hemos enviado las instrucciones al turista"*.
