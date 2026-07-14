# Entregable 5 (D5): Architectural Style Selection

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5 (D4):* Este ADR rige las convenciones internas de cÃ³digo para las 5 unidades modulares establecidas en la decisiÃ³n de descomposiciÃ³n (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-003: SelecciÃ³n de Estilos HÃ­bridos (Clean Architecture vs Layered) por MÃ³dulo

## Context
Tras decidir desplegar un "Modular Monolith" en Vercel/Next.js (D4), necesitamos establecer las reglas de cÃ³mo estructurar el cÃ³digo fuente de cada mÃ³dulo internamente. SegÃºn el Domain Model (D6), no todos los mÃ³dulos tienen el mismo nivel de complejidad. 
Forzar "Clean Architecture" globalmente genera un exceso de abstracciones (interfaces, mappers, puertos) que ralentiza el desarrollo inicial en dominios simples (como CatÃ¡logo o Notificaciones). Sin embargo, usar un modelo simple "MVC/Layered" en los mÃ³dulos de Reservas y Pagos expone las reglas financieras crÃ­ticas y la mÃ¡quina de estados a bugs catastrÃ³ficos si se mezclan accidentalmente con librerÃ­as de Next.js o consultas SQL de Supabase.

## Options Considered
1. **Clean Architecture / Hexagonal Global:** Todos los mÃ³dulos aÃ­slan estrictamente su dominio mediante Puertos (Interfaces) y Adaptadores. **Rechazado.** AltÃ­simo coste inicial, fatiga cognitiva y "boilerplate" innecesario para leer un listado de fincas o enviar un email.
2. **Layered Architecture / MVC Global:** Todo el cÃ³digo usa un patrÃ³n simple de 3 capas (Controlador -> Servicio -> Repositorio). **Rechazado.** La lÃ³gica compleja de las transacciones (Booking) terminarÃ­a fuertemente acoplada a la infraestructura.
3. **Hybrid Modular Styles (SelecciÃ³n HÃ­brida):** Asignar un estilo arquitectÃ³nico basado en la complejidad real del dominio, protegiendo lo crÃ­tico con Clean Architecture y acelerando lo simple con Layered Architecture. **Aprobado.**

## Decision
Cada mÃ³dulo lÃ³gico implementarÃ¡ su estilo arquitectÃ³nico interno de acuerdo a su criticidad, basÃ¡ndose en capas conceptuales puras (sin dictaminar rutas de sistema de archivos fÃ­sicos aÃºn):

**A. MÃ³dulos de Alta Criticidad (Booking Engine, Billing & Payouts)**
- **Estilo:** `Clean Architecture (Light)`
- **Capas Conceptuales:**
  - `Domain:` Entidades puras y reglas de negocio (TypeScript sin librerÃ­as de UI o BD).
  - `Application:` Casos de uso (Use Cases) y orquestaciÃ³n.
  - `Infrastructure:` Adaptadores para Supabase, Wompi y Webhooks.

**B. MÃ³dulos de Baja/Media Criticidad (Catalog, Identity, Notification Service)**
- **Estilo:** `Layered Architecture` (Orientado a Server Actions)
- **Capas Conceptuales:**
  - `Application:` Puntos de entrada (Next.js Server Actions / API Routes).
  - `Service:` LÃ³gica de negocio y orquestaciÃ³n mezcladas.
  - `DataAccess:` Llamadas directas al SDK de Supabase.

## Consequences
- **Positive:** Se optimiza la velocidad del equipo (*Time-to-Market*). El equipo no pierde tiempo escribiendo abstracciones para leer el catÃ¡logo de fincas. Sin embargo, el cÃ³digo que procesa el dinero (Billing) o las aprobaciones B2B (Booking) estÃ¡ blindado, testeable de forma unitaria, e inmune a los cambios de librerÃ­as de infraestructura.
- **Negative:** Los desarrolladores deben cambiar su modelo mental ("context switch") al moverse entre dominios. Si un programador asume que todo el proyecto usa `Layered` e inyecta una consulta SQL directamente en la mÃ¡quina de estados del `Booking Engine` sin respetar la capa de `Domain`, romperÃ¡ el aislamiento arquitectÃ³nico. RequerirÃ¡ code reviews estrictos.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 â€” D1 (Codebase & Folder Architecture):** La Fase 6 deberÃ¡ mapear estas "capas conceptuales" abstractas a un Ã¡rbol de directorios fÃ­sico (carpetas reales) compatible con Next.js App Router (Ej. decidir si el `Domain` de Booking vive en `/src/modules/booking/domain`).
- **Phase 6 â€” D5 (Class & Entity Diagrams):** Dicta que las clases del Booking Engine deben separar sus entidades de dominio de sus modelos de base de datos, mientras que el CatÃ¡logo puede usar el mismo modelo para todo.
- **D10 (ADR Consolidation):** Se agregarÃ¡ al Ã­ndice global de decisiones de la Fase 5.

