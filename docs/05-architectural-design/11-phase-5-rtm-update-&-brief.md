# Entregable 11 (D11): Phase 5 RTM Update & Brief

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Approved

*Backlink a Fase 4:* Este documento actualiza la Matriz de Trazabilidad original cerrada en el entregable `[[PHASE_4_SYSTEM_MODELING/15.Phase_4_RTM_Update/example_output_d15_rtm.md]]`, expandiendola con la arquitectura definida en esta fase.

---

## 2. Traceability Matrix Update (Phase 3 â†’ 4 â†’ 5)

La siguiente matriz asegura que cada requerimiento de negocio exigido (FR) tenga un contenedor arquitectonico (servidor o funcion) que se haga cargo de el. Como definimos un Monolito Modular en el **D4**, todos recaen en el mismo gran componente de Spring Boot (Java).

| FR-ID | User Story | D3/D5 Wireframe | D7 Sequence | D9 API Endpoint | D9 Architectural Container (Fase 5) | Estado |
|---|---|---|---|---|---|---|
| FR-001 | Buscar fincas por ubicacion | `/search` | Guestâ†’APIâ†’DB | `GET /properties?location=X` | Web Application (Spring Boot (Java)) | âœ… OK |
| FR-002 | Reservar una finca | `/property/{id}` | Guestâ†’APIâ†’Wompiâ†’DB | `POST /bookings` | Web Application (Spring Boot (Java)) | âœ… OK |
| FR-003 | Cancelar una reserva | `/guest/bookings` | Guestâ†’APIâ†’DB | `PATCH /bookings/{id}` | Web Application (Spring Boot (Java)) | âœ… OK |
| FR-004 | Dashboard de Anfitrion | `/host/dashboard` | Hostâ†’APIâ†’DB | `GET /host/stats` | Web Application + WebSockets via Spring WebSocket | âœ… OK |
| FR-005 | Registro de usuario | `/auth/register` | Guestâ†’APIâ†’DB | `POST /auth/register` | Web Application + Spring Security + JWT | âœ… OK |
| FR-006 | Login de usuario | `/auth/login` | Guestâ†’APIâ†’DBâ†’JWT | `POST /auth/login` | Web Application + Spring Security + JWT | âœ… OK |
| FR-007 | Publicar finca (Host) | `/host/properties/new` | Hostâ†’APIâ†’S3â†’DB | `POST /properties` | Web Application + Cloudinary / S3 para imagenes| âœ… OK |

**GAPs Detectados:** 0 (Cero). Ningun requerimiento quedo huerfano.

---

## 3. Phase 5 Execution Brief

Durante la Fase 5 (*Architectural Design*), se transformo el modelado logico de la aplicacion en una topologia fisica e infraestructura tecnica concreta. Tras evaluar los NFRs (velocidad de carga < 1.5s y notificaciones en tiempo real B2B), se descarto el uso de orquestacion pesada (Kubernetes/IaaS), eligiendo una topologia basada en Railway/Render (PaaS) y PostgreSQL (PostgreSQL + Spring Boot). A nivel de base de codigo, se rechazaron firmemente los microservicios a favor de un **Monolito Modular**, estructurado internamente de forma hibrida: usando *Clean Architecture* para aislar y blindar las transacciones financieras y la maquina de estados de reservas, y arquitectura en capas (*Layered MVC*) para flexibilizar la lectura del catalogo.

El cruce final en la Matriz de Trazabilidad (RTM) de arriba confirma que **todos** los requerimientos y endpoints modelados en la Fase 4 encajan perfectamente dentro del Contenedor Web principal delineado en el Modelo C4 (D9). No se identificaron GAPs arquitectonicos. Los protocolos transversales (Auth JWT seguro, limitacion de APIs, Caching mediante Spring Cache (@Cacheable) y un pipeline de CI/CD Trunk-Based) estan documentados, consolidados (D10) y listos para materializarse en codigo.

> **Dictamen Final:** La Fase 5 (Architectural Design) esta formalmente CERRADA. El proyecto "Nos Fuimos de Finca" esta **AUTORIZADO** para iniciar la **Fase 6: Development / Implementation**.

---

## 4. Downstream Consumers
Este entregable es la llave final y es input obligatorio para:
- **Phase 6 â€” D0 (Execution Order):** Usa esta autorizacion de cierre como el "Gate" oficial para permitir que los desarrolladores abran sus IDEs y empiecen a escribir el primer `Maven init`.
- **Phase 7 â€” D1 (AI Task Breakdown & Sprint Planning):** Usara este mapeo FR â†’ Container como base matematica para crear los tickets en Jira o Github Projects.

