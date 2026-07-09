# Wireframe Specifications: `/checkout/success` (Confirmación de Pago)

**Ruta UI:** `/checkout/success` (Página Final del Embudo B2C)
**Requisitos Funcionales Inyectados:** `MOD-PAY` (Recibo de Transacción Wompi).

---

## Resultados
![Confirmación de Pago - Wireframe Estricto Desktop.png](<Confirmación de Pago - Wireframe Estricto Desktop.png>)
![Confirmación de Pago - Wireframe Estricto Mobile.png](<Confirmación de Pago - Wireframe Estricto Mobile.png>)

- **Diagnóstico:** El Turista acaba de entregarle su dinero a una plataforma en internet. Su carga cognitiva bajó a cero, pero su nivel de ansiedad por confirmación está al máximo. Necesita saber que todo salió bien y qué debe hacer ahora.
- **Patrón Principal:** `Success Celebration + Clear Next Steps`.
  - El diseño debe ser exultante y tranquilizador. Un gran icono de éxito en el centro superior.
  - El Navbar vuelve a aparecer, devolviéndole el control de navegación al usuario.
  - La pantalla se compone de un bloque central (Tarjeta de Recibo) que resume la operación, seguido de instrucciones hiper-claras de qué esperar (Ej. "El dueño de la finca tiene 90 minutos para aceptar tu solicitud. Revisa tu correo").

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar la pantalla de Éxito:

### A. Átomos
- `SuccessAnimation`: Una ilustración o animación Lottie (Checkmark verde grande y amigable).
- `TransactionRef` **(Obligatorio por MOD-PAY)**: Texto monoespaciado en color gris (Ej. `Ref: WOMPI-9A8B7C6D`).
- `SecondaryButton`: Botón para volver al Inicio o imprimir el recibo.

### B. Moléculas
- `StatusBanner`: Franja de color que indica el estado actual (Ej. Amarillo: "Esperando Confirmación del Dueño").
- `ReceiptRow` **(Obligatorio por MOD-PAY)**: Fila doble texto para datos clave (Fecha, Monto Pagado, Tarjeta usada).

### C. Organismos
- `DigitalReceiptCard` **(Obligatorio por MOD-PAY)**: Una tarjeta con apariencia de recibo o tiquete de avión. Une (`SuccessAnimation` + Título "¡Pago Procesado!" + Múltiples `ReceiptRow` + `TransactionRef`).
- `NextStepsBlock`: Un bloque debajo del recibo con 3 pasos (Iconos + Texto) explicando: 1. Pago retenido seguro, 2. El finquero te aprueba, 3. ¡Empacas maletas!.

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Jerarquía Visual de Tranquilidad:**
   - El elemento más grande de la pantalla debe ser el `SuccessAnimation` y el monto total cobrado. El turista no debe esforzarse por buscar cuánto se le descontó de su tarjeta.
2. **Claridad del Estado Transaccional:**
   - Según las reglas de `MOD-RSV`, el hecho de que Wompi cobre no significa que la reserva esté asegurada. Significa que el dinero está retenido hasta que el Finquero apruebe. El `StatusBanner` debe dejar esto explícitamente claro usando lenguaje humano (No jerga bancaria).
3. **Escaneabilidad (Receipt Print):**
   - El `DigitalReceiptCard` debe tener un diseño que sea amigable para imprimir (`Ctrl+P` o Guardar como PDF), con fondo blanco puro y sin sombras complejas.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/checkout/success`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja la pantalla con el `DigitalReceiptCard` centrado y el `NextStepsBlock` debajo. El Navbar y Footer normales deben volver a verse.
- `[ ]` **Mobile (390px):** Layout en 1 columna, ocupando el ancho completo de la pantalla para simular un tiquete.

### ✅ Mutaciones de Estado y Módulos
- `[ ]` **Recibo Oficial (Obligatorio por MOD-PAY):** Dibuja los datos simulados en el recibo: Total pagado, Terminación de tarjeta (Visa ****1234), y Código de Referencia.

### ✅ Excepciones (Unhappy Paths)
- *No aplica para esta vista. Si Wompi falla, el usuario nunca llega a esta ruta, se queda en el Checkout (`/checkout/[id]`) viendo el modal de error.*
