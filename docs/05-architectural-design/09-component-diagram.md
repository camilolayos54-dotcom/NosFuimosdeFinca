 # Entregable 9 (D9): Component Diagram (C4 Model)

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5:* Este diagrama consolida y rinde cuentas exactas de las decisiones previas de infraestructura (`[[PHASE_5_ARCHITECTURAL_DESIGN/3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md]]`), particion de codigo (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`), y protocolos de red (`[[PHASE_5_ARCHITECTURAL_DESIGN/6.Communication_Pattern_Decision/example_output_d6_communication_pattern.md]]`).

---

## 2. Level 1: System Context Diagram

El Nivel 1 muestra a "Nos Fuimos de Finca" como una caja negra (System), rodeada de los usuarios (Turista, Finquero) y las plataformas externas criticas identificadas en la Fase 4.

```mermaid
C4Context
title System Context Diagram - Nos Fuimos de Finca

Person(turista, "Turista", "Busca fincas, realiza reservas y pagos.")
Person(host, "Finquero (Host)", "Publica fincas, aprueba reservas y recibe cobros.")

System(marketplace, "Nos Fuimos de Finca", "Plataforma central (Marketplace B2C/B2B) para alquiler de fincas de recreo.")

System_Ext(wompi, "Wompi (Bancolombia)", "Pasarela externa de pagos (Tarjetas, PSE).")
System_Ext(whatsapp, "WhatsApp Business API", "Sistema de mensajeria para notificaciones push.")
System_Ext(postgresql_auth, "Spring Security + JWT/Storage", "Proveedor externo de Identidad (JWT) y CDN de imagenes.")

Rel(turista, marketplace, "Busca y reserva fincas", "HTTPS")
Rel(host, marketplace, "Administra inventario y aprueba reservas", "HTTPS")

Rel(marketplace, wompi, "Inicia transacciones de cobro y dispersion", "API REST")
Rel(marketplace, whatsapp, "Envia notificaciones de reserva", "Webhooks / API")
Rel(marketplace, postgresql_auth, "Autentica usuarios y lee/escribe fotos", "API REST")
```

---

## 3. Level 2: Container Diagram

El Nivel 2 hace zoom dentro de la caja "Marketplace" y revela las unidades de software desplegables reales (Containers). Aqui aplicamos estrictamente nuestra decision de **Monolito Modular** (1 solo ejecutable web) y etiquetamos cada flecha de red con el protocolo exacto.

```mermaid
C4Container
title Container Diagram - Nos Fuimos de Finca (Modular Monolith)

Person(turista, "Turista", "Busca fincas y reserva.")
Person(host, "Finquero (Host)", "Administra y aprueba.")

System_Boundary(c1, "Marketplace (Nos Fuimos de Finca)") {
    Container(webapp, "Web & API Application", "Spring Boot (Java) (Railway/Render (Dockerizado))", "Monolito Modular. Sirve la UI (Vite + JavaScript (frontend)) y ejecuta la logica de negocio (Spring MVC @Service + @RestController/APIs) para Booking, Billing, Catalog e Identity.")
    ContainerDb(database, "Primary Database & Realtime", "PostgreSQL (PostgreSQL + HikariCP (Connection Pooling))", "Almacena el modelo relacional (15 entidades). Provee pooling y suscripciones a cambios (WebSockets).")
}

System_Ext(wompi, "Wompi", "Pasarela de Pagos")
System_Ext(whatsapp, "WhatsApp API", "Notificaciones")

Rel(turista, webapp, "Navega, reserva y paga", "HTTPS / REST")
Rel(host, webapp, "Administra inventario", "HTTPS / REST")
Rel(host, database, "Recibe notificaciones en vivo", "WebSockets (WSS)")

Rel(webapp, database, "Lee y escribe datos transaccionales", "HTTPS / SQL")

Rel(webapp, wompi, "Inicia transacciones", "HTTPS / REST")
Rel(wompi, webapp, "Notifica estado de pago", "Webhooks (HTTPS)")

Rel(database, whatsapp, "Notifica a finquero (Database Trigger)", "Webhooks (HTTPS)")
```

---

## 4. Consistency Notes
- **Verificacion contra D4 (System Decomposition):** [OK]. Se muestra un solo contenedor ejecutable (`webapp`), honrando estrictamente la decision de desarrollar un Monolito Modular y descartar microservicios.
- **Verificacion contra D3 (Deployment Topology) & D6 (Communication):** [OK]. Los protocolos (`WebSockets/WSS`) y las capacidades avanzadas de la base de datos (Database Webhooks / `Spring Scheduler / @Async` para llamar a WhatsApp) encajan al 100% con la topologia PostgreSQL (PostgreSQL + Spring Boot) aprobada. No hay tecnologias inventadas en este diagrama.

---

## 5. Downstream Consumers
Este entregable es la fotografia oficial arquitectonica y es input obligatorio para:
- **D11 (Phase 5 RTM Update & Brief):** Al mapear requerimientos contra el codigo real, utilizaremos estos "Containers" como destino.
- **Phase 6 D1 (Codebase & Folder Architecture):** La Fase 6 debe tomar el contenedor `webapp` y estructurarlo fisicamente en un arbol de directorios de Spring Boot (Java), respetando sus modulos internos.
- **Phase 7 D3 (Walking Skeleton Implementation):** El primer hito de codigo real debera trazar con exito la ruta: `[UI Turista] -> [Spring Boot (Java) webapp] -> [PostgreSQL database]`, comprobando que la comunicacion entre contenedores funciona en la nube antes de programar las reglas de negocio.

