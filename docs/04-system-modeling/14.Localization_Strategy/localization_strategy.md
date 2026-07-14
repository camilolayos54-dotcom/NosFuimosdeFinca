 # Entregable 14 (D14): Estrategia de Localizacion e i18n

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Estado:** Aprobado

---

## 1. Locale y Reglas de Zona Horaria

Construido en `[[example_step_1_utc_enforcement.md]]`.

**Locales Soportados:**
- Default: `es-CO` (Espanol Colombia)
- Futuro: `en-US` (Ingles Estados Unidos)
- Fallback: `es-CO`

**Reglas de Almacenamiento Temporal (Backend y BD):**
- Tipo conceptual: `TIMESTAMP WITH TIME ZONE`. Tipo fisico definido en P6-D2.
- Toda fecha almacenada en **UTC** sin excepcion.
- Serializacion API: ISO-8601 con zona explicita: `2026-12-24T20:00:00Z`.
- Conversion a hora local: responsabilidad exclusiva del **Frontend** (`Intl.DateTimeFormat` o `date-fns-tz`).
- Fallback timezone: `America/Bogota` (UTC-5) si el dispositivo no reporta zona.

**Formato de Fecha y Numero por Locale:**

| Concepto | `es-CO` | `en-US` |
|---|---|---|
| Fecha | 15/07/2026 | 07/15/2026 |
| Hora | 15:00 | 3:00 PM |
| Separador de miles | `.` $250.000 | `,` $250,000 |
| Separador decimal | `,` 3,50 | `.` 3.50 |

---

## 2. Reglas de Almacenamiento Monetario

Construido en `[[example_step_2_currency_storage.md]]`.

| Columna | Tabla | Tipo Conceptual | Unidad | Ejemplo |
|---|---|---|---|---|
| `price_per_night` | `properties` | `BIGINT` (centavos) | COP | $250.000 = `25000000` |
| `total_price` | `bookings` | `BIGINT` (centavos) | COP | $870.000 = `87000000` |
| `amount` | `payments` | `BIGINT` (centavos) | COP | Alineado con Stripe API |

**Tipos PROHIBIDOS:** `FLOAT`, `DOUBLE`, `DECIMAL`, `MONEY`.
**Columna auxiliar:** `currency VARCHAR(3)` con codigo ISO 4217 junto a cada monto (default: `'COP'`).
**Formateo visual:** Responsabilidad exclusiva del Frontend con `Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' })`.

---

## 3. Estrategia de Traduccion (Frontera de Traduccion)

Construido en `[[example_step_3_translation_boundaries.md]]`.

| Dominio | Estrategia MVP | Estrategia Futura |
|---|---|---|
| **UI Estatica** (Botones, Labels, Navegacion) | Claves i18n obligatorias `t('key')` + archivo `es.json` | Agregar `en.json` |
| **Mensajes de Error (UI)** | Claves i18n `t('booking.errors.PAYMENT_DECLINED')` | Agregar `en.json` |
| **Codigos de Error API (D9)** | Codigo constante EN (`DATES_UNAVAILABLE`) + traduccion en `es.json` | Agregar `en.json` |
| **Templates de Notificaciones (D10)** | Templates en espanol con variables `[Variable]` | Templates biling es |
| **Contenido Dinamico BD** (`property.name`, `review.body`) | Idioma original del autor. Sin traduccion. | Tabla `entity_translations(entity_id, locale, field, value)` |

**Framework i18n:** `react-i18next` (React) o `vue-i18n` (Vue).
**Convencion de claves:** `namespace.component.element` Ej: `booking.form.btn_submit`.
**Regla de Fallback:** Si una clave falta en `en.json`, usar `es.json`.

---

## Implicacion de Fase

- El equipo de Backend sabe que toda fecha es UTC y todo dinero es centavos en `BIGINT`. Estas son las dos reglas de datos mas importantes del sistema para la correctitud financiera y temporal.
- El equipo de Frontend sabe que **no puede hardcodear texto visible** toda cadena de UI debe ser una clave `t()`. Esta regla puede validarse con `eslint-plugin-i18n-json`.
- **Proceder a D15:** Phase 4 RTM Update y Brief Final.

