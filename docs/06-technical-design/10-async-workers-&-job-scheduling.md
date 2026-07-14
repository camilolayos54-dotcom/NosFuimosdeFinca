# Deliverable 10 (D10): Async Workers & Job Scheduling

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4:* Este entregable implementa los requisitos de eventos asÃ­ncronos y programaciÃ³n cronolÃ³gica definidos en la State Machine (`[[8.State_Machine_Diagrams.md]]`).

---

## 2. Colas AsÃ­ncronas y Payloads (Redis/BullMQ)

> [!WARNING]
> La latencia de la red es el enemigo de la experiencia de usuario. Tareas como mandar un correo de confirmaciÃ³n de reserva no deben realizarse sÃ­ncronamente en el mismo ciclo en el que se guarda la reserva en BD. Utilizaremos **Inngest** o **Upstash Redis / BullMQ** para delegar esto.

### 2.1 Cola: `booking-events-queue`

**PropÃ³sito:** Procesar eventos derivados de las acciones del Turista y el Finquero.

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
- **Flujo LÃ³gico de EjecuciÃ³n:**
  1. El worker recibe el Payload de la cola de Redis.
  2. Consulta la base de datos para recuperar los nÃºmeros de telÃ©fono del Host y Guest.
  3. Ejecuta el Dispatcher del Notification Service (envÃ­a SMS o WhatsApp usando la API externa).
  4. Si la API de mensajerÃ­a falla temporalmente, ejecuta un reintento.
- **Retry Policy:** 3 Reintentos. Backoff Exponencial (2s, 10s, 30s). No quemamos la API del proveedor de mensajerÃ­a incesantemente.
- **Dead-Letter Queue (DLQ):** Si el proveedor externo se cae permanentemente o los datos del JSON estÃ¡n corruptos, tras el tercer reintento, el evento se mueve a la cola `booking-events-dlq`. 
- **Manejo de Alertas en DLQ:** Todo evento que caiga aquÃ­ dispara inmediatamente una alerta crÃ­tica a un Webhook interno de Slack/Discord para que el equipo de DevOps/Soporte sepa que el Turista **NO** recibiÃ³ su notificaciÃ³n.

---

## 3. ProgramaciÃ³n Cron (Scheduled Jobs)

Ciertas acciones de mantenimiento del inventario de reservas no son provocadas por clics, sino por el paso del tiempo. Estas tareas se ejecutarÃ¡n con precisiÃ³n matemÃ¡tica.

> [!TIP]
> **DefiniciÃ³n de Zona Horaria:** Todos los CRON del proyecto deben evaluarse en base a **UTC**. Si apuntamos a que algo ocurra a las 2 de la tarde hora de Colombia (UTC-5), el CRON debe configurarse para las 19:00 horas UTC.

| Nombre de Tarea Interna | ExpresiÃ³n Cron (UTC) | PropÃ³sito y LÃ³gica Interna |
|---|---|---|
| `CancelExpiredBookings` | `0 * * * *` (Cada hora en punto) | **LÃ³gica:** Ejecuta un SELECT de reservas en estado `PENDING` cuyo `createdAt` supere las 24 horas. Las actualiza a `CANCELLED`, liberando inmediatamente las fechas de la Finca para que otros las arrienden. |
| `SendPreCheckinReminders` | `0 19 * * *` (Diario a las 14:00 COT) | **LÃ³gica:** Busca reservas `APPROVED` cuyo check-in ocurra exactamente el dÃ­a siguiente. Encola eventos en `booking-events-queue` para enviar al Turista un WhatsApp de recordatorio con la direcciÃ³n GPS. |

---

## 4. Downstream Consumers
- **Phase 7 â€” D5 (Backend API Implementation):** El desarrollador backend debe crear los ficheros `workers/` correspondientes y configurar las conexiones a Upstash Redis o el gestor serverless.
- **Phase 10 â€” D1 (Monitoring & Alerting):** DevOps mapearÃ¡ las Dead-Letter Queues nombradas aquÃ­ (`booking-events-dlq`) a un dashboard de Datadog / Sentry.

