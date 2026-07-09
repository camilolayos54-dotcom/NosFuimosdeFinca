# Portal de Documentación Arquitectónica e Ingeniería de Software

**Proyecto:** Nos Fuimos de Finca  
**Propósito:** El presente portal constituye el repositorio centralizado de documentación técnica, estratégica y arquitectónica del sistema. Su objetivo primordial es garantizar la trazabilidad completa del Ciclo de Vida de Desarrollo de Software (SDLC) bajo la metodología *Full Stack Development*. 

---

## Estructura de Directorios y Explicación de Módulos (Modular Monolith)

Para entender cómo está estructurado este repositorio, es vital comprender que el sistema no está diseñado como una gran aplicación monolítica tradicional, ni como cientos de microservicios. En su lugar, hemos adoptado un enfoque de **Monolito Modular**.

### ¿Por qué existe una carpeta `modules/` en varias fases?
En las Fases de diseño avanzado (como la Fase 4 y la Fase 6), notarás que la documentación se divide dentro de una carpeta llamada `modules`. Esto se debe a que el sistema está dividido en "Contextos Delimitados" independientes basados en el negocio. Por ejemplo:
- **MOD-AUTH**: Se encarga únicamente del registro, inicio de sesión y perfiles.
- **MOD-RSV**: Maneja exclusivamente la lógica transaccional de reservas y bloqueos de fechas.
- **MOD-PAY**: Centraliza la comunicación con pasarelas de pago y webhooks.

Esta separación modular garantiza que el código, la base de datos y la documentación de las reservas no se enreden con el sistema de notificaciones o de pagos. Por ende, los entregables de diseño muy específicos (como diagramas de clases, contratos API o diseños de base de datos) viven organizados dentro de la subcarpeta de su respectivo módulo, facilitando su lectura y mantenimiento por equipos independientes.

---

## Índice Analítico de Entregables e Instrumentos

A continuación se detalla el objetivo metodológico de cada artefacto documental estructurado a lo largo del SDLC. Todos los nombres listados aquí coinciden exactamente con los nombres de los archivos fuente en formato Markdown.

### 📂 00. Reconocimiento del Problema (Problem Recognition)
**Objetivo de la Fase:** Validar empíricamente la existencia de una problemática de negocio que justifique el desarrollo de software.

- **`00_phase-0-brief.md`**: El Brief histórico fundamental que dio origen al proyecto.
- **`1. Problem Statement.md`**: Declarar unívocamente la problemática central que afecta al mercado objetivo.
- **`2. Evidence Record.md`**: Consolidar métricas empíricas que demuestren el impacto y recurrencia del problema.
- **`3. Existing Solutions Analysis.md`**: Evaluar las alternativas actuales del mercado para identificar deficiencias.
- **`4. Problem Classification Record.md`**: Categorizar el riesgo y la complejidad técnica inherente al problema.
- **`5. Impact Matrix.md`**: Cuantificar las ramificaciones operativas y financieras.
- **`6. Project Objectives.md`**: Definir metas estratégicas medibles que dictarán el éxito de la solución.
- **`7. Stakeholder Map.md`**: Identificar y clasificar a los actores afectados por el sistema.
- **`8. Risk Register.md`**: Documentar amenazas iniciales y factores críticos de fracaso.
- **`9. Go_No-Go Signal.md`**: Formalizar la decisión gerencial de proceder o detener el proyecto.
- **`10. Problem Pattern Log Entry.md`**: Registrar patrones recurrentes para futuras referencias.

### 📂 01. Viabilidad Temprana (Early Viability)
**Objetivo de la Fase:** Cuantificar la rentabilidad y evaluar el riesgo técnico antes de comprometer recursos.

- **`18.Brief.md`**: Contexto ejecutivo de la viabilidad temprana.
- **`1. User Profile.md`**: Perfilar demográficamente a los usuarios finales.
- **`2. Market Validation Document.md`**: Evidenciar la demanda latente del mercado.
- **`3. Competitive Analysis Document.md`**: Identificar la posición frente a competidores directos.
- **`4. Stakeholder Map.md`**: Actualizar la matriz de intereses de los actores clave.
- **`5. Technical Feasibility Record.md`**: Diagnosticar si la tecnología permite solucionar el problema.
- **`6. Data Accessibility Record.md`**: Validar la existencia y calidad de los datos requeridos.
- **`7. Legal and Regulatory Clearance Record.md`**: Mitigar riesgos de cumplimiento y privacidad.
- **`8. Team Capability Assessment.md`**: Contrastar competencias técnicas contra talento disponible.
- **`9. Viability Document.md`**: Dictamen integral de factibilidad operativa, técnica y financiera.
- **`10. Risk Register.md`**: Catálogo de amenazas actualizado.
- **`11. Critical Assumptions List.md`**: Hipótesis cuya invalidez provocaría el colapso del proyecto.
- **`12. MVP Definition Document.md`**: Límites estrictos para el Producto Mínimo Viable.
- **`13. Lean Canvas.md`**: Motores financieros y de tracción del ecosistema.
- **`14. OKR Document.md`**: Objetivos y Resultados Clave para medir el progreso.
- **`15. Initial Plan Document.md`**: Cronograma macro de alto nivel.
- **`16. Work Process Document.md`**: Cadencia de trabajo, canales y metodología.
- **`17. Go_No-Go_Pivot Decision Record.md`**: Decisión ejecutiva para transicionar al Kickoff.

### 📂 02. Inicialización del Proyecto (Project Kickoff)
**Objetivo de la Fase:** Formalizar el ecosistema de desarrollo, convenciones de ingeniería y decisiones base.

- **`13. Phase 2 Brief.md`**: Compilación de directrices del Kickoff.
- **`1. Project Identity.md`**: Estandarizar taxonomía y visión central del repositorio.
- **`2. NFR Constraints.md`**: Restricciones obligatorias (Latencia, Concurrencia, Seguridad).
- **`3. Stack Decision.md`**: Justificar lenguaje, frameworks y base de datos elegidos.
- **`4. Repository Structure.md`**: Normar la arquitectura de carpetas.
- **`5. Branching Strategy.md`**: Dictaminar el flujo de versionamiento (Git).
- **`6. Environment Definitions.md`**: Definir ciclos de promoción de código.
- **`7. Coding Standards.md`**: Reglas de nomenclatura y guías idiomáticas.
- **`8. Testing Strategy.md`**: Umbrales de cobertura y tipos de pruebas requeridas.
- **`9. Definition of Done and Definition of Ready.md`**: Criterios para aceptar un ticket funcional.
- **`10. Tooling.md`**: Decisiones sobre CI/CD, monitoreo y gestión.
- **`11. Communication and Escalation Protocols.md`**: Vías formales de reporte ante fallos.
- **`12. Risk Register Update.md`**: Vulnerabilidades descubiertas en infraestructura.

### 📂 03. Ingeniería de Requisitos
**Objetivo de la Fase:** Mapear exhaustivamente las funciones y reglas de negocio sin ambigüedad lógica, centralizando todo en 9 módulos principales de negocio.

- **`1. System Context Diagram.md`**: Frontera entre el sistema propuesto y el entorno externo.
- **`2. Actor and Role Definition.md`**: Roles de usuario y vectores de acción primarios.
- **`3. Domain Glossary.md`**: "Lenguaje Ubicuo" para unificar negocio e ingeniería.
- **`4. Elicitation Records.md`**: Requisitos formales directos de fuentes de negocio.
- **`5. Functional Module Decomposition.md`**: Descomposición de complejidad en 9 contextos modulares.
- **Módulos Específicos (`5.1` al `5.9`)**: Requisitos, historias y casos de uso organizados por módulo (`MOD-AUTH`, `MOD-SRCH`, `MOD-RSV`, `MOD-PAY`, `MOD-POWN`, `MOD-PADM`, `MOD-FCNT`, `MOD-REV`, `MOD-NOT`).
- **`6. Non-Functional Requirements.md`**: Requerimientos sistémicos globales.
- **`8. Inter-Module Conflict Check.md`**: Prevención de choques lógicos tempranos.
- **`10. Requirements Traceability Matrix.md`**: Vinculación matemática de negocio e ingeniería.
- **`11. SRS Document.md`**: Especificación de Requisitos de Software final.

### 📂 04. Modelado del Sistema
**Objetivo de la Fase:** Moldear conceptual y visualmente el comportamiento del software, separando claramente la interfaz de usuario y la arquitectura de datos relacional.

- **[1. Estrategia de Contenido y AI](04-system-modeling/1.Content_Strategy_Information_Architecture/1.Content_Strategy_Information_Architecture.md)**: Estructuración taxonómica del portal.
- **[2. Flujos de Usuario y Tareas (User Flows)](#)**: Mapeo visual interactivo y lógico separado en los módulos de negocio.
- **[3. Wireframes](#)**: 14 vistas estructurales (baja fidelidad) de las interfaces críticas para Desktop y Mobile.
- **[4. Diseño de Sistema y UI Kit](04-system-modeling/4.Design%20System%20UI%20Kit/Design%20System%20UI%20Kit.md)**: Estandarización de tipografías, paletas de colores y componentes.
- **[5. High Fidelity Mockups](#)**: Las 14 vistas finales de alta fidelidad, aplicando el UI Kit a los Wireframes.
- **[6. Modelo de Dominio y ERD Conceptual](04-system-modeling/6.Domain%20Model%20and%20ERD/domain_model_and_erd.md)**: El modelo relacional unificado blindado con seguridad y performance.

> **Nota para Fases Posteriores:** Dado el refinamiento metodológico del proyecto, los entregables de diseño técnico avanzado (API Contracts, Arquitectura de Componentes y Guías de Implementación) se definirán dinámicamente y se enlazarán aquí a medida que se completen de acuerdo a los requerimientos de la Fase 5 y posteriores.

---

> [!NOTE]
> **Integración de Modelado Visual**
> Todos los artefactos de diseño técnico UML y C4 han sido codificados mediante sintaxis estricta *Mermaid*, lo que permite el renderizado automático interactivo dentro de este portal de documentación.
