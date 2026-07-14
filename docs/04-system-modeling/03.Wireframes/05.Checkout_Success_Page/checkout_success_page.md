# Wireframe Specifications: `/checkout/success` (Confirmacion de Pago)

**Ruta UI:** `/checkout/success` (Pagina Final del Embudo B2C)
**Requisitos Funcionales Inyectados:** `MOD-PAY` (Recibo de Transaccion Wompi).

---

## Resultados
![Confirmacion de Pago - Wireframe Estricto Desktop.png](Confirmaci%C3%B3n%20de%20Pago%20-%20Wireframe%20Estricto%20Desktop.png)
![Confirmacion de Pago - Wireframe Estricto Mobile.png](Confirmaci%C3%B3n%20de%20Pago%20-%20Wireframe%20Estricto%20Mobile.png)

- **Diagnostico:** El Turista acaba de entregarle su dinero a una plataforma en internet. Su carga cognitiva bajo a cero, pero su nivel de ansiedad por confirmacion esta al maximo. Necesita saber que todo salio bien y que debe hacer ahora.
- **Patron Principal:** `Success Celebration + Clear Next Steps`.
  - El diseno debe ser exultante y tranquilizador. Un gran icono de exito en el centro superior.
  - El Navbar vuelve a aparecer, devolviendole el control de navegacion al usuario.
  - La pantalla se compone de un bloque central (Tarjeta de Recibo) que resume la operacion, seguido de instrucciones hiper-claras de que esperar (Ej. "El dueno de la finca tiene 90 minutos para aceptar tu solicitud. Revisa tu correo").

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la pantalla de Exito:

### A. Atomos
- `SuccessAnimation`: Una ilustracion o animacion Lottie (Checkmark verde grande y amigable).
- `TransactionRef` **(Obligatorio por MOD-PAY)**: Texto monoespaciado en color gris (Ej. `Ref: WOMPI-9A8B7C6D`).
- `SecondaryButton`: Boton para volver al Inicio o imprimir el recibo.

### B. Moleculas
- `StatusBanner`: Franja de color que indica el estado actual (Ej. Amarillo: "Esperando Confirmacion del Dueno").
- `ReceiptRow` **(Obligatorio por MOD-PAY)**: Fila doble texto para datos clave (Fecha, Monto Pagado, Tarjeta usada).

### C. Organismos
- `DigitalReceiptCard` **(Obligatorio por MOD-PAY)**: Una tarjeta con apariencia de recibo o tiquete de avion. Une (`SuccessAnimation` + Titulo " Pago Procesado!" + Multiples `ReceiptRow` + `TransactionRef`).
- `NextStepsBlock`: Un bloque debajo del recibo con 3 pasos (Iconos + Texto) explicando: 1. Pago retenido seguro, 2. El finquero te aprueba, 3. Empacas maletas!.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Jerarquia Visual de Tranquilidad:**
   - El elemento mas grande de la pantalla debe ser el `SuccessAnimation` y el monto total cobrado. El turista no debe esforzarse por buscar cuanto se le desconto de su tarjeta.
2. **Claridad del Estado Transaccional:**
   - Segun las reglas de `MOD-RSV`, el hecho de que Wompi cobre no significa que la reserva este asegurada. Significa que el dinero esta retenido hasta que el Finquero apruebe. El `StatusBanner` debe dejar esto explicitamente claro usando lenguaje humano (No jerga bancaria).
3. **Escaneabilidad (Receipt Print):**
   - El `DigitalReceiptCard` debe tener un diseno que sea amigable para imprimir (`Ctrl+P` o Guardar como PDF), con fondo blanco puro y sin sombras complejas.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/checkout/success`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja la pantalla con el `DigitalReceiptCard` centrado y el `NextStepsBlock` debajo. El Navbar y Footer normales deben volver a verse.
- `[ ]` **Mobile (390px):** Layout en 1 columna, ocupando el ancho completo de la pantalla para simular un tiquete.

### Mutaciones de Estado y Modulos
- `[ ]` **Recibo Oficial (Obligatorio por MOD-PAY):** Dibuja los datos simulados en el recibo: Total pagado, Terminacion de tarjeta (Visa ****1234), y Codigo de Referencia.

### Excepciones (Unhappy Paths)
- *No aplica para esta vista. Si Wompi falla, el usuario nunca llega a esta ruta, se queda en el Checkout (`/checkout/[id]`) viendo el modal de error.*
