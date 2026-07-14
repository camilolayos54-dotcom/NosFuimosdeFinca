# Deliverable 11 (D11): Semantic HTML & ARIA Contracts

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4:* Este documento obliga a nivel de cÃ³digo el cumplimiento de los estÃ¡ndares de accesibilidad visuales y de interacciÃ³n definidos en la Fase 4 (D13 - Accessibility Standards).

---

## 2. Mapeo de Roles ARIA por Componente

La regla fundamental para este proyecto es: **El HTML semÃ¡ntico nativo siempre gana**. Solo utilizaremos atributos ARIA cuando creemos componentes (MolÃ©culas u Organismos) desde cero que el navegador no pueda entender por sÃ­ mismo.

| Componente (Ref. D9) | Elemento Nativo a Usar | Rol ARIA Asignado (Si aplica) | Atributos de Estado Obligatorios |
|---|---|---|---|
| **Modal de CancelaciÃ³n** | `<dialog>` nativo | Ninguno. El navegador entiende `<dialog>`. | Atributo `open` para abrirlo. |
| **DateRangePicker** | Ninguno. (Flotante custom). | `role="dialog"` | `aria-modal="false"`, `aria-label="Seleccionar fechas"` |
| **GuestCounter** | `<input type="number">` descartado por el diseÃ±o UI especÃ­fico. | `role="spinbutton"` | `aria-valuenow`, `aria-valuemin`, `aria-valuemax` |

---

## 3. Reglas de Tags SemÃ¡nticos y Button vs Link

Para facilitar la navegaciÃ³n mediante lectores de pantalla (Screen Readers), estructuraremos las vistas de la siguiente forma, **prohibiendo** el uso de `<div>` como contenedor raÃ­z para secciones principales.

### 3.1 Landmarks por PÃ¡gina

**PÃ¡gina: `BookingCheckoutPage`**
- **`<main>`**: EnvolverÃ¡ obligatoriamente al formulario de reserva (`BookingForm`).
- **`<aside>`**: EnvolverÃ¡ la tarjeta de resumen financiero (`BookingSummary`).

**PÃ¡gina: `MyBookingsPage`**
- **`<nav>`**: EnvolverÃ¡ los filtros/solapas de la parte superior (`BookingFilters`).
- **`<main>`**: EnvolverÃ¡ el listado de tarjetas (`BookingList`).

### 3.2 ClasificaciÃ³n Estricta Button vs Link

| Elemento | FunciÃ³n LÃ³gica | Tag Obligatorio |
|---|---|---|
| **CheckoutButton** | Ejecutar una MutaciÃ³n (Guardar reserva). | `<button type="submit">` |
| **Increase/Decrease Guest** | Modificar estado local en memoria. | `<button type="button">` (Evita envÃ­o accidental de forms) |
| **BookingCard** | Navegar a la URL del detalle (`/bookings/123`). | `<a href="...">` (VÃ­a Next.js `<Link>`) |
| **ActionMenu Toggle** | Desplegar menÃº de opciones de la tarjeta. | `<button type="button" aria-expanded="false/true">` |

> [!WARNING]
> **Prohibido:** No se aceptarÃ¡n Pull Requests que contengan `<div onClick={...}>` sin excepciÃ³n.

---

## 4. Manejo de Teclado y aria-live

### 4.1 Comportamiento de Teclado y Focus Trap

- **Modal de CancelaciÃ³n (`<dialog>`):** Next.js / el Navegador encerrarÃ¡n el ciclo del tabulador (`Tab`) dentro del modal. `Escape` lo cerrarÃ¡.
- **DateRangePicker (Calendario Flotante):**
  - Debe permitir a los usuarios navegar los dÃ­as del mes utilizando las flechas del teclado (`ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`).
  - La tecla `Enter` o `Space` debe seleccionar la fecha.

### 4.2 Notificaciones DinÃ¡micas (aria-live)

Dado que es una SPA (Single Page Application), el navegador no recarga tras crear la reserva, por tanto el lector de pantalla debe ser avisado.

- **Toast de Reserva Exitosa:** Usar **`aria-live="polite"`**. El Screen Reader lo leerÃ¡ cuando termine su frase actual.
  ```html
  <div role="status" aria-live="polite">Tu reserva ha sido confirmada.</div>
  ```
- **Toast de Pago Fallido (Wompi):** Usar **`aria-live="assertive"`**. Es urgente; interrumpe al Screen Reader inmediatamente.
  ```html
  <div role="alert" aria-live="assertive">Las fechas ya no estÃ¡n disponibles, pago abortado.</div>
  ```

---

## 5. ConfiguraciÃ³n de Linter

Para hacer cumplir la mayorÃ­a de estas reglas de manera automatizada en IntegraciÃ³n Continua (CI), el archivo de configuraciÃ³n ESLint del Frontend deberÃ¡ contener este bloque:

```json
{
  "plugins": ["jsx-a11y"],
  "rules": {
    "jsx-a11y/click-events-have-key-events": "error",
    "jsx-a11y/no-static-element-interactions": "error",
    "jsx-a11y/aria-role": "error",
    "jsx-a11y/aria-props": "error",
    "jsx-a11y/anchor-is-valid": "error"
  }
}
```

### 5.1 Reglas de VerificaciÃ³n Manual (Code Review)
El Linter es ciego a la lÃ³gica de negocio profunda. Las siguientes dos mÃ©tricas deben ser probadas manualmente por el QA o el Developer en Code Review:
1. **Focus Trap del DateRangePicker:** Validar que al abrir el calendario, el foco del teclado no se escape hacia los inputs de atrÃ¡s.
2. **Uso LÃ³gico de aria-live:** Validar que no hayan usado `assertive` para todo, lo cual ensordecerÃ­a al usuario ciego con constantes interrupciones.

