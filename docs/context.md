# Resumen Contextual Ejecutivo: Nos Fuimos de Finca

## 1. Visión General del Sistema

**Nos Fuimos de Finca** es una plataforma digital B2B2C orientada a la gestión de reservas y pagos de propiedades turísticas rurales. Su propósito fundacional es establecer un puente transaccional seguro entre Finqueros y Turistas, erradicando los procesos informales (cuadernos físicos) y el riesgo de estafas en transacciones directas (Nequi/Transferencias no verificadas).

### 1.1. Problemática Central
El sector del turismo rural sufre de una severa fragmentación en la gestión. Esto provoca:
- Riesgos operativos como reservas duplicadas (Double-Booking) y conflictos de disponibilidad.
- Tiempos de respuesta lentos y fricción en la recolección de anticipos.
- Desconfianza por parte del turista al realizar pagos directos a cuentas personales desconocidas.

La plataforma mitiga estos riesgos proveyendo un motor de reservas atómico (State Machine con TTL) acoplado a una pasarela de pagos (Wompi) que transfiere el dinero directamente al Finquero, cobrando un Service Fee al Turista.

---

## 2. Alcance y Fronteras Operativas (MVP)

El sistema ha sido acotado mediante límites estrictos (Definidos en la Fase 1) para garantizar un lanzamiento viable en tiempo récord, operando bajo un modelo donde **el Finquero trae su propio tráfico compartiendo su URL pública**.

### 2.1. Funciones Dentro del Alcance (In-Scope)
- **Gestión de Identidades (Finquero):** Registro, Onboarding KYC (RUT/Cuenta) y Row Level Security (RLS).
- **Checkout Guest:** Flujo de reserva sin fricción, donde el Turista no necesita crear cuenta para pagar.
- **Transaccionalidad Core:** Ciclo completo de reserva con bloqueo estricto temporal (Soft-Lock) y definitivo (Hard-Lock).
- **Procesamiento P2P (Wompi):** Recaudación del Service Fee para la plataforma y dispersión directa del costo del alojamiento a la cuenta del Finquero.
- **Dashboard Básico:** Panel de control para que el Finquero gestione disponibilidad, bloqueos manuales y vea su histórico de reservas.

### 2.2. Funciones Fuera del Alcance (Out-of-Scope)
- **Marketplace o Buscador General:** No habrá un "home" tipo Airbnb para buscar fincas. El tráfico es directo al link de la finca.
- **Sistema de Reseñas y Calificaciones:** Innecesario en la etapa inicial de validación transaccional.
- **Mensajería / Chat In-App:** El contacto directo seguirá ocurriendo por WhatsApp si hay dudas.
- **Desarrollo Móvil Nativo:** Solo Web App responsiva (Mobile-First estricto).

---

## 3. Ecosistema de Módulos Funcionales

La arquitectura lógica de la plataforma se compone estrictamente de siete (7) módulos cohesivos y débilmente acoplados, siguiendo una jerarquía unidireccional:

1. **MOD-AUTH (Autenticación y KYC):** Emisión de JWTs y validación de documentos bancarios del Finquero.
2. **MOD-PROP (Propiedad):** Gestión del perfil público de la finca (Fotos, descripciones, precios).
3. **MOD-CAL (Calendario):** State machine de disponibilidad (Disponible -> Soft-Lock -> Hard-Lock).
4. **MOD-RSV (Reservas):** Motor de cálculo de totales y creación de la orden transaccional.
5. **MOD-PAY (Pagos):** Integración idempotente de Webhooks de Wompi.
6. **MOD-NOT (Notificaciones):** Orquestador de confirmaciones vía SMS/Email asíncronas.
7. **MOD-DASH (Dashboard):** Panel de visualización de analíticas y estados para el dueño.

---

## 4. Marco Metodológico y Técnico

El ciclo de vida se rige bajo la metodología estructurada **FULLSTACK_DEVELOPMENT**.
- **Stack Tecnológico:** Next.js 14 (App Router), Supabase (PostgreSQL + Auth), Tailwind CSS.
- **Arquitectura:** Monolito Modular, garantizando que cada módulo (`MOD-`) tenga fronteras de datos y código limpias, facilitando una futura migración a microservicios si se requiere.

---

## 5. Análisis Estratégico (Matriz DOFA del MVP)

### Variables Internas
- **Fortalezas:** Cero costo de adquisición de usuarios turista (CAC = $0), ya que el Finquero utiliza la plataforma como su datáfono personal compartiendo su propio link. Arquitectura Serverless sin costo operativo base.
- **Debilidades:** Fricción inicial para el Finquero al tener que pasar el proceso KYC para habilitar cobros P2P.

### Variables Externas
- **Oportunidades:** El 90% de los anfitriones rurales en LATAM siguen usando cuadernos y WhatsApp para cobrar.
- **Amenazas:** Caídas del servicio de la pasarela local (Wompi) paralizan el flujo de ingresos de la plataforma.