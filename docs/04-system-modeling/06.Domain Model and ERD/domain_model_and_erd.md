# Entregable 6 (D6): Domain Model y ERD Conceptual

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**Alcance:** Global (RevisiÃ³n Extendida B2B/B2C y Financiera)
**Estado:** Aprobado

---

## 1. Diagrama Entidad-RelaciÃ³n Conceptual (ERD)

*Backlink a Fase 3:* Las entidades se derivan del `[[PHASE_3_REQUIREMENTS_ENGINEERING/7.Module_Specification.md]]` y los flujos de dominio. Esta segunda revisiÃ³n profunda garantiza el soporte contable completo (Payouts, Cupones, Fees), la gestiÃ³n detallada del catÃ¡logo (Precios estacionales, Habitaciones) y la usabilidad (Favoritos).

Construido en `[[example_step_2_cardinality_relations.md]]`. 15 entidades base normalizadas en 3NF. NingÃºn tipo fÃ­sico de motor asignado.

````mermaid
    USERS {
        uuid id PK "[REQUERIDO, UNICO]"
        string email "[REQUERIDO, UK]"
        string password_hash "[REQUERIDO]"
        string role "[REQUERIDO]"
        string full_name "[REQUERIDO]"
        string phone_number "[REQUERIDO]"
        string document_number "UK"
        string avatar_url
        string bank_name
        string bank_account_number
        string bank_account_type
        string kyc_status "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PROPERTIES {
        uuid id PK "[REQUERIDO, UNICO]"
        uuid host_id FK "[REQUERIDO]"
        string name "[REQUERIDO]"
        text description "[REQUERIDO]"
        bigint price_per_night "[REQUERIDO, MONETARIO]"
        bigint cleaning_fee "[REQUERIDO, MONETARIO]"
        int max_guests "[REQUERIDO]"
        int bedrooms_count "[REQUERIDO]"
        int bathrooms_count "[REQUERIDO]"
        int beds_count "[REQUERIDO]"
        float location_lat "[REQUERIDO, GEO]"
        float location_lng "[REQUERIDO, GEO]"
        string location_address "[REQUERIDO]"
        string status "[REQUERIDO]"
        boolean is_active "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PROPERTY_IMAGES {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        string url_hd "[REQUERIDO]"
        int sort_order "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PROPERTY_AMENITIES {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        string amenity_key "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PROPERTY_RULES {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO, UNICO]"
        string check_in_time "[REQUERIDO]"
        string check_out_time "[REQUERIDO]"
        boolean allows_pets "[REQUERIDO]"
        boolean allows_parties "[REQUERIDO]"
        text additional_rules
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PROPERTY_AVAILABILITY {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        date start_date "[REQUERIDO]"
        date end_date "[REQUERIDO]"
        string reason "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    SEASONAL_PRICES {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        date start_date "[REQUERIDO]"
        date end_date "[REQUERIDO]"
        bigint price_per_night "[REQUERIDO, MONETARIO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    WISHLISTS {
        uuid id PK "[REQUERIDO]"
        uuid user_id FK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    COUPONS {
        uuid id PK "[REQUERIDO]"
        string code "[REQUERIDO, UK]"
        float discount_percentage
        bigint max_discount_amount "[MONETARIO]"
        date valid_from "[REQUERIDO]"
        date valid_until "[REQUERIDO]"
        int usage_limit
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    BOOKINGS {
        uuid id PK "[REQUERIDO, UNICO]"
        uuid property_id FK "[REQUERIDO]"
        uuid guest_id FK "[REQUERIDO]"
        uuid coupon_id FK
        date check_in "[REQUERIDO]"
        date check_out "[REQUERIDO]"
        int guest_count "[REQUERIDO]"
        string agency_client_name
        bigint base_price_amount "[REQUERIDO, MONETARIO]"
        bigint cleaning_fee_amount "[REQUERIDO, MONETARIO]"
        bigint platform_fee_amount "[REQUERIDO, MONETARIO]"
        bigint taxes_amount "[REQUERIDO, MONETARIO]"
        bigint total_price "[REQUERIDO, MONETARIO]"
        string status "[REQUERIDO]"
        string cancellation_reason
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PAYMENTS {
        uuid id PK "[REQUERIDO, UNICO]"
        uuid booking_id FK "[REQUERIDO]"
        bigint amount "[REQUERIDO, MONETARIO]"
        string currency "[REQUERIDO]"
        string gateway_reference "UK"
        string payment_method
        timestamp transaction_date "[REQUERIDO]"
        string receipt_url
        string status "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    PAYOUTS {
        uuid id PK "[REQUERIDO, UNICO]"
        uuid booking_id FK "[REQUERIDO, UNICO]"
        uuid host_id FK "[REQUERIDO]"
        bigint amount "[REQUERIDO, MONETARIO]"
        string currency "[REQUERIDO]"
        string bank_reference
        timestamp transaction_date
        string status "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    REVIEWS {
        uuid id PK "[REQUERIDO]"
        uuid property_id FK "[REQUERIDO]"
        uuid guest_id FK "[REQUERIDO]"
        int rating "[REQUERIDO]"
        text comment
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    NOTIFICATIONS {
        uuid id PK "[REQUERIDO]"
        uuid user_id FK "[REQUERIDO]"
        string type "[REQUERIDO]"
        string title "[REQUERIDO]"
        text body "[REQUERIDO]"
        timestamp read_at
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    REFRESH_TOKENS {
        uuid id PK "[REQUERIDO]"
        uuid user_id FK "[REQUERIDO]"
        string token_hash "[REQUERIDO, UK]"
        timestamp expires_at "[REQUERIDO]"
        timestamp created_at "[AUDITORIA]"
        timestamp updated_at "[AUDITORIA]"
        timestamp deleted_at "[AUDITORIA]"
    }

    %% Relaciones
    USERS ||--o{ PROPERTIES : "hosts (1:N)"
    USERS ||--o{ BOOKINGS : "guest_of (1:N)"
    USERS ||--o{ REVIEWS : "writes (1:N)"
    USERS ||--o{ NOTIFICATIONS : "receives_alerts (1:N)"
    USERS ||--o{ REFRESH_TOKENS : "owns_session (1:N)"
    USERS ||--o{ WISHLISTS : "saves (1:N)"
    USERS ||--o{ PAYOUTS : "receives_money (1:N)"
    
    PROPERTIES ||--o{ PROPERTY_IMAGES : "has_photos (1:N)"
    PROPERTIES ||--o{ PROPERTY_AMENITIES : "has_amenities (1:N)"
    PROPERTIES ||--|| PROPERTY_RULES : "enforces (1:1)"
    PROPERTIES ||--o{ PROPERTY_AVAILABILITY : "blocked_dates (1:N)"
    PROPERTIES ||--o{ SEASONAL_PRICES : "seasonal_rates (1:N)"
    PROPERTIES ||--o{ BOOKINGS : "receives (1:N)"
    PROPERTIES ||--o{ REVIEWS : "is_reviewed (1:N)"
    PROPERTIES ||--o{ WISHLISTS : "is_favorited (1:N)"
    
    COUPONS ||--o{ BOOKINGS : "applied_to (1:N)"
    BOOKINGS ||--o{ PAYMENTS : "generates_transaction (1:N)"
    BOOKINGS ||--|| PAYOUTS : "triggers_payout (1:1)"
```

---

## 2. Diccionario de Sensibilidad Conceptual

Construido en `[[example_step_3_data_dictionary.md]]`. Las etiquetas `[MONETARIO]`, `[ÃšNICO]`, `[REQUERIDO]`, `[GEO]` son instrucciones semÃ¡nticas para P6-D2 (Physical Data Modeling). NingÃºn tipo SQL exacto fue asignado en esta fase.

### 2.1 Tablas Base de Identidad y Perfil

#### Tabla: `users`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `email` | `[REQUERIDO]`, `[ÃšNICO]` |
| `password_hash` | `[REQUERIDO]` |
| `role` | `[REQUERIDO]` (TOURIST, AGENCY_USER, OWNER_API) |
| `full_name` | `[REQUERIDO]` |
| `phone_number` | `[REQUERIDO]` (CrÃ­tico para WhatsApp B2B) |
| `document_number` | `[ÃšNICO]` (Opcional hasta el KYC) |
| `avatar_url` | (Opcional, perfil UX) |
| `bank_name` | (Requerido para payouts si es OWNER_API) |
| `bank_account_number` | (Requerido para payouts) |
| `bank_account_type` | (Ahorros/Corriente) |
| `kyc_status` | `[REQUERIDO]` |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `wishlists`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `user_id` | `[FK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

### 2.2 Tablas Base de CatÃ¡logo (Inmuebles)

#### Tabla: `properties`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `host_id` | `[FK]`, `[REQUERIDO]` |
| `name` | `[REQUERIDO]` |
| `description` | `[REQUERIDO]` |
| `price_per_night` | `[REQUERIDO]`, `[MONETARIO]` (Tarifa Base) |
| `cleaning_fee` | `[REQUERIDO]`, `[MONETARIO]` (Fijo por estadÃ­a) |
| `max_guests` | `[REQUERIDO]` |
| `bedrooms_count` | `[REQUERIDO]` |
| `bathrooms_count` | `[REQUERIDO]` |
| `beds_count` | `[REQUERIDO]` |
| `location_lat` | `[GEO]`, `[REQUERIDO]` |
| `location_lng` | `[GEO]`, `[REQUERIDO]` |
| `location_address` | `[REQUERIDO]` |
| `status` | `[REQUERIDO]` (Pendiente, Aprobado, Suspendido) |
| `is_active` | `[REQUERIDO]` (Soft-delete flag) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `seasonal_prices`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `start_date` | `[REQUERIDO]` |
| `end_date` | `[REQUERIDO]` |
| `price_per_night` | `[REQUERIDO]`, `[MONETARIO]` (Sobreescribe base) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `property_images`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `url_hd` | `[REQUERIDO]` |
| `sort_order` | `[REQUERIDO]` |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `property_amenities`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `amenity_key` | `[REQUERIDO]` (pool, wifi, bbq, pet-friendly) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `property_rules`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `check_in_time` | `[REQUERIDO]` |
| `check_out_time` | `[REQUERIDO]` |
| `allows_pets` | `[REQUERIDO]` |
| `allows_parties` | `[REQUERIDO]` |
| `additional_rules` | (Opcional) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `property_availability`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `start_date` | `[REQUERIDO]` |
| `end_date` | `[REQUERIDO]` |
| `reason` | `[REQUERIDO]` (Maintenance, Personal Use) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

### 2.3 Tablas Transaccionales y Financieras

#### Tabla: `coupons`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `code` | `[REQUERIDO]`, `[ÃšNICO]` (Ej. FINCA26) |
| `discount_percentage` | (Mutuamente excluyente con amount) |
| `max_discount_amount`| `[MONETARIO]` (LÃ­mite del descuento) |
| `valid_from` | `[REQUERIDO]` |
| `valid_until` | `[REQUERIDO]` |
| `usage_limit` | (Opcional, lÃ­mite de redenciones) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `bookings`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `guest_id` | `[FK]`, `[REQUERIDO]` |
| `coupon_id` | `[FK]` (Opcional) |
| `check_in` | `[REQUERIDO]` |
| `check_out` | `[REQUERIDO]` |
| `guest_count` | `[REQUERIDO]` |
| `agency_client_name`| (Opcional, B2B) |
| `base_price_amount` | `[REQUERIDO]`, `[MONETARIO]` |
| `cleaning_fee_amount`| `[REQUERIDO]`, `[MONETARIO]` |
| `platform_fee_amount`| `[REQUERIDO]`, `[MONETARIO]` (Ganancia Nos Fuimos de Finca) |
| `taxes_amount` | `[REQUERIDO]`, `[MONETARIO]` |
| `total_price` | `[REQUERIDO]`, `[MONETARIO]` |
| `status` | `[REQUERIDO]` (PENDING, APPROVED, CANCELLED...) |
| `cancellation_reason` | (Opcional) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `payments` (Ingresos a Wompi)
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `booking_id` | `[FK]`, `[REQUERIDO]` |
| `amount` | `[REQUERIDO]`, `[MONETARIO]` |
| `currency` | `[REQUERIDO]` |
| `gateway_reference` | `[ÃšNICO]` |
| `payment_method` | (Opcional, Nequi/Card/PSE) |
| `transaction_date` | `[REQUERIDO]` |
| `receipt_url` | (Opcional) |
| `status` | `[REQUERIDO]` |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `payouts` (Egresos al Finquero)
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `booking_id` | `[FK]`, `[REQUERIDO]`, `[ÃšNICO]` |
| `host_id` | `[FK]`, `[REQUERIDO]` |
| `amount` | `[REQUERIDO]`, `[MONETARIO]` (Total - Platform Fee) |
| `currency` | `[REQUERIDO]` |
| `bank_reference` | (ID de transferencia del banco) |
| `transaction_date` | (Fecha efectiva del pago) |
| `status` | `[REQUERIDO]` (PENDING, PROCESSING, PAID, FAILED) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

### 2.4 Tablas de Plataforma

#### Tabla: `reviews`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `property_id` | `[FK]`, `[REQUERIDO]` |
| `guest_id` | `[FK]`, `[REQUERIDO]` |
| `rating` | `[REQUERIDO]` (Escala 1-5) |
| `comment` | (Opcional) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `notifications`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `user_id` | `[FK]`, `[REQUERIDO]` |
| `type` | `[REQUERIDO]` (Email, WhatsApp, Push) |
| `title` | `[REQUERIDO]` |
| `body` | `[REQUERIDO]` |
| `read_at` | (Opcional) |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

#### Tabla: `refresh_tokens`
| Columna | Etiqueta Conceptual |
|---|---|
| `id` | `[PK]`, `[REQUERIDO]` |
| `user_id` | `[FK]`, `[REQUERIDO]` |
| `token_hash` | `[REQUERIDO]`, `[ÃšNICO]` |
| `expires_at` | `[REQUERIDO]` |
| `created_at`, `updated_at`, `deleted_at` | `[AUDITORÃA]` |

---

**Nota de ensamblaje:** Este documento consolida aspectos CONCEPTUALES rigurosos que abarcan la totalidad del dominio B2B/B2C, sentando las bases para reglas de negocio (ej. lÃ­mites geogrÃ¡ficos, manejo transaccional). Las decisiones de tipos de datos de motor y constraints se delegan a P6-D2 (Physical Data Modeling).

### ImplicaciÃ³n de Fase
- El diagrama ERD representa 15 entidades con flujos lÃ³gicos cubiertos. Las relaciones financieras de desembolso (`payouts`) y descuentos (`coupons`) garantizan viabilidad comercial.
- El Diccionario de Datos es integral, asegurando trazabilidad de todo cÃ©ntimo procesado y los datos bancarios del Finquero.
- **Proceder a D7:** Diagramas de Secuencia del Sistema.

