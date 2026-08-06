# TASK DB-001 — `V001__create_users_table.sql`

**Módulo:** `backend/src/main/resources/db/migration/`  
**Tipo de Archivo:** Script DDL de Migración Flyway  
**Prioridad:** CRÍTICA — Crea el esquema principal de identidades y sesiones de usuario.  
**Depende de:** Contenedor de PostgreSQL 15 corriendo  
**Bloquea:** Módulo IAM, autenticación JWT, registro de usuarios y resto del esquema SQL  

---

## 1. Propósito y Justificación Técnica

Crea las tablas fundamentales `users` y `refresh_tokens`. La tabla `users` almacena la información de perfil, credenciales con hash BCrypt, rol del sistema (`TOURIST`, `AGENCY_USER`, `OWNER_API`), datos bancarios de desembolso para el finquero y estado del proceso de verificación KYC (`PENDING`, `VERIFIED`, `REJECTED`). La tabla `refresh_tokens` almacena los tokens de refresco de sesión vinculados 1:N con borrado en cascada `ON DELETE CASCADE`.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear la estructura de carpetas de migración Flyway
1. En el directorio `backend/src/main/resources/`, crea la carpeta `db/migration/`.
2. Crea el archivo `V001__create_users_table.sql` (asegúrate de usar doble guión bajo entre `V001` y la descripción).

### Paso 2: Escribir la definición de la tabla `users`
1. Declara `CREATE TABLE users (...)` con los siguientes atributos:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `email VARCHAR(255) NOT NULL UNIQUE`
   * `password_hash VARCHAR(255) NOT NULL`
   * `role VARCHAR(50) NOT NULL CHECK (role IN ('TOURIST', 'AGENCY_USER', 'OWNER_API'))`
   * `full_name VARCHAR(255) NOT NULL`
   * `phone_number VARCHAR(20) NOT NULL`
   * `document_number VARCHAR(50) UNIQUE`
   * `avatar_url TEXT`
   * `bank_name VARCHAR(100)`
   * `bank_account_number VARCHAR(50)`
   * `bank_account_type VARCHAR(20) CHECK (bank_account_type IN ('AHORROS', 'CORRIENTE'))`
   * `kyc_status VARCHAR(30) NOT NULL DEFAULT 'PENDING' CHECK (kyc_status IN ('PENDING', 'VERIFIED', 'REJECTED'))`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
   * `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
   * `deleted_at TIMESTAMPTZ`

### Paso 3: Escribir la definición de la tabla `refresh_tokens`
1. Declara `CREATE TABLE refresh_tokens (...)` con los siguientes atributos:
   * `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
   * `user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE`
   * `token_hash VARCHAR(255) NOT NULL UNIQUE`
   * `expires_at TIMESTAMPTZ NOT NULL`
   * `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
   * `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`
   * `deleted_at TIMESTAMPTZ`

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Archivo nombrado exactamente `V001__create_users_table.sql` | Flyway ignora el archivo y el arranque de Spring Boot falla |
| 2 | Columna `email` tiene restricción `UNIQUE` | Se permiten registros duplicados con el mismo correo |
| 3 | Restricción CHECK en `role` restringe únicamente a `'TOURIST'`, `'AGENCY_USER'`, `'OWNER_API'` | Permite valores de rol inválidos en la base de datos |
| 4 | Clave foránea `refresh_tokens.user_id` incluye `ON DELETE CASCADE` | Errores de referencialidad al eliminar o purgar un usuario |
| 5 | Columna `deleted_at TIMESTAMPTZ` presente en ambas tablas | Falla la implementación del Soft-delete obligatorio |

---

## 4. Errores Comunes a Evitar

1. **Usar `VARCHAR` o `TIMESTAMP` sin zona horaria para `created_at` / `updated_at` / `deleted_at`:** Utilizar siempre `TIMESTAMPTZ` para evitar desfases de horas entre el servidor PostgreSQL y Colombia (COT UTC-5).
2. **Olvidar `DEFAULT gen_random_uuid()`:** Si no se especifica el valor por defecto, las inserciones SQL directas fallarán exigiendo un UUID manual.

---

## 5. Comando de Verificación

Ejecuta la migración de Flyway desde la raíz del backend:
```bash
./mvnw flyway:info
```
**Salida esperada:** La migración `V001__create_users_table.sql` debe figurar en estado `Success`.
