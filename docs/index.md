# Portal de DocumentaciÃ³n ArquitectÃ³nica e IngenierÃ­a de Software

**Proyecto:** Nos Fuimos de Finca  
**PropÃ³sito:** El presente portal constituye el repositorio centralizado de documentaciÃ³n tÃ©cnica, estratÃ©gica y arquitectÃ³nica del sistema. Su objetivo primordial es garantizar la trazabilidad completa del Ciclo de Vida de Desarrollo de Software (SDLC) bajo la metodologÃ­a *Full Stack Development*. 

---

## Estructura de Directorios y ExplicaciÃ³n de MÃ³dulos (Modular Monolith)

Para entender cÃ³mo estÃ¡ estructurado este repositorio, es vital comprender que el sistema no estÃ¡ diseÃ±ado como una gran aplicaciÃ³n monolÃ­tica tradicional, ni como cientos de microservicios. En su lugar, hemos adoptado un enfoque de **Monolito Modular**.

### Â¿Por quÃ© existe una carpeta `modules/` en varias fases?
En las Fases de diseÃ±o avanzado (como la Fase 4 y la Fase 6), notarÃ¡s que la documentaciÃ³n se divide dentro de una carpeta llamada `modules`. Esto se debe a que el sistema estÃ¡ dividido en "Contextos Delimitados" independientes basados en el negocio. Por ejemplo:
- **MOD-AUTH**: Se encarga Ãºnicamente del registro, inicio de sesiÃ³n y perfiles.
- **MOD-RSV**: Maneja exclusivamente la lÃ³gica transaccional de reservas y bloqueos de fechas.
- **MOD-PAY**: Centraliza la comunicaciÃ³n con pasarelas de pago y webhooks.

Esta separaciÃ³n modular garantiza que el cÃ³digo, la base de datos y la documentaciÃ³n de las reservas no se enreden con el sistema de notificaciones o de pagos. Por ende, los entregables de diseÃ±o muy especÃ­ficos (como diagramas de clases, contratos API o diseÃ±os de base de datos) viven organizados dentro de la subcarpeta de su respectivo mÃ³dulo, facilitando su lectura y mantenimiento por equipos independientes.

---

## Ãndice AnalÃ­tico de Entregables e Instrumentos

A continuaciÃ³n se detalla el objetivo metodolÃ³gico de cada artefacto documental estructurado a lo largo del SDLC. Todos los nombres listados aquÃ­ coinciden exactamente con los nombres de los archivos fuente en formato Markdown.

### ðŸ“‚ 00. Reconocimiento del Problema (Problem Recognition)
**Objetivo de la Fase:** Validar empÃ­ricamente la existencia de una problemÃ¡tica de negocio que justifique el desarrollo de software.

- **`00_phase-0-brief.md`**: El Brief histÃ³rico fundamental que dio origen al proyecto.
- **`1. Problem Statement.md`**: Declarar unÃ­vocamente la problemÃ¡tica central que afecta al mercado objetivo.
- **`2. Evidence Record.md`**: Consolidar mÃ©tricas empÃ­ricas que demuestren el impacto y recurrencia del problema.
- **`3. Existing Solutions Analysis.md`**: Evaluar las alternativas actuales del mercado para identificar deficiencias.
- **`4. Problem Classification Record.md`**: Categorizar el riesgo y la complejidad tÃ©cnica inherente al problema.
- **`5. Impact Matrix.md`**: Cuantificar las ramificaciones operativas y financieras.
- **`6. Project Objectives.md`**: Definir metas estratÃ©gicas medibles que dictarÃ¡n el Ã©xito de la soluciÃ³n.
- **`7. Stakeholder Map.md`**: Identificar y clasificar a los actores afectados por el sistema.
- **`8. Risk Register.md`**: Documentar amenazas iniciales y factores crÃ­ticos de fracaso.
- **`9. Go_No-Go Signal.md`**: Formalizar la decisiÃ³n gerencial de proceder o detener el proyecto.
- **`10. Problem Pattern Log Entry.md`**: Registrar patrones recurrentes para futuras referencias.

### ðŸ“‚ 01. Viabilidad Temprana (Early Viability)
**Objetivo de la Fase:** Cuantificar la rentabilidad y evaluar el riesgo tÃ©cnico antes de comprometer recursos.

- **`18.Brief.md`**: Contexto ejecutivo de la viabilidad temprana.
- **`1. User Profile.md`**: Perfilar demogrÃ¡ficamente a los usuarios finales.
- **`2. Market Validation Document.md`**: Evidenciar la demanda latente del mercado.
- **`3. Competitive Analysis Document.md`**: Identificar la posiciÃ³n frente a competidores directos.
- **`4. Stakeholder Map.md`**: Actualizar la matriz de intereses de los actores clave.
- **`5. Technical Feasibility Record.md`**: Diagnosticar si la tecnologÃ­a permite solucionar el problema.
- **`6. Data Accessibility Record.md`**: Validar la existencia y calidad de los datos requeridos.
- **`7. Legal and Regulatory Clearance Record.md`**: Mitigar riesgos de cumplimiento y privacidad.
- **`8. Team Capability Assessment.md`**: Contrastar competencias tÃ©cnicas contra talento disponible.
- **`9. Viability Document.md`**: Dictamen integral de factibilidad operativa, tÃ©cnica y financiera.
- **`10. Risk Register.md`**: CatÃ¡logo de amenazas actualizado.
- **`11. Critical Assumptions List.md`**: HipÃ³tesis cuya invalidez provocarÃ­a el colapso del proyecto.
- **`12. MVP Definition Document.md`**: LÃ­mites estrictos para el Producto MÃ­nimo Viable.
- **`13. Lean Canvas.md`**: Motores financieros y de tracciÃ³n del ecosistema.
- **`14. OKR Document.md`**: Objetivos y Resultados Clave para medir el progreso.
- **`15. Initial Plan Document.md`**: Cronograma macro de alto nivel.
- **`16. Work Process Document.md`**: Cadencia de trabajo, canales y metodologÃ­a.
- **`17. Go_No-Go_Pivot Decision Record.md`**: DecisiÃ³n ejecutiva para transicionar al Kickoff.

### ðŸ“‚ 02. InicializaciÃ³n del Proyecto (Project Kickoff)
**Objetivo de la Fase:** Formalizar el ecosistema de desarrollo, convenciones de ingenierÃ­a y decisiones base.

- **`13. Phase 2 Brief.md`**: CompilaciÃ³n de directrices del Kickoff.
- **`1. Project Identity.md`**: Estandarizar taxonomÃ­a y visiÃ³n central del repositorio.
- **`2. NFR Constraints.md`**: Restricciones obligatorias (Latencia, Concurrencia, Seguridad).
- **`3. Stack Decision.md`**: Justificar lenguaje, frameworks y base de datos elegidos.
- **`4. Repository Structure.md`**: Normar la arquitectura de carpetas.
- **`5. Branching Strategy.md`**: Dictaminar el flujo de versionamiento (Git).
- **`6. Environment Definitions.md`**: Definir ciclos de promociÃ³n de cÃ³digo.
- **`7. Coding Standards.md`**: Reglas de nomenclatura y guÃ­as idiomÃ¡ticas.
- **`8. Testing Strategy.md`**: Umbrales de cobertura y tipos de pruebas requeridas.
- **`9. Definition of Done and Definition of Ready.md`**: Criterios para aceptar un ticket funcional.
- **`10. Tooling.md`**: Decisiones sobre CI/CD, monitoreo y gestiÃ³n.
- **`11. Communication and Escalation Protocols.md`**: VÃ­as formales de reporte ante fallos.
- **`12. Risk Register Update.md`**: Vulnerabilidades descubiertas en infraestructura.

### ðŸ“‚ 03. IngenierÃ­a de Requisitos
**Objetivo de la Fase:** Mapear exhaustivamente las funciones y reglas de negocio sin ambigÃ¼edad lÃ³gica, centralizando todo en 8 mÃ³dulos principales de negocio.

- **`01. Diagrama de Contexto del Sistema.md`**: Frontera entre el sistema propuesto y el entorno externo.
- **`02. Definicion de Actores y Roles.md`**: Estipular roles de usuario y sus vectores de acciÃ³n primarios.
- **`03. Glosario de Dominio.md`**: Estandarizar el "Lenguaje Ubicuo" para unificar la semÃ¡ntica de negocio e ingenierÃ­a.
- **`04. Elicitacion de Requerimientos.md`**: Capturar requisitos formales directamente de las fuentes de negocio.
- **`05. Descomposicion Modular Funcional.md`**: Descomponer la complejidad del sistema en contextos modulares.
- **`06. Requerimientos No Funcionales.md`**: Requerimientos sistÃ©micos globales como desempeÃ±o, escalabilidad y resiliencia.
- **`07. Module Specifications/modules`**: Contiene las especificaciones detalladas, reglas e historias de usuario para cada uno de los 8 mÃ³dulos consolidados (`MOD-AUTH`, `MOD-CAL`, `MOD-DASH`, `MOD-NOT`, `MOD-PAY`, `MOD-PROP`, `MOD-RSV`, `MOD-SRCH`).
- **`08. System Requirements Specification.md`**: Documento de especificaciÃ³n de requisitos del sistema final (SRS) unificado.

### ðŸ“‚ 04. Modelado del Sistema
**Objetivo de la Fase:** Moldear conceptual y visualmente el comportamiento del software, separando claramente la interfaz de usuario y la arquitectura de datos relacional.

- **[1. Estrategia de Contenido y AI](04-system-modeling/01.Content_Strategy_Information_Architecture/1.Content_Strategy_Information_Architecture.md)**: EstructuraciÃ³n taxonÃ³mica del portal.
- **[2. Flujos de Usuario y Tareas (User Flows)](#)**: Mapeo visual interactivo y lÃ³gico separado en los mÃ³dulos de negocio.
- **[3. Wireframes](#)**: 14 vistas estructurales (baja fidelidad) de las interfaces crÃ­ticas para Desktop y Mobile.
- **[4. DiseÃ±o de Sistema y UI Kit](04-system-modeling/04.Design%20System%20UI%20Kit/Design%20System%20UI%20Kit.md)**: EstandarizaciÃ³n de tipografÃ­as, paletas de colores y componentes.
- **[5. High Fidelity Mockups](#)**: Las 14 vistas finales de alta fidelidad, aplicando el UI Kit a los Wireframes.
- **[6. Modelo de Dominio y ERD Conceptual](04-system-modeling/06.Domain%20Model%20and%20ERD/domain_model_and_erd.md)**: El modelo relacional unificado blindado con seguridad y performance.

> **Nota para Fases Posteriores:** Dado el refinamiento metodolÃ³gico del proyecto, los entregables de diseÃ±o tÃ©cnico avanzado (API Contracts, Arquitectura de Componentes y GuÃ­as de ImplementaciÃ³n) se definirÃ¡n dinÃ¡micamente y se enlazarÃ¡n aquÃ­ a medida que se completen de acuerdo a los requerimientos de la Fase 5 y posteriores.

---

> [!NOTE]
> **IntegraciÃ³n de Modelado Visual**
> Todos los artefactos de diseÃ±o tÃ©cnico UML y C4 han sido codificados mediante sintaxis estricta *Mermaid*, lo que permite el renderizado automÃ¡tico interactivo dentro de este portal de documentaciÃ³n.
