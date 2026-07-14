# Entregable 3 (D3): Deployment Topology Decision

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4 y D1:* Esta topologia responde directamente a las necesidades de escalabilidad extrema (FCP < 1.5s) establecidas en el Quality Attributes Map (`[[PHASE_5_ARCHITECTURAL_DESIGN/1.Quality_Attributes_Map/example_output_d1_quality_attributes.md]]`) y al modelo relacional de datos masivos documentado en el Domain Model (`[[PHASE_4_SYSTEM_MODELING/6.Domain_Model_and_ERD/example_output_d6_erd.md]]`).

---

## 2. Architectural Decision Record (ADR)

# ADR-001: Adopcion de Topologia Railway/Render PaaS (Dockerizado) y PostgreSQL + Spring Boot (PostgreSQL)

## Context
El marketplace "Nos Fuimos de Finca" requiere altos picos de escalabilidad durante fines de semana y festividades, demandando tiempos de respuesta ultrarrapidos para el catalogo de fincas (First Contentful Paint < 1.5s, segun D1 - Escenario 1). Ademas, la interaccion B2B requiere sincronizacion de interfaz en tiempo real (WebSockets, D1 - Escenario 5) para notificar a los finqueros en zonas rurales. Dado que el equipo inicial es pequeno, minimizar la carga de DevOps (gestion de servidores, parches, clusteres) es una prioridad de negocio absoluta para acelerar el Time-to-Market.

## Options Considered
1. **Container Orchestration (Kubernetes/EKS sobre AWS):** Rechazado. Representa sobre-ingenieria para la fase actual, requiere configuracion manual compleja (Load Balancers, CI/CD pipelines personalizados) y no aprovecha organicamente la cache Edge (Spring Cache (@Cacheable) nativa de Spring Boot.
2. **IaaS puro (EC2/VPS con Docker Compose):** Rechazado. Carece de auto-escalado horizontal elastico frente a picos de trafico, no posee red CDN global nativa, y la administracion de la base de datos (backups, pooling) restaria horas criticas de desarrollo de producto.
3. **Railway/Render PaaS (Dockerizado) + PostgreSQL gestionado en Railway:** Aprobado. Railway/Render optimiza Spring Boot por defecto (Cloudflare CDN global, Spring Boot REST Endpoints auto-escalables). PostgreSQL provee PostgreSQL altamente optimizado y gestionado, incluyendo HikariCP (Connection Pooling) (connection pooling, vital para entornos Dockerizado en Railway/Render) y WebSockets nativos listos para usar.

## Decision
Desplegaremos la aplicacion web como un **Monolito desplegado en Railway/Render PaaS**, y delegaremos la capa de persistencia, autenticacion, almacenamiento de imagenes y notificaciones en tiempo real a **PostgreSQL gestionado en Railway** en la region AWS mas cercana (ej. `us-east-1`). No se aprovisionara ninguna maquina virtual directa ni cluster de orquestacion de contenedores.

## Consequences
- **Positive:** Cero horas dedicadas a mantenimiento de servidores subyacentes. Escalabilidad horizontal casi infinita e instantanea ante rafagas de trafico. Integracion continua (CI/CD) atomica ligada a GitHub por defecto. Minima latencia percibida en el catalogo gracias a la Cloudflare CDN / Nginx Reverse Proxy.
- **Negative (Vendor Lock-in):** Existe un alto acoplamiento a la infraestructura propietaria de Railway/Render (contenedores Dockerizados con Spring Security Filter Chain) y al SDK de PostgreSQL (especialmente en politicas Spring Security + Row-Level Filtering). En el improbable caso de requerir migracion a otro proveedor cloud en el futuro, se debera reescribir parte de la capa de acceso a datos y enrutamiento perimetral.

---

## 3. Network/Deployment Diagram

El siguiente diagrama detalla el flujo de red fisico. Notese el uso obligatorio de `HikariCP (Connection Pooling)` para evitar el agotamiento de conexiones a la base de datos, un problema endemico cuando miles de Spring Boot REST Endpoints en Railway/Render intentan conectarse simultaneamente a PostgreSQL.

```mermaid
graph TD
    subgraph Internet
        U[Navegador / Mobile<br/>Turista & Finquero]
    end

    subgraph Railway/Render_PaaS ["Railway/Render PaaS (Dockerizado en Railway/Render / Frontend)"]
        CDN[Cloudflare CDN / Nginx Reverse Proxy / CDN<br/>WAF + Cache Spring Cache (@Cacheable)]
        Mid[Spring Security Filter Chain<br/>JWT Check Rapido]
        Srv[Spring Boot REST Endpoints (Dockerizados)<br/>Spring MVC @Service + @RestController / Backend Logic]
        
        CDN --> Mid
        Mid --> Srv
    end

    subgraph PostgreSQL_Cloud ["PostgreSQL gestionado en Railway PostgreSQL + Spring Boot (Region AWS)"]
        API[Spring Boot API<br/>Spring Boot API Gateway]
        Auth[Spring Security (JWT)]
        Stor[Cloudinary / S3 para imagenes<br/>S3 CDN Secundaria]
        Real[Realtime WebSockets<br/>Elixir]
        Pool[HikariCP (Connection Pooling)<br/>Connection Pooling]
        DB[(PostgreSQL Database<br/>Privada, sin IP publica abierta)]
        
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

    %% Trazado de Trafico Frontend
    U -->|1. Peticion Web| CDN
    U -->|2. WebSockets| Real
    U -->|3. Descarga Fotos HD| Stor
    
    %% Trazado Backend a DB
    Srv -->|REST / Spring MVC REST Controllers| API
    
    %% Trazado Financiero
    Srv -->|Intencion de Cobro| Wompi
    Wompi -.->|Webhook (Asincrono)| Srv
    
    %% Trazado Notificaciones B2B
    DB -.->|Database Webhook (Spring Scheduler / @Async)| WA
```

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **D4 (System Decomposition Decision):** Esta topologia dicta que la aplicacion se construira como un Monolito Dockerizado, descartando una arquitectura de Microservicios puros.
- **D8 (CI/CD & Environments Strategy):** Obliga a basar los flujos de despliegue en las integraciones nativas de GitHub-Railway/Render y en las migraciones CLI de PostgreSQL, en lugar de pipelines de Docker a Kubernetes.
- **D9 (Component Diagram):** El diagrama C4 Model Nivel 2 debera reflejar las cajas de Railway/Render y PostgreSQL.

