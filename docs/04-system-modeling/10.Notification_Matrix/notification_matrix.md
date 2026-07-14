 # Entregable 10 (D10): Matriz de Notificaciones y Eventos

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Modulo:** MOD-BOOKING / MOD-NOT
**Estado:** Aprobado

---

## Matriz Completa de Notificaciones

*Backlink a Fase 3:* Los eventos disparadores provienen de los diagramas de Use Cases y las restricciones de canal (WhatsApp en lugar de SMS) respetan los NFRs de la Fase 3 (`[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements]]`).

| Evento | Destinatario | Canal | Estrategia de Disparo | Asunto / Titulo / UX Copy |
|:---|:---|:---|:---|:---|
| **`BOOKING_APPROVAL_REQUEST`** | Finquero (OWNER_API) | WhatsApp API | Async Worker | **Plantilla WA:** ` Hola [Host.Name]! Tienes una solicitud de reserva para [Property.Name] del [Booking.CheckInDate] al [Booking.CheckOutDate]. Responde SI para aprobar o NO para rechazar en los proximos 90 minutos.` |
| **`BOOKING_CONFIRMED`** | Turista / Agencia | Email | Async Worker | **Asunto:** ` Confirmado! Tu reserva en [Property.Name] esta lista `<br>**Body:** `Hola [Guest.Name], Tu reserva ha sido confirmada. Codigo: [Booking.ID].` |
| **`BOOKING_CONFIRMED`** | Finquero (OWNER_API) | WhatsApp API + Email | Async Worker | **Plantilla WA:** `Aprobaste la reserva [Booking.ID]. El pago de $[Payment.Amount] ha sido asegurado. A preparar la finca!` |
| **`BOOKING_EXPIRED`** | Turista / Agencia | Email | Async Worker | **Asunto:** `Tu sesion de reserva expiro `<br>**Body:** `Vencio tu tiempo de pago. Inicia de nuevo si aun deseas reservar.` |
| **`BOOKING_CANCELLED`** | Turista / Agencia | Email | Async Worker | **Asunto:** `Tu reserva en [Property.Name] fue cancelada`<br>**Body:** `Tu reserva fue cancelada. Reembolso procesado en Wompi (si aplica).` |
| **`BOOKING_CANCELLED`** | Finquero (OWNER_API) | WhatsApp API | Async Worker | **Plantilla WA:** `La reserva [Booking.ID] fue cancelada. Las fechas han sido liberadas en tu calendario.` |
| **`BOOKING_COMPLETED`** | Turista / Agencia | Email | Async Worker (24h) | **Asunto:** ` Como fue tu estadia en [Property.Name]? `<br>**Body:** `Dejanos una resena: [Review.Link]` |
| **`BOOKING_COMPLETED`** | Finquero (OWNER_API) | Email | Async Worker | **Asunto:** `Reserva [Booking.ID] completada`<br>**Body:** `El pago sera desembolsado pronto a tu cuenta bancaria registrada.` |
| **`PAYOUT_SUCCESS`** | Finquero (OWNER_API) | Push + Email | Async Worker | **Asunto:** ` Pago enviado! `<br>**Body:** `Hemos enviado $[Payout.Amount] a tu cuenta [Host.BankAccount] por la reserva [Booking.ID].` |
| **`PAYOUT_FAILED`** | Finquero (OWNER_API) | WhatsApp API | Inmediato | **Plantilla WA:** ` Fallo en el desembolso de la reserva [Booking.ID]. Por favor verifica tu cuenta bancaria terminada en [Host.BankAccountEnd] en el panel de control.` |
| **`PROPERTY_PENDING_REVIEW`** | Admin | Email | Async Worker | **Asunto:** `Nueva Finca para Revision: [Property.Name]`<br>**Body:** `El anfitrion [Host.Name] ha enviado una nueva propiedad. Revisa las fotos y reglas.` |
| **`PROPERTY_PUBLISHED`** | Finquero (OWNER_API) | Push + Email | Async Worker | **Asunto:** ` Tu Finca esta en linea! `<br>**Body:** `Tu propiedad [Property.Name] ha sido aprobada y ya esta disponible en el marketplace.` |

---

## Reglas de Jerarquia de Canales

| Canal | Costo Aproximado | Restriccion de Uso | Garantia de Entrega |
|---|---|---|---|
| **Email** | ~$0.001/msg | Canal por defecto | Entrega en segundos, lectura no garantizada |
| **WhatsApp Business API** | ~$0.01/msg (Meta) | Exclusivo B2B Finqueros (NFR Fase 3) | Aprobacion en doble via (Mensajes HSM), Lectura alta |

---

## Implicacion de Fase

- Los canales estandarizados con variables dinamicas formales (`[Variable.Campo]`) eliminan la ambig edad de redaccion en el codigo base.
- Los `Async Worker` deben implementarse como colas de mensajes (SQS/Redis) para no bloquear el flujo transaccional.
- Se integra WhatsApp Business API como canal B2B primario (aprobaciones y alertas), reemplazando SMS/Push (prohibidos por NFRs de Fase 3).
- **Proceder a D11:** Matriz de Autorizacion y Seguridad.

