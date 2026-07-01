# Resumen Contextual Ejecutivo: Nos Fuimos de Finca

## 1. Visión General del Sistema

**Nos Fuimos de Finca (FinCapp)** es una plataforma digital centralizada, orientada a la gestión integral de reservas de propiedades turísticas rurales. Su propósito fundacional es establecer un puente transaccional seguro y estructurado entre turistas (arrendatarios) y propietarios, erradicando los procesos informales y manuales que actualmente dominan este nicho de mercado.

### 1.1. Problemática Central
El sector del turismo rural sufre de una severa fragmentación en la gestión de la información. La ausencia de sistemas de control centralizados provoca:
- Riesgos operativos como reservas duplicadas (Overbooking) y conflictos de disponibilidad.
- Falta de trazabilidad financiera y opacidad en el manejo de pagos y reembolsos.
- Dispersión en la comunicación, lo que vulnera la seguridad y confianza de ambas partes.

La plataforma mitiga estos riesgos proveyendo un flujo digital inmutable desde la publicación inicial del inmueble hasta el procesamiento del pago y la calificación post-estadía.

---

## 2. Alcance y Fronteras Operativas

El sistema ha sido acotado mediante límites estrictos para garantizar un lanzamiento viable y mantenible, mitigando la inflación del alcance (Feature Creep).

### 2.1. Funciones Dentro del Alcance (In-Scope)
- **Gestión de Identidades:** Registro, autenticación y control de acceso basado en roles.
- **Catálogo y Motor de Búsqueda:** Navegación paramétrica con filtros avanzados de capacidad, geolocalización y rangos de fechas.
- **Transaccionalidad Core:** Ciclo completo de reserva con bloqueo estricto de disponibilidad (Pessimistic Locking).
- **Procesamiento de Pagos:** Integración con pasarelas externas certificadas para la recaudación segura.
- **Gobierno de la Plataforma:** Paneles de control independientes para Propietarios (gestión de inventario) y Administradores (moderación y auditoría).

### 2.2. Funciones Fuera del Alcance (Out-of-Scope)
- Desarrollo de aplicaciones móviles nativas (iOS/Android).
- Procesos de verificación de identidad biométrica o integración gubernamental directa.
- Generación y gestión de contratos legales o firmas electrónicas vinculantes.
- Soporte internacional (Soporte multimoneda o multiidioma).
- Integración automatizada de calendarios con plataformas globales (Airbnb, Booking.com).

---

## 3. Ecosistema de Módulos Funcionales

La arquitectura lógica de la plataforma se compone de diez (10) módulos cohesivos y débilmente acoplados:

1. **M-01 — Autenticación y Gestión de Usuarios:** Emisión de tokens de sesión y gestión de perfiles.
2. **M-02 — Búsqueda y Navegación:** Motor de descubrimiento y consulta de disponibilidad.
3. **M-03 — Gestión de Reservas:** Motor transaccional para la protección del inventario en tiempo real.
4. **M-04 — Pagos y Facturación:** Abstracción y orquestación de la pasarela de pagos.
5. **M-05 — Comunicación:** Servicio de mensajería interna y trazable entre actores.
6. **M-06 — Panel del Propietario:** Centro de mando para la gestión de disponibilidad y métricas financieras.
7. **M-07 — Panel del Administrador:** Consola de moderación global y resolución de disputas.
8. **M-08 — Gestión de Contenido:** Flujo de publicación y revisión de nuevas fincas.
9. **M-09 — Calificaciones y Reseñas:** Sistema de reputación para mitigar la asimetría de información.
10. **M-10 — Notificaciones:** Servicio de orquestación de correos electrónicos y alertas in-app.

---

## 4. Marco Metodológico y Gobierno

El ciclo de vida de desarrollo de software (SDLC) se rige bajo un marco ágil fundamentado en principios de **Scrum** y **Kanban**. 

- **Historias de Usuario:** Toda funcionalidad técnica se especifica a través de requerimientos centrados en el valor entregable al actor final, delimitados por criterios de aceptación estrictos y verificables.
- **Trazabilidad:** La gestión del avance se ejerce a través de estados lógicos (*Pendiente, En Progreso, Completado*), garantizando transparencia mediante artefactos de control visual.
- **Priorización Orientada al Riesgo:** El desarrollo se planifica mitigando primero los riesgos operativos más altos (Ej. La transaccionalidad de reservas y pasarelas de pago precede a funcionalidades secundarias como las reseñas).

---

## 5. Análisis Estratégico (Matriz DOFA)

El proyecto opera bajo las siguientes variables estratégicas identificadas:

### Variables Internas
- **Fortalezas:** Centralización absoluta del flujo de reserva, arquitectura robusta basada en Monolito Modular, e interfaz de usuario de baja fricción operativa.
- **Debilidades:** Carencia inicial de ecosistema móvil nativo, ausencia de analítica predictiva avanzada y dependencia estructural de pasarelas de pago de terceros.

### Variables Externas
- **Oportunidades:** Crecimiento sostenido del turismo rural nacional, bajo nivel de madurez digital en los competidores locales del mismo nicho, y un cambio en las tendencias post-pandemia hacia el turismo hiperlocal.
- **Amenazas:** Entrada potencial de plataformas hegemónicas internacionales al mercado rural especializado, vulnerabilidad ante la inestabilidad de la infraestructura de telecomunicaciones en zonas rurales, y fluctuaciones en la regulación fiscal local referente a servicios turísticos digitales.