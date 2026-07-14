# Entregable 4 (D4): System Decomposition Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5 (D2 y D3):* Esta decisiÃ³n consolida los lÃ­mites lÃ³gicos identificados en el Bounded Context Formalization (`[[PHASE_5_ARCHITECTURAL_DESIGN/2.Bounded_Context_Formalization/example_output_d2_bounded_contexts.md]]`) y los empaqueta para ser compatibles con la infraestructura Serverless elegida en el Deployment Topology (`[[PHASE_5_ARCHITECTURAL_DESIGN/3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-002: AdopciÃ³n de PatrÃ³n "Modular Monolith" sobre Arquitectura Serverless

## Context
El sistema ha sido lÃ³gicamente dividido en 5 Bounded Contexts (Identity, Catalog, Booking, Billing, Notifications). Actualmente, el equipo de desarrollo consta de un tamaÃ±o reducido y la prioridad de negocio es el *Time-to-Market*. Adicionalmente, la topologÃ­a fÃ­sica ya elegida (Vercel Serverless) asume y optimiza el despliegue de repositorios Ãºnicos (Monorepos) construidos bajo el framework Next.js. Dividir la base de cÃ³digo en mÃºltiples repositorios, bases de datos o servicios fÃ­sicos separados en esta etapa temprana introducirÃ­a una fricciÃ³n operativa masiva.

## Options Considered
1. **Microservices (Despliegue Independiente):** Cada uno de los 5 Bounded Contexts vive en su propio repositorio con su propia base de datos, desplegados independientemente. **Rechazado.** ObligarÃ­a a implementar una red compleja (Service Mesh), forzarÃ­a a lidiar con problemas de consistencia eventual (ej. transacciones fallidas entre pagos y reservas) y destruirÃ­a la velocidad de desarrollo del equipo inicial. Vercel no estÃ¡ diseÃ±ado para orquestar microservicios puros.
2. **Monolito Tradicional ("Big Ball of Mud"):** Todo el cÃ³digo de los 5 contextos convive sin reglas estrictas de separaciÃ³n interna. **Rechazado.** Aunque es rÃ¡pido al inicio, el acoplamiento descontrolado a mediano plazo causa que un cambio menor (ej. notificaciones) rompa lÃ³gicas crÃ­ticas (ej. cobros).
3. **Modular Monolith (Monolito Modular):** El cÃ³digo se despliega como una **Ãºnica unidad atÃ³mica** (un solo proyecto Next.js en Vercel), compartiendo la misma conexiÃ³n a la base de datos (Supabase). Sin embargo, internamente el cÃ³digo fuente estÃ¡ rÃ­gidamente dividido en mÃ³dulos lÃ³gicos que reflejan los 5 Bounded Contexts, comunicÃ¡ndose a travÃ©s de interfaces formales (APIs internas), no leyendo directamente la base de datos del otro dominio. **Aprobado.**

## Decision
Construiremos el sistema como un **Modular Monolith**. Toda la aplicaciÃ³n (Frontend y Backend serverless) residirÃ¡ en un Ãºnico repositorio Git. El cÃ³digo fuente estarÃ¡ estructurado en espacios de nombres (namespaces) o carpetas estrictas (Ej. `src/modules/booking`, `src/modules/catalog`). Esta Ãºnica base de cÃ³digo serÃ¡ desplegada de forma atÃ³mica en Vercel.

## Consequences
- **Positive:** Simplicidad operativa inmejorable: un solo pipeline de CI/CD, un solo entorno local para los desarrolladores. Permite refactorizaciÃ³n segura y rÃ¡pida. Al compartir la base de datos (Supabase), se pueden utilizar transacciones atÃ³micas estÃ¡ndar (ACID Rollbacks) entre diferentes mÃ³dulos (ej. cobrar en Billing y reservar en Booking en la misma transacciÃ³n SQL), garantizando la consistencia absoluta de los datos de pagos sin escribir cÃ³digo complejo de compensaciÃ³n.
- **Negative:** Requiere extrema disciplina tÃ©cnica por parte del equipo. Si los desarrolladores ignoran las fronteras lÃ³gicas y comienzan a importar funciones o consultar directamente las tablas SQL de otros dominios saltÃ¡ndose las interfaces pÃºblicas de cada mÃ³dulo, la arquitectura degenerarÃ¡ inevitablemente en un monolito acoplado (Big Ball of Mud), perdiendo todos los beneficios del Domain-Driven Design y haciendo imposible extraer un mÃ³dulo a Microservicio en el futuro si el negocio crece masivamente.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para las siguientes decisiones:
- **D5 (Architectural Style Selection):** Al ser un Monolito Modular en Next.js, limitaremos los estilos arquitectÃ³nicos internos. No usaremos Clean Architecture pesada, sino estilos mÃ¡s Ã¡giles adecuados para Server Actions.
- **D6 (Communication Pattern Decision):** Simplifica la comunicaciÃ³n. La comunicaciÃ³n entre contextos serÃ¡ "In-Process" (llamadas a funciones dentro del mismo servidor de memoria) en lugar de HTTP inter-servicio, salvo para sistemas externos.
- **D9 (Component Diagram):** En el diagrama C4, veremos solo una gran caja de cÃ³digo (Web App Container), dividida visualmente en sub-mÃ³dulos lÃ³gicos, sin flechas de red entre ellos.

