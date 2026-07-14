# Entregable 6 (D6): Communication Pattern Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4 y 5:* Esta decision satisface los requerimientos de sincronizacion asincrona planteados en el API Conceptual Design (`[[PHASE_4_SYSTEM_MODELING/9.API_Conceptual_Design/example_output_d9_api.md]]`) y se adapta a la topologia monolitica decidida en el System Decomposition (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-004: Adopcion de REST y WebSockets (WebSockets via Spring WebSocket) sobre Monolito

## Context
La arquitectura del proyecto esta basada en un Modular Monolith Dockerizado en Railway/Render (D4). El diseno de la API (D9) expone operaciones transaccionales directas (ej. crear reserva, listar fincas) que no varian drasticamente su estructura de datos entre las distintas pantallas del cliente. Adicionalmente, el atributo de calidad (D1 - Escenario 5) y las State Machines (D8) exigen notificar al usuario finquero sobre nuevas peticiones de reserva en tiempo real, sin requerir que refresque su panel de administracion manualmente. 

## Options Considered
1. **GraphQL + Subscriptions:** Proveeria maxima flexibilidad al Frontend y actualizaciones push. **Rechazado.** Introduce alta complejidad operativa. Obliga a mantener "TypeDefs" y "Resolvers", y el equipo tendria que resolver manualmente los clasicos problemas N+1 de base de datos.
2. **REST puro (con Long-Polling):** Usar solo REST e invocar periodicamente el backend desde el cliente. **Rechazado.** En una arquitectura Dockerizado en Railway/Render (Railway/Render), cada invocacion cuesta dinero (compute time). Agotaria cuotas rapidamente y saturaria el Connection Pooler hacia PostgreSQL sin sentido.
3. **REST + WebSockets (WebSockets via Spring WebSocket):** Usar REST para escrituras/lecturas tradicionales y abrir un WebSocket pasivo gestionado por PostgreSQL para recibir transmisiones (broadcasts) directas desde la base de datos. **Aprobado.** 

## Decision
- **Client-Server (Frontend â†” Backend):** 
  Se utilizara **REST (JSON sobre HTTPS)** como protocolo base para todas las operaciones sincronas de lectura y mutacion (implementado a traves de Spring Boot (Java) Spring MVC @Service + @RestController y Route Handlers). 
  Para eventos en tiempo real, el Frontend se suscribira a un canal de **WebSockets** utilizando `WebSockets via Spring WebSocket` (escuchando mutaciones SQL directamente desde el motor PostgreSQL).
- **Server-Server (Modulo Interno â†” Modulo Interno):** 
  **N/A.** Dado que el sistema es un Monolito Modular (D4), los modulos no se comunicaran por red. Utilizaran comunicacion **In-Process** (importacion e invocacion de funciones de Java en la misma memoria).
- **Server-External (Backend â†” Terceros):** 
  Se utilizara **REST Asincrono (Webhooks HTTP POST)** para integrarse con Wompi y WhatsApp.

## Consequences
- **Positive:** Se aprovecha al 100% el SDK del ecosistema (PostgreSQL). Se dota al sistema de caracteristicas Push-Notification de nivel empresarial sin configurar brokers, RabbitMQ ni Socket.io. Reduce los costos de Dockerizado en Railway/Render al eliminar el polling.
- **Negative:** Dado que no usamos GraphQL, si una pagina futura requiere datos profundamente anidados (ej. Una finca con sus fotos, comentarios, detalles del host y ofertas), el Frontend debera realizar llamadas REST concurrentes, o el Backend debera escribir consultas SQL hechas a la medida para ese endpoint (sobre-fetching), reduciendo la agilidad del cliente.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **D8 (CI/CD & Environments Strategy):** Determina que las pruebas de integracion deben validar estructuras JSON planas (REST) y simulaciones de Webhooks, sin requerir la validacion de esquemas de Message Brokers (Kafka).
- **D9 (Component Diagram):** En el diagrama C4 nivel Container, las flechas del navegador a Railway/Render estaran etiquetadas como `[REST/HTTPS]`, las del navegador a PostgreSQL como `[WebSockets]`, y la conexion entre Railway/Render y PostgreSQL como `[Spring MVC REST Controllers]`.
- **D10 (ADR Consolidation):** Se indexara en la bitacora final de Fase 5.

