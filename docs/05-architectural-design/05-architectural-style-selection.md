 # Entregable 5 (D5): Architectural Style Selection

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5 (D4):* Este ADR rige las convenciones internas de codigo para las 5 unidades modulares establecidas en la decision de descomposicion (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-003: Seleccion de Estilos Hibridos (Clean Architecture vs Layered) por Modulo

## Context
Tras decidir desplegar un "Modular Monolith" en Railway/Render/Spring Boot (Java) (D4), necesitamos establecer las reglas de como estructurar el codigo fuente de cada modulo internamente. Segun el Domain Model (D6), no todos los modulos tienen el mismo nivel de complejidad. 
Forzar "Clean Architecture" globalmente genera un exceso de abstracciones (interfaces, mappers, puertos) que ralentiza el desarrollo inicial en dominios simples (como Catalogo o Notificaciones). Sin embargo, usar un modelo simple "MVC/Layered" en los modulos de Reservas y Pagos expone las reglas financieras criticas y la maquina de estados a bugs catastroficos si se mezclan accidentalmente con librerias de Spring Boot (Java) o consultas SQL de PostgreSQL.

## Options Considered
1. **Clean Architecture / Hexagonal Global:** Todos los modulos aislan estrictamente su dominio mediante Puertos (Interfaces) y Adaptadores. **Rechazado.** Altisimo coste inicial, fatiga cognitiva y "boilerplate" innecesario para leer un listado de fincas o enviar un email.
2. **Layered Architecture / MVC Global:** Todo el codigo usa un patron simple de 3 capas (Controlador -> Servicio -> Repositorio). **Rechazado.** La logica compleja de las transacciones (Booking) terminaria fuertemente acoplada a la infraestructura.
3. **Hybrid Modular Styles (Seleccion Hibrida):** Asignar un estilo arquitectonico basado en la complejidad real del dominio, protegiendo lo critico con Clean Architecture y acelerando lo simple con Layered Architecture. **Aprobado.**

## Decision
Cada modulo logico implementara su estilo arquitectonico interno de acuerdo a su criticidad, basandose en capas conceptuales puras (sin dictaminar rutas de sistema de archivos fisicos aun):

**A. Modulos de Alta Criticidad (Booking Engine, Billing & Payouts)**
- **Estilo:** `Clean Architecture (Light)`
- **Capas Conceptuales:**
  - `Domain:` Entidades puras y reglas de negocio (Java sin librerias de UI o BD).
  - `Application:` Casos de uso (Use Cases) y orquestacion.
  - `Infrastructure:` Adaptadores para PostgreSQL, Wompi y Webhooks.

**B. Modulos de Baja/Media Criticidad (Catalog, Identity, Notification Service)**
- **Estilo:** `Layered Architecture` (Orientado a Spring MVC @Service + @RestController)
- **Capas Conceptuales:**
  - `Application:` Puntos de entrada (Spring Boot (Java) Spring MVC @Service + @RestController / API Routes).
  - `Service:` Logica de negocio y orquestacion mezcladas.
  - `DataAccess:` Llamadas directas al SDK de PostgreSQL.

## Consequences
- **Positive:** Se optimiza la velocidad del equipo (*Time-to-Market*). El equipo no pierde tiempo escribiendo abstracciones para leer el catalogo de fincas. Sin embargo, el codigo que procesa el dinero (Billing) o las aprobaciones B2B (Booking) esta blindado, testeable de forma unitaria, e inmune a los cambios de librerias de infraestructura.
- **Negative:** Los desarrolladores deben cambiar su modelo mental ("context switch") al moverse entre dominios. Si un programador asume que todo el proyecto usa `Layered` e inyecta una consulta SQL directamente en la maquina de estados del `Booking Engine` sin respetar la capa de `Domain`, rompera el aislamiento arquitectonico. Requerira code reviews estrictos.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 D1 (Codebase & Folder Architecture):** La Fase 6 debera mapear estas "capas conceptuales" abstractas a un arbol de directorios fisico (carpetas reales) compatible con Spring Boot REST API (Ej. decidir si el `Domain` de Booking vive en `/com.nosfuimosdefinica.booking/domain`).
- **Phase 6 D5 (Class & Entity Diagrams):** Dicta que las clases del Booking Engine deben separar sus entidades de dominio de sus modelos de base de datos, mientras que el Catalogo puede usar el mismo modelo para todo.
- **D10 (ADR Consolidation):** Se agregara al indice global de decisiones de la Fase 5.

