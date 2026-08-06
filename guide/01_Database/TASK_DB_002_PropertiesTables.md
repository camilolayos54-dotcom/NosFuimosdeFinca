# TASK DB-002 — `V002__create_properties_tables.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** CRÍTICA — Define el catálogo de propiedades, galerías, reglas, bloqueos de disponibilidad y precios de temporada.  
**Depende de:** `TASK_DB_001`  
**Bloquea:** Módulo de Catálogo, módulo de Reservas y Búsqueda Facetada  

---

## 1. Propósito y Justificación Técnica

Crea las 6 tablas necesarias para representar las fincas y sus atributos dinámicos: `properties`, `property_images`, `property_amenities`, `property_rules`, `property_availability` y `seasonal_prices`. Todos los campos monetarios (`price_per_night`, `cleaning_fee`) se definen explícitamente en centavos de COP como `BIGINT` para garantizar precisión matemática total y cero errores de redondeo.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo de migración
1. En `backend/src/main/resources/db/migration/`, crea `V002__create_properties_tables.sql`.

### Paso 2: Crear la tabla `properties`
1. Escribe el DDL para `properties`:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `host_id UUID NOT NULL REFERENCES users(id)`
   * `name VARCHAR(255) NOT NULL`
   * `description TEXT NOT NULL`
   * `price_per_night BIGINT NOT NULL` (en centavos COP)
   * `cleaning_fee BIGINT NOT NULL DEFAULT 0` (en centavos COP)
   * `max_guests INT NOT NULL`
   * `bedrooms_count INT NOT NULL DEFAULT 1`
   * `bathrooms_count INT NOT NULL DEFAULT 1`
   * `beds_count INT NOT NULL DEFAULT 1`
   * `location_lat DECIMAL(10,8) NOT NULL`
   * `location_lng DECIMAL(11,8) NOT NULL`
   * `location_address VARCHAR(500) NOT NULL`
   * `status VARCHAR(30) NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'APPROVED', 'SUSPENDED'))`
   * `is_active BOOLEAN NOT NULL DEFAULT TRUE`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

### Paso 3: Crear las tablas de soporte
1. **`property_images`:** `id UUID`, `property_id UUID REFERENCES properties(id) ON DELETE CASCADE`, `url_hd TEXT NOT NULL`, `sort_order INT DEFAULT 0`, timestamps.
2. **`property_amenities`:** `id UUID`, `property_id UUID REFERENCES properties(id) ON DELETE CASCADE`, `amenity_key VARCHAR(50) CHECK (amenity_key IN ('POOL', 'WIFI', 'BBQ', 'PET_FRIENDLY', 'PARKING', 'AIR_CONDITIONING', 'KITCHEN'))`, timestamps.
3. **`property_rules`:** `id UUID`, `property_id UUID UNIQUE REFERENCES properties(id) ON DELETE CASCADE` (relación 1:1), `check_in_time VARCHAR(10) DEFAULT '15:00'`, `check_out_time VARCHAR(10) DEFAULT '12:00'`, `allows_pets BOOLEAN DEFAULT FALSE`, `allows_parties BOOLEAN DEFAULT FALSE`, `additional_rules TEXT`, timestamps.
4. **`property_availability`:** `id UUID`, `property_id UUID REFERENCES properties(id) ON DELETE CASCADE`, `start_date DATE NOT NULL`, `end_date DATE NOT NULL`, `reason VARCHAR(50) CHECK (reason IN ('MAINTENANCE', 'PERSONAL_USE', 'OTHER'))`, timestamps.
5. **`seasonal_prices`:** `id UUID`, `property_id UUID REFERENCES properties(id) ON DELETE CASCADE`, `start_date DATE NOT NULL`, `end_date DATE NOT NULL`, `price_per_night BIGINT NOT NULL` (centavos COP sobreescribe precio base), timestamps.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Las 6 tablas creadas exitosamente con claves foráneas a `properties(id)` | Errores en la persistencia del catálogo |
| 2 | Tarifas `price_per_night` y `cleaning_fee` declaradas como `BIGINT` | Fallo de tipo en Java JPA y pérdidas por punto flotante |
| 3 | Tabla `property_rules` declara `property_id` como `UNIQUE` | Se rompe el principio de relación 1:1 estricta |
| 4 | Restricción CHECK en `property_amenities.amenity_key` coincide con la lista blanca | Error de validación al cargar amenidades inválidas |

---

## 4. Errores Comunes a Evitar

1. **Usar `FLOAT` o `NUMERIC` con decimales para precios:** La regla global 9 exige centavos de COP almacenados como `BIGINT` entero.
2. **Omitir `ON DELETE CASCADE` en tablas hijas:** Causará errores de clave foránea al eliminar una propiedad de la base de datos.

---

## 5. Comando de Verificación

```bash
./mvnw flyway:info
```
**Salida esperada:** `V002__create_properties_tables.sql` en estado `Success`.
