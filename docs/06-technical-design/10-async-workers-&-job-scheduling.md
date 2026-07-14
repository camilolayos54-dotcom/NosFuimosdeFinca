# Deliverable 10 (D10): Async Workers & Job Scheduling

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4:* Este entregable implementa los requisitos de eventos asincronos y programacion cronologica definidos en la State Machine (`[[8.State_Machine_Diagrams.md]]`).

---

## 2. Colas Asincronas y Payloads (Redis/BullMQ)

> [!WARNING]
> La latencia de la red es el enemigo de la experiencia de usuario. Tareas como mandar un correo de confirmacion de reserva no deben realizarse sincronamente en el mismo ciclo en el que se guarda la reserva en BD. Utilizaremos **Inngest** o **Upstash Redis / BullMQ** para delegar esto.

### 2.1 Cola: `booking-events-queue`

**Proposito:** Procesar eventos derivados de las acciones del Turista y el Finquero.

#### Worker: NotifyBookingStatusChange
**Payload Esperado (JSON):**
```json
{
  "bookingId": "uuid-1234-abcd",
  "eventType": "BOOKING_CREATED",
  "guestId": "uuid-guest",
  "propertyId": "uuid-prop"
}
```
- **Flujo Logico de Ejecucion:**
  1. El worker recibe el Payload de la cola de Redis.
  2. Consulta la base de datos para recuperar los numeros de telefono del Host y Guest.
  3. Ejecuta el Dispatcher del Notification Service (envia SMS o WhatsApp usando la API externa).
  4. Si la API de mensajeria falla temporalmente, ejecuta un reintento.
- **Retry Policy:** 3 Reintentos. Backoff Exponencial (2s, 10s, 30s). No quemamos la API del proveedor de mensajeria incesantemente.
- **Dead-Letter Queue (DLQ):** Si el proveedor externo se cae permanentemente o los datos del JSON estan corruptos, tras el tercer reintento, el evento se mueve a la cola `booking-events-dlq`. 
- **Manejo de Alertas en DLQ:** Todo evento que caiga aqui dispara inmediatamente una alerta critica a un Webhook interno de Slack/Discord para que el equipo de DevOps/Soporte sepa que el Turista **NO** recibio su notificacion.

---

## 3. Programacion Cron (Scheduled Jobs)

Ciertas acciones de mantenimiento del inventario de reservas no son provocadas por clics, sino por el paso del tiempo. Estas tareas se ejecutaran con precision matematica.

> [!TIP]
> **Definicion de Zona Horaria:** Todos los CRON del proyecto deben evaluarse en base a **UTC**. Si apuntamos a que algo ocurra a las 2 de la tarde hora de Colombia (UTC-5), el CRON debe configurarse para las 19:00 horas UTC.

| Nombre de Tarea Interna | Expresion Cron (UTC) | Proposito y Logica Interna |
|---|---|---|
| `CancelExpiredBookings` | `0 * * * *` (Cada hora en punto) | **Logica:** Ejecuta un SELECT de reservas en estado `PENDING` cuyo `createdAt` supere las 24 horas. Las actualiza a `CANCELLED`, liberando inmediatamente las fechas de la Finca para que otros las arrienden. |
| `SendPreCheckinReminders` | `0 19 * * *` (Diario a las 14:00 COT) | **Logica:** Busca reservas `APPROVED` cuyo check-in ocurra exactamente el dia siguiente. Encola eventos en `booking-events-queue` para enviar al Turista un WhatsApp de recordatorio con la direccion GPS. |

---

## 4. Downstream Consumers
- **Phase 7 â€” D5 (Backend API Implementation):** El desarrollador backend debe crear los ficheros `workers/` correspondientes y configurar las conexiones a Upstash Redis o el gestor dockerizado.
- **Phase 10 â€” D1 (Monitoring & Alerting):** DevOps mapeara las Dead-Letter Queues nombradas aqui (`booking-events-dlq`) a un dashboard de Datadog / Sentry.

