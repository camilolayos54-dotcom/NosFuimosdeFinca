 # Entregable 13 (D13): Estandares de Accesibilidad (a11y)

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Estandar:** WCAG 2.1 Nivel AA
**Estado:** Aprobado

---

## 1. Validacion de Contraste de Colores (WCAG 1.4.3)

Construido en `[[example_step_1_contrast.md]]`. Umbral: 4.5:1 para texto normal, 3:1 para texto grande ( 18pt o 14pt Bold).

| Combinacion | Foreground | Background | Ratio | Resultado |
|---|---|---|---|---|
| Boton Primario (Bold 14px) | `#FFFFFF` | `#1A73E8` | 4.25:1 | [OK] PASS (Large Text) |
| Texto Body | `#212121` | `#FFFFFF` | 15.7:1 | [OK] PASS |
| Placeholder (corregido) | `#616161` | `#F5F5F5` | 4.6:1 | [OK] PASS (era `#757575` 3.78:1 ) |
| Error Text | `#D32F2F` | `#FFFFFF` | 5.33:1 | [OK] PASS |
| Link Text en cuerpo (corregido) | `#1558B0` | `#FFFFFF` | 5.2:1 | [OK] PASS (era `#1A73E8` 4.25:1 ) |
| Boton Deshabilitado | `#9E9E9E` | `#E0E0E0` | 1.6:1 | Exento (WCAG 1.4.3) |

**Tokens actualizados en Design System D4:**
- `color.text.placeholder`: `#757575` `#616161`
- `color.text.link`: `#1A73E8` `#1558B0` *(en contexto de texto, no botones)*

---

## 2. Directivas de Teclado y Focus (WCAG 2.1.1, 2.1.2)

Construido en `[[example_step_2_focus_states.md]]`.

- **Focus Ring:** `:focus-visible { outline: 2px solid #1558B0; outline-offset: 2px; }`
- **Prohibicion absoluta:** `outline: none;` sin reemplazo visible.
- **Semantic HTML Enforcement:**
  - Cards de navegacion `<a href>` (no `<div onClick>`)
  - Botones de accion `<button type="button">` (no `<div onClick>`)
  - Date Pickers `tabindex="0"` + `role="application"` + roving tabindex
- **Tab Order:** Flujo natural del DOM. Prohibido `tabindex > 0`.
- **Keyboard Trap en Modales:** Focus Trap (`aria-modal="true"`, ciclo Tab dentro del modal, Escape cerrar modal, devolver foco al elemento disparador).

---

## 3. Lectores de Pantalla y Comunicacion No-Color (WCAG 1.1.1, 1.4.1)

Construido en `[[example_step_3_aria_labels.md]]`.

**ARIA Labels Botones Icon-Only:**
| Boton | `aria-label` |
|---|---|
| Lupa | `"Buscar fincas"` |
| Favorito (vacio) | `"Agregar [Finca.Name] a favoritos"` |
| Favorito (lleno) | `"Quitar [Finca.Name] de favoritos"` + `aria-pressed="true"` |
| Papelera | `"Eliminar esta foto de la galeria"` |
| Atras | `"Volver a los resultados de busqueda"` |
| Cerrar modal | `"Cerrar modal de confirmacion"` |

**Alt Text Imagenes de Negocio:**
- Foto galeria: `alt="[Tipo de vista] de [Nombre de Finca] en [Ubicacion]"`
- Iconos decorativos: `alt=""` (lector de pantalla los ignora)

**Validacion de Formularios Triple comunicacion (WCAG 1.4.1):**
```html
<input type="email" aria-invalid="true" aria-describedby="error-email-msg" />
<span id="error-email-msg" role="alert">
         El formato del email no es valido. Ej: nombre@correo.com
</span>
```
*(Borde rojo + icono + texto descriptivo nunca solo color)*

**Estados del Calendario:**
- Disponible: fondo verde + + `aria-label="Disponible"`
- No disponible: fondo rojo + + tachado + `aria-label="No disponible"` + `aria-disabled="true"`

**Elementos dinamicos:**
- Alertas urgentes (pagos, errores): `role="alert"` anunciado inmediatamente
- Mensajes de estado (guardado): `role="status"` anunciado al terminar la accion actual

---

## Implicacion de Fase

- Los tokens de contraste corregidos (`#616161`, `#1558B0`) deben actualizarse en el Design System D4 antes de la implementacion de Fase 6.
- Las directivas ARIA pueden configurarse como reglas de `eslint-plugin-jsx-a11y` para rechazar automaticamente `<div onClick>`, `outline: none`, y `<img>` sin `alt`.
- **Proceder a D14:** Estrategia de Localizacion e i18n.

