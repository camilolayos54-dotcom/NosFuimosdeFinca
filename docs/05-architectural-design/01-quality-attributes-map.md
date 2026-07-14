# Deliverable 1 (D1): Quality Attributes Map

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

---

## 2. Utility Tree

| Escenario | Atributo | Business Value | Architectural Impact | Rank |
|---|---|---|---|---|
| Escenario 1: Cache Spring Cache (@Cacheable) Catalogo | Performance | Alto | Alto | 1 |
| Escenario 3: Data Isolation Spring Security + Row-Level Filtering | Security | Alto | Alto | 2 |
| Escenario 5: Real-Time Push | Availability | Alto | Alto | 3 |
| Escenario 4: Soft-Lock Concurrente | Performance | Alto | Medio | 4 |
| Escenario 2: Carga Media HD CDN | Performance | Medio | Medio | 5 |

---

## 3. Concrete Scenarios

#### Escenario 1: Performance (Cache de Catalogo)
- **Source:** Turista anonimo (Browser/Mobile).
- **Stimulus:** Accede a la URL principal `/` o al catalogo de fincas `/api/v1/properties`.
- **Environment:** Bajo carga de trafico normal de fin de semana (proporcion R/W 100:1).
- **Artifact:** Spring Boot REST API y CDN (Railway/Render).
- **Response:** El sistema renderiza el catalogo estatico pre-construido y solicita la revalidacion en background si el TTL de cache expiro (Spring Cache (@Cacheable)).
- **Measure:** El First Contentful Paint (FCP) ocurre en < 1.5s y la latencia del TTFB (Time to First Byte) no supera los 200ms en el percentil 95. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-001]]`, `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|DS-01]]`)*

#### Escenario 2: Performance (Carga de Media HD)
- **Source:** Turista anonimo (Browser).
- **Stimulus:** Entra a la galeria de fotos de una finca especifica.
- **Environment:** Conexion de red estandar, solicitando hasta 20 imagenes HD de 10MB.
- **Artifact:** Cloudinary / S3 para imagenes (Buckets) y su CDN integrada.
- **Response:** Las imagenes son servidas directamente desde la CDN perimetral, sin atravesar el servidor de aplicaciones de Spring Boot (Java), previniendo cuellos de botella de ancho de banda.
- **Measure:** Las imagenes comienzan a cargar inmediatamente, manteniendo el FCP general de la pagina < 1.5s. *(Fuente: `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|DS-02]]`)*

#### Escenario 3: Security (Data Isolation Spring Security + Row-Level Filtering)
- **Source:** Finquero autenticado (`OWNER_API`) malintencionado.
- **Stimulus:** Intenta enviar una peticion `PATCH /api/v1/properties/999` (id ajeno) mediante Postman.
- **Environment:** Sistema operando normalmente.
- **Artifact:** Base de datos relacional (PostgreSQL PostgreSQL).
- **Response:** La peticion alcanza la base de datos, pero es denegada inmediatamente a nivel de fila antes de procesar cualquier mutacion.
- **Measure:** El sistema retorna HTTP 403 (Forbidden) sin revelar existencia o alteracion de datos ajenos. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-004]]`)*

#### Escenario 4: Performance / Scalability (Soft-Lock Concurrente)
- **Source:** Turista autenticado.
- **Stimulus:** Intenta crear una reserva `POST /api/v1/bookings` (creacion de Soft-Lock).
- **Environment:** Bajo carga transaccional alta (â‰¤ 50 req/s concurrentes).
- **Artifact:** Spring Boot (Java) Spring MVC @Service + @RestController y PostgreSQL PostgreSQL.
- **Response:** El sistema crea el Soft-Lock, validando primero que las fechas no se solapen con otras transacciones concurrentes (Race Condition prevention).
- **Measure:** La API responde en el percentil 95 (p95) en â‰¤ 800ms bajo carga. *(Fuente: `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements/example_output_nfr.md|NFR-002]]`)*

#### Escenario 5: Availability (Notificaciones Real-Time Push)
- **Source:** Sistema backend (Webhook procesado exitosamente).
- **Stimulus:** El sistema inserta un nuevo registro en la tabla `bookings` con estado `PENDING_APPROVAL`.
- **Environment:** El Finquero tiene su dashboard de gestion abierto en el navegador (conexion rural intermitente).
- **Artifact:** WebSockets via Spring WebSocket (PostgreSQL LISTEN/NOTIFY).
- **Response:** WebSockets via Spring WebSocket empuja el cambio (push) directamente al cliente conectado a traves de WebSockets, sin requerir que el cliente ejecute polling repetitivo.
- **Measure:** La notificacion UI aparece en el dashboard del Finquero en < 2 segundos desde la insercion en la BD, sin refrescar la pagina. *(Fuente: `[[PHASE_4_SYSTEM_MODELING/12.Architectural_Signals/example_output_d12_signals.md|NS-01]]`)*

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D3 (Deployment Topology Decision):** Los escenarios dictan explicitamente el uso de Railway/Render (CDN/Spring Cache (@Cacheable)) y PostgreSQL gestionado en Railway, justificando una topologia Dockerizado en Railway/Render + PostgreSQL + Spring Boot.
- **D5 (Architectural Style Selection):** La delegacion de seguridad y validaciones a PostgreSQL reduce la necesidad de estilos pesados de backend (Hexagonal), inclinando el peso a favor de un MVC simplificado o Transaction Script en Spring MVC @Service + @RestController.
- **D6 (Communication Pattern Decision):** El uso de WebSockets via Spring WebSocket marca la pauta para conexiones WebSockets de lectura pasiva.

