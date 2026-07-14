# Entregable 2 (D2): Bounded Context Formalization

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Diseno Arquitectonico
**Estado:** Aprobado

*Backlink a Fase 4:* Este documento agrupa las 15 entidades resultantes de la expansion del modelo de base de datos (`[[PHASE_4_SYSTEM_MODELING/6.Domain_Model_and_ERD/example_output_d6_erd.md]]`) bajo los principios formales de Domain-Driven Design (DDD).

---

## 2. Context Definitions

### Bounded Context: Identity & Profile
- **Clasificacion:** Generic
- **Responsabilidad:** Gestor maestro de autenticacion (AuthN), perfiles, roles y datos financieros base (cuenta bancaria para payouts).
- **Entidades que posee:** `users`, `refresh_tokens`.
- **Excepciones (Shared Kernel):** Los datos basicos de `users` (UID, Rol, Cuenta Bancaria) operan como *Shared Kernel*. Son inyectados globalmente por PostgreSQL via JWT y consumidos en modo solo lectura por Booking y Billing.

### Bounded Context: Property Catalog
- **Clasificacion:** Core
- **Responsabilidad:** Gestion integral del inventario de fincas, atributos fisicos, amenidades, precios por temporada y bloqueos de disponibilidad en el calendario.
- **Entidades que posee:** `properties`, `property_images`, `property_amenities`, `property_rules`, `property_availability`, `seasonal_prices`.
- **Excepciones:** Ninguna. (Provee su estado sincronamente al Booking Engine).

### Bounded Context: Booking Engine
- **Clasificacion:** Core
- **Responsabilidad:** Motor de orquestacion de intenciones de reserva, flujos de aprobacion B2B por parte del finquero, sistema de favoritos y resenas.
- **Entidades que posee:** `bookings`, `reviews`, `wishlists`.
- **Excepciones:** Ninguna.

### Bounded Context: Billing & Payouts
- **Clasificacion:** Supporting
- **Responsabilidad:** Manejo financiero con pasarelas externas. Ejecuta cobros (Payments) a turistas, valida descuentos (Coupons) y dispara liquidaciones (Payouts) a finqueros.
- **Entidades que posee:** `payments`, `payouts`, `coupons`.
- **Excepciones:** Ninguna.

### Bounded Context: Notification Service
- **Clasificacion:** Generic
- **Responsabilidad:** Despacho asincrono y centralizado de alertas omnicanal (Email, Push, WhatsApp).
- **Entidades que posee:** `notifications`.
- **Excepciones:** Ninguna.

---

## 3. Context Map Diagram

```mermaid
graph TD
    %% Generic & Shared
    Identity["Identity & Profile (Generic)<br/>[users, refresh_tokens]"]

    %% Core Domains
    Catalog["Property Catalog (Core)<br/>[properties, seasonal_prices, availability...]"]
    Booking["Booking Engine (Core)<br/>[bookings, reviews, wishlists]"]
    
    %% Supporting
    Billing["Billing & Payouts (Supporting)<br/>[payments, payouts, coupons]"]
    
    %% Generic Services
    Notif["Notification Service (Generic)<br/>[notifications]"]

    %% Relaciones Shared Kernel
    Identity -.->|Shared Kernel: UID, Role, Bank| Catalog
    Identity -.->|Shared Kernel: UID, Role, Bank| Booking
    Identity -.->|Shared Kernel: UID, Role, Bank| Billing

    %% Relaciones Core
    Catalog -->|Upstream/Downstream (Conformist)<br/>Provee Precio y Disp.| Booking
    
    %% Relaciones Financieras
    Booking -->|Upstream/Downstream (ACL)<br/>Gatilla Cobros y Desembolsos| Billing
    Billing -.->|ACL| Wompi((Wompi API Externo))
    
    %% Eventos
    Booking -.->|Events (Pub/Sub)| Notif
    Billing -.->|Events (Pub/Sub)| Notif
    Catalog -.->|Events (Pub/Sub)| Notif
    Notif -.->|ACL| WhatsApp((WhatsApp API))
```

---

## 4. Downstream Consumers
Este entregable es input obligatorio para las siguientes decisiones arquitectonicas:
- **D4 (System Decomposition Decision):** Determinara si estos 5 contextos se despliegan como 5 Microservicios independientes, o si se agrupan en un Monolito Modular con PostgreSQL.
- **D6 (Communication Pattern Decision):** Determinara como se implementan tecnicamente las lineas puente del Context Map (ej. Webhooks vs HTTP sincrono vs Base de Datos Compartida).
- **D9 (Component Diagram):** Las 5 cajas documentadas aqui formaran los Contenedores Nivel 2 en el modelo C4.

