# Entregable 7 (D7): Diagramas de Secuencia del Sistema

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**Estado:** Aprobado

Este documento es el Ã­ndice central de los diagramas de secuencia del sistema, organizados por mÃ³dulos crÃ­ticos. Cada mÃ³dulo tiene un subarchivo dedicado en la carpeta `example_outputs/`.

---

## MÃ³dulos Modelados

*Backlink a Fase 3:* Estos diagramas de secuencia se basan en los flujos transaccionales definidos en los requerimientos de `[[PHASE_3_REQUIREMENTS_ENGINEERING/7.Module_Specification.md]]` y el mapeo de `[[PHASE_4_SYSTEM_MODELING/2.User_Flows_Task_Flows/example_output_d2_user_flows.md]]`.

- `[[example_outputs/MOD-BOOKING]]`: Proceso transaccional completo de reserva y pago (incluyendo manejo de fechas ocupadas y pagos declinados).
- `[[example_outputs/MOD-AUTH]]`: Proceso de autenticaciÃ³n, generaciÃ³n de JWT y renovaciÃ³n mediante Refresh Token.
- `[[example_outputs/MOD-HOSTING]]`: Proceso de creaciÃ³n de propiedad y subida asÃ­ncrona de imÃ¡genes al Object Storage.
- `[[example_outputs/MOD-CALENDAR]]`: Proceso de bloqueo de calendario por el Finquero y detecciÃ³n de conflictos de disponibilidad.

---

## Decisiones ArquitectÃ³nicas Transversales

| DecisiÃ³n | JustificaciÃ³n |
|---|---|
| **Email y Push â†’ AsÃ­ncronos** | Las notificaciones se delegan a un Background Worker post-confirmaciÃ³n para no bloquear la respuesta al Frontend (latencia < 500ms). |
| **Pasarela de pago â†’ SÃ­ncrona** | La confirmaciÃ³n del pago debe preceder obligatoriamente a la creaciÃ³n de la reserva. No se puede crear reserva sin pago confirmado. |
| **ValidaciÃ³n de disponibilidad â†’ SÃ­ncrona** | Se valida antes de llamar a la pasarela para no cobrar en fechas ya ocupadas (race condition prevention). |
| **Frontend â†’ Backend â†’ DB** | El Frontend nunca accede directamente a la base de datos ni a APIs de pago. Toda comunicaciÃ³n pasa por el Backend API. |

---

## Implicaciones de Fase Generales

- **â†’ D8 (State Machine Diagrams):** Los triggers identificados en D7 (Webhook de pago exitoso, timeout de 15 minutos sin pago) se convierten en los disparadores formales de las transiciones de estado de la entidad `bookings`.
- **â†’ D9 (API Conceptual Design):** Las interacciones sÃ­ncronas Clienteâ†”Backend de D7 definen los endpoints REST que deben existir (`POST /api/v1/bookings`, `GET /api/v1/properties/availability`).
- **â†’ D11 (Authorization & Security Matrix):** Las fronteras de lifeline de D7 determinan quÃ© endpoints requieren JWT obligatorio (cualquier endpoint que modifique datos del usuario).
- **Proceder a D8:** Diagramas de MÃ¡quinas de Estado.

