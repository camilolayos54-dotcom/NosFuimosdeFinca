# Deliverable 7 (D7): System Sequence Diagrams

**Proyecto:** Nosfuimos de Finca
**Fase:** 4 — System Modeling
**Estado:** Aprobado

Este documento sirve como índice central para los diagramas de secuencia del sistema, organizados por módulos críticos.

## Módulos Modelados

- [[example_outputs/MOD-BOOKING]]: Proceso transaccional de reserva y pago.
- [[example_outputs/MOD-AUTH]]: Proceso de Autenticación y Generación de JWT.
- [[example_outputs/MOD-HOSTING]]: Proceso de Creación de Propiedad y subida de imágenes a S3.
- [[example_outputs/MOD-CALENDAR]]: Proceso de Sincronización y Bloqueo de Calendarios.

---
### Implicaciones de Fase Generales
- Las integraciones con pasarelas de pago y servicios en la nube (S3) se confirmaron como procesos asíncronos en su mayoría o con manejo riguroso de fallos.
- **Proceder a D8:** State Machine & Activity Diagrams.
