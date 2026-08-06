# TASK DB-005 — `V005__create_platform_tables.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** ALTA — Crea tablas para favoritos, reseñas verificadas y sistema multicanal de notificaciones.  
**Depende de:** `TASK_DB_001`  
**Bloquea:** Módulos de Wishlist, Reviews y Notifications  

---

## 1. Propósito y Justificación Técnica

Crea las tablas `wishlists`, `reviews` y `notifications`. `reviews` impone la restricción única `UNIQUE(booking_id)` garantizando que únicamente turistas que hayan completado exitosamente una reserva puedan dejar una única reseña verificada (calificación 1 a 5 estrellas).

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo de migración
1. En `backend/src/main/resources/db/migration/`, crea `V005__create_platform_tables.sql`.

### Paso 2: Crear las tablas de la plataforma
1. **`wishlists`:**
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE`
   * `property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE`
   * `UNIQUE(user_id, property_id)`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`
2. **`reviews`:**
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `property_id UUID NOT NULL REFERENCES properties(id)`
   * `guest_id UUID NOT NULL REFERENCES users(id)`
   * `booking_id UUID NOT NULL UNIQUE REFERENCES bookings(id)`
   * `rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5)`
   * `comment TEXT`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`
3. **`notifications`:**
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE`
   * `type VARCHAR(30) NOT NULL CHECK (type IN ('EMAIL','WHATSAPP','PUSH','IN_APP'))`
   * `title VARCHAR(255) NOT NULL`, `body TEXT NOT NULL`
   * `read_at TIMESTAMPTZ`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`, `deleted_at TIMESTAMPTZ`

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Restricción `UNIQUE(user_id, property_id)` en `wishlists` | Duplicación de la misma finca en favoritos |
| 2 | Restricción `booking_id` `UNIQUE` en `reviews` | Un turista podría publicar múltiples reseñas por 1 estancia |
| 3 | Restricción CHECK en `reviews.rating BETWEEN 1 AND 5` | Calificaciones fuera del rango de 1 a 5 estrellas |

---

## 4. Errores Comunes a Evitar

1. **Permitir reseñas sin reserva válida:** La FK `booking_id` debe apuntar a la reserva real y ser obligatoria.

---

## 5. Comando de Verificación

```bash
./mvnw flyway:info
```
**Salida esperada:** `V005__create_platform_tables.sql` en estado `Success`.
