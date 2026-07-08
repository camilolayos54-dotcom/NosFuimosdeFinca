# Wireframe Specifications: `/checkout/[id]` (Embudo de Reservas)

**Ruta UI:** `/checkout/[id]` (Proceso de Pago y Toma de Datos)
**Requisitos Funcionales Inyectados:** `MOD-RSV` (Toma de Huéspedes y Reglas), `MOD-PAY` (Pasarela Wompi e Idempotencia), `MOD-CAL` (Cronómetro de 90 Minutos).

---

## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** El turista está a punto de gastar una cantidad alta de dinero. Su carga cognitiva es máxima, mezclada con estrés (miedo a equivocarse o a que le roben la tarjeta) y urgencia (miedo a perder la finca).
- **Patrón Principal:** `Focus Wizard (Checkout Aislado)`.
  - Cuando el usuario entra a esta ruta, **desaparece el Navbar global y el Footer**. No debe haber links que lo distraigan o lo hagan salir por error de la pasarela. Solo debe existir el logo de la empresa (para dar confianza) y un botón de "Atrás".
  - El diseño debe dividirse en 2 columnas en Desktop (Formulario a la izquierda, Resumen de Compra pegajoso a la derecha) y apilarse verticalmente en Mobile.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Checkout:

### A. Átomos
- `CountdownTimer` **(Obligatorio por MOD-CAL)**: Texto en rojo o naranja que muestra un reloj en cuenta regresiva (Ej. `14:59`).
- `SecurityBadge` **(Obligatorio por MOD-PAY)**: Icono de un candado verde con el texto "Pago 100% Seguro por Wompi PCI-DSS".
- `StepperDot`: Círculos para indicar en qué paso del checkout va el usuario.
- `PayButton` **(Obligatorio por MOD-PAY)**: Botón principal de pago. *Debe tener una variante `DisabledLoading` (Gris con spinner) innegociable.*

### B. Moléculas
- `GuestInputRow` **(Obligatorio por MOD-RSV)**: Fila para añadir un huésped (Nombre + Documento de Identidad).
- `LegalCheckbox` **(Obligatorio por MOD-RSV)**: Checkbox + Texto "Acepto los Términos, Condiciones y Políticas de Cancelación".
- `PriceBreakdownRow`: Fila matemática (Ej. "Subtotal" a la izquierda, "$1.000.000" a la derecha).

### C. Organismos
- `CheckoutWizardForm` **(Obligatorio por MOD-RSV)**: Agrupa el formulario de quién viaja y el `LegalCheckbox`.
- `OrderSummaryCard` **(Obligatorio por MOD-PAY)**: Tarjeta lateral que agrupa la foto miniatura de la finca, fechas, múltiples `PriceBreakdownRow` (incluyendo el Service Fee de la plataforma) y el `Total a Pagar`.
- `TimeoutAlertModal` **(Obligatorio por MOD-CAL)**: Modal de error bloqueante indicando que el tiempo expiró.

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Ley de Idempotencia UI (Prevención de Doble Cobro):**
   - El `PayButton` DEBE transicionar a su estado `DisabledLoading` en el milisegundo exacto en que el usuario le hace clic. Es **obligatorio** dibujar este estado para que el desarrollador frontend bloquee el botón y evite que un turista ansioso haga clic 5 veces y se le cobren 5 millones de pesos por error.
2. **Jerarquía del Reloj (Urgencia Cognitiva):**
   - El `CountdownTimer` de 90 minutos (`MOD-CAL`) debe estar anclado visiblemente cerca del `OrderSummaryCard` en Desktop y en la parte superior del celular en Mobile (fijado). Si el contador llega a `00:00`, debe detonar el Modal de Error.
3. **Visibilidad del Service Fee (Confianza):**
   - El desglose de precios en el `OrderSummaryCard` jamás debe ocultar el "Service Fee" (Comisión). Según `MOD-PAY`, ocultarlo genera desconfianza y aumento de quejas en servicio al cliente. Dibújalo explícitamente en el desglose matemático.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/checkout/[id]`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el layout de 2 columnas. Sin Navbar ni Footer (Solo el logo de *Nos Fuimos de Finca* arriba).
- `[ ]` **Mobile (390px):** Dibuja el formulario apilado arriba del Resumen de Orden.

### ✅ Estados de Seguridad Financiera
- `[ ]` **Botón Mutado (Obligatorio por MOD-PAY):** Dibuja el estado exacto donde el botón de "Pagar" fue oprimido y ahora es color gris, no clickeable, con un spinner de carga diciendo *"Abriendo pasarela segura..."*.

### ✅ Excepciones Legales y Temporales (Unhappy Paths)
- `[ ]` **Validation Error Legal (Obligatorio por MOD-RSV):** Pantalla donde el usuario intentó oprimir Pagar sin marcar el `LegalCheckbox`. El checkbox debe parpadear en rojo brillante con un texto de ayuda.
- `[ ]` **Timeout Expirado (Obligatorio por MOD-CAL):** El usuario se fue al baño, pasaron 90 minutos y el Soft-Lock expiró. Dibuja el `TimeoutAlertModal` a pantalla completa, bloqueando el formulario, que diga: *"Tu tiempo de reserva ha expirado y las fechas han sido liberadas. Por favor, vuelve a intentarlo"*. Solo debe tener un botón: "Volver a la Finca".
