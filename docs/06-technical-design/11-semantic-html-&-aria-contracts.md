 # Deliverable 11 (D11): Semantic HTML & ARIA Contracts

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4:* Este documento obliga a nivel de codigo el cumplimiento de los estandares de accesibilidad visuales y de interaccion definidos en la Fase 4 (D13 - Accessibility Standards).

---

## 2. Mapeo de Roles ARIA por Componente

La regla fundamental para este proyecto es: **El HTML semantico nativo siempre gana**. Solo utilizaremos atributos ARIA cuando creemos componentes (Moleculas u Organismos) desde cero que el navegador no pueda entender por si mismo.

| Componente (Ref. D9) | Elemento Nativo a Usar | Rol ARIA Asignado (Si aplica) | Atributos de Estado Obligatorios |
|---|---|---|---|
| **Modal de Cancelacion** | `<dialog>` nativo | Ninguno. El navegador entiende `<dialog>`. | Atributo `open` para abrirlo. |
| **DateRangePicker** | Ninguno. (Flotante custom). | `role="dialog"` | `aria-modal="false"`, `aria-label="Seleccionar fechas"` |
| **GuestCounter** | `<input type="number">` descartado por el diseno UI especifico. | `role="spinbutton"` | `aria-valuenow`, `aria-valuemin`, `aria-valuemax` |

---

## 3. Reglas de Tags Semanticos y Button vs Link

Para facilitar la navegacion mediante lectores de pantalla (Screen Readers), estructuraremos las vistas de la siguiente forma, **prohibiendo** el uso de `<div>` como contenedor raiz para secciones principales.

### 3.1 Landmarks por Pagina

**Pagina: `BookingCheckoutPage`**
- **`<main>`**: Envolvera obligatoriamente al formulario de reserva (`BookingForm`).
- **`<aside>`**: Envolvera la tarjeta de resumen financiero (`BookingSummary`).

**Pagina: `MyBookingsPage`**
- **`<nav>`**: Envolvera los filtros/solapas de la parte superior (`BookingFilters`).
- **`<main>`**: Envolvera el listado de tarjetas (`BookingList`).

### 3.2 Clasificacion Estricta Button vs Link

| Elemento | Funcion Logica | Tag Obligatorio |
|---|---|---|
| **CheckoutButton** | Ejecutar una Mutacion (Guardar reserva). | `<button type="submit">` |
| **Increase/Decrease Guest** | Modificar estado local en memoria. | `<button type="button">` (Evita envio accidental de forms) |
| **BookingCard** | Navegar a la URL del detalle (`/bookings/123`). | `<a href="...">` (Via Spring Boot (Java) `<Link>`) |
| **ActionMenu Toggle** | Desplegar menu de opciones de la tarjeta. | `<button type="button" aria-expanded="false/true">` |

> [!WARNING]
> **Prohibido:** No se aceptaran Pull Requests que contengan `<div onClick={...}>` sin excepcion.

---

## 4. Manejo de Teclado y aria-live

### 4.1 Comportamiento de Teclado y Focus Trap

- **Modal de Cancelacion (`<dialog>`):** Spring Boot (Java) / el Navegador encerraran el ciclo del tabulador (`Tab`) dentro del modal. `Escape` lo cerrara.
- **DateRangePicker (Calendario Flotante):**
  - Debe permitir a los usuarios navegar los dias del mes utilizando las flechas del teclado (`ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`).
  - La tecla `Enter` o `Space` debe seleccionar la fecha.

### 4.2 Notificaciones Dinamicas (aria-live)

Dado que es una SPA (Single Page Application), el navegador no recarga tras crear la reserva, por tanto el lector de pantalla debe ser avisado.

- **Toast de Reserva Exitosa:** Usar **`aria-live="polite"`**. El Screen Reader lo leera cuando termine su frase actual.
  ```html
  <div role="status" aria-live="polite">Tu reserva ha sido confirmada.</div>
  ```
- **Toast de Pago Fallido (Wompi):** Usar **`aria-live="assertive"`**. Es urgente; interrumpe al Screen Reader inmediatamente.
  ```html
  <div role="alert" aria-live="assertive">Las fechas ya no estan disponibles, pago abortado.</div>
  ```

---

## 5. Configuracion de Linter

Para hacer cumplir la mayoria de estas reglas de manera automatizada en Integracion Continua (CI), el archivo de configuracion ESLint del Frontend debera contener este bloque:

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

### 5.1 Reglas de Verificacion Manual (Code Review)
El Linter es ciego a la logica de negocio profunda. Las siguientes dos metricas deben ser probadas manualmente por el QA o el Developer en Code Review:
1. **Focus Trap del DateRangePicker:** Validar que al abrir el calendario, el foco del teclado no se escape hacia los inputs de atras.
2. **Uso Logico de aria-live:** Validar que no hayan usado `assertive` para todo, lo cual ensordeceria al usuario ciego con constantes interrupciones.

