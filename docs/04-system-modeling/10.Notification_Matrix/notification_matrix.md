# Entregable 10 (D10): Matriz de Notificaciones y Eventos

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**MÃ³dulo:** MOD-BOOKING / MOD-NOT
**Estado:** Aprobado

---

## Matriz Completa de Notificaciones

*Backlink a Fase 3:* Los eventos disparadores provienen de los diagramas de Use Cases y las restricciones de canal (WhatsApp en lugar de SMS) respetan los NFRs de la Fase 3 (`[[PHASE_3_REQUIREMENTS_ENGINEERING/6.Non-Functional_Requirements]]`).

| Evento | Destinatario | Canal | Estrategia de Disparo | Asunto / TÃ­tulo / UX Copy |
|:---|:---|:---|:---|:---|
| **`BOOKING_APPROVAL_REQUEST`** | Finquero (OWNER_API) | WhatsApp API | Async Worker | **Plantilla WA:** `Â¡Hola [Host.Name]! Tienes una solicitud de reserva para [Property.Name] del [Booking.CheckInDate] al [Booking.CheckOutDate]. Responde SI para aprobar o NO para rechazar en los prÃ³ximos 90 minutos.` |
| **`BOOKING_CONFIRMED`** | Turista / Agencia | Email | Async Worker | **Asunto:** `Â¡Confirmado! Tu reserva en [Property.Name] estÃ¡ lista ðŸŒ´`<br>**Body:** `Hola [Guest.Name], Tu reserva ha sido confirmada. CÃ³digo: [Booking.ID].` |
| **`BOOKING_CONFIRMED`** | Finquero (OWNER_API) | WhatsApp API + Email | Async Worker | **Plantilla WA:** `Aprobaste la reserva [Booking.ID]. El pago de $[Payment.Amount] ha sido asegurado. Â¡A preparar la finca!` |
| **`BOOKING_EXPIRED`** | Turista / Agencia | Email | Async Worker | **Asunto:** `Tu sesiÃ³n de reserva expirÃ³ â³`<br>**Body:** `VenciÃ³ tu tiempo de pago. Inicia de nuevo si aÃºn deseas reservar.` |
| **`BOOKING_CANCELLED`** | Turista / Agencia | Email | Async Worker | **Asunto:** `Tu reserva en [Property.Name] fue cancelada`<br>**Body:** `Tu reserva fue cancelada. Reembolso procesado en Wompi (si aplica).` |
| **`BOOKING_CANCELLED`** | Finquero (OWNER_API) | WhatsApp API | Async Worker | **Plantilla WA:** `La reserva [Booking.ID] fue cancelada. Las fechas han sido liberadas en tu calendario.` |
| **`BOOKING_COMPLETED`** | Turista / Agencia | Email | Async Worker (24h) | **Asunto:** `Â¿CÃ³mo fue tu estadÃ­a en [Property.Name]? ðŸŒŸ`<br>**Body:** `DÃ©janos una reseÃ±a: [Review.Link]` |
| **`BOOKING_COMPLETED`** | Finquero (OWNER_API) | Email | Async Worker | **Asunto:** `Reserva [Booking.ID] completada`<br>**Body:** `El pago serÃ¡ desembolsado pronto a tu cuenta bancaria registrada.` |
| **`PAYOUT_SUCCESS`** | Finquero (OWNER_API) | Push + Email | Async Worker | **Asunto:** `Â¡Pago enviado! ðŸ’¸`<br>**Body:** `Hemos enviado $[Payout.Amount] a tu cuenta [Host.BankAccount] por la reserva [Booking.ID].` |
| **`PAYOUT_FAILED`** | Finquero (OWNER_API) | WhatsApp API | Inmediato | **Plantilla WA:** `ðŸš¨ Fallo en el desembolso de la reserva [Booking.ID]. Por favor verifica tu cuenta bancaria terminada en [Host.BankAccountEnd] en el panel de control.` |
| **`PROPERTY_PENDING_REVIEW`** | Admin | Email | Async Worker | **Asunto:** `Nueva Finca para RevisiÃ³n: [Property.Name]`<br>**Body:** `El anfitriÃ³n [Host.Name] ha enviado una nueva propiedad. Revisa las fotos y reglas.` |
| **`PROPERTY_PUBLISHED`** | Finquero (OWNER_API) | Push + Email | Async Worker | **Asunto:** `Â¡Tu Finca estÃ¡ en lÃ­nea! ðŸŽ‰`<br>**Body:** `Tu propiedad [Property.Name] ha sido aprobada y ya estÃ¡ disponible en el marketplace.` |

---

## Reglas de JerarquÃ­a de Canales

| Canal | Costo Aproximado | RestricciÃ³n de Uso | GarantÃ­a de Entrega |
|---|---|---|---|
| **Email** | ~$0.001/msg | Canal por defecto | Entrega en segundos, lectura no garantizada |
| **WhatsApp Business API** | ~$0.01/msg (Meta) | Exclusivo B2B Finqueros (NFR Fase 3) | AprobaciÃ³n en doble vÃ­a (Mensajes HSM), Lectura alta |

---

## ImplicaciÃ³n de Fase

- Los canales estandarizados con variables dinÃ¡micas formales (`[Variable.Campo]`) eliminan la ambigÃ¼edad de redacciÃ³n en el cÃ³digo base.
- Los `Async Worker` deben implementarse como colas de mensajes (SQS/Redis) para no bloquear el flujo transaccional.
- Se integra WhatsApp Business API como canal B2B primario (aprobaciones y alertas), reemplazando SMS/Push (prohibidos por NFRs de Fase 3).
- **Proceder a D11:** Matriz de AutorizaciÃ³n y Seguridad.

