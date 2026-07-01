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

- **`00_resumen-fase-0.md`**: Establecer el mandato inicial y alinear expectativas fundacionales.
- **`1. Declaración del Problema.md`**: Declarar unívocamente la problemática central que afecta al mercado objetivo.
- **`2. Registro de Evidencia.md`**: Consolidar métricas empíricas que demuestren el impacto y recurrencia del problema.
- **`3. Análisis de Soluciones Existentes.md`**: Evaluar las alternativas actuales del mercado para identificar deficiencias sistémicas.
- **`4. Registro de Clasificación del Problema.md`**: Categorizar el riesgo y la complejidad técnica inherente al problema.
- **`5. Matriz de Impacto.md`**: Cuantificar las ramificaciones operativas y financieras derivadas de no solucionar la problemática.
- **`6. Objetivos del Proyecto.md`**: Definir metas estratégicas medibles que dictarán el éxito de la solución a implementar.
- **`7. Mapa de Partes Interesadas.md`**: Identificar y clasificar a todos los actores directos e indirectos afectados por el sistema.
- **`8. Registro de Riesgos.md`**: Documentar amenazas iniciales y factores críticos de fracaso para la fase de ideación.
- **`9. Señal de Proceder_No-Proceder.md`**: Formalizar la decisión gerencial de proceder o detener la investigación del proyecto.
- **`10. Entrada del Registro de Patrones de Problemas.md`**: Registrar patrones recurrentes descubiertos durante la fase de reconocimiento para futuras referencias.

### 📂 01. Viabilidad Temprana (Early Viability)
**Objetivo de la Fase:** Cuantificar la rentabilidad y evaluar el riesgo técnico antes de comprometer recursos de desarrollo.

- **`1. Perfil de Usuario.md`**: Perfilar demográficamente a los usuarios finales para guiar las decisiones de interfaz.
- **`2. Documento de Validación de Mercado.md`**: Evidenciar la demanda latente del mercado frente a la solución proyectada.
- **`3. Documento de Análisis Competitivo.md`**: Identificar la posición estratégica frente a competidores directos.
- **`4. Mapa de Partes Interesadas.md`**: Actualizar la matriz de intereses e influencia de los actores clave.
- **`5. Registro de Factibilidad Técnica.md`**: Diagnosticar tempranamente si la tecnología actual permite solucionar el problema.
- **`6. Registro de Accesibilidad de Datos.md`**: Validar la existencia, calidad y disponibilidad de los datos requeridos por el sistema.
- **`7. Registro de Autorización Legal y Regulatoria.md`**: Mitigar riesgos de cumplimiento, privacidad de datos y restricciones legales.
- **`8. Evaluación de Capacidad del Equipo.md`**: Contrastar las competencias técnicas requeridas contra el talento humano disponible.
- **`9. Documento de Viabilidad.md`**: Emitir un dictamen integral consolidando las factibilidades operativa, técnica y financiera.
- **`10. Registro de Riesgos.md`**: Actualizar el catálogo de amenazas a la luz del análisis de mercado y limitaciones técnicas.
- **`11. Lista de Suposiciones Críticas.md`**: Enumerar hipótesis fundamentales cuya invalidez provocaría el colapso del proyecto.
- **`12. Documento de Definición de MVP.md`**: Trazar límites estrictos para el Producto Mínimo Viable, garantizando un alcance conservador.
- **`13. Lean Canvas.md`**: Plasmar en una página los motores financieros y de tracción del ecosistema.
- **`14. Documento OKR.md`**: Establecer Objetivos y Resultados Clave para medir el progreso metodológico.
- **`15. Documento de Plan Inicial.md`**: Perfilar un cronograma macro de alto nivel para la provisión de recursos.
- **`16. Documento de Proceso de Trabajo.md`**: Estipular la cadencia de trabajo, canales de comunicación y metodología.
- **`17. Registro de Decisión Proceder_No-Proceder_Pivotar.md`**: Documentar la autorización ejecutiva formal para transicionar al Kickoff.
- **`18. Resumen.md`**: Consolidar ejecutivamente los hallazgos de viabilidad para consulta rápida.

### 📂 02. Inicialización del Proyecto (Project Kickoff)
**Objetivo de la Fase:** Formalizar el ecosistema de desarrollo, convenciones de ingeniería y decisiones de arquitectura base.

- **`1. Identidad del Proyecto.md`**: Estandarizar la taxonomía, nombre en clave y visión central del repositorio.
- **`2. Restricciones NFR.md`**: Fijar las restricciones obligatorias (Latencia, Concurrencia, Seguridad) que dictarán las decisiones.
- **`3. Decision de Stack.md`**: Justificar el lenguaje de programación, frameworks y motores de base de datos elegidos.
- **`4. Estructura del Repositorio.md`**: Normar la arquitectura de carpetas y repositorios para evitar entropía estructural.
- **`5. Estrategia de Ramificacion.md`**: Dictaminar el flujo de versionamiento para prevenir conflictos de integración.
- **`6. Definiciones de Entorno.md`**: Definir los ciclos de promoción de código (Local, Staging, Producción).
- **`7. Estandares de Codificacion.md`**: Establecer reglas de nomenclatura y guías de estilo idiomáticas obligatorias.
- **`8. Estrategia de Pruebas.md`**: Obligar umbrales de cobertura y tipos de pruebas requeridas.
- **`9. Definicion de Hecho y Preparado.md`**: Cuantificar matemáticamente los criterios para aceptar un ticket funcional.
- **`10. Herramientas.md`**: Centralizar las decisiones sobre herramientas de CI/CD, monitoreo y gestión de incidencias.
- **`11. Protocolos de Comunicacion y Escalacion.md`**: Establecer las vías formales de reporte ante fallos críticos.
- **`12. Actualizacion de Registro de Riesgos.md`**: Registrar vulnerabilidades de infraestructura descubiertas.
- **`13. Resumen de Fase 2.md`**: Compilar las directrices técnicas del Kickoff para inducción (Onboarding) de ingenieros.

### 📂 03. Ingeniería de Requisitos
**Objetivo de la Fase:** Mapear exhaustivamente las funciones y reglas de negocio sin ambigüedad lógica.

- **`1. Diagrama de Contexto del Sistema.md`**: Mapear la frontera entre el sistema propuesto y el entorno externo.
- **`2. Definicion de Actores y Roles.md`**: Estipular roles de usuario y sus vectores de acción primarios.
- **`3. Glosario de Dominio.md`**: Estandarizar el "Lenguaje Ubicuo" para unificar la semántica de negocio e ingeniería.
- **`4. Registros de Elicitacion.md`**: Capturar requisitos formales directamente de las fuentes de negocio.
- **`5. Descomposicion de Modulos Funcionales.md`**: Descomponer la complejidad en contextos modulares.
- **`5.1` al `5.9` (`MOD-AUTH` a `MOD-NOT`)**: Listado de requisitos funcionales específicos para cada uno de los módulos.
- **`6. Requisitos No Funcionales.md`**: Requerimientos sistémicos globales como desempeño y resiliencia.
- **`8. Verificacion de Conflictos Inter-Modulos.md`**: Prevenir choques lógicos tempranos entre dominios acotados.
- **`10. Matriz de Trazabilidad de Requisitos.md`**: Vincular matemáticamente cada regla de negocio con un caso de uso (Zero Gaps).
- **`11. Documento SRS.md`**: Documento de especificación de requisitos del sistema final y congelado.

### 📂 04. Modelado del Sistema
**Objetivo de la Fase:** Moldear de forma conceptual y visual el comportamiento del software y su arquitectura de información.

- **`1.Estrategia de Contenido y AI.md`**: Definir la taxonomía y la arquitectura de la información (AI).
- **`4.Sistema de Diseno y UI Kit.md`**: Consolidar variables de diseño, paletas, tipografías y componentes base de interfaz.
- **`6.Modelo de Dominio y ERD Conceptual.md`**: Diseñar el modelo relacional conceptual primario de la base de datos (PostgreSQL).
- **`11.Matriz de Autorizacion y Seguridad.md`**: Estructurar la Matriz de Control de Acceso Basado en Roles (RBAC).
- **`12.Sintesis de Senales Arquitectonicas.md`**: Extraer inductores arquitectónicos críticos que impactarán decisiones sistémicas futuras.
- **`13.Actualizacion RTM y Resumen Fase 4.md`**: Cierre de la fase y cruce de validación contra los requerimientos originales.

- **Carpeta `modules/`**:
  *Contiene las descripciones gráficas (casos de uso, flujos, wireframes y modelado conceptual API) aislados para cada módulo del negocio.*
  - **`2.Flujos de Usuario y Tareas.md`**: Mapas visuales de cómo navega el usuario por este módulo en particular.
  - **`3.Wireframes.md` y `5.Mockups_Alta_Fidelidad.md`**: Prototipos visuales específicos (Ej. La pantalla de Checkout en Reservas).
  - **`7.Diagramas de Secuencia del Sistema.md`**: Interacciones temporales entre el actor y las APIs internas.
  - **`8.Diagramas de Maquina de Estado.md`**: Cambios de estado en entidades complejas (Ej. Soft-Lock a Hard-Lock).
  - **`9.Diseno Conceptual de API.md` y `10.Matriz de Notificaciones y Eventos.md`**: Bocetos de endpoints y eventos asíncronos.

### 📂 05. Diseño Arquitectónico (Architectural Design)
**Objetivo de la Fase:** Construir la topología física y el andamiaje estructural macro del software utilizando el framework C4.

- **`1.Mapa de Atributos de Calidad.md`**: Mapear tácticas arquitectónicas directas para mitigar riesgos sistémicos.
- **`2.Formalizacion de Contexto Delimitado.md`**: Trazar límites lógicos (Domain-Driven Design) definitivos entre los módulos.
- **`3.Decision de Topologia de Despliegue.md`**: Diagramar la topología física de infraestructura (AWS, Vercel, RDS).
- **`4.Decision de Descomposicion del Sistema.md`**: Justificar el particionamiento (Spring Boot Monolito Modular).
- **`5.Seleccion de Estilo Arquitectonico.md`**: Ratificar formalmente la interacción API REST y Eventos Locales.
- **`6.Decision de Patron de Comunicacion.md`**: Dictaminar interacciones síncronas vs asíncronas para resolver cuellos de botella.
- **`7.Preocupaciones Transversales.md`**: Diseñar la infraestructura compartida (Logs, JWT, Manejo Global de Excepciones).
- **`8.Estrategia CI-CD y Entornos.md`**: Formalizar las tuberías de GitHub Actions y pases a Producción.
- **`9.Diagrama de Componentes.md`**: Proveer el Nivel 3 del modelo C4, exhibiendo interfaces internas.
- **`10.Consolidacion ADR.md`**: Centralizar los Registros de Decisiones Arquitectónicas (ADRs).
- **`11.Actualizacion RTM y Resumen Fase 5.md`**: Comprobar el mapeo bidireccional final de infraestructura.

### 📂 06. Diseño Técnico (Technical Design)
**Objetivo de la Fase:** Emitir planos de ingeniería deterministas, a nivel de código, para su ejecución directa.

- **`1.Arquitectura del Codigo.md`**: Definir jerarquías de paquetes estructurales en el repositorio Java y Next.js.
- **`2.Modelado Fisico de Datos.md`**: Dictaminar los scripts SQL DDL, extensiones y estrategias de indexación PostgreSQL.
- **`3.Configuracion y Secretos.md`**: Estructurar los esquemas de inyección segura de variables de entorno (Ej. llaves de Wompi, AWS, JWT).
- **`4.Implementacion de Seguridad.md`**: Proveer especificaciones algorítmicas para el `JwtAuthenticationFilter` y seguridad RBAC en endpoints.
- **`11.Actualizacion RTM y Resumen Fase 6.md`**: Auditar la consistencia de los planos técnicos contra requerimientos.

- **Carpeta `modules/`**:
  *Contiene los planos a bajo nivel (Clases, Repositorios, Endpoints) dictaminados para cada módulo independiente, blindando el desarrollo concurrente por múltiples desarrolladores sin provocar conflictos Git.*
  - **`5.Diagramas de Clases.md`**: UML que define las entidades, DTOs y Servicios de Spring Boot.
  - **`6.Acceso a Datos.md`**: Interfaces `JpaRepository` y consultas SQL personalizadas críticas (Ej. el Pessimistic Lock).
  - **`7.Contratos API.md`**: Esquemas estandarizados OpenAPI 3.0 listos para importarse en Swagger o Postman.
  - **`8.Integraciones Terceros.md`**: Firmas de Webhooks entrantes (Wompi) o clientes externos (AWS S3, Sendgrid).
  - **`9.Arquitectura Frontend.md`**: Árboles lógicos de componentes React y manejo de estado (Zustand, React Query).
  - **`10.Workers Asincronos.md`**: Especificaciones para cronjobs de limpieza y escuchadores de eventos Spring (Listeners).

### 📂 07. Implementación (Implementation)
**Objetivo de la Fase:** Transformar los modelos de diseño técnico de la Fase 6 en activos de código fuente. Guías paso a paso de ejecución (SOPs).

- **`1.Desglose de Tareas AI.md`**: Establecer una Estructura de Desglose del Trabajo (WBS) planificada en 7 Sprints ejecutables.
- **`2.Guia de Ejecucion Estructura de Proyecto.md`**: Inicialización física de Node.js, Spring Boot y Docker.
- **`3.Guia de Ejecucion Walking Skeleton.md`**: Despliegue fundacional inicial "End-to-End" con el healthcheck.
- **`4.Implementacion de Migraciones de Base de Datos.md`**: Ejecutar Flyway con los scripts SQL DDL extraídos de la fase 6.
- **`5.Implementacion API Backend.md`**: Instrucciones sistemáticas para programar los módulos backend en Java.
- **`6.Implementacion UI Frontend.md`**: Instrucciones para armar los layouts y componentes en Next.js.
- **`7.Guia de Implementacion de Seguridad.md`**: Construcción del interceptor JWT y protección perimetral del servidor.
- **`8.Guia de Integraciones Externas.md`**: Inyección y verificación HMAC criptográfica de Webhooks (Wompi) y servicios AWS/Sendgrid.
- **`9.Revision y Resumen Fase 7.md`**: Checklist técnica para certificar un *Build* libre de errores y warnings antes del QA.

---

> [!NOTE]
> **Integración de Modelado Visual**
> Todos los artefactos de diseño técnico UML y C4 han sido codificados mediante sintaxis estricta *Mermaid*, lo que permite el renderizado automático interactivo dentro de este portal de documentación.
