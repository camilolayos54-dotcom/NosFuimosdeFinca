 # Entregable 7 (D7): Diagramas de Secuencia del Sistema

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Estado:** Aprobado

Este documento es el indice central de los diagramas de secuencia del sistema, organizados por modulos criticos. Cada modulo tiene un subarchivo dedicado en la carpeta `example_outputs/`.

---

## Modulos Modelados

*Backlink a Fase 3:* Estos diagramas de secuencia se basan en los flujos transaccionales definidos en los requerimientos de `[[PHASE_3_REQUIREMENTS_ENGINEERING/7.Module_Specification.md]]` y el mapeo de `[[PHASE_4_SYSTEM_MODELING/2.User_Flows_Task_Flows/example_output_d2_user_flows.md]]`.

- `[[example_outputs/MOD-BOOKING]]`: Proceso transaccional completo de reserva y pago (incluyendo manejo de fechas ocupadas y pagos declinados).
- `[[example_outputs/MOD-AUTH]]`: Proceso de autenticacion, generacion de JWT y renovacion mediante Refresh Token.
- `[[example_outputs/MOD-HOSTING]]`: Proceso de creacion de propiedad y subida asincrona de imagenes al Object Storage.
- `[[example_outputs/MOD-CALENDAR]]`: Proceso de bloqueo de calendario por el Finquero y deteccion de conflictos de disponibilidad.

---

## Decisiones Arquitectonicas Transversales

| Decision | Justificacion |
|---|---|
| **Email y Push Asincronos** | Las notificaciones se delegan a un Background Worker post-confirmacion para no bloquear la respuesta al Frontend (latencia < 500ms). |
| **Pasarela de pago Sincrona** | La confirmacion del pago debe preceder obligatoriamente a la creacion de la reserva. No se puede crear reserva sin pago confirmado. |
| **Validacion de disponibilidad Sincrona** | Se valida antes de llamar a la pasarela para no cobrar en fechas ya ocupadas (race condition prevention). |
| **Frontend Backend DB** | El Frontend nunca accede directamente a la base de datos ni a APIs de pago. Toda comunicacion pasa por el Backend API. |

---

## Implicaciones de Fase Generales

- ** D8 (State Machine Diagrams):** Los triggers identificados en D7 (Webhook de pago exitoso, timeout de 15 minutos sin pago) se convierten en los disparadores formales de las transiciones de estado de la entidad `bookings`.
- ** D9 (API Conceptual Design):** Las interacciones sincronas Cliente Backend de D7 definen los endpoints REST que deben existir (`POST /api/v1/bookings`, `GET /api/v1/properties/availability`).
- ** D11 (Authorization & Security Matrix):** Las fronteras de lifeline de D7 determinan que endpoints requieren JWT obligatorio (cualquier endpoint que modifique datos del usuario).
- **Proceder a D8:** Diagramas de Maquinas de Estado.

