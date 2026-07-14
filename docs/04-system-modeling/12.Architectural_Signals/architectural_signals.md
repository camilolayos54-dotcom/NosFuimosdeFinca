# Entregable 12 (D12): SÃ­ntesis de SeÃ±ales ArquitectÃ³nicas

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**Estado:** Aprobado

---

## 1. SeÃ±ales ExtraÃ­das (Red y Datos)

### 1.1 SeÃ±ales de Capa de Red

| Signal ID | DescripciÃ³n | MÃ³dulo Origen | ImplicaciÃ³n para Fase 5 |
|---|---|---|---|
| **NS-01** | Real-Time Push: el Dashboard del Finquero debe recibir alertas de nueva reserva en tiempo real sin refrescar la pÃ¡gina. | `MOD-NOT` (D10) | Implementar **Supabase Realtime (PostgreSQL LISTEN/NOTIFY)** sobre la tabla `bookings`. Elimina la necesidad de un servidor WebSocket/Redis PubSub custom. |

### 1.2 SeÃ±ales de Capa de Datos

| Signal ID | DescripciÃ³n | Entidad Origen (D6) | ImplicaciÃ³n para Fase 5 |
|---|---|---|---|
| **DS-01** | ProporciÃ³n R/W de ~100:1 en el catÃ¡logo de fincas (`properties`). Todo Turista ejecuta `GET /api/v1/properties`. | `properties` + `GET /api/v1/properties` | Aprovechar cachÃ© de CDN estÃ¡tica para SSG/ISR (Next.js App Router) para el listado pÃºblico. |
| **DS-02** | Archivos binarios HD (hasta 10MB/foto, 5-20 fotos por finca). No pueden almacenarse en el disco local del servidor. | `property_images.url_hd` | Implementar **Supabase Storage**. El servidor Next.js sube el archivo al bucket y guarda la URL pÃºblica en BD. |

---

## 2. Estado de Pre-Architecture Blockers

| Signal | Estado | ResoluciÃ³n |
|---|---|---|
| **NS-01** (Supabase Realtime) | âœ… `RESUELTO` | Incluido en el stack de Supabase (SaaS). Evita montar websockets manuales. |
| **DS-01** (Next.js Cache) | âœ… `RESUELTO` | Nativo en Next.js (App Router ISR). |
| **DS-02** (Supabase Storage) | âœ… `RESUELTO` | Integrado en la consola del proyecto. |

---

## 3. Veredicto ArquitectÃ³nico Final

**Estado: `CLEARED` â€” Sin Blockers CrÃ­ticos No Resueltos.**

Tras sintetizar las seÃ±ales de red y datos, y verificar su compatibilidad con la arquitectura acordada en Fase 2 (y revisada en los NFRs de `[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements.md]]`):

> El sistema **PUEDE** construirse exitosamente bajo un stack **BaaS + Serverless** (Next.js + Supabase). Las 3 seÃ±ales detectadas (NS-01, DS-01, DS-02) son resueltas de manera nativa por el ecosistema elegido, evitando la configuraciÃ³n manual de infraestructura tradicional.

**Componentes de Infraestructura que Fase 5 debe contemplar:**
- **Supabase PostgreSQL** (BD relacional + RLS + GoTrue Auth)
- **Supabase Realtime** (Suscripciones Websocket a la DB)
- **Supabase Storage** (Buckets de imÃ¡genes)
- **Next.js Vercel/Node** (Frontend React, Server Actions y Webhooks B2B)

---

## ImplicaciÃ³n de Fase

- El equipo de DevOps y Arquitectura de Fase 5 tiene la lista exacta de componentes de infraestructura que debe cotizar en AWS/GCP/Azure.
- El dictamen aprueba la construcciÃ³n de un Monolito Modular â€” cualquier migraciÃ³n futura a Microservicios requerirÃ¡ justificaciÃ³n cuantitativa de trÃ¡fico.
- **Proceder a D13:** EstÃ¡ndares de Accesibilidad.

