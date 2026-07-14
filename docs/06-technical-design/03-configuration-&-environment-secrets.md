# Deliverable 3 (D3): Configuration & Environment Secrets

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved

*Backlink a Fase 2/5:* Este entregable deriva directamente del `[[PHASE_2_PROJECT_KICKOFF/3.Stack_Decision/example_output_d3_stack.md\|Stack TÃ©cnico]]`. Debido al patrÃ³n *Modular Monolith* en Next.js, en la prÃ¡ctica el proyecto tendrÃ¡ un Ãºnico archivo `.env.local` o gestor de secretos en Vercel, pero lo hemos dividido lÃ³gicamente para identificar el riesgo (Server = Privado vs Client = PÃºblico).

---

## 2. Variables de Entorno â€” Backend (Server-side Only)

> [!WARNING]
> Las variables documentadas a continuaciÃ³n **nunca** deben incluirse en un commit, y **no** llevan el prefijo `NEXT_PUBLIC_`. El equipo DevOps debe provisionarlas directamente en el entorno de despliegue de Vercel.

```bash
# ==========================================
# BACKEND SECRETS (LÃ³gica y OrquestaciÃ³n)
# ==========================================

# 1. SUPABASE (BaaS Database & Auth)
# ------------------------------------------
# URL del proyecto
SUPABASE_URL=https://[PROJECT_ID].supabase.co
# SENSIBLE â€” Llave de acceso total, salta polÃ­ticas RLS (Row Level Security).
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR...

# 2. VERCEL (PaaS Hosting)
# ------------------------------------------
# Vercel inyecta esto automÃ¡ticamente; usar en local para mocks de Webhooks.
VERCEL_URL=localhost:3000

# 3. WOMPI (Pagos) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# SENSIBLE â€” Clave privada para crear transacciones o reembolsos.
WOMPI_PRIVATE_KEY=prv_test_...
# SENSIBLE â€” Secreto criptogrÃ¡fico para validar el Hash de los Webhooks (Previene inyecciÃ³n de pagos falsos).
WOMPI_WEBHOOK_SECRET=events_test_...

# 4. WHATSAPP API (Meta) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# SENSIBLE â€” Token Bearer permanente de Meta for Developers.
WHATSAPP_ACCESS_TOKEN=EAAQ...
# Identificador oficial del nÃºmero de telÃ©fono desde donde se envÃ­a.
WHATSAPP_PHONE_NUMBER_ID=123456789
```

---

## 3. Variables de Entorno â€” Frontend (Client-side)

> [!TIP]
> Las siguientes variables llevan el prefijo `NEXT_PUBLIC_`, lo que le indica a Next.js que debe empaquetarlas y enviarlas al navegador del Turista/Finquero. **Cualquier clave aquÃ­ es pÃºblica y puede ser leÃ­da inspeccionando la pÃ¡gina web.**

```bash
# ==========================================
# FRONTEND PUBLIC VARIABLES (React & UX)
# ==========================================

# 1. SUPABASE (BaaS Client)
# ------------------------------------------
# URL pÃºblica de la API de Supabase.
NEXT_PUBLIC_SUPABASE_URL=https://[PROJECT_ID].supabase.co
# Llave AnÃ³nima (PÃºblica). Completamente segura de exponer. 
# La seguridad real para evitar lecturas no autorizadas recae en el RLS de PostgreSQL (Phase 6, D2).
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR...

# 2. WOMPI (Widget de Pagos) - #PENDIENTE-VALIDAR-CONTRA-D8
# ------------------------------------------
# Llave PÃºblica. Solo se usa para inicializar la tarjeta de crÃ©dito del lado del cliente de forma segura.
NEXT_PUBLIC_WOMPI_PUBLISHABLE_KEY=pub_test_...

# 3. CORE ROUTING
# ------------------------------------------
# URL Base de la aplicaciÃ³n (Ej. para armar redirecciones hacia pasarelas de pago externas)
NEXT_PUBLIC_BASE_URL=http://localhost:3000
```

---

## 4. Downstream Consumers
Este entregable es vital para los flujos operativos y de seguridad:
- **Phase 7 â€” D2 (Project Scaffolding):** El desarrollador tomarÃ¡ el contenido de estos dos bloques, quitarÃ¡ los comentarios `[PROJECT_ID]` / `eyJhb...` y crearÃ¡ un archivo `.env.example` literal en el repositorio de cÃ³digo, exigiendo a todos llenar sus valores locales.
- **Phase 9 â€” D3 (Infrastructure as Code / SecOps):** Operaciones utilizarÃ¡ la lista del apartado 2 (Backend) para crear los Secretos cifrados en el entorno Cloud de producciÃ³n antes del lanzamiento (Go-Live).

