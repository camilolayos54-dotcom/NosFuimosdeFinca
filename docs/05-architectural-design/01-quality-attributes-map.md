# Deliverable 1 (D1): Quality Attributes Map

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

---

## 2. Utility Tree

| Escenario | Atributo | Business Value | Architectural Impact | Rank |
|---|---|---|---|---|
| Escenario 1: CachÃ© ISR CatÃ¡logo | Performance | Alto | Alto | 1 |
| Escenario 3: Data Isolation RLS | Security | Alto | Alto | 2 |
| Escenario 5: Real-Time Push | Availability | Alto | Alto | 3 |
| Escenario 4: Soft-Lock Concurrente | Performance | Alto | Medio | 4 |
| Escenario 2: Carga Media HD CDN | Performance | Medio | Medio | 5 |

---

## 3. Concrete Scenarios

#### Escenario 1: Performance (CachÃ© de CatÃ¡logo)
- **Source:** Turista anÃ³nimo (Browser/Mobile).
- **Stimulus:** Accede a la URL principal `/` o al catÃ¡logo de fincas `/api/v1/properties`.
- **Environment:** Bajo carga de trÃ¡fico normal de fin de semana (proporciÃ³n R/W 100:1).
- **Artifact:** Next.js App Router y CDN (Vercel).
- **Response:** El sistema renderiza el catÃ¡logo estÃ¡tico pre-construido y solicita la revalidaciÃ³n en background si el TTL de cachÃ© expirÃ³ (ISR).
- **Measure:** El First Contentful Paint (FCP) ocurre en < 1.5s y la latencia del TTFB (Time to First Byte) no supera los 200ms en el percentil 95. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-001]]`, `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|DS-01]]`)*

#### Escenario 2: Performance (Carga de Media HD)
- **Source:** Turista anÃ³nimo (Browser).
- **Stimulus:** Entra a la galerÃ­a de fotos de una finca especÃ­fica.
- **Environment:** ConexiÃ³n de red estÃ¡ndar, solicitando hasta 20 imÃ¡genes HD de 10MB.
- **Artifact:** Supabase Storage (Buckets) y su CDN integrada.
- **Response:** Las imÃ¡genes son servidas directamente desde la CDN perimetral, sin atravesar el servidor de aplicaciones de Next.js, previniendo cuellos de botella de ancho de banda.
- **Measure:** Las imÃ¡genes comienzan a cargar inmediatamente, manteniendo el FCP general de la pÃ¡gina < 1.5s. *(Fuente: `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|DS-02]]`)*

#### Escenario 3: Security (Data Isolation RLS)
- **Source:** Finquero autenticado (`OWNER_API`) malintencionado.
- **Stimulus:** Intenta enviar una peticiÃ³n `PATCH /api/v1/properties/999` (id ajeno) mediante Postman.
- **Environment:** Sistema operando normalmente.
- **Artifact:** Base de datos relacional (Supabase PostgreSQL).
- **Response:** La peticiÃ³n alcanza la base de datos, pero es denegada inmediatamente a nivel de fila antes de procesar cualquier mutaciÃ³n.
- **Measure:** El sistema retorna HTTP 403 (Forbidden) sin revelar existencia o alteraciÃ³n de datos ajenos. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-004]]`)*

#### Escenario 4: Performance / Scalability (Soft-Lock Concurrente)
- **Source:** Turista autenticado.
- **Stimulus:** Intenta crear una reserva `POST /api/v1/bookings` (creaciÃ³n de Soft-Lock).
- **Environment:** Bajo carga transaccional alta (â‰¤ 50 req/s concurrentes).
- **Artifact:** Next.js Server Actions y Supabase PostgreSQL.
- **Response:** El sistema crea el Soft-Lock, validando primero que las fechas no se solapen con otras transacciones concurrentes (Race Condition prevention).
- **Measure:** La API responde en el percentil 95 (p95) en â‰¤ 800ms bajo carga. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-002]]`)*

#### Escenario 5: Availability (Notificaciones Real-Time Push)
- **Source:** Sistema backend (Webhook procesado exitosamente).
- **Stimulus:** El sistema inserta un nuevo registro en la tabla `bookings` con estado `PENDING_APPROVAL`.
- **Environment:** El Finquero tiene su dashboard de gestiÃ³n abierto en el navegador (conexiÃ³n rural intermitente).
- **Artifact:** Supabase Realtime (PostgreSQL LISTEN/NOTIFY).
- **Response:** Supabase Realtime empuja el cambio (push) directamente al cliente conectado a travÃ©s de WebSockets, sin requerir que el cliente ejecute polling repetitivo.
- **Measure:** La notificaciÃ³n UI aparece en el dashboard del Finquero en < 2 segundos desde la inserciÃ³n en la BD, sin refrescar la pÃ¡gina. *(Fuente: `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|NS-01]]`)*

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D3 (Deployment Topology Decision):** Los escenarios dictan explÃ­citamente el uso de Vercel (CDN/ISR) y Supabase Cloud, justificando una topologÃ­a Serverless + BaaS.
- **D5 (Architectural Style Selection):** La delegaciÃ³n de seguridad y validaciones a Supabase reduce la necesidad de estilos pesados de backend (Hexagonal), inclinando el peso a favor de un MVC simplificado o Transaction Script en Server Actions.
- **D6 (Communication Pattern Decision):** El uso de Supabase Realtime marca la pauta para conexiones WebSockets de lectura pasiva.

