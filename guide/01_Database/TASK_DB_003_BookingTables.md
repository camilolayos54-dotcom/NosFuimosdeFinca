# TASK DB-003 — `V003__create_booking_tables.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** CRÍTICA — Define la estructura del motor de reservas y cupones promocionales.  
**Depende de:** `TASK_DB_002`  
**Bloquea:** Módulo de Reservas, Pasarela Wompi y Flujo Checkout Frontend  

---

## 1. Propósito y Justificación Técnica

Crea las tablas `coupons` y `bookings`. `bookings` es la entidad central del negocio, almacenando el desglose financiero exacto (`base_price_amount`, `cleaning_fee_amount`, `platform_fee_amount`, `taxes_amount`, `total_price`) en `BIGINT` centavos de COP, asegurando la auditoría de cada peso cobrado al turista.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo de migración
1. En `backend/src/main/resources/db/migration/`, crea `V003__create_booking_tables.sql`.

### Paso 2: Crear la tabla `coupons`
1. Escribe la estructura de `coupons`:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `code VARCHAR(50) NOT NULL UNIQUE`
   * `discount_percentage DECIMAL(5,2)`
   * `max_discount_amount BIGINT` (en centavos COP)
   * `valid_from DATE NOT NULL`, `valid_until DATE NOT NULL`
   * `usage_limit INT`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

### Paso 3: Crear la tabla `bookings`
1. Escribe la estructura de `bookings`:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `property_id UUID NOT NULL REFERENCES properties(id)`
   * `guest_id UUID NOT NULL REFERENCES users(id)`
   * `coupon_id UUID REFERENCES coupons(id)` (opcional)
   * `check_in DATE NOT NULL`, `check_out DATE NOT NULL`
   * `guest_count INT NOT NULL`
   * `agency_client_name VARCHAR(255)` (para canal B2B)
   * `base_price_amount BIGINT NOT NULL`
   * `cleaning_fee_amount BIGINT NOT NULL DEFAULT 0`
   * `platform_fee_amount BIGINT NOT NULL DEFAULT 0`
   * `taxes_amount BIGINT NOT NULL DEFAULT 0`
   * `total_price BIGINT NOT NULL`
   * `status VARCHAR(30) NOT NULL DEFAULT 'PENDING_PAYMENT' CHECK (status IN ('PENDING_PAYMENT','PENDING_APPROVAL','CONFIRMED','COMPLETED','CANCELLED'))`
   * `cancellation_reason TEXT`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Restricción CHECK en `status` restringe los 5 estados válidos del ciclo de vida | Se permiten estados de reserva inconsistentes |
| 2 | Todos los campos de precio declarados como `BIGINT` | Fallos en el cálculo de totales y comisiones |
| 3 | Clave foránea `coupon_id` permite valores `NULL` | Las reservas sin cupón fallarían en base de datos |
| 4 | Fechas `check_in` y `check_out` definidas como tipo `DATE` | Desfases de zona horaria alteran el número de noches |

---

## 4. Errores Comunes a Evitar

1. **No validar que `check_out > check_in` a nivel de aplicación:** Aunque la BD almacena las fechas, el Backend Java debe validar siempre que `check_out` sea posterior a `check_in`.

---

## 5. Comando de Verificación

```bash
./mvnw flyway:info
```
**Salida esperada:** `V003__create_booking_tables.sql` en estado `Success`.
