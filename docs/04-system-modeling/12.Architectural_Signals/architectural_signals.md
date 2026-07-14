 # Entregable 12 (D12): Sintesis de Senales Arquitectonicas

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Estado:** Aprobado

---

## 1. Senales Extraidas (Red y Datos)

### 1.1 Senales de Capa de Red

| Signal ID | Descripcion | Modulo Origen | Implicacion para Fase 5 |
|---|---|---|---|
| **NS-01** | Real-Time Push: el Dashboard del Finquero debe recibir alertas de nueva reserva en tiempo real sin refrescar la pagina. | `MOD-NOT` (D10) | Implementar **PostgreSQL Realtime (PostgreSQL LISTEN/NOTIFY)** sobre la tabla `bookings`. Elimina la necesidad de un servidor WebSocket/Redis PubSub custom. |

### 1.2 Senales de Capa de Datos

| Signal ID | Descripcion | Entidad Origen (D6) | Implicacion para Fase 5 |
|---|---|---|---|
| **DS-01** | Proporcion R/W de ~100:1 en el catalogo de fincas (`properties`). Todo Turista ejecuta `GET /api/v1/properties`. | `properties` + `GET /api/v1/properties` | Aprovechar cache de CDN estatica para Spring Cache (@Cacheable) (Spring Boot) para el listado publico. |
| **DS-02** | Archivos binarios HD (hasta 10MB/foto, 5-20 fotos por finca). No pueden almacenarse en el disco local del servidor. | `property_images.url_hd` | Implementar **Cloudinary / S3**. El servidor Spring Boot (Java) sube el archivo al bucket y guarda la URL publica en BD. |

---

## 2. Estado de Pre-Architecture Blockers

| Signal | Estado | Resolucion |
|---|---|---|
| **NS-01** (PostgreSQL Realtime) | [OK] `RESUELTO` | Incluido en el stack de PostgreSQL (SaaS). Evita montar websockets manuales. |
| **DS-01** (Spring Boot (Java) Cache) | [OK] `RESUELTO` | Nativo en Spring Boot (Java) (Spring Cache). |
| **DS-02** (Cloudinary / S3) | [OK] `RESUELTO` | Integrado en la consola del proyecto. |

---

## 3. Veredicto Arquitectonico Final

**Estado: `CLEARED` Sin Blockers Criticos No Resueltos.**

Tras sintetizar las senales de red y datos, y verificar su compatibilidad con la arquitectura acordada en Fase 2 (y revisada en los NFRs de `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements.md]]`):

> El sistema **PUEDE** construirse exitosamente bajo un stack **BaaS + Serverless** (Java Spring Boot + PostgreSQL). Las 3 senales detectadas (NS-01, DS-01, DS-02) son resueltas de manera nativa por el ecosistema elegido, evitando la configuracion manual de infraestructura tradicional.

**Componentes de Infraestructura que Fase 5 debe contemplar:**
- **PostgreSQL PostgreSQL** (BD relacional + RLS + GoTrue Auth)
- **PostgreSQL Realtime** (Suscripciones Websocket a la DB)
- **Cloudinary / S3** (Buckets de imagenes)
- **Spring Boot (Java) Vercel/Node** (Frontend React, Server Actions y Webhooks B2B)

---

## Implicacion de Fase

- El equipo de DevOps y Arquitectura de Fase 5 tiene la lista exacta de componentes de infraestructura que debe cotizar en AWS/GCP/Azure.
- El dictamen aprueba la construccion de un Monolito Modular cualquier migracion futura a Microservicios requerira justificacion cuantitativa de trafico.
- **Proceder a D13:** Estandares de Accesibilidad.


