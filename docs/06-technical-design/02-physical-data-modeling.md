 # Deliverable 2 (D2): Physical Data Modeling

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Estado:** Approved

*Backlink a Fase 4 y 5:* Este entregable aterriza las entidades teoricas del Dominio (`[[PHASE_4_SYSTEM_MODELING/6.Domain_Model_and_ERD/example_output_d6_erd.md]]`) a codigo SQL ejecutable para PostgreSQL, que es el dialecto del motor PostgreSQL + Spring Boot elegido en la Fase 5 (PostgreSQL).

---

## 2. Scripts de Creacion de Base de Datos (DDL)

```sql
-- Habilitar extension UUID nativa de PostgreSQL
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. USERS
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role VARCHAR(50) NOT NULL,
    full_name TEXT NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    document_number VARCHAR(100) UNIQUE,
    avatar_url TEXT,
    bank_name TEXT,
    bank_account_number TEXT,
    bank_account_type VARCHAR(50),
    kyc_status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 2. PROPERTIES
CREATE TABLE properties (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    host_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price_per_night BIGINT NOT NULL,
    cleaning_fee BIGINT NOT NULL,
    max_guests INT NOT NULL,
    bedrooms_count INT NOT NULL,
    bathrooms_count INT NOT NULL,
    beds_count INT NOT NULL,
    location_lat NUMERIC(10, 7) NOT NULL,
    location_lng NUMERIC(10, 7) NOT NULL,
    location_address TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 3. PROPERTY_IMAGES
CREATE TABLE property_images (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    url_hd TEXT NOT NULL,
    sort_order INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 4. PROPERTY_AMENITIES
CREATE TABLE property_amenities (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    amenity_key VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 5. PROPERTY_RULES
CREATE TABLE property_rules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL UNIQUE REFERENCES properties(id) ON DELETE CASCADE,
    check_in_time VARCHAR(50) NOT NULL,
    check_out_time VARCHAR(50) NOT NULL,
    allows_pets BOOLEAN NOT NULL DEFAULT false,
    allows_parties BOOLEAN NOT NULL DEFAULT false,
    additional_rules TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 6. PROPERTY_AVAILABILITY (Fechas bloqueadas)
CREATE TABLE property_availability (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 7. SEASONAL_PRICES
CREATE TABLE seasonal_prices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price_per_night BIGINT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 8. WISHLISTS
CREATE TABLE wishlists (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 9. COUPONS
CREATE TABLE coupons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percentage NUMERIC(5,2),
    max_discount_amount BIGINT,
    valid_from TIMESTAMPTZ NOT NULL,
    valid_until TIMESTAMPTZ NOT NULL,
    usage_limit INT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 10. BOOKINGS
CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE RESTRICT,
    guest_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    coupon_id UUID REFERENCES coupons(id) ON DELETE SET NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    guest_count INT NOT NULL,
    agency_client_name TEXT,
    base_price_amount BIGINT NOT NULL,
    cleaning_fee_amount BIGINT NOT NULL,
    platform_fee_amount BIGINT NOT NULL,
    taxes_amount BIGINT NOT NULL,
    total_price BIGINT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    cancellation_reason TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 11. PAYMENTS
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    booking_id UUID NOT NULL REFERENCES bookings(id) ON DELETE RESTRICT,
    amount BIGINT NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'COP',
    gateway_reference VARCHAR(255) UNIQUE,
    payment_method VARCHAR(50),
    transaction_date TIMESTAMPTZ NOT NULL DEFAULT now(),
    receipt_url TEXT,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 12. PAYOUTS
CREATE TABLE payouts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    booking_id UUID NOT NULL UNIQUE REFERENCES bookings(id) ON DELETE RESTRICT,
    host_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    amount BIGINT NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'COP',
    bank_reference VARCHAR(255),
    transaction_date TIMESTAMPTZ,
    status VARCHAR(50) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 13. REVIEWS
CREATE TABLE reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
    guest_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 14. NOTIFICATIONS
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    read_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);

-- 15. REFRESH_TOKENS
CREATE TABLE refresh_tokens (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token_hash TEXT NOT NULL UNIQUE,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    deleted_at TIMESTAMPTZ
);
```

---

## 3. Scripts de Indexacion y Optimizacion

Estos indices estan disenados especificamente para resolver los requerimientos no funcionales (NFRs) de carga rapida del sistema (Catalogo y Dashboard de reservas).

```sql
-- 1. Acelerar el dashboard del Finquero (Buscar todas MIS fincas)
CREATE INDEX idx_properties_host_id ON properties(host_id);

-- 2. Acelerar el catalogo de Turistas (Listar solo las fincas activas en el buscador)
CREATE INDEX idx_properties_is_active ON properties(is_active);

-- 3. Acelerar cruces matematicos de fechas para los calculos de disponibilidad y precios estacionales
CREATE INDEX idx_property_availability_dates ON property_availability(start_date, end_date);
CREATE INDEX idx_seasonal_prices_dates ON seasonal_prices(start_date, end_date);

-- 4. Acelerar el montaje visual de fotos por finca en el UI
CREATE INDEX idx_property_images_property_id ON property_images(property_id);

-- 5. Acelerar el listado historico de reservas para el Turista (MIS VIAJES) y el Finquero (MIS HUESPEDES)
CREATE INDEX idx_bookings_guest_id ON bookings(guest_id);
CREATE INDEX idx_bookings_property_id ON bookings(property_id);

-- 6. Acelerar la campanita de notificaciones (Filtrado condicional parcial para ahorrar memoria en Postgres)
CREATE INDEX idx_notifications_user_unread ON notifications(user_id) WHERE read_at IS NULL;
```

---

## 4. Downstream Consumers
Este entregable es la hoja de ruta para la creacion fisica del proyecto:
- **Fase 6 D6 (Data Access & Repositories):** Usara los nombres de columna exactos y las sentencias SQL escritas aqui para los mappers y DTOs de codigo.
- **Fase 7 D4 (Database Migrations Implementation):** Tomara estos bloques de codigo, casi textualmente, y los insertara en el CLI de PostgreSQL como la primera gran migracion de la base de datos (`postgresql migration new initial_schema`).

