# Deliverable 1 (D1): Codebase & Folder Architecture

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved

*Backlink a Fase 5:* Este entregable obedece a las resoluciones arquitectonicas tomadas en `[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md\|System Decomposition]]` (Modular Monolith) y `[[PHASE_5_ARCHITECTURAL_DESIGN/5.Architectural_Style_Selection/example_output_d5_architectural_style.md\|Architectural Style]]` (Estilo Hibrido).

---

## 2. Estructura Unificada del Repositorio (Monolito Modular)

Dado que la topologia elegida es Dockerizado en Railway/Render, **Frontend y Backend comparten exactamente la misma base de codigo** utilizando el framework Spring Boot. El patron aplicado es *Feature-Sliced Design* a nivel raiz (`src/modules`), permitiendo que el Frontend (`src/app`) consuma logicas encapsuladas por Bounded Contexts.

Se observa el cumplimiento estricto del Modelo Hibrido: los dominios criticos (`booking`, `billing`) estan protegidos con *Clean Architecture*, mientras los de lectura (`catalog`) utilizan un patron mas sencillo (*Layered MVC*).

```text
nos-fuimos-de-finca/
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ app/                         # Frontend: Vite + JavaScript (SPA)
â”‚   â”‚   â”œâ”€â”€ (public)/                # Paginas publicas: Landing, Catalogo
â”‚   â”‚   â”œâ”€â”€ (host)/                  # Paginas privadas: Dashboard del Finquero
â”‚   â”‚   â””â”€â”€ api/                     # Endpoints REST expuestos explicitamente (Webhooks)
â”‚   â”‚
â”‚   â”œâ”€â”€ components/                  # Frontend: Componentes reutilizables Vite + JavaScript
â”‚   â”‚   â”œâ”€â”€ ui/                      # Sistema de diseno generico (Botones, Inputs)
â”‚   â”‚   â””â”€â”€ shared/                  # Componentes reutilizables entre modulos
â”‚   â”‚
â”‚   â”œâ”€â”€ modules/                     # Backend: Core del Monolito Modular
â”‚   â”‚   â”œâ”€â”€ booking/                 # [Clean Architecture] Core Transaccional
â”‚   â”‚   â”‚   â”œâ”€â”€ domain/              # Entidades (Booking, BookingStatus) y Reglas Puras
â”‚   â”‚   â”‚   â”œâ”€â”€ application/         # Casos de uso (CreateBookingUseCase)
â”‚   â”‚   â”‚   â””â”€â”€ infrastructure/      # Spring @Service + JPA Repositories (PostgreSQL)
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ billing/                 # [Clean Architecture] Core Financiero
â”‚   â”‚   â”‚   â”œâ”€â”€ domain/              # Entidades (Payment, Invoice)
â”‚   â”‚   â”‚   â”œâ”€â”€ application/         # Casos de uso (ProcessPaymentWebhook)
â”‚   â”‚   â”‚   â””â”€â”€ infrastructure/      # Wompi Adapter, PostgreSQL Repositories
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ catalog/                 # [Layered MVC] Lectura de Fincas
â”‚   â”‚   â”‚   â”œâ”€â”€ controllers/         # Spring @RestController para UI
â”‚   â”‚   â”‚   â”œâ”€â”€ services/            # Queries a PostgreSQL con Spring Cache (@Cacheable)
â”‚   â”‚   â”‚   â””â”€â”€ models/              # Interfaces Java (DTOs)
â”‚   â”‚   â”‚
â”‚   â”‚   â”œâ”€â”€ iam/                     # [Layered MVC] Identidad y Acceso
â”‚   â”‚   â”‚   â””â”€â”€ services/            # Spring Security + JWT wrappers
â”‚   â”‚   â”‚
â”‚   â”‚   â””â”€â”€ notifications/           # [Layered MVC] Mensajeria
â”‚   â”‚       â””â”€â”€ services/            # WhatsApp API, Push Realtime
â”‚   â”‚
â”‚   â”œâ”€â”€ shared/                      # Codigo comun tecnico (no ligado a un modulo)
â”‚   â”‚   â”œâ”€â”€ types/                   # Clases de utilidad y tipos globales (Java POJOs)
â”‚   â”‚   â”œâ”€â”€ utils/                   # Helpers generales
â”‚   â”‚   â””â”€â”€ config/                  # Inicializacion de DataSource (JDBC/JPA), env vars
â”‚   â”‚
â”‚   â””â”€â”€ SecurityConfig.java                # Spring Security Filter (JWT Validation, Rate Limiting)
â”‚
â”œâ”€â”€ public/                          # Assets estaticos
â”œâ”€â”€ Dockerfile + railway.toml  # Imagen Docker y configuracion Railway/Render
â”œâ”€â”€ application.yml                       # Secrets (No versionado)
â””â”€â”€ pom.xml                     # Dependencias
```

---

## 3. Downstream Consumers
Este entregable es la hoja de ruta fisica para los desarrolladores y es input obligatorio para:
- **Phase 7 â€” D2 (Project Scaffolding & Setup):** Los desarrolladores tomaran este arbol de carpetas exacto para crear los directorios con `mkdir` e inicializar el repositorio GitHub.
- **Phase 6 â€” D3 (Configuration & Environment Secrets):** Mapeara las claves secretas necesarias que deben residir en el `application.yml` raiz de este proyecto unificado.
- **Phase 6 â€” D9 (Frontend Component & State Architecture):** Profundizara en la gestion del estado global que habitara en el directorio `src/main/java/com/nosfuimosdefinica/` y `src/components/`.

