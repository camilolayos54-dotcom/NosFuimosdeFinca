### 1. Cabecera de Metadatos

```markdown
### Resumen de la Fase 0

**Proyecto:** Nos Fuimos de Finca
**Fase:** 0 — Reconocimiento del Problema
**Entregable:** 11 of 11
**Estado:** Aprobado
```

### 2. Problema
Propietarios de fincas turísticas y turistas rurales en Colombia coordinan la disponibilidad, tarifas y la confirmación de fechas de alquiler mediante herramientas de uso general (WhatsApp, Facebook, llamadas) y registros manuales descentralizados (libretas físicas o Excel aislado). Cuando una transacción ocurre, esta ausencia de una estructura de bloqueo concurrente (atomicidad) causa fallas críticas en la coordinación: los propietarios aprueban frecuentemente el mismo rango de fechas a distintos turistas que depositan sus anticipos casi simultáneamente. Cuando el servicio finalmente debe prestarse, esto se traduce en reservas cruzadas ineludibles, forzando cancelaciones de último minuto. Como consecuencia, el mercado sufre un profundo quiebre de confianza: los turistas asumen el riesgo de fraude o pérdida irremediable de sus vacaciones, mientras que los propietarios sufren estrés operativo severo, pérdida de capital por devoluciones y daño de reputación al intentar conciliar abonos cruzados sin un registro central de verdad.

### 3. Evidencia Clave
|ID|Hallazgo Clave|Confirma|
|---|---|---|
|E-01|Anotó una reserva en una libreta física y otra confirmación en su teléfono para las mismas fechas. Dos familias llegaron a la vez. Reembolsó el 100% más compensación por daños.|recurrencia + causalidad estructural + efecto derivado|
|E-02|Alto volumen de turistas denunciando que pagaron su anticipo (50%) pero al llegar la finca estaba ocupada o el dueño no encontraba el comprobante en su WhatsApp.|recurrencia + efecto derivado|
|E-04|El propietario revisó tres libretas diferentes y audios de WhatsApp para confirmar si una fecha de diciembre estaba libre. Tomó 4 horas responder, perdiendo 2 clientes.|causalidad estructural|

### 4. Brecha
Existe un vacío crítico ("whitespace") evidente en el mercado de tecnología operativa para alquileres de corta estancia rural. Las soluciones manuales acomodan los flujos de caja locales, pero colapsan inevitablemente bajo concurrencia, produciendo reservas cruzadas y pérdida de depósitos. Simultáneamente, las soluciones globales garantizan el control de concurrencia atómico, pero imponen un ahogo financiero y políticas de retención de pagos draconianas. El mercado exige un sistema intermedio (un "Ledger" o Libro Mayor) que aplique el bloqueo transaccional de disponibilidad de una OTA, pero que respete el flujo de abonos directos e inmediatos sin retención prolongada ni comisiones prohibitivas.

### 5. Clasificación e Impacto
|Campo|Valor|Fuente|
|---|---|---|
|Tipo primario|eficiencia|D4|
|Tipo secundario|confianza|D4|
|Recurrencia|primera observación|D4|
|Criterio cumplido|Criterio C|D5|
|Confianza|Alta|D5|

### 6. Objetivo y Métricas de Éxito
Propietarios de fincas turísticas y turistas rurales en Colombia pueden coordinar la disponibilidad, tarifas y la confirmación de fechas de alquiler bajo alta demanda concurrente, sin incurrir en reservas cruzadas ineludibles ni causar pérdida de anticipos o vacaciones.

**Métricas de Éxito** _(si están disponibles)_
|Objetivo|Métrica|Fuente|
|---|---|---|
|Propietarios de fincas validan disponibilidad y cruces de fechas de manera inmediata (reducción de latencia logística).|Menos de 5 segundos de respuesta|D2 row E-04|
|Turistas rurales formalizan alquileres eliminando escenarios de denuncias de fraude informal.|0% de pérdida documentada por concurrencia|D2 row E-02|

### 7. Actores Clave
|Nombre / Rol|Interés|Tipo de Influencia|Bloqueador|
|---|---|---|---|
|Patrocinador del Proyecto|Lanzar un MVP viable que recupere comisiones en un submercado altamente atomizado.|Patrocinador|S|
|Propietario de Finca (Carlos M. / Oferta)|Maximizar ocupación sin sufrir estrés logístico, retener control inmediato sobre su flujo de caja (abonos).|Usuario|S|
|Pasarelas de Pago (Wompi, PayU)|Recaudar comisión transaccional, cumplir normativas fiscales nacionales y antilavado (KYC/AML).|Bloqueador|S|

### 8. Excepciones Activas
|Constraint|Source|Scope Implication|
|---|---|---|
|Dependencia asíncrona bancaria|D8 disqualifier 1|Obliga a implementar arquitecturas de reversión automática si un pago falla tras X minutos, limitando la rigidez del modelo de datos.|
|Riesgo de Adopción (Brecha Digital)|D8 disqualifier 2|Impone una directiva inquebrantable de "Mobile-First" y fricción cero para la interfaz del Propietario.|

### 9. Decisión y Autorización
Proceder a la Fase 1

El análisis confirma un colapso logístico y sistémico verificable en la coordinación asíncrona de alquileres de propiedades rurales, resultando consistentemente en reservas cruzadas y pérdida financiera (E-01, E-03 documentados en D2). Este fallo estructural ha sido clasificado como una ineficiencia logística (D4) que escala a fallos de confianza en el mercado. La evaluación de impacto superó el umbral crítico por pérdida financiera (D5 - Criterion C). Además, la evaluación de riesgos confirma que se trata de un límite físico de la coordinación manual asíncrona y no de una decisión política, estableciendo que la intervención técnica (Libro Mayor) es abordable, justificando plenamente el avance del proyecto sin impedimentos bloqueantes inmediatos (D8).

**Autorización:** Patrocinador del Proyecto — 2026-06-29
