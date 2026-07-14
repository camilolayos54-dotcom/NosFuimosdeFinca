# Entregable 8 (D8): CI/CD & Environments Strategy

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5:* Este entregable materializa el ciclo de vida del cÃ³digo para la infraestructura Serverless elegida en el Deployment Topology (`[[PHASE_5_ARCHITECTURAL_DESIGN/3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md]]`) y la base de cÃ³digo Ãºnica definida en el System Decomposition (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. DevOps & Delivery Pipeline

### Estrategia de Branching
Dada la agilidad requerida para un producto B2B/B2C en etapa temprana y el tamaÃ±o reducido del equipo inicial, implementaremos **Trunk-Based Development** (descartando GitFlow).
- Existe una Ãºnica rama perpetua de la verdad: `main`.
- Los desarrolladores crean ramas efÃ­meras (`feature/nombre-corto`) que deben vivir un mÃ¡ximo de 48 horas antes de someterse a revisiÃ³n (Pull Request) e integrarse de vuelta a `main`.

### Ambientes (Environments)
1. **Local:** MÃ¡quina del desarrollador. Utiliza Next.js Development Server (`npm run dev`) y un contenedor Docker instanciado vÃ­a `Supabase CLI` para emular la base de datos sin afectar datos reales.
2. **Staging (Preview):** Entornos efÃ­meros y automÃ¡ticos por cada rama/PR abierto. Apuntan a un proyecto de base de datos de "Staging" aislado en Supabase Cloud.
3. **Production:** El ambiente pÃºblico frente a clientes. Vercel Production + Supabase Production (AWS Region).

### Reglas de PromociÃ³n
- **PromociÃ³n a Staging:** AutomÃ¡tica. Abrir un Pull Request contra `main` desencadena la creaciÃ³n de un URL Ãºnico en Vercel.
- **PromociÃ³n a Production:** SemiautomÃ¡tica. Una vez aprobado y *mergeado* el cÃ³digo a `main`, el despliegue hacia el dominio de producciÃ³n ocurre de forma automÃ¡tica y atÃ³mica.

### IntegraciÃ³n Continua (CI)
Todo cambio propuesto hacia `main` debe pasar este muro de protecciÃ³n (Pipeline de CI):
1. **Type Check:** `tsc --noEmit` (Vital en un Monolito Modular para no romper contratos entre dominios).
2. **Linting & Formatting:** `next lint` & Prettier.
3. **Unit Tests:** EjecuciÃ³n de suites (Jest/Vitest) centradas exclusivamente en los dominios de alta criticidad: *Booking Engine* y *Billing & Payouts*.
4. **Build Check:** EjecuciÃ³n de `next build` para simular la generaciÃ³n de rutas estÃ¡ticas (ISR) e interceptar errores de pre-renderizado.

### Despliegue Continuo (CD)
Dado que la topologÃ­a es Serverless (D3), descartamos la orquestaciÃ³n de contenedores (Kubernetes/Docker). El CD consta de:
1. **Database Migrations:** AplicaciÃ³n de cambios SQL mediante `supabase db push` contra la base de datos destino.
2. **Edge Deployment:** Vercel asume la responsabilidad del empaquetado del cÃ³digo (Monolito) y su distribuciÃ³n global a la Vercel Edge Network. No hay servidores web que reiniciar manualmente.

### Automation & Tooling
- **Plataforma CI/CD:** **GitHub Actions** para orquestar la fase de CI y las migraciones. La fase de CD pura se delega a la integraciÃ³n nativa de **Vercel for GitHub**.
- **IaC (Infrastructure as Code):** **No aplica** el uso de herramientas pesadas como Terraform o Pulumi. La infraestructura se gobierna mediante la configuraciÃ³n declarativa nativa (`vercel.json`) y el sistema de migraciones controladas por cÃ³digo de `Supabase CLI`.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 â€” D3 (Configuration & Environment Secrets):** Los 3 ambientes definidos aquÃ­ obligan a crear 3 sets de variables de entorno distintas (`.env.local`, `.env.preview`, `.env.production`).
- **Phase 7 â€” D2 (Project Scaffolding & Setup):** Inicializa el repositorio GitHub con los workflows `.github/workflows/ci.yml` basÃ¡ndose exactamente en los pasos definidos aquÃ­.
- **D10 (ADR Consolidation):** Las elecciones de herramientas (Trunk-Based, GitHub Actions) quedarÃ¡n indexadas en el resumen final.

