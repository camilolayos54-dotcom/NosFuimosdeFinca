# Índice Maestro de Tareas: Base de Datos (PostgreSQL 15+) — Nos Fuimos de Finca

**Proyecto:** Nos Fuimos de Finca  
**Capa:** Base de Datos Relacional (`PostgreSQL 15+` & `Flyway`)  
**Ubicación de Migraciones:** `backend/src/main/resources/db/migration/`  

---

## Descripción General de la Capa de Datos

La capa de persistencia se administra mediante scripts SQL normativos de **Flyway** (`V{numero}__{descripcion}.sql`). Cumple con:
- Primary Keys de tipo `UUID` con `gen_random_uuid()`.
- Montos monetarios obligatorios en centavos de COP (`BIGINT`), nunca flotantes.
- Soft-delete habilitado vía columna `deleted_at TIMESTAMPTZ`.
- Aislamiento de esquemas y claves foráneas con `ON DELETE CASCADE` para hijos.

---

## Catalogo Detallado de Tareas

| ID Tarea | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **DB-001** | [`TASK_DB_001`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_001_UsersTable.md) | **Crea el esquema de identidad y autenticación:** Script `V001__create_users_table.sql`. Crea la tabla `users` (UUID, email único, password hash BCrypt, rol CHECK ['TOURIST', 'AGENCY_USER', 'OWNER_API'], KYC status CHECK ['PENDING', 'VERIFIED', 'REJECTED'], campos bancarios para desembolso) y la tabla `refresh_tokens` vinculada a `users(id)` con `ON DELETE CASCADE` y hash de token único. | CRÍTICA | Ninguna |
| **DB-002** | [`TASK_DB_002`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_002_PropertiesTables.md) | **Crea el catálogo de propiedades y precios:** Script `V002__create_properties_tables.sql`. Crea `properties` (geolocalización lat/lng, capacidad máxima de huéspedes, tarifa base por noche `price_per_night BIGINT`, estado CHECK), `property_images` (URLs HD y orden de galería), `property_amenities` (lista blanca CHECK ['POOL', 'WIFI', 'BBQ', 'PET_FRIENDLY', 'PARKING', 'AIR_CONDITIONING', 'KITCHEN']), `property_rules` (relación 1:1 con horarios check-in/out), `property_availability` (bloqueos manuales por finquero) y `seasonal_prices` (tarifas de temporada alta en centavos). | CRÍTICA | DB-001 |
| **DB-003** | [`TASK_DB_003`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_003_BookingTables.md) | **Crea el motor de reservas y promociones:** Script `V003__create_booking_tables.sql`. Crea `coupons` (código único, porcentaje de descuento y límites de vigencia) y `bookings` (relaciona `property_id`, `guest_id`, `coupon_id` opcional, fechas `check_in` / `check_out`, desglose financiero estricto: `base_price_amount`, `cleaning_fee_amount`, `platform_fee_amount`, `taxes_amount`, `total_price` en BIGINT, y estado CHECK ['PENDING_PAYMENT', 'PENDING_APPROVAL', 'CONFIRMED', 'COMPLETED', 'CANCELLED']). | CRÍTICA | DB-002 |
| **DB-004** | [`TASK_DB_004`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_004_PaymentTables.md) | **Crea la pasarela de pagos y transacciones bancarias:** Script `V004__create_payment_tables.sql`. Crea `payments` (transacciones Wompi entrantes con `gateway_reference` ÚNICO, método de pago ['NEQUI', 'CARD', 'PSE', 'BANCOLOMBIA_TRANSFER'], y estado CHECK ['PENDING', 'APPROVED', 'DECLINED', 'VOIDED']) y `payouts` (desembolsos a finqueros vinculados 1:1 con reservas aprobadas, monto neto deduciendo comisión de plataforma). | CRÍTICA | DB-003 |
| **DB-005** | [`TASK_DB_005`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_005_PlatformTables.md) | **Crea las interacciones de plataforma y notificaciones:** Script `V005__create_platform_tables.sql`. Crea `wishlists` (relación UNIQUE user-property para favoritos), `reviews` (calificaciones 1-5 estrellas vinculadas UNIQUE 1:1 a reservas completadas para evitar reseñas falsas), y `notifications` (mensajes para el usuario por canal CHECK ['EMAIL', 'WHATSAPP', 'PUSH', 'IN_APP']). | ALTA | DB-001 |
| **DB-006** | [`TASK_DB_006`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/01_Database/TASK_DB_006_Indexes.md) | **Optimización de consultas mediante índices B-Tree:** Script `V006__create_indexes.sql`. Crea índices obligatorios en claves foráneas y columnas de filtrado frecuente (`properties(host_id)`, `properties(status) WHERE deleted_at IS NULL`, `bookings(property_id)`, `bookings(guest_id)`, `bookings(check_in, check_out)`, `notifications(user_id) WHERE read_at IS NULL`) para garantizar tiempos de respuesta <5ms. | ALTA | DB-005 |
