# Entregable 13 (D13): EstÃ¡ndares de Accesibilidad (a11y)

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**EstÃ¡ndar:** WCAG 2.1 Nivel AA
**Estado:** Aprobado

---

## 1. ValidaciÃ³n de Contraste de Colores (WCAG 1.4.3)

Construido en `[[example_step_1_contrast.md]]`. Umbral: 4.5:1 para texto normal, 3:1 para texto grande (â‰¥18pt o â‰¥14pt Bold).

| CombinaciÃ³n | Foreground | Background | Ratio | Resultado |
|---|---|---|---|---|
| BotÃ³n Primario (Bold â‰¥14px) | `#FFFFFF` | `#1A73E8` | 4.25:1 | âœ… PASS (Large Text) |
| Texto Body | `#212121` | `#FFFFFF` | 15.7:1 | âœ… PASS |
| Placeholder (corregido) | `#616161` | `#F5F5F5` | 4.6:1 | âœ… PASS (era `#757575` â†’ 3.78:1 âŒ) |
| Error Text | `#D32F2F` | `#FFFFFF` | 5.33:1 | âœ… PASS |
| Link Text en cuerpo (corregido) | `#1558B0` | `#FFFFFF` | 5.2:1 | âœ… PASS (era `#1A73E8` â†’ 4.25:1 âŒ) |
| BotÃ³n Deshabilitado | `#9E9E9E` | `#E0E0E0` | 1.6:1 | âš ï¸ Exento (WCAG 1.4.3) |

**Tokens actualizados en Design System D4:**
- `color.text.placeholder`: `#757575` â†’ `#616161`
- `color.text.link`: `#1A73E8` â†’ `#1558B0` *(en contexto de texto, no botones)*

---

## 2. Directivas de Teclado y Focus (WCAG 2.1.1, 2.1.2)

Construido en `[[example_step_2_focus_states.md]]`.

- **Focus Ring:** `:focus-visible { outline: 2px solid #1558B0; outline-offset: 2px; }`
- **ProhibiciÃ³n absoluta:** `outline: none;` sin reemplazo visible.
- **Semantic HTML Enforcement:**
  - Cards de navegaciÃ³n â†’ `<a href>` (no `<div onClick>`)
  - Botones de acciÃ³n â†’ `<button type="button">` (no `<div onClick>`)
  - Date Pickers â†’ `tabindex="0"` + `role="application"` + roving tabindex
- **Tab Order:** Flujo natural del DOM. Prohibido `tabindex > 0`.
- **Keyboard Trap en Modales:** Focus Trap (`aria-modal="true"`, ciclo Tab dentro del modal, Escape â†’ cerrar modal, devolver foco al elemento disparador).

---

## 3. Lectores de Pantalla y ComunicaciÃ³n No-Color (WCAG 1.1.1, 1.4.1)

Construido en `[[example_step_3_aria_labels.md]]`.

**ARIA Labels â€” Botones Icon-Only:**
| BotÃ³n | `aria-label` |
|---|---|
| ðŸ” Lupa | `"Buscar fincas"` |
| â™¡ Favorito (vacÃ­o) | `"Agregar [Finca.Name] a favoritos"` |
| â™¥ Favorito (lleno) | `"Quitar [Finca.Name] de favoritos"` + `aria-pressed="true"` |
| ðŸ—‘ï¸ Papelera | `"Eliminar esta foto de la galerÃ­a"` |
| â† AtrÃ¡s | `"Volver a los resultados de bÃºsqueda"` |
| Ã— Cerrar modal | `"Cerrar modal de confirmaciÃ³n"` |

**Alt Text â€” ImÃ¡genes de Negocio:**
- Foto galerÃ­a: `alt="[Tipo de vista] de [Nombre de Finca] en [UbicaciÃ³n]"`
- Ãconos decorativos: `alt=""` (lector de pantalla los ignora)

**ValidaciÃ³n de Formularios â€” Triple comunicaciÃ³n (WCAG 1.4.1):**
```html
<input type="email" aria-invalid="true" aria-describedby="error-email-msg" />
<span id="error-email-msg" role="alert">
  âš ï¸ El formato del email no es vÃ¡lido. Ej: nombre@correo.com
</span>
```
*(Borde rojo + Ã­cono âš ï¸ + texto descriptivo â€” nunca solo color)*

**Estados del Calendario:**
- Disponible: fondo verde + âœ“ + `aria-label="Disponible"`
- No disponible: fondo rojo + âœ— + tachado + `aria-label="No disponible"` + `aria-disabled="true"`

**Elementos dinÃ¡micos:**
- Alertas urgentes (pagos, errores): `role="alert"` â†’ anunciado inmediatamente
- Mensajes de estado (guardado): `role="status"` â†’ anunciado al terminar la acciÃ³n actual

---

## ImplicaciÃ³n de Fase

- Los tokens de contraste corregidos (`#616161`, `#1558B0`) deben actualizarse en el Design System D4 antes de la implementaciÃ³n de Fase 6.
- Las directivas ARIA pueden configurarse como reglas de `eslint-plugin-jsx-a11y` para rechazar automÃ¡ticamente `<div onClick>`, `outline: none`, y `<img>` sin `alt`.
- **Proceder a D14:** Estrategia de LocalizaciÃ³n e i18n.

