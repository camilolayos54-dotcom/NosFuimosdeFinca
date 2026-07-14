 # Entregable 10 (D10): ADR Consolidation

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 Architectural Design
**Estado:** Aprobado

*Backlink a Fase 11:* Este documento sera absorbido por la Fase 11 como el nucleo inicial de la bitacora historica arquitectonica del proyecto.

---

## 2. ADR Registry Table

El siguiente registro consolida todas las decisiones de alto nivel tomadas y documentadas a lo largo de la Fase 5. Las 4 decisiones fundacionales se consideran `Accepted` y son de caracter vinculante para el equipo de desarrollo de la Fase 6.

| ID | Title | Status | Date | Link |
|---|---|---|---|---|
| ADR-001 | Adopcion de Topologia Railway/Render PaaS (Dockerizado) y PostgreSQL + Spring Boot (PostgreSQL) | Accepted | 2026-07-13 | [[3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md\|D3: Deployment Topology]] |
| ADR-002 | Adopcion de Patron "Modular Monolith" sobre Arquitectura Dockerizado en Railway/Render | Accepted | 2026-07-13 | [[4.System_Decomposition_Decision/example_output_d4_system_decomposition.md\|D4: System Decomposition]] |
| ADR-003 | Seleccion de Estilos Hibridos (Clean Architecture vs Layered) por Modulo | Accepted | 2026-07-13 | [[5.Architectural_Style_Selection/example_output_d5_architectural_style.md\|D5: Architectural Style]] |
| ADR-004 | Adopcion de REST y WebSockets (WebSockets via Spring WebSocket) sobre Monolito | Accepted | 2026-07-13 | [[6.Communication_Pattern_Decision/example_output_d6_communication_pattern.md\|D6: Communication Pattern]] |

---

## 3. Architectural Trade-off Summary

**El Trade-off Dominante: Agilidad Operativa extrema a cambio de Vendor Lock-in y Disciplina de Equipo.**

El conjunto de decisiones arquitectonicas de la Fase 5 prioriza drasticamente el *Time-to-Market* y la reduccion a cero del mantenimiento de infraestructura (Cero DevOps). Aceptamos el riesgo tecnico de anclar fuertemente la aplicacion a plataformas especificas (Railway/Render (Dockerizado) y el SDK nativo de PostgreSQL) y el riesgo organizacional de construir un **Monolito Modular** (que requiere alta disciplina de los programadores para no degenerar en codigo acoplado). 

A cambio de asumir estos riesgos, el equipo se libera totalmente de gestionar Kubernetes, redes de microservicios o Message Brokers pesados, permitiendole iterar el producto a maxima velocidad con un solo pipeline de CI/CD. 

Para mitigar la debilidad del monolito, hemos implementado una politica de proteccion asimetrica (ADR-003): las areas criticas donde fluye el dinero (Reservas y Pagos) estan aisladas con *Clean Architecture*, mientras que las areas visuales (Catalogo) fluyen con un estilo mas laxo para no frenar el desarrollo.

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D11 (Phase 5 RTM Update & Brief):** Servira como punto de comprobacion de que todas las directrices arquitectonicas fueron cerradas y unificadas antes del paso a la Fase 6.
- **Phase 11 D2 (ADR Log):** Este registro es la semilla principal del archivo historico definitivo del proyecto.

