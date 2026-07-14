# Deliverable 8 (D8): Third-Party Integrations & Webhooks

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Modulo:** MOD-Billing
**Estado:** Approved

*Backlink a Fase 4 y Fase 6 (D3):* Este entregable documenta el mecanismo fisico de interaccion con las pasarelas externas que mueven el dinero, consumiendo los secretos que marcamos como pendientes en el D3 (Configuration & Secrets).

---

## 2. Llamadas Salientes API/SDK (Outbound)

Dado que la pasarela **Wompi** no cuenta con un SDK oficial moderno para Node.js, las integraciones se haran mediante llamadas REST estandar con control de errores explicito.

### 2.1 Wompi: Tokenizacion y Cobros
- **Mecanismo:** Llamada REST `POST /v1/transactions` (Client-side via Widget o Server-side).
- **Autenticacion:** Requiere `WOMPI_PUBLISHABLE_KEY` (Cliente) o `WOMPI_PRIVATE_KEY` (Servidor).
- **Naturaleza:** Sincrona y critica. Determina si el flujo del `Booking Engine` avanza.
- **Politica de Reintentos (Server-side):**
  - **Maximo Reintentos:** 2
  - **Estrategia Backoff:** Exponencial (1000ms, 3000ms).
  - **Condicion:** Solo reintentar ante Timeouts (`ECONNABORTED`) o Errores de Red de Wompi (`500`, `502`, `503`). 
  - **Excepcion Estricta:** Errores `4xx` (Tarjetas declinadas, sin fondos, bloqueadas por fraude) **NO se reintentan**, fallan instantaneamente y se devuelve el error al frontend.

### 2.2 Wompi: Reembolsos (Refunds)
- **Mecanismo:** Llamada REST `POST /v1/transactions/{id}/refunds`.
- **Autenticacion:** Requiere `WOMPI_PRIVATE_KEY` estricto (Server-only).
- **Naturaleza:** Asincrona (Background Job). No bloquea al Finquero que esta cancelando la reserva desde la UI.
- **Politica de Reintentos:** 3 reintentos con intervalo amplio (10s, 30s, 60s) en caso de fallos de la pasarela.

---

## 3. Definiciones de Webhooks Entrantes (Inbound)

Los Webhooks de Wompi informan al sistema de forma asincrona cuando Nequi, PSE o las redes de tarjetas finalizan el proceso (ej. un pago en efectivo tarda minutos en ser confirmado).

### 3.1 Webhook: `transaction.updated`

**Endpoint de Captura:** `POST /api/webhooks/wompi`

> [!WARNING]
> Este endpoint es la puerta de entrada a la manipulacion financiera del sistema. Las validaciones criptograficas son obligatorias para evitar inyecciones (fraude).

#### 1. Validacion de Firma (Seguridad)
No confiaremos en el cuerpo del webhook si no esta firmado. 
- Extraer `data.transaction.id`, `data.transaction.status`, `data.transaction.amount_in_cents`, el `timestamp` y combinarlos con la clave privada `WOMPI_WEBHOOK_SECRET`.
- Ejecutar calculo local en SHA-256.
- Comparar con la clave proveida en `signature.checksum`. Si el match es fallido, devolver **HTTP 403 Forbidden**.

#### 2. Regla de Idempotencia
Wompi advierte que la red puede demorarse y enviar el mismo evento dos veces.
- Buscar en base de datos la reserva (`bookings`) o pago (`payments`) usando `data.transaction.reference`.
- **Verificacion:** Si la tabla ya indica que este pago esta `APPROVED` y el webhook entrante dice `APPROVED`, abortar el proceso y retornar **HTTP 200 OK** para que Wompi deje de insistir, pero **no ejecutar** los gatillos secundarios (ej. no enviar el correo electronico dos veces).

#### 3. Payload Estandar Esperado
```json
{
  "event": "transaction.updated",
  "data": {
    "transaction": {
      "id": "123-abc",
      "amount_in_cents": 15000000,
      "reference": "booking-uuid",
      "customer_email": "turista@example.com",
      "status": "APPROVED",
      "payment_method_type": "NEQUI"
    }
  },
  "environment": "test",
  "signature": {
    "properties": [
      "transaction.id",
      "transaction.status",
      "transaction.amount_in_cents"
    ],
    "checksum": "c2b...hash...1f8"
  },
  "timestamp": 1614092400
}
```

---

## 4. Downstream Consumers
- **Phase 6 â€” D10 (Async Workers & Job Scheduling):** Usara la definicion del Reembolso (Refund) para programar las colas asincronas de trabajo.
- **Phase 7 â€” D8 (External Integrations Implementation):** El programador escribira el controlador `wompi.controller.ts` asegurandose de transcribir la logica criptografica de SHA-256 para los Webhooks.

