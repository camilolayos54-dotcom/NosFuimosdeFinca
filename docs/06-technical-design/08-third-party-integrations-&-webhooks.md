# Deliverable 8 (D8): Third-Party Integrations & Webhooks

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Billing
**Estado:** Approved

*Backlink a Fase 4 y Fase 6 (D3):* Este entregable documenta el mecanismo fÃ­sico de interacciÃ³n con las pasarelas externas que mueven el dinero, consumiendo los secretos que marcamos como pendientes en el D3 (Configuration & Secrets).

---

## 2. Llamadas Salientes API/SDK (Outbound)

Dado que la pasarela **Wompi** no cuenta con un SDK oficial moderno para Node.js, las integraciones se harÃ¡n mediante llamadas REST estÃ¡ndar con control de errores explÃ­cito.

### 2.1 Wompi: TokenizaciÃ³n y Cobros
- **Mecanismo:** Llamada REST `POST /v1/transactions` (Client-side vÃ­a Widget o Server-side).
- **AutenticaciÃ³n:** Requiere `WOMPI_PUBLISHABLE_KEY` (Cliente) o `WOMPI_PRIVATE_KEY` (Servidor).
- **Naturaleza:** SÃ­ncrona y crÃ­tica. Determina si el flujo del `Booking Engine` avanza.
- **PolÃ­tica de Reintentos (Server-side):**
  - **MÃ¡ximo Reintentos:** 2
  - **Estrategia Backoff:** Exponencial (1000ms, 3000ms).
  - **CondiciÃ³n:** Solo reintentar ante Timeouts (`ECONNABORTED`) o Errores de Red de Wompi (`500`, `502`, `503`). 
  - **ExcepciÃ³n Estricta:** Errores `4xx` (Tarjetas declinadas, sin fondos, bloqueadas por fraude) **NO se reintentan**, fallan instantÃ¡neamente y se devuelve el error al frontend.

### 2.2 Wompi: Reembolsos (Refunds)
- **Mecanismo:** Llamada REST `POST /v1/transactions/{id}/refunds`.
- **AutenticaciÃ³n:** Requiere `WOMPI_PRIVATE_KEY` estricto (Server-only).
- **Naturaleza:** AsÃ­ncrona (Background Job). No bloquea al Finquero que estÃ¡ cancelando la reserva desde la UI.
- **PolÃ­tica de Reintentos:** 3 reintentos con intervalo amplio (10s, 30s, 60s) en caso de fallos de la pasarela.

---

## 3. Definiciones de Webhooks Entrantes (Inbound)

Los Webhooks de Wompi informan al sistema de forma asÃ­ncrona cuando Nequi, PSE o las redes de tarjetas finalizan el proceso (ej. un pago en efectivo tarda minutos en ser confirmado).

### 3.1 Webhook: `transaction.updated`

**Endpoint de Captura:** `POST /api/webhooks/wompi`

> [!WARNING]
> Este endpoint es la puerta de entrada a la manipulaciÃ³n financiera del sistema. Las validaciones criptogrÃ¡ficas son obligatorias para evitar inyecciones (fraude).

#### 1. ValidaciÃ³n de Firma (Seguridad)
No confiaremos en el cuerpo del webhook si no estÃ¡ firmado. 
- Extraer `data.transaction.id`, `data.transaction.status`, `data.transaction.amount_in_cents`, el `timestamp` y combinarlos con la clave privada `WOMPI_WEBHOOK_SECRET`.
- Ejecutar cÃ¡lculo local en SHA-256.
- Comparar con la clave proveÃ­da en `signature.checksum`. Si el match es fallido, devolver **HTTP 403 Forbidden**.

#### 2. Regla de Idempotencia
Wompi advierte que la red puede demorarse y enviar el mismo evento dos veces.
- Buscar en base de datos la reserva (`bookings`) o pago (`payments`) usando `data.transaction.reference`.
- **VerificaciÃ³n:** Si la tabla ya indica que este pago estÃ¡ `APPROVED` y el webhook entrante dice `APPROVED`, abortar el proceso y retornar **HTTP 200 OK** para que Wompi deje de insistir, pero **no ejecutar** los gatillos secundarios (ej. no enviar el correo electrÃ³nico dos veces).

#### 3. Payload EstÃ¡ndar Esperado
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
- **Phase 6 â€” D10 (Async Workers & Job Scheduling):** UsarÃ¡ la definiciÃ³n del Reembolso (Refund) para programar las colas asÃ­ncronas de trabajo.
- **Phase 7 â€” D8 (External Integrations Implementation):** El programador escribirÃ¡ el controlador `wompi.controller.ts` asegurÃ¡ndose de transcribir la lÃ³gica criptogrÃ¡fica de SHA-256 para los Webhooks.

