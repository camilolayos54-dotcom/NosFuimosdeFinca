# Portal de Documentacion Arquitectonica e Ingenieria de Software

**Proyecto:** Nos Fuimos de Finca  
**Proposito:** El presente portal constituye el repositorio centralizado de documentacion tecnica, estrategica y arquitectonica del sistema. Su objetivo primordial es garantizar la trazabilidad completa del Ciclo de Vida de Desarrollo de Software (SDLC) bajo la metodologia *Full Stack Development*. 

---

## Estructura de Directorios y Explicacion de Modulos (Modular Monolith)

Para entender como esta estructurado este repositorio, es vital comprender que el sistema no esta disenado como una gran aplicacion monolitica tradicional, ni como cientos de microservicios. En su lugar, hemos adoptado un enfoque de **Monolito Modular**.

### Por que existe una carpeta `modules/` en varias fases?
En las Fases de diseno avanzado (como la Fase 4 y la Fase 6), notaras que la documentacion se divide dentro de una carpeta llamada `modules`. Esto se debe a que el sistema esta dividido en "Contextos Delimitados" independientes basados en el negocio. Por ejemplo:
- **MOD-AUTH**: Se encarga unicamente del registro, inicio de sesion y perfiles.
- **MOD-RSV**: Maneja exclusivamente la logica transaccional de reservas y bloqueos de fechas.
- **MOD-PAY**: Centraliza la comunicacion con pasarelas de pago y webhooks.

Esta separacion modular garantiza que el codigo, la base de datos y la documentacion de las reservas no se enreden con el sistema de notificaciones o de pagos. Por ende, los entregables de diseno muy especificos (como diagramas de clases, contratos API o disenos de base de datos) viven organizados dentro de la subcarpeta de su respectivo modulo, facilitando su lectura y mantenimiento por equipos independientes.

---

## Indice Analitico de Entregables e Instrumentos

A continuacion se detalla el objetivo metodologico de cada artefacto documental estructurado a lo largo del SDLC. Todos los nombres listados aqui coinciden exactamente con los nombres de los archivos fuente en formato Markdown.

###  00. Reconocimiento del Problema (Problem Recognition)
**Objetivo de la Fase:** Validar empiricamente la existencia de una problematica de negocio que justifique el desarrollo de software.

- **`00_phase-0-brief.md`**: El Brief historico fundamental que dio origen al proyecto.
- **`1. Problem Statement.md`**: Declarar univocamente la problematica central que afecta al mercado objetivo.
- **`2. Evidence Record.md`**: Consolidar metricas empiricas que demuestren el impacto y recurrencia del problema.
- **`3. Existing Solutions Analysis.md`**: Evaluar las alternativas actuales del mercado para identificar deficiencias.
- **`4. Problem Classification Record.md`**: Categorizar el riesgo y la complejidad tecnica inherente al problema.
- **`5. Impact Matrix.md`**: Cuantificar las ramificaciones operativas y financieras.
- **`6. Project Objectives.md`**: Definir metas estrategicas medibles que dictaran el exito de la solucion.
- **`7. Stakeholder Map.md`**: Identificar y clasificar a los actores afectados por el sistema.
- **`8. Risk Register.md`**: Documentar amenazas iniciales y factores criticos de fracaso.
- **`9. Go_No-Go Signal.md`**: Formalizar la decision gerencial de proceder o detener el proyecto.
- **`10. Problem Pattern Log Entry.md`**: Registrar patrones recurrentes para futuras referencias.

###  01. Viabilidad Temprana (Early Viability)
**Objetivo de la Fase:** Cuantificar la rentabilidad y evaluar el riesgo tecnico antes de comprometer recursos.

- **`18.Brief.md`**: Contexto ejecutivo de la viabilidad temprana.
- **`1. User Profile.md`**: Perfilar demograficamente a los usuarios finales.
- **`2. Market Validation Document.md`**: Evidenciar la demanda latente del mercado.
- **`3. Competitive Analysis Document.md`**: Identificar la posicion frente a competidores directos.
- **`4. Stakeholder Map.md`**: Actualizar la matriz de intereses de los actores clave.
- **`5. Technical Feasibility Record.md`**: Diagnosticar si la tecnologia permite solucionar el problema.
- **`6. Data Accessibility Record.md`**: Validar la existencia y calidad de los datos requeridos.
- **`7. Legal and Regulatory Clearance Record.md`**: Mitigar riesgos de cumplimiento y privacidad.
- **`8. Team Capability Assessment.md`**: Contrastar competencias tecnicas contra talento disponible.
- **`9. Viability Document.md`**: Dictamen integral de factibilidad operativa, tecnica y financiera.
- **`10. Risk Register.md`**: Catalogo de amenazas actualizado.
- **`11. Critical Assumptions List.md`**: Hipotesis cuya invalidez provocaria el colapso del proyecto.
- **`12. MVP Definition Document.md`**: Limites estrictos para el Producto Minimo Viable.
- **`13. Lean Canvas.md`**: Motores financieros y de traccion del ecosistema.
- **`14. OKR Document.md`**: Objetivos y Resultados Clave para medir el progreso.
- **`15. Initial Plan Document.md`**: Cronograma macro de alto nivel.
- **`16. Work Process Document.md`**: Cadencia de trabajo, canales y metodologia.
- **`17. Go_No-Go_Pivot Decision Record.md`**: Decision ejecutiva para transicionar al Kickoff.

###  02. Inicializacion del Proyecto (Project Kickoff)
**Objetivo de la Fase:** Formalizar el ecosistema de desarrollo, convenciones de ingenieria y decisiones base.

- **`13. Phase 2 Brief.md`**: Compilacion de directrices del Kickoff.
- **`1. Project Identity.md`**: Estandarizar taxonomia y vision central del repositorio.
- **`2. NFR Constraints.md`**: Restricciones obligatorias (Latencia, Concurrencia, Seguridad).
- **`3. Stack Decision.md`**: Justificar lenguaje, frameworks y base de datos elegidos.
- **`4. Repository Structure.md`**: Normar la arquitectura de carpetas.
- **`5. Branching Strategy.md`**: Dictaminar el flujo de versionamiento (Git).
- **`6. Environment Definitions.md`**: Definir ciclos de promocion de codigo.
- **`7. Coding Standards.md`**: Reglas de nomenclatura y guias idiomaticas.
- **`8. Testing Strategy.md`**: Umbrales de cobertura y tipos de pruebas requeridas.
- **`9. Definition of Done and Definition of Ready.md`**: Criterios para aceptar un ticket funcional.
- **`10. Tooling.md`**: Decisiones sobre CI/CD, monitoreo y gestion.
- **`11. Communication and Escalation Protocols.md`**: Vias formales de reporte ante fallos.
- **`12. Risk Register Update.md`**: Vulnerabilidades descubiertas en infraestructura.

###  03. Ingenieria de Requisitos
**Objetivo de la Fase:** Mapear exhaustivamente las funciones y reglas de negocio sin ambigedad logica, centralizando todo en 8 modulos principales de negocio.

- **`01. Diagrama de Contexto del Sistema.md`**: Frontera entre el sistema propuesto y el entorno externo.
- **`02. Definicion de Actores y Roles.md`**: Estipular roles de usuario y sus vectores de accion primarios.
- **`03. Glosario de Dominio.md`**: Estandarizar el "Lenguaje Ubicuo" para unificar la semantica de negocio e ingenieria.
- **`04. Elicitacion de Requerimientos.md`**: Capturar requisitos formales directamente de las fuentes de negocio.
- **`05. Descomposicion Modular Funcional.md`**: Descomponer la complejidad del sistema en contextos modulares.
- **`06. Requerimientos No Funcionales.md`**: Requerimientos sistemicos globales como desempeno, escalabilidad y resiliencia.
- **`07. Module Specifications/modules`**: Contiene las especificaciones detalladas, reglas e historias de usuario para cada uno de los 8 modulos consolidados (`MOD-AUTH`, `MOD-CAL`, `MOD-DASH`, `MOD-NOT`, `MOD-PAY`, `MOD-PROP`, `MOD-RSV`, `MOD-SRCH`).
- **`08. System Requirements Specification.md`**: Documento de especificacion de requisitos del sistema final (SRS) unificado.

### 04. Modelado del Sistema
**Objetivo de la Fase:** Moldear conceptual y visualmente el comportamiento del software, separando claramente la interfaz de usuario y la arquitectura de datos relacional.

- **[1. Estrategia de Contenido y AI](04-system-modeling/01.Content_Strategy_Information_Architecture/1.Content_Strategy_Information_Architecture.md)**: Estructuracion taxonomica del portal.
- **[2. Flujos de Usuario y Tareas (User Flows)](#)**: Mapeo visual interactivo y logico separado en los modulos de negocio.
- **[3. Wireframes](#)**: 14 vistas estructurales (baja fidelidad) de las interfaces criticas para Desktop y Mobile.
- **[4. Diseno de Sistema y UI Kit](04-system-modeling/04.Design System UI Kit/Design System UI Kit.md)**: Estandarizacion de tipografias, paletas de colores y componentes.
- **[5. High Fidelity Mockups](#)**: Las 14 vistas finales de alta fidelidad, aplicando el UI Kit a los Wireframes.
- **[6. Modelo de Dominio y ERD Conceptual](04-system-modeling/06.Domain Model and ERD/domain_model_and_erd.md)**: El modelo relacional unificado blindado con seguridad y performance.
- **[7. System Sequence Diagrams](04-system-modeling/07.System Sequence Diagrams/system_sequence_diagrams.md)**: Interacciones sincronas y asincronas del sistema.
- **[8. State Machine Diagrams](04-system-modeling/08.State_Machine_Diagrams/state_machine_diagrams.md)**: Estados de las entidades clave.
- **[9. API Conceptual Design](04-system-modeling/09.API_Conceptual_Design/api_conceptual_design.md)**: Diseno conceptual de la API.
- **[10. Notification Matrix](04-system-modeling/10.Notification_Matrix/notification_matrix.md)**: Matriz de notificaciones y alertas en el sistema.
- **[11. Authorization and Security](04-system-modeling/11.Authorization_and_Security/authorization_and_security.md)**: Estrategia de roles, permisos y politicas.
- **[12. Architectural Signals](04-system-modeling/12.Architectural_Signals/architectural_signals.md)**: Senales y restricciones arquitectonicas de transicion.
- **[13. Accessibility Standards](04-system-modeling/13.Accessibility_Standards/accessibility_standards.md)**: Estandares de accesibilidad WCAG.
- **[14. Localization Strategy](04-system-modeling/14.Localization_Strategy/localization_strategy.md)**: Estrategia de internacionalizacion (i18n).
- **[15. Phase 4 RTM Update](04-system-modeling/15.Phase_4_RTM_Update/phase_4_rtm_update.md)**: Matriz de trazabilidad de requisitos actualizada.

### 05. Diseno Arquitectonico (Architectural Design)
**Objetivo de la Fase:** Definir la infraestructura, topologia y patrones de comunicacion del sistema base.

- **[01. Quality Attributes Map](05-architectural-design/01-quality-attributes-map.md)**
- **[02. Bounded Context Formalization](05-architectural-design/02-bounded-context-formalization.md)**
- **[03. Deployment Topology Decision](05-architectural-design/03-deployment-topology-decision.md)**
- **[04. System Decomposition Decision](05-architectural-design/04-system-decomposition-decision.md)**
- **[05. Architectural Style Selection](05-architectural-design/05-architectural-style-selection.md)**
- **[06. Communication Pattern Decision](05-architectural-design/06-communication-pattern-decision.md)**
- **[07. Cross Cutting Concerns](05-architectural-design/07-cross-cutting-concerns.md)**
- **[08. CI CD & Environments Strategy](05-architectural-design/08-ci-cd-&-environments-strategy.md)**
- **[09. Component Diagram](05-architectural-design/09-component-diagram.md)**
- **[10. ADR Consolidation](05-architectural-design/10-adr-consolidation.md)**
- **[11. Phase 5 RTM Update & Brief](05-architectural-design/11-phase-5-rtm-update-&-brief.md)**

### 06. Diseno Tecnico (Technical Design)
**Objetivo de la Fase:** Producir los contratos especificos, modelos de datos fisicos y especificaciones exactas para iniciar el desarrollo.

- **[01. Codebase & Folder Architecture](06-technical-design/01-codebase-&-folder-architecture.md)**
- **[02. Physical Data Modeling](06-technical-design/02-physical-data-modeling.md)**
- **[03. Configuration & Environment Secrets](06-technical-design/03-configuration-&-environment-secrets.md)**
- **[04. Security Implementation & Middleware](06-technical-design/04-security-implementation-&-middleware.md)**
- **[05. Class & Entity Diagrams](06-technical-design/05-class-&-entity-diagrams.md)**
- **[06. Data Access & Repositories](06-technical-design/06-data-access-&-repositories.md)**
- **[07. API Contracts (OpenAPI Swagger)](06-technical-design/07-api-contracts-(openapi-swagger).md)**
- **[08. Third Party Integrations & Webhooks](06-technical-design/08-third-party-integrations-&-webhooks.md)**
- **[09. Frontend Component & State Architecture](06-technical-design/09-frontend-component-&-state-architecture.md)**
- **[10. Async Workers & Job Scheduling](06-technical-design/10-async-workers-&-job-scheduling.md)**
- **[11. Semantic HTML & ARIA Contracts](06-technical-design/11-semantic-html-&-aria-contracts.md)**
- **[12. i18n Technical Implementation](06-technical-design/12-i18n-technical-implementation.md)**
- **[13. Data Seeding & Legacy Migration Plan](06-technical-design/13-data-seeding-&-legacy-migration-plan.md)**
- **[14. Phase 6 RTM Update & Brief](06-technical-design/14-phase-6-rtm-update-&-brief.md)**

---

> [!NOTE]
> **Integracion de Modelado Visual**
> Todos los artefactos de diseno tecnico UML y C4 han sido codificados mediante sintaxis estricta *Mermaid*, lo que permite el renderizado automatico interactivo dentro de este portal de documentacion.
