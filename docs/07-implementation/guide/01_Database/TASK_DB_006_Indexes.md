# TASK DB-006 — `V006__create_indexes.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** ALTA — Optimización de índices B-Tree para la búsqueda facetada y consultas de rendimiento.  
**Depende de:** `TASK_DB_005`  
**Bloquea:** Pruebas de carga y tiempo de respuesta <5ms en producción  

---

## 1. Propósito y Justificación Técnica

Crea índices B-Tree estratégicos en claves foráneas y columnas con cláusulas `WHERE` de filtrado concurrente para evitar exploraciones completas de tabla (*seq scans*) durante las búsquedas del turista y la actualización del panel del finquero.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo de migración
1. En `backend/src/main/resources/db/migration/`, crea `V006__create_indexes.sql`.

### Paso 2: Declarar la creación de índices B-Tree
1. Agrega las sentencias SQL:
   * `CREATE INDEX idx_properties_host_id ON properties(host_id);`
   * `CREATE INDEX idx_properties_status ON properties(status) WHERE deleted_at IS NULL;`
   * `CREATE INDEX idx_bookings_property_id ON bookings(property_id);`
   * `CREATE INDEX idx_bookings_guest_id ON bookings(guest_id);`
   * `CREATE INDEX idx_bookings_status ON bookings(status);`
   * `CREATE INDEX idx_bookings_check_in_out ON bookings(check_in, check_out);`
   * `CREATE INDEX idx_notifications_user_id ON notifications(user_id) WHERE read_at IS NULL;`
   * `CREATE INDEX idx_refresh_tokens_user_id ON refresh_tokens(user_id);`

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Los 8 índices B-Tree creados correctamente en la base de datos | Consultas lentas >500ms al crecer el volumen de datos |
| 2 | Índices parciales con `WHERE deleted_at IS NULL` aplicados | El índice incluiría registros eliminados lógicamente |

---

## 4. Errores Comunes a Evitar

1. **Olvidar la condición `WHERE deleted_at IS NULL` en índices de consulta pública:** Indexar filas eliminadas aumenta el tamaño del índice en disco innecesariamente.

---

## 5. Comando de Verificación

```bash
./mvnw flyway:info
```
**Salida esperada:** `V006__create_indexes.sql` en estado `Success`.
