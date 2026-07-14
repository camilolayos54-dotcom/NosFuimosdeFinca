# Entregable 4 (D4): System Decomposition Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5 (D2 y D3):* Esta decision consolida los limites logicos identificados en el Bounded Context Formalization (`[[PHASE_5_ARCHITECTURAL_DESIGN/2.Bounded_Context_Formalization/example_output_d2_bounded_contexts.md]]`) y los empaqueta para ser compatibles con la infraestructura Dockerizado en Railway/Render elegida en el Deployment Topology (`[[PHASE_5_ARCHITECTURAL_DESIGN/3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-002: Adopcion de Patron "Modular Monolith" sobre Arquitectura Dockerizado en Railway/Render

## Context
El sistema ha sido logicamente dividido en 5 Bounded Contexts (Identity, Catalog, Booking, Billing, Notifications). Actualmente, el equipo de desarrollo consta de un tamano reducido y la prioridad de negocio es el *Time-to-Market*. Adicionalmente, la topologia fisica ya elegida (Railway/Render (Dockerizado)) asume y optimiza el despliegue de repositorios unicos (Monorepos) construidos bajo el framework Spring Boot. Dividir la base de codigo en multiples repositorios, bases de datos o servicios fisicos separados en esta etapa temprana introduciria una friccion operativa masiva.

## Options Considered
1. **Microservices (Despliegue Independiente):** Cada uno de los 5 Bounded Contexts vive en su propio repositorio con su propia base de datos, desplegados independientemente. **Rechazado.** Obligaria a implementar una red compleja (Service Mesh), forzaria a lidiar con problemas de consistencia eventual (ej. transacciones fallidas entre pagos y reservas) y destruiria la velocidad de desarrollo del equipo inicial. El equipo actual no tiene capacidad operacional para orquestar microservicios puros.
2. **Monolito Tradicional ("Big Ball of Mud"):** Todo el codigo de los 5 contextos convive sin reglas estrictas de separacion interna. **Rechazado.** Aunque es rapido al inicio, el acoplamiento descontrolado a mediano plazo causa que un cambio menor (ej. notificaciones) rompa logicas criticas (ej. cobros).
3. **Modular Monolith (Monolito Modular):** El codigo se despliega como una **unica unidad atomica** (un solo proyecto Spring Boot en Railway/Render), compartiendo la misma conexion a la base de datos (PostgreSQL). Sin embargo, internamente el codigo fuente esta rigidamente dividido en modulos logicos que reflejan los 5 Bounded Contexts, comunicandose a traves de interfaces formales (APIs internas), no leyendo directamente la base de datos del otro dominio. **Aprobado.**

## Decision
Construiremos el sistema como un **Modular Monolith**. Toda la aplicacion (Frontend y Backend dockerizado) residira en un unico repositorio Git. El codigo fuente estara estructurado en espacios de nombres (namespaces) o carpetas estrictas (Ej. `com.nosfuimosdefinica.booking`, `com.nosfuimosdefinica.catalog`). Esta unica base de codigo sera desplegada de forma atomica en Railway/Render.

## Consequences
- **Positive:** Simplicidad operativa inmejorable: un solo pipeline de CI/CD, un solo entorno local para los desarrolladores. Permite refactorizacion segura y rapida. Al compartir la base de datos (PostgreSQL), se pueden utilizar transacciones atomicas estandar (ACID Rollbacks) entre diferentes modulos (ej. cobrar en Billing y reservar en Booking en la misma transaccion SQL), garantizando la consistencia absoluta de los datos de pagos sin escribir codigo complejo de compensacion.
- **Negative:** Requiere extrema disciplina tecnica por parte del equipo. Si los desarrolladores ignoran las fronteras logicas y comienzan a importar funciones o consultar directamente las tablas SQL de otros dominios saltandose las interfaces publicas de cada modulo, la arquitectura degenerara inevitablemente en un monolito acoplado (Big Ball of Mud), perdiendo todos los beneficios del Domain-Driven Design y haciendo imposible extraer un modulo a Microservicio en el futuro si el negocio crece masivamente.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para las siguientes decisiones:
- **D5 (Architectural Style Selection):** Al ser un Monolito Modular en Spring Boot, limitaremos los estilos arquitectonicos internos. No usaremos Clean Architecture pesada, sino estilos mas agiles adecuados para Spring MVC Controllers y Services.
- **D6 (Communication Pattern Decision):** Simplifica la comunicacion. La comunicacion entre contextos sera "In-Process" (llamadas a funciones dentro del mismo servidor de memoria) en lugar de HTTP inter-servicio, salvo para sistemas externos.
- **D9 (Component Diagram):** En el diagrama C4, veremos solo una gran caja de codigo (Web App Container), dividida visualmente en sub-modulos logicos, sin flechas de red entre ellos.

