 # Deliverable 1 (D1): Codebase & Folder Architecture

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Estado:** Approved

*Backlink a Fase 5:* Este entregable obedece a las resoluciones arquitectonicas tomadas en `[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md\|System Decomposition]]` (Modular Monolith) y `[[PHASE_5_ARCHITECTURAL_DESIGN/5.Architectural_Style_Selection/example_output_d5_architectural_style.md\|Architectural Style]]` (Estilo Hibrido).

---

## 2. Estructura Unificada del Repositorio (Monolito Modular)

Dado que la topologia elegida es Dockerizado en Railway/Render, **Frontend y Backend comparten exactamente la misma base de codigo** utilizando el framework Spring Boot. El patron aplicado es *Feature-Sliced Design* a nivel raiz (`src/modules`), permitiendo que el Frontend (`src/app`) consuma logicas encapsuladas por Bounded Contexts.

Se observa el cumplimiento estricto del Modelo Hibrido: los dominios criticos (`booking`, `billing`) estan protegidos con *Clean Architecture*, mientras los de lectura (`catalog`) utilizan un patron mas sencillo (*Layered MVC*).

```text
nos-fuimos-de-finca/
          src/
                app/ # Frontend: HTML Multi-Page Application (MPA)
                      (public)/ # Paginas publicas: Landing, Catalogo
                      (host)/ # Paginas privadas: Dashboard del Finquero
                      api/ # Endpoints REST expuestos explicitamente (Webhooks)
         
                components/ # Frontend: Componentes reutilizables HTML/JS (MPA)
                      ui/ # Sistema de diseno generico (Botones, Inputs)
                      shared/ # Componentes reutilizables entre modulos
         
                modules/ # Backend: Core del Monolito Modular
                      booking/ # [Clean Architecture] Core Transaccional
                            domain/ # Entidades (Booking, BookingStatus) y Reglas Puras
                            application/ # Casos de uso (CreateBookingUseCase)
                            infrastructure/ # Spring @Service + JPA Repositories (PostgreSQL)
               
                      billing/ # [Clean Architecture] Core Financiero
                            domain/ # Entidades (Payment, Invoice)
                            application/ # Casos de uso (ProcessPaymentWebhook)
                            infrastructure/ # Wompi Adapter, PostgreSQL Repositories
               
                      catalog/ # [Layered MVC] Lectura de Fincas
                            controllers/ # Spring @RestController para UI
                            services/ # Queries a PostgreSQL con Spring Cache (@Cacheable)
                            models/ # Interfaces Java (DTOs)
               
                      iam/ # [Layered MVC] Identidad y Acceso
                            services/ # Spring Security + JWT wrappers
               
                      notifications/ # [Layered MVC] Mensajeria
                          services/ # WhatsApp API, Push Realtime
         
                shared/ # Codigo comun tecnico (no ligado a un modulo)
                      types/ # Clases de utilidad y tipos globales (Java POJOs)
                      utils/ # Helpers generales
                      config/ # Inicializacion de DataSource (JDBC/JPA), env vars
         
                SecurityConfig.java # Spring Security Filter (JWT Validation, Rate Limiting)
   
          public/ # Assets estaticos
          Dockerfile + railway.toml # Imagen Docker y configuracion Railway/Render
          application.yml # Secrets (No versionado)
          pom.xml # Dependencias
```

---

## 3. Downstream Consumers
Este entregable es la hoja de ruta fisica para los desarrolladores y es input obligatorio para:
- **Phase 7 - D2 (Project Scaffolding & Setup):** Los desarrolladores tomaran este arbol de carpetas exacto para crear los directorios con `mkdir` e inicializar el repositorio GitHub.
- **Phase 6 - D3 (Configuration & Environment Secrets):** Mapeara las claves secretas necesarias que deben residir en el `application.yml` raiz de este proyecto unificado.
- **Phase 6 - D9 (Frontend Component & State Architecture):** Profundizara en la gestion del estado global que habitara en el directorio `src/main/java/com/nosfuimosdefinica/` y `src/components/`.

