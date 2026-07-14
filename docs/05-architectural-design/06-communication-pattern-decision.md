# Entregable 6 (D6): Communication Pattern Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4 y 5:* Esta decisiÃ³n satisface los requerimientos de sincronizaciÃ³n asÃ­ncrona planteados en el API Conceptual Design (`[[PHASE_4_SYSTEM_MODELING/9.API_Conceptual_Design/example_output_d9_api.md]]`) y se adapta a la topologÃ­a monolÃ­tica decidida en el System Decomposition (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-004: AdopciÃ³n de REST y WebSockets (Supabase Realtime) sobre Monolito

## Context
La arquitectura del proyecto estÃ¡ basada en un Modular Monolith Serverless (D4). El diseÃ±o de la API (D9) expone operaciones transaccionales directas (ej. crear reserva, listar fincas) que no varÃ­an drÃ¡sticamente su estructura de datos entre las distintas pantallas del cliente. Adicionalmente, el atributo de calidad (D1 - Escenario 5) y las State Machines (D8) exigen notificar al usuario finquero sobre nuevas peticiones de reserva en tiempo real, sin requerir que refresque su panel de administraciÃ³n manualmente. 

## Options Considered
1. **GraphQL + Subscriptions:** ProveerÃ­a mÃ¡xima flexibilidad al Frontend y actualizaciones push. **Rechazado.** Introduce alta complejidad operativa. Obliga a mantener "TypeDefs" y "Resolvers", y el equipo tendrÃ­a que resolver manualmente los clÃ¡sicos problemas N+1 de base de datos.
2. **REST puro (con Long-Polling):** Usar solo REST e invocar periÃ³dicamente el backend desde el cliente. **Rechazado.** En una arquitectura Serverless (Vercel), cada invocaciÃ³n cuesta dinero (compute time). AgotarÃ­a cuotas rÃ¡pidamente y saturarÃ­a el Connection Pooler hacia PostgreSQL sin sentido.
3. **REST + WebSockets (Supabase Realtime):** Usar REST para escrituras/lecturas tradicionales y abrir un WebSocket pasivo gestionado por Supabase para recibir transmisiones (broadcasts) directas desde la base de datos. **Aprobado.** 

## Decision
- **Client-Server (Frontend â†” Backend):** 
  Se utilizarÃ¡ **REST (JSON sobre HTTPS)** como protocolo base para todas las operaciones sÃ­ncronas de lectura y mutaciÃ³n (implementado a travÃ©s de Next.js Server Actions y Route Handlers). 
  Para eventos en tiempo real, el Frontend se suscribirÃ¡ a un canal de **WebSockets** utilizando `Supabase Realtime` (escuchando mutaciones SQL directamente desde el motor PostgreSQL).
- **Server-Server (MÃ³dulo Interno â†” MÃ³dulo Interno):** 
  **N/A.** Dado que el sistema es un Monolito Modular (D4), los mÃ³dulos no se comunicarÃ¡n por red. UtilizarÃ¡n comunicaciÃ³n **In-Process** (importaciÃ³n e invocaciÃ³n de funciones de TypeScript en la misma memoria).
- **Server-External (Backend â†” Terceros):** 
  Se utilizarÃ¡ **REST AsÃ­ncrono (Webhooks HTTP POST)** para integrarse con Wompi y WhatsApp.

## Consequences
- **Positive:** Se aprovecha al 100% el SDK del ecosistema (Supabase). Se dota al sistema de caracterÃ­sticas Push-Notification de nivel empresarial sin configurar brokers, RabbitMQ ni Socket.io. Reduce los costos de Serverless al eliminar el polling.
- **Negative:** Dado que no usamos GraphQL, si una pÃ¡gina futura requiere datos profundamente anidados (ej. Una finca con sus fotos, comentarios, detalles del host y ofertas), el Frontend deberÃ¡ realizar llamadas REST concurrentes, o el Backend deberÃ¡ escribir consultas SQL hechas a la medida para ese endpoint (sobre-fetching), reduciendo la agilidad del cliente.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **D8 (CI/CD & Environments Strategy):** Determina que las pruebas de integraciÃ³n deben validar estructuras JSON planas (REST) y simulaciones de Webhooks, sin requerir la validaciÃ³n de esquemas de Message Brokers (Kafka).
- **D9 (Component Diagram):** En el diagrama C4 nivel Container, las flechas del navegador a Vercel estarÃ¡n etiquetadas como `[REST/HTTPS]`, las del navegador a Supabase como `[WebSockets]`, y la conexiÃ³n entre Vercel y Supabase como `[PostgREST]`.
- **D10 (ADR Consolidation):** Se indexarÃ¡ en la bitÃ¡cora final de Fase 5.

