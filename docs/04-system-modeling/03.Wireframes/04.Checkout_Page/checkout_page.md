# Wireframe Specifications: `/checkout/[id]` (Embudo de Reservas)

**Ruta UI:** `/checkout/[id]` (Proceso de Pago y Toma de Datos)
**Requisitos Funcionales Inyectados:** `MOD-RSV` (Toma de Huespedes y Reglas), `MOD-PAY` (Pasarela Wompi e Idempotencia), `MOD-CAL` (Cronometro de 90 Minutos).

---

# RESULTADOS
![Checkout - Wireframe Desktop.png](Checkout%20-%20Wireframe%20Desktop.png)
![Checkout - Wireframe Mobile.png](Checkout%20-%20Wireframe%20Mobile.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** El turista esta a punto de gastar una cantidad alta de dinero. Su carga cognitiva es maxima, mezclada con estres (miedo a equivocarse o a que le roben la tarjeta) y urgencia (miedo a perder la finca).
- **Patron Principal:** `Focus Wizard (Checkout Aislado)`.
  - Cuando el usuario entra a esta ruta, **desaparece el Navbar global y el Footer**. No debe haber links que lo distraigan o lo hagan salir por error de la pasarela. Solo debe existir el logo de la empresa (para dar confianza) y un boton de "Atras".
  - El diseno debe dividirse en 2 columnas en Desktop (Formulario a la izquierda, Resumen de Compra pegajoso a la derecha) y apilarse verticalmente en Mobile.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar el Checkout:

### A. Atomos
- `CountdownTimer` **(Obligatorio por MOD-CAL)**: Texto en rojo o naranja que muestra un reloj en cuenta regresiva (Ej. `14:59`).
- `SecurityBadge` **(Obligatorio por MOD-PAY)**: Icono de un candado verde con el texto "Pago 100% Seguro por Wompi PCI-DSS".
- `StepperDot`: Circulos para indicar en que paso del checkout va el usuario.
- `PayButton` **(Obligatorio por MOD-PAY)**: Boton principal de pago. *Debe tener una variante `DisabledLoading` (Gris con spinner) innegociable.*

### B. Moleculas
- `GuestInputRow` **(Obligatorio por MOD-RSV)**: Fila para anadir un huesped (Nombre + Documento de Identidad).
- `LegalCheckbox` **(Obligatorio por MOD-RSV)**: Checkbox + Texto "Acepto los Terminos, Condiciones y Politicas de Cancelacion".
- `PriceBreakdownRow`: Fila matematica (Ej. "Subtotal" a la izquierda, "$1.000.000" a la derecha).

### C. Organismos
- `CheckoutWizardForm` **(Obligatorio por MOD-RSV)**: Agrupa el formulario de quien viaja y el `LegalCheckbox`.
- `OrderSummaryCard` **(Obligatorio por MOD-PAY)**: Tarjeta lateral que agrupa la foto miniatura de la finca, fechas, multiples `PriceBreakdownRow` (incluyendo el Service Fee de la plataforma) y el `Total a Pagar`.
- `TimeoutAlertModal` **(Obligatorio por MOD-CAL)**: Modal de error bloqueante indicando que el tiempo expiro.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Ley de Idempotencia UI (Prevencion de Doble Cobro):**
   - El `PayButton` DEBE transicionar a su estado `DisabledLoading` en el milisegundo exacto en que el usuario le hace clic. Es **obligatorio** dibujar este estado para que el desarrollador frontend bloquee el boton y evite que un turista ansioso haga clic 5 veces y se le cobren 5 millones de pesos por error.
2. **Jerarquia del Reloj (Urgencia Cognitiva):**
   - El `CountdownTimer` de 90 minutos (`MOD-CAL`) debe estar anclado visiblemente cerca del `OrderSummaryCard` en Desktop y en la parte superior del celular en Mobile (fijado). Si el contador llega a `00:00`, debe detonar el Modal de Error.
3. **Visibilidad del Service Fee (Confianza):**
   - El desglose de precios en el `OrderSummaryCard` jamas debe ocultar el "Service Fee" (Comision). Segun `MOD-PAY`, ocultarlo genera desconfianza y aumento de quejas en servicio al cliente. Dibujalo explicitamente en el desglose matematico.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/checkout/[id]`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el layout de 2 columnas. Sin Navbar ni Footer (Solo el logo de *Nos Fuimos de Finca* arriba).
- `[ ]` **Mobile (390px):** Dibuja el formulario apilado arriba del Resumen de Orden.

### Estados de Seguridad Financiera
- `[ ]` **Boton Mutado (Obligatorio por MOD-PAY):** Dibuja el estado exacto donde el boton de "Pagar" fue oprimido y ahora es color gris, no clickeable, con un spinner de carga diciendo *"Abriendo pasarela segura..."*.

### Excepciones Legales y Temporales (Unhappy Paths)
- `[ ]` **Validation Error Legal (Obligatorio por MOD-RSV):** Pantalla donde el usuario intento oprimir Pagar sin marcar el `LegalCheckbox`. El checkbox debe parpadear en rojo brillante con un texto de ayuda.
- `[ ]` **Timeout Expirado (Obligatorio por MOD-CAL):** El usuario se fue al bano, pasaron 90 minutos y el Soft-Lock expiro. Dibuja el `TimeoutAlertModal` a pantalla completa, bloqueando el formulario, que diga: *"Tu tiempo de reserva ha expirado y las fechas han sido liberadas. Por favor, vuelve a intentarlo"*. Solo debe tener un boton: "Volver a la Finca".
