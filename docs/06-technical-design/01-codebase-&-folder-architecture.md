# Deliverable 1 (D1): Codebase & Folder Architecture

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved

*Backlink a Fase 5:* Este entregable obedece a las resoluciones arquitectÃ³nicas tomadas en `[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md\|System Decomposition]]` (Modular Monolith) y `[[PHASE_5_ARCHITECTURAL_DESIGN/5.Architectural_Style_Selection/example_output_d5_architectural_style.md\|Architectural Style]]` (Estilo HÃ­brido).

---

## 2. Estructura Unificada del Repositorio (Monolito Modular)

Dado que la topologÃ­a elegida es Serverless en Vercel, **Frontend y Backend comparten exactamente la misma base de cÃ³digo** utilizando el framework Next.js. El patrÃ³n aplicado es *Feature-Sliced Design* a nivel raÃ­z (`src/modules`), permitiendo que el Frontend (`src/app`) consuma lÃ³gicas encapsuladas por Bounded Contexts.

Se observa el cumplimiento estricto del Modelo HÃ­brido: los dominios crÃ­ticos (`booking`, `billing`) estÃ¡n protegidos con *Clean Architecture*, mientras los de lectura (`catalog`) utilizan un patrÃ³n mÃ¡s sencillo (*Layered MVC*).

```text
nos-fuimos-de-finca/
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ app/                         # Frontend: Next.js App Router (Rutas Web y API Routes)
â”‚   â”‚   â”œâ”€â”€ (public)/                # Grupo de rutas: Landing, CatÃ¡logo
â”‚   â”‚   â”œâ”€â”€ (host)/                  # Grupo de rutas: Dashboard de Finquero
â”‚   â”‚   â””â”€â”€ api/                     # Endpoints REST expuestos explÃ­citamente (Webhooks)
â”‚   â”‚
â”‚   â”œâ”€â”€ components/                  # Frontend: React Components
â”‚   â”‚   â”œâ”€â”€ ui/                      # Sistema de diseÃ±o genÃ©rico (Botones, Inputs)
â”‚   â”‚   â””â”€â”€ shared/                  # Componentes reutilizables entre mÃ³dulos
â”‚   â”‚
â”‚   â”œâ”€â”€ modules/                     # Backend: Core del Monolito Modular
â”‚   â”‚   â”œâ”€â”€ booking/                 # [Clean Architecture] Core Transaccional
â”‚   â”‚   â”‚   â”œâ”€â”€ domain/              # Entidades (Booking, BookingStatus) y Reglas Puras
â”‚   â”‚   â”‚   â”œâ”€â”€ application/         # Casos de uso (CreateBookingUseCase)
â”‚   â”‚   â”‚   â””â”€â”€ infrastructure/      # Server Actions, Repositorios Supabase
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ billing/                 # [Clean Architecture] Core Financiero
â”‚   â”‚   â”‚   â”œâ”€â”€ domain/              # Entidades (Payment, Invoice)
â”‚   â”‚   â”‚   â”œâ”€â”€ application/         # Casos de uso (ProcessPaymentWebhook)
â”‚   â”‚   â”‚   â””â”€â”€ infrastructure/      # Wompi Adapter, Supabase Repositories
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ catalog/                 # [Layered MVC] Lectura de Fincas
â”‚   â”‚   â”‚   â”œâ”€â”€ controllers/         # Server Actions para UI
â”‚   â”‚   â”‚   â”œâ”€â”€ services/            # Fetching de Supabase (ISR/Caching)
â”‚   â”‚   â”‚   â””â”€â”€ models/              # Interfaces TS
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ iam/                     # [Layered MVC] Identidad y Acceso
â”‚   â”‚   â”‚   â””â”€â”€ services/            # Supabase Auth wrappers
â”‚   â”‚   â”‚
â”‚   â”‚   â””â”€â”€ notifications/           # [Layered MVC] MensajerÃ­a
â”‚   â”‚       â””â”€â”€ services/            # WhatsApp API, Push Realtime
â”‚   â”‚
â”‚   â”œâ”€â”€ shared/                      # CÃ³digo comÃºn tÃ©cnico (no ligado a un mÃ³dulo)
â”‚   â”‚   â”œâ”€â”€ types/                   # Tipos globales de TypeScript
â”‚   â”‚   â”œâ”€â”€ utils/                   # Helpers generales
â”‚   â”‚   â””â”€â”€ config/                  # InicializaciÃ³n de Supabase client, env vars
â”‚   â”‚
â”‚   â””â”€â”€ middleware.ts                # Next.js Middleware (Auth Edge guards, Rate Limiting)
â”‚
â”œâ”€â”€ public/                          # Assets estÃ¡ticos
â”œâ”€â”€ vercel.json                      # ConfiguraciÃ³n de IaC Serverless
â”œâ”€â”€ .env.local                       # Secrets (No versionado)
â””â”€â”€ package.json                     # Dependencias
```

---

## 3. Downstream Consumers
Este entregable es la hoja de ruta fÃ­sica para los desarrolladores y es input obligatorio para:
- **Phase 7 â€” D2 (Project Scaffolding & Setup):** Los desarrolladores tomarÃ¡n este Ã¡rbol de carpetas exacto para crear los directorios con `mkdir` e inicializar el repositorio GitHub.
- **Phase 6 â€” D3 (Configuration & Environment Secrets):** MapearÃ¡ las claves secretas necesarias que deben residir en el `.env.local` raÃ­z de este proyecto unificado.
- **Phase 6 â€” D9 (Frontend Component & State Architecture):** ProfundizarÃ¡ en la gestiÃ³n del estado global que habitarÃ¡ en el directorio `src/app/` y `src/components/`.

