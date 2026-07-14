 # Entregable 8 (D8): CI/CD & Environments Strategy

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 Architectural Design
**Estado:** Aprobado

*Backlink a Fase 5:* Este entregable materializa el ciclo de vida del codigo para la infraestructura Dockerizado en Railway/Render elegida en el Deployment Topology (`[[PHASE_5_ARCHITECTURAL_DESIGN/3.Deployment_Topology_Decision/example_output_d3_deployment_topology.md]]`) y la base de codigo unica definida en el System Decomposition (`[[PHASE_5_ARCHITECTURAL_DESIGN/4.System_Decomposition_Decision/example_output_d4_system_decomposition.md]]`).

---

## 2. DevOps & Delivery Pipeline

### Estrategia de Branching
Dada la agilidad requerida para un producto B2B/B2C en etapa temprana y el tamano reducido del equipo inicial, implementaremos **Trunk-Based Development** (descartando GitFlow).
- Existe una unica rama perpetua de la verdad: `main`.
- Los desarrolladores crean ramas efimeras (`feature/nombre-corto`) que deben vivir un maximo de 48 horas antes de someterse a revision (Pull Request) e integrarse de vuelta a `main`.

### Ambientes (Environments)
1. **Local:** Maquina del desarrollador. Utiliza Spring Boot (Java) Development Server (`mvn dev`) y un contenedor Docker instanciado via `PostgreSQL CLI` para emular la base de datos sin afectar datos reales.
2. **Staging (Preview):** Entornos efimeros y automaticos por cada rama/PR abierto. Apuntan a un proyecto de base de datos de "Staging" aislado en PostgreSQL gestionado en Railway.
3. **Production:** El ambiente publico frente a clientes. Railway/Render Production + PostgreSQL Production (AWS Region).

### Reglas de Promocion
- **Promocion a Staging:** Automatica. Abrir un Pull Request contra `main` desencadena la creacion de un URL unico en Railway/Render.
- **Promocion a Production:** Semiautomatica. Una vez aprobado y *mergeado* el codigo a `main`, el despliegue hacia el dominio de produccion ocurre de forma automatica y atomica.

### Integracion Continua (CI)
Todo cambio propuesto hacia `main` debe pasar este muro de proteccion (Pipeline de CI):
1. **Type Check:** `tsc --noEmit` (Vital en un Monolito Modular para no romper contratos entre dominios).
2. **Linting & Formatting:** `next lint` & Prettier.
3. **Unit Tests:** Ejecucion de suites (Jest/Vitest) centradas exclusivamente en los dominios de alta criticidad: *Booking Engine* y *Billing & Payouts*.
4. **Build Check:** Ejecucion de `next build` para simular la generacion de rutas estaticas (Spring Cache (@Cacheable)) e interceptar errores de pre-renderizado.

### Despliegue Continuo (CD)
Dado que la topologia es Dockerizado en Railway/Render (D3), descartamos la orquestacion de contenedores (Kubernetes/Docker). El CD consta de:
1. **Database Migrations:** Aplicacion de cambios SQL mediante `postgresql db push` contra la base de datos destino.
2. **Edge Deployment:** Railway/Render asume la responsabilidad del empaquetado del codigo (Monolito) y su distribucion global a la Cloudflare CDN / Nginx Reverse Proxy. No hay servidores web que reiniciar manualmente.

### Automation & Tooling
- **Plataforma CI/CD:** **GitHub Actions** para orquestar la fase de CI y las migraciones. La fase de CD pura se delega a la integracion nativa de **Railway/Render for GitHub**.
- **IaC (Infrastructure as Code):** **No aplica** el uso de herramientas pesadas como Terraform o Pulumi. La infraestructura se gobierna mediante la configuracion declarativa nativa (`railway.toml / Dockerfile`) y el sistema de migraciones controladas por codigo de `PostgreSQL CLI`.

---

## 3. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 - D3 (Configuration & Environment Secrets):** Los 3 ambientes definidos aqui obligan a crear 3 sets de variables de entorno distintas (`application.yml`, `.env.preview`, `.env.production`).
- **Phase 7 - D2 (Project Scaffolding & Setup):** Inicializa el repositorio GitHub con los workflows `.github/workflows/ci.yml` basandose exactamente en los pasos definidos aqui.
- **D10 (ADR Consolidation):** Las elecciones de herramientas (Trunk-Based, GitHub Actions) quedaran indexadas en el resumen final.

