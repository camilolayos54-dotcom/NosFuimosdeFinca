# Entregable 3 (D3): Deployment Topology Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4 y D1:* Esta topologÃ­a responde directamente a las necesidades de escalabilidad extrema (FCP < 1.5s) establecidas en el Quality Attributes Map (`[[PHASE_5_ARCHITECTURAL_DESIGN/1.Quality_Attributes_Map/example_output_d1_quality_attributes.md]]`) y al modelo relacional de datos masivos documentado en el Domain Model (`[[PHASE_4_SYSTEM_MODELING/6.Domain_Model_and_ERD/example_output_d6_erd.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-001: AdopciÃ³n de TopologÃ­a Serverless PaaS (Vercel) y BaaS (Supabase)

## Context
El marketplace "Nos Fuimos de Finca" requiere altos picos de escalabilidad durante fines de semana y festividades, demandando tiempos de respuesta ultrarrÃ¡pidos para el catÃ¡logo de fincas (First Contentful Paint < 1.5s, segÃºn D1 - Escenario 1). AdemÃ¡s, la interacciÃ³n B2B requiere sincronizaciÃ³n de interfaz en tiempo real (WebSockets, D1 - Escenario 5) para notificar a los finqueros en zonas rurales. Dado que el equipo inicial es pequeÃ±o, minimizar la carga de DevOps (gestiÃ³n de servidores, parches, clÃºsteres) es una prioridad de negocio absoluta para acelerar el Time-to-Market.

## Options Considered
1. **Container Orchestration (Kubernetes/EKS sobre AWS):** Rechazado. Representa sobre-ingenierÃ­a para la fase actual, requiere configuraciÃ³n manual compleja (Load Balancers, CI/CD pipelines personalizados) y no aprovecha orgÃ¡nicamente la cachÃ© Edge (ISR) nativa de Next.js.
2. **IaaS puro (EC2/VPS con Docker Compose):** Rechazado. Carece de auto-escalado horizontal elÃ¡stico frente a picos de trÃ¡fico, no posee red CDN global nativa, y la administraciÃ³n de la base de datos (backups, pooling) restarÃ­a horas crÃ­ticas de desarrollo de producto.
3. **Serverless PaaS (Vercel) + BaaS (Supabase Cloud):** Aprobado. Vercel optimiza Next.js por defecto (CDN Edge global, Serverless Functions auto-escalables). Supabase provee PostgreSQL altamente optimizado y gestionado, incluyendo pgBouncer (connection pooling, vital para entornos Serverless) y WebSockets nativos listos para usar.

## Decision
Desplegaremos la aplicaciÃ³n web como un **Monolito Serverless en la plataforma PaaS de Vercel**, y delegaremos la capa de persistencia, autenticaciÃ³n, almacenamiento de imÃ¡genes y notificaciones en tiempo real a **Supabase Cloud (BaaS)** en la regiÃ³n AWS mÃ¡s cercana (ej. `us-east-1`). No se aprovisionarÃ¡ ninguna mÃ¡quina virtual directa ni clÃºster de orquestaciÃ³n de contenedores.

## Consequences
- **Positive:** Cero horas dedicadas a mantenimiento de servidores subyacentes. Escalabilidad horizontal casi infinita e instantÃ¡nea ante rÃ¡fagas de trÃ¡fico. IntegraciÃ³n continua (CI/CD) atÃ³mica ligada a GitHub por defecto. MÃ­nima latencia percibida en el catÃ¡logo gracias a la Vercel Edge Network.
- **Negative (Vendor Lock-in):** Existe un alto acoplamiento a la infraestructura propietaria de Vercel (funciones serverless y Edge Middleware) y al SDK de Supabase (especialmente en polÃ­ticas RLS). En el improbable caso de requerir migraciÃ³n a otro proveedor cloud en el futuro, se deberÃ¡ reescribir parte de la capa de acceso a datos y enrutamiento perimetral.

---

## 3. Network/Deployment Diagram

El siguiente diagrama detalla el flujo de red fÃ­sico. NÃ³tese el uso obligatorio de `PgBouncer` para evitar el agotamiento de conexiones a la base de datos, un problema endÃ©mico cuando miles de Serverless Functions (Vercel) intentan conectarse simultÃ¡neamente a PostgreSQL.

```mermaid
graph TD
    subgraph Internet
        U[Navegador / Mobile<br/>Turista & Finquero]
    end

    subgraph Vercel_PaaS ["Vercel PaaS (Serverless / Frontend)"]
        CDN[Vercel Edge Network / CDN<br/>WAF + Cache ISR]
        Mid[Edge Middleware<br/>JWT Check RÃ¡pido]
        Srv[Next.js Serverless Functions<br/>Server Actions / Backend Logic]
        
        CDN --> Mid
        Mid --> Srv
    end

    subgraph Supabase_Cloud ["Supabase Cloud BaaS (RegiÃ³n AWS)"]
        API[Supabase API Gateway<br/>Kong]
        Auth[GoTrue Auth]
        Stor[Supabase Storage<br/>S3 CDN Secundaria]
        Real[Realtime WebSockets<br/>Elixir]
        Pool[PgBouncer<br/>Connection Pooling]
        DB[(PostgreSQL Database<br/>Privada, sin IP pÃºblica abierta)]
        
        API --> Auth
        API --> Stor
        API --> Real
        API --> Pool
        Pool --> DB
    end
    
    subgraph External_APIs ["Terceros (APIs)"]
        Wompi[Wompi Pasarela de Pagos]
        WA[WhatsApp Business API]
    end

    %% Trazado de TrÃ¡fico Frontend
    U -->|1. PeticiÃ³n Web| CDN
    U -->|2. WebSockets| Real
    U -->|3. Descarga Fotos HD| Stor
    
    %% Trazado Backend a DB
    Srv -->|REST / PostgREST| API
    
    %% Trazado Financiero
    Srv -->|IntenciÃ³n de Cobro| Wompi
    Wompi -.->|Webhook (AsÃ­ncrono)| Srv
    
    %% Trazado Notificaciones B2B
    DB -.->|Database Webhook (pg_net)| WA
```

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D4 (System Decomposition Decision):** Esta topologÃ­a dicta que la aplicaciÃ³n se construirÃ¡ como un Monolito Serverless, descartando una arquitectura de Microservicios puros.
- **D8 (CI/CD & Environments Strategy):** Obliga a basar los flujos de despliegue en las integraciones nativas de GitHub-Vercel y en las migraciones CLI de Supabase, en lugar de pipelines de Docker a Kubernetes.
- **D9 (Component Diagram):** El diagrama C4 Model Nivel 2 deberÃ¡ reflejar las cajas de Vercel y Supabase.

