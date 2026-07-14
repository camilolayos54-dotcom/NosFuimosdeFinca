 # Deliverable 3 (D3): Configuration & Environment Secrets

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Estado:** Approved

*Backlink a Fase 2/5:* Este entregable deriva directamente del `[[PHASE_2_PROJECT_KICKOFF/3.Stack_Decision/example_output_d3_stack.md\|Stack Tecnico]]`. Debido al patron *Modular Monolith* en Spring Boot, en la practica el proyecto tendra un unico archivo `application.yml` o gestor de secretos en Railway/Render, pero lo hemos dividido logicamente para identificar el riesgo (Server = Privado vs Client = Publico).

---

## 2. Variables de Entorno Backend (Server-side Only)

> [!WARNING]
> Las variables documentadas a continuacion **nunca** deben incluirse en un commit, y **no** llevan el prefijo `NEXT_PUBLIC_`. El equipo DevOps debe provisionarlas directamente en el entorno de despliegue de Railway/Render.

```bash
# ==========================================
# BACKEND SECRETS (Logica y Orquestacion)
# ==========================================

# 1. SUPABASE (PostgreSQL + Spring Boot Database & Auth)
# ------------------------------------------
# URL del proyecto
SUPABASE_URL=https://[PROJECT_ID].postgresql.co
# SENSIBLE Llave de acceso total, salta politicas Spring Security + Row-Level Filtering (Row Level Security).
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR...

# 2. VERCEL (PaaS Hosting)
# ------------------------------------------
# Railway/Render inyecta esto automaticamente; usar en local para mocks de Webhooks.
VERCEL_URL=localhost:3000

# 3. WOMPI (Pagos) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# SENSIBLE Clave privada para crear transacciones o reembolsos.
WOMPI_PRIVATE_KEY=prv_test_...
# SENSIBLE Secreto criptografico para validar el Hash de los Webhooks (Previene inyeccion de pagos falsos).
WOMPI_WEBHOOK_SECRET=events_test_...

# 4. WHATSAPP API (Meta) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# SENSIBLE Token Bearer permanente de Meta for Developers.
WHATSAPP_ACCESS_TOKEN=EAAQ...
# Identificador oficial del numero de telefono desde donde se envia.
WHATSAPP_PHONE_NUMBER_ID=123456789
```

---

## 3. Variables de Entorno Frontend (Client-side)

> [!TIP]
> Las siguientes variables llevan el prefijo `NEXT_PUBLIC_`, lo que le indica a Spring Boot (Java) que debe empaquetarlas y enviarlas al navegador del Turista/Finquero. **Cualquier clave aqui es publica y puede ser leida inspeccionando la pagina web.**

```bash
# ==========================================
# FRONTEND PUBLIC VARIABLES (HTML/JS (MPA) & UX)
# ==========================================

# 1. SUPABASE (PostgreSQL + Spring Boot Client)
# ------------------------------------------
# URL publica de la API de PostgreSQL.
NEXT_PUBLIC_SUPABASE_URL=https://[PROJECT_ID].postgresql.co
# Llave Anonima (Publica). Completamente segura de exponer. 
# La seguridad real para evitar lecturas no autorizadas recae en el Spring Security + Row-Level Filtering de PostgreSQL (Phase 6, D2).
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR...

# 2. WOMPI (Widget de Pagos) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# Llave Publica. Solo se usa para inicializar la tarjeta de credito del lado del cliente de forma segura.
NEXT_PUBLIC_WOMPI_PUBLISHABLE_KEY=pub_test_...

# 3. CORE ROUTING
# ------------------------------------------
# URL Base de la aplicacion (Ej. para armar redirecciones hacia pasarelas de pago externas)
NEXT_PUBLIC_BASE_URL=http://localhost:3000
```

---

## 4. Downstream Consumers
Este entregable es vital para los flujos operativos y de seguridad:
- **Phase 7 - D2 (Project Scaffolding):** El desarrollador tomara el contenido de estos dos bloques, quitara los comentarios `[PROJECT_ID]` / `eyJhb...` y creara un archivo `.env.example` literal en el repositorio de codigo, exigiendo a todos llenar sus valores locales.
- **Phase 9 D3 (Infrastructure as Code / SecOps):** Operaciones utilizara la lista del apartado 2 (Backend) para crear los Secretos cifrados en el entorno Cloud de produccion antes del lanzamiento (Go-Live).

