# TASK DB-004 — `V004__create_payment_tables.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** CRÍTICA — Crea las tablas de procesamiento de pagos Wompi y desembolsos a finqueros.  
**Depende de:** `TASK_DB_003`  
**Bloquea:** Módulo de Facturación, Webhook Wompi y Payouts  

---

## 1. Propósito y Justificación Técnica

Crea las tablas `payments` y `payouts`. `payments` registra las transacciones de cobro recibidas a través de la pasarela Wompi (Nequi, Tarjetas, PSE, Bancolombia Transfer). `payouts` gestiona la orden de transferencia bancaria al finquero (desembolsando `total_price - platform_fee_amount`) vinculada 1:1 con la reserva.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo de migración
1. En `backend/src/main/resources/db/migration/`, crea `V004__create_payment_tables.sql`.

### Paso 2: Crear la tabla `payments`
1. Escribe el DDL para `payments`:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `booking_id UUID NOT NULL REFERENCES bookings(id)`
   * `amount BIGINT NOT NULL` (en centavos COP)
   * `currency VARCHAR(3) NOT NULL DEFAULT 'COP'`
   * `gateway_reference VARCHAR(255) UNIQUE` (ID de transacción entregado por Wompi)
   * `payment_method VARCHAR(30)` (CHECK IN `'NEQUI'`, `'CARD'`, `'PSE'`, `'BANCOLOMBIA_TRANSFER'`)
   * `transaction_date TIMESTAMPTZ NOT NULL`
   * `receipt_url TEXT`
   * `status VARCHAR(30) NOT NULL CHECK (status IN ('PENDING','APPROVED','DECLINED','VOIDED'))`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

### Paso 3: Crear la tabla `payouts`
1. Escribe el DDL para `payouts`:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `booking_id UUID NOT NULL UNIQUE REFERENCES bookings(id)` (garantiza un único desembolso por reserva)
   * `host_id UUID NOT NULL REFERENCES users(id)`
   * `amount BIGINT NOT NULL` (monto neto en centavos COP)
   * `currency VARCHAR(3) NOT NULL DEFAULT 'COP'`
   * `bank_reference VARCHAR(255)`
   * `transaction_date TIMESTAMPTZ`
   * `status VARCHAR(30) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING','PROCESSING','PAID','FAILED'))`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | `gateway_reference` en `payments` es `UNIQUE` | Se procesan cobros duplicados del mismo webhook |
| 2 | `booking_id` en `payouts` es `UNIQUE` | Se generan múltiples giros bancarios para una sola reserva |
| 3 | Montos declarados como `BIGINT` | Fallos de discrepancia monetaria en conciliación bancaria |

---

## 4. Errores Comunes a Evitar

1. **Permitir nulos en `gateway_reference` en pagos aprobados:** Al recibir la confirmación de Wompi, la referencia debe guardarse inmediatamente para evitar idempotencia fallida.

---

## 5. Comando de Verificación

```bash
./mvnw flyway:info
```
**Salida esperada:** `V004__create_payment_tables.sql` en estado `Success`.
