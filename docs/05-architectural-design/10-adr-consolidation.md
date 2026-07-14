# Entregable 10 (D10): ADR Consolidation

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 11:* Este documento serÃ¡ absorbido por la Fase 11 como el nÃºcleo inicial de la bitÃ¡cora histÃ³rica arquitectÃ³nica del proyecto.

---

## 2. ADR Registry Table

El siguiente registro consolida todas las decisiones de alto nivel tomadas y documentadas a lo largo de la Fase 5. Las 4 decisiones fundacionales se consideran `Accepted` y son de carÃ¡cter vinculante para el equipo de desarrollo de la Fase 6.

| ID | Title | Status | Date | Link |
|---|---|---|---|---|
| ADR-001 | AdopciÃ³n de TopologÃ­a Serverless PaaS (Vercel) y BaaS (Supabase) | Accepted | 2026-07-13 | [[3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md\|D3: Deployment Topology]] |
| ADR-002 | AdopciÃ³n de PatrÃ³n "Modular Monolith" sobre Arquitectura Serverless | Accepted | 2026-07-13 | [[4.System_Decomposition_Decision/example_output_d4_system_decomposition.md\|D4: System Decomposition]] |
| ADR-003 | SelecciÃ³n de Estilos HÃ­bridos (Clean Architecture vs Layered) por MÃ³dulo | Accepted | 2026-07-13 | [[5.Architectural_Style_Selection/example_output_d5_architectural_style.md\|D5: Architectural Style]] |
| ADR-004 | AdopciÃ³n de REST y WebSockets (Supabase Realtime) sobre Monolito | Accepted | 2026-07-13 | [[6.Communication_Pattern_Decision/example_output_d6_communication_pattern.md\|D6: Communication Pattern]] |

---

## 3. Architectural Trade-off Summary

**El Trade-off Dominante: Agilidad Operativa extrema a cambio de Vendor Lock-in y Disciplina de Equipo.**

El conjunto de decisiones arquitectÃ³nicas de la Fase 5 prioriza drÃ¡sticamente el *Time-to-Market* y la reducciÃ³n a cero del mantenimiento de infraestructura (Cero DevOps). Aceptamos el riesgo tÃ©cnico de anclar fuertemente la aplicaciÃ³n a plataformas especÃ­ficas (Vercel Serverless y el SDK nativo de Supabase) y el riesgo organizacional de construir un **Monolito Modular** (que requiere alta disciplina de los programadores para no degenerar en cÃ³digo acoplado). 

A cambio de asumir estos riesgos, el equipo se libera totalmente de gestionar Kubernetes, redes de microservicios o Message Brokers pesados, permitiÃ©ndole iterar el producto a mÃ¡xima velocidad con un solo pipeline de CI/CD. 

Para mitigar la debilidad del monolito, hemos implementado una polÃ­tica de protecciÃ³n asimÃ©trica (ADR-003): las Ã¡reas crÃ­ticas donde fluye el dinero (Reservas y Pagos) estÃ¡n aisladas con *Clean Architecture*, mientras que las Ã¡reas visuales (CatÃ¡logo) fluyen con un estilo mÃ¡s laxo para no frenar el desarrollo.

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D11 (Phase 5 RTM Update & Brief):** ServirÃ¡ como punto de comprobaciÃ³n de que todas las directrices arquitectÃ³nicas fueron cerradas y unificadas antes del paso a la Fase 6.
- **Phase 11 â€” D2 (ADR Log):** Este registro es la semilla principal del archivo histÃ³rico definitivo del proyecto.

