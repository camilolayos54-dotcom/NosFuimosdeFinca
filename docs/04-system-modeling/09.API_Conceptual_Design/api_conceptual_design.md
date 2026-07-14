 # Entregable 9 (D9): Diseno Conceptual de API MOD-BOOKING

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 Modelado del Sistema
**Modulo:** MOD-BOOKING
**Estado:** Aprobado

---

## 1. Catalogo de Endpoints

*Backlink a Fase 3:* El diseno de estos endpoints satisface los contratos de datos requeridos por los Use Cases (`[[PHASE_3_REQUIREMENTS_ENGINEERING/3.Use_Case_Diagram.md]]`) y las restricciones de rendimiento de los NFRs.

### `POST /api/v1/bookings` Crear Reserva
*Inicia el flujo transaccional de reserva y dispara la autorizacion de cobro a Wompi.*

**Autenticacion requerida:** `Bearer Token (rol: TOURIST, AGENCY_USER)`

**Cuerpo de solicitud:**
```json
{
  "property_id": "texto (requerido)",
  "check_in_date": "fecha ISO-8601 (requerido)",
  "check_out_date": "fecha ISO-8601 (requerido)",
  "guest_count": "numero (requerido)",
  "wompi_token": "texto (requerido)",
  "promo_code": "texto (opcional)",
  "agency_client_name": "texto (opcional - solo AGENCY_USER)"
}
```

**Respuesta exitosa HTTP 201 Created:**
```json
{
  "data": {
    "booking_id": "texto",
    "status": "texto (= CONFIRMED)",
    "total_price": "numero (centavos)",
    "check_in_date": "fecha ISO-8601",
    "check_out_date": "fecha ISO-8601",
    "created_at": "fecha ISO-8601"
  }
}
```

**Errores (Caminos Tristes):**
**Errores (Caminos Tristes):**


| Codigo HTTP | Codigo Constante | Causa |
| ------------------ | ------------------- | ------------------------------------------- |
| `409 Conflict` | `DATES_UNAVAILABLE` | Fechas ocupadas por otra reserva simultanea |
| `401 Unauthorized` | `UNAUTHORIZED` | JWT (gestionado por Spring Security) invalido o ausente |
| `403 Forbidden` | `FORBIDDEN` | Rol no autorizado para reservar |

---

### `POST /api/v1/webhooks/wompi` Procesar Eventos de Wompi
*Recibe notificaciones asincronas de Wompi (transacciones aprobadas o declinadas).*

**Autenticacion requerida:** `Wompi HMAC-SHA256 Signature en Header`

**Cuerpo de solicitud (Ejemplo Wompi Event):**
```json
{
  "event": "transaction.updated",
  "data": {
    "transaction": {
      "id": "texto",
      "status": "APPROVED",
      "amount_in_cents": 10000,
      "reference": "booking_123"
    }
  },
  "signature": {
    "checksum": "hex_string"
  }
}
```

**Respuesta exitosa HTTP 200 OK:** `Acknowledge sin body.`

### `GET /api/v1/bookings` Listar Reservas
*Devuelve el historial de reservas. Un `TOURIST` ve las suyas. Un `OWNER_API` ve las recibidas en sus fincas. Una `AGENCY_USER` ve las de sus clientes.*

**Autenticacion requerida:** `Bearer Token (TOURIST, AGENCY_USER, OWNER_API)`

**Query Parameters:**
- `?page=1&limit=20` Paginacion obligatoria
- `?status=CONFIRMED` Filtrar por estado (opcional)
- `?sort=-created_at` Ordenamiento (default: mas reciente primero)

**Respuesta exitosa HTTP 200 OK:**
```json
{
  "data": [
    {
      "booking_id": "texto",
      "property_name": "texto",
      "check_in_date": "fecha ISO-8601",
      "check_out_date": "fecha ISO-8601",
      "status": "texto",
      "total_price": "numero (centavos)"
    }
  ],
  "meta": {
    "current_page": "numero",
    "total_pages": "numero",
    "total_items": "numero"
  }
}
```

---

### `PATCH /api/v1/bookings/:id` Cancelar/Aprobar Reserva
*Permite a Turistas/Agencias cancelar su reserva. Permite al Finquero APROBAR o RECHAZAR la reserva pendiente.*

**Autenticacion requerida:** `Bearer Token (TOURIST, AGENCY_USER, OWNER_API)`

**Cuerpo de solicitud:**
```json
{
  "status": "texto (requerido valor: 'CANCELLED')"
}
```

**Respuesta exitosa HTTP 200 OK:**
```json
{
  "data": {
    "booking_id": "texto",
    "status": "texto (= CANCELLED)",
    "refund_amount": "numero (centavos, si aplica reembolso)",
    "cancelled_at": "fecha ISO-8601"
  }
}
```

**Errores:**
| Codigo HTTP | Codigo Constante | Causa |
|---|---|---|
| `403 Forbidden` | `FORBIDDEN` | Intento de cancelar la reserva de otro usuario (IDOR) |
| `409 Conflict` | `CANCELLATION_WINDOW_EXPIRED` | Fuera de la ventana de cancelacion (< 48h antes de check-in) |

---

### `GET /api/v1/properties` Buscar Fincas
*Devuelve el catalogo paginado de fincas con filtros opcionales.*

**Autenticacion requerida:** Publica (sin JWT)

**Query Parameters:**
`?page=1&limit=20&location=quindio&check_in=2026-12-24&check_out=2026-12-31&max_guests=4&amenities=pool,wifi&sort=price_asc`

**Respuesta exitosa HTTP 200 OK:**
```json
{
  "data": [
    {
      "property_id": "texto",
      "name": "texto",
      "location_address": "texto",
      "price_per_night": "numero (centavos)",
      "cleaning_fee": "numero (centavos)",
      "max_guests": "numero",
      "bedrooms_count": "numero",
      "bathrooms_count": "numero",
      "beds_count": "numero",
      "cover_image_url": "texto",
      "average_rating": "numero",
      "amenities": ["texto"]
    }
  ],
  "meta": {
    "current_page": "numero",
    "total_pages": "numero",
    "total_items": "numero"
  }
}
```

---

### `POST /api/v1/wishlists` Guardar Favorito
*Permite a un turista guardar una finca en su lista de deseos.*

**Autenticacion requerida:** `Bearer Token (TOURIST)`

**Cuerpo de solicitud:**
```json
{
  "property_id": "texto (requerido)"
}
```

**Respuesta exitosa HTTP 201 Created:** `Acknowledge sin body.`

---

### `POST /api/v1/coupons/validate` Validar Cupon
*Verifica si un cupon es valido para una fecha y usuario antes de aplicar el descuento.*

**Autenticacion requerida:** `Bearer Token (TOURIST, AGENCY_USER)`

**Cuerpo de solicitud:**
```json
{
  "code": "texto (requerido)",
  "property_id": "texto (requerido)"
}
```

**Respuesta exitosa HTTP 200 OK:**
```json
{
  "data": {
    "valid": true,
    "discount_percentage": "numero (opcional)",
    "max_discount_amount": "numero (opcional, en centavos)"
  }
}
```

---

### `GET /api/v1/payouts` Consultar Desembolsos
*El finquero visualiza el historial de dinero girado a su cuenta.*

**Autenticacion requerida:** `Bearer Token (OWNER_API)`

**Respuesta exitosa HTTP 200 OK:**
```json
{
  "data": [
    {
      "payout_id": "texto",
      "booking_id": "texto",
      "amount": "numero (centavos)",
      "currency": "texto",
      "status": "texto (PENDING, PROCESSING, PAID, FAILED)",
      "transaction_date": "fecha ISO-8601"
    }
  ]
}
```

---

## 2. Estandar de Errores Universal

Todo error del sistema devuelve la misma estructura, sin excepciones:

```json
{
  "error": {
    "code": "C DIGO_CONSTANTE_STRING",
    "message": "Mensaje descriptivo en espanol.",
    "details": null
  }
}
```

| Codigo HTTP | Codigo Constante | Descripcion |
|---|---|---|
| `409` | `DATES_UNAVAILABLE` | Conflicto de fechas en reserva |
| `402` | `PAYMENT_DECLINED` | Pago rechazado por pasarela |
| `401` | `UNAUTHORIZED` | JWT ausente o expirado |
| `403` | `FORBIDDEN` | Acceso a recurso ajeno (IDOR) |
| `404` | `RESOURCE_NOT_FOUND` | Recurso no existe |
| `500` | `INTERNAL_SERVER_ERROR` | Error interno del servidor |

---

## Implicacion de Fase

- El contrato de comunicacion esta sellado. El equipo de Frontend puede construir Mock Servers con estas estructuras JSON mientras el Backend implementa la logica real.
- Los `code` constantes del objeto de error son el contrato para la localizacion i18n (D14): el Frontend usara `t('errors.DATES_UNAVAILABLE')` para mostrar el mensaje en el idioma del usuario.
- **Proceder a D10:** Matriz de Notificaciones y Eventos.

