# Entregable 11 (D11): Phase 5 RTM Update & Brief

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Approved

*Backlink a Fase 4:* Este documento actualiza la Matriz de Trazabilidad original cerrada en el entregable `[[PHASE_4_SYSTEM_MODELING/15.Phase_4_RTM_Update/example_output_d15_rtm.md]]`, expandiÃ©ndola con la arquitectura definida en esta fase.

---

## 2. Traceability Matrix Update (Phase 3 â†’ 4 â†’ 5)

La siguiente matriz asegura que cada requerimiento de negocio exigido (FR) tenga un contenedor arquitectÃ³nico (servidor o funciÃ³n) que se haga cargo de Ã©l. Como definimos un Monolito Modular en el **D4**, todos recaen en el mismo gran componente de Next.js.

| FR-ID | User Story | D3/D5 Wireframe | D7 Sequence | D9 API Endpoint | D9 Architectural Container (Fase 5) | Estado |
|---|---|---|---|---|---|---|
| FR-001 | Buscar fincas por ubicaciÃ³n | `/search` | Guestâ†’APIâ†’DB | `GET /properties?location=X` | Web Application (Next.js) | âœ… OK |
| FR-002 | Reservar una finca | `/property/{id}` | Guestâ†’APIâ†’Wompiâ†’DB | `POST /bookings` | Web Application (Next.js) | âœ… OK |
| FR-003 | Cancelar una reserva | `/guest/bookings` | Guestâ†’APIâ†’DB | `PATCH /bookings/{id}` | Web Application (Next.js) | âœ… OK |
| FR-004 | Dashboard de AnfitriÃ³n | `/host/dashboard` | Hostâ†’APIâ†’DB | `GET /host/stats` | Web Application + Supabase Realtime | âœ… OK |
| FR-005 | Registro de usuario | `/auth/register` | Guestâ†’APIâ†’DB | `POST /auth/register` | Web Application + Supabase Auth | âœ… OK |
| FR-006 | Login de usuario | `/auth/login` | Guestâ†’APIâ†’DBâ†’JWT | `POST /auth/login` | Web Application + Supabase Auth | âœ… OK |
| FR-007 | Publicar finca (Host) | `/host/properties/new` | Hostâ†’APIâ†’S3â†’DB | `POST /properties` | Web Application + Supabase Storage| âœ… OK |

**GAPs Detectados:** 0 (Cero). NingÃºn requerimiento quedÃ³ huÃ©rfano.

---

## 3. Phase 5 Execution Brief

Durante la Fase 5 (*Architectural Design*), se transformÃ³ el modelado lÃ³gico de la aplicaciÃ³n en una topologÃ­a fÃ­sica e infraestructura tÃ©cnica concreta. Tras evaluar los NFRs (velocidad de carga < 1.5s y notificaciones en tiempo real B2B), se descartÃ³ el uso de orquestaciÃ³n pesada (Kubernetes/IaaS), eligiendo una topologÃ­a basada en Vercel (PaaS) y Supabase (BaaS). A nivel de base de cÃ³digo, se rechazaron firmemente los microservicios a favor de un **Monolito Modular**, estructurado internamente de forma hÃ­brida: usando *Clean Architecture* para aislar y blindar las transacciones financieras y la mÃ¡quina de estados de reservas, y arquitectura en capas (*Layered MVC*) para flexibilizar la lectura del catÃ¡logo.

El cruce final en la Matriz de Trazabilidad (RTM) de arriba confirma que **todos** los requerimientos y endpoints modelados en la Fase 4 encajan perfectamente dentro del Contenedor Web principal delineado en el Modelo C4 (D9). No se identificaron GAPs arquitectÃ³nicos. Los protocolos transversales (Auth JWT seguro, limitaciÃ³n de APIs, Caching mediante ISR y un pipeline de CI/CD Trunk-Based) estÃ¡n documentados, consolidados (D10) y listos para materializarse en cÃ³digo.

> **Dictamen Final:** La Fase 5 (Architectural Design) estÃ¡ formalmente CERRADA. El proyecto "Nos Fuimos de Finca" estÃ¡ **AUTORIZADO** para iniciar la **Fase 6: Development / Implementation**.

---

## 4. Downstream Consumers
Este entregable es la llave final y es input obligatorio para:
- **Phase 6 â€” D0 (Execution Order):** Usa esta autorizaciÃ³n de cierre como el "Gate" oficial para permitir que los desarrolladores abran sus IDEs y empiecen a escribir el primer `npm init`.
- **Phase 7 â€” D1 (AI Task Breakdown & Sprint Planning):** UsarÃ¡ este mapeo FR â†’ Container como base matemÃ¡tica para crear los tickets en Jira o Github Projects.

