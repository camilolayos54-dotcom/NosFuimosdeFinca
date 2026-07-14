# Entregable 9 (D9): DiseÃ±o Conceptual de API â€” MOD-BOOKING

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**MÃ³dulo:** MOD-BOOKING
**Estado:** Aprobado

---

## 1. CatÃ¡logo de Endpoints

*Backlink a Fase 3:* El diseÃ±o de estos endpoints satisface los contratos de datos requeridos por los Use Cases (`[[PHASE_3_REQUIREMENTS_ENGINEERING/3.Use_Case_Diagram.md]]`) y las restricciones de rendimiento de los NFRs.

### `POST /api/v1/bookings` â€” Crear Reserva
*Inicia el flujo transaccional de reserva y dispara la autorizaciÃ³n de cobro a Wompi.*

**AutenticaciÃ³n requerida:** `Bearer Token (rol: TOURIST, AGENCY_USER)`

**Cuerpo de solicitud:**
```json
{
  "property_id": "texto (requerido)",
  "check_in_date": "fecha ISO-8601 (requerido)",
  "check_out_date": "fecha ISO-8601 (requerido)",
  "guest_count": "nÃºmero (requerido)",
  "wompi_token": "texto (requerido)",
  "promo_code": "texto (opcional)",
  "agency_client_name": "texto (opcional - solo AGENCY_USER)"
}
```

**Respuesta exitosa â€” HTTP 201 Created:**
```json
{
  "data": {
    "booking_id": "texto",
    "status": "texto (= CONFIRMED)",
    "total_price": "nÃºmero (centavos)",
    "check_in_date": "fecha ISO-8601",
    "check_out_date": "fecha ISO-8601",
    "created_at": "fecha ISO-8601"
  }
}
```

**Errores (Caminos Tristes):**
**Errores (Caminos Tristes):**


| CÃ³digo HTTP        | CÃ³digo Constante    | Causa                                       |
| ------------------ | ------------------- | ------------------------------------------- |
| `409 Conflict`     | `DATES_UNAVAILABLE` | Fechas ocupadas por otra reserva simultÃ¡nea |
| `401 Unauthorized` | `UNAUTHORIZED`      | Supabase JWT invÃ¡lido o ausente             |
| `403 Forbidden`    | `FORBIDDEN`         | Rol no autorizado para reservar             |

---

### `POST /api/v1/webhooks/wompi` â€” Procesar Eventos de Wompi
*Recibe notificaciones asÃ­ncronas de Wompi (transacciones aprobadas o declinadas).*

**AutenticaciÃ³n requerida:** `Wompi HMAC-SHA256 Signature en Header`

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

**Respuesta exitosa â€” HTTP 200 OK:** `Acknowledge sin body.`

### `GET /api/v1/bookings` â€” Listar Reservas
*Devuelve el historial de reservas. Un `TOURIST` ve las suyas. Un `OWNER_API` ve las recibidas en sus fincas. Una `AGENCY_USER` ve las de sus clientes.*

**AutenticaciÃ³n requerida:** `Bearer Token (TOURIST, AGENCY_USER, OWNER_API)`

**Query Parameters:**
- `?page=1&limit=20` â€” PaginaciÃ³n obligatoria
- `?status=CONFIRMED` â€” Filtrar por estado (opcional)
- `?sort=-created_at` â€” Ordenamiento (default: mÃ¡s reciente primero)

**Respuesta exitosa â€” HTTP 200 OK:**
```json
{
  "data": [
    {
      "booking_id": "texto",
      "property_name": "texto",
      "check_in_date": "fecha ISO-8601",
      "check_out_date": "fecha ISO-8601",
      "status": "texto",
      "total_price": "nÃºmero (centavos)"
    }
  ],
  "meta": {
    "current_page": "nÃºmero",
    "total_pages": "nÃºmero",
    "total_items": "nÃºmero"
  }
}
```

---

### `PATCH /api/v1/bookings/:id` â€” Cancelar/Aprobar Reserva
*Permite a Turistas/Agencias cancelar su reserva. Permite al Finquero APROBAR o RECHAZAR la reserva pendiente.*

**AutenticaciÃ³n requerida:** `Bearer Token (TOURIST, AGENCY_USER, OWNER_API)`

**Cuerpo de solicitud:**
```json
{
  "status": "texto (requerido â€” valor: 'CANCELLED')"
}
```

**Respuesta exitosa â€” HTTP 200 OK:**
```json
{
  "data": {
    "booking_id": "texto",
    "status": "texto (= CANCELLED)",
    "refund_amount": "nÃºmero (centavos, si aplica reembolso)",
    "cancelled_at": "fecha ISO-8601"
  }
}
```

**Errores:**
| CÃ³digo HTTP | CÃ³digo Constante | Causa |
|---|---|---|
| `403 Forbidden` | `FORBIDDEN` | Intento de cancelar la reserva de otro usuario (IDOR) |
| `409 Conflict` | `CANCELLATION_WINDOW_EXPIRED` | Fuera de la ventana de cancelaciÃ³n (< 48h antes de check-in) |

---

### `GET /api/v1/properties` â€” Buscar Fincas
*Devuelve el catÃ¡logo paginado de fincas con filtros opcionales.*

**AutenticaciÃ³n requerida:** PÃºblica (sin JWT)

**Query Parameters:**
`?page=1&limit=20&location=quindio&check_in=2026-12-24&check_out=2026-12-31&max_guests=4&amenities=pool,wifi&sort=price_asc`

**Respuesta exitosa â€” HTTP 200 OK:**
```json
{
  "data": [
    {
      "property_id": "texto",
      "name": "texto",
      "location_address": "texto",
      "price_per_night": "nÃºmero (centavos)",
      "cleaning_fee": "nÃºmero (centavos)",
      "max_guests": "nÃºmero",
      "bedrooms_count": "nÃºmero",
      "bathrooms_count": "nÃºmero",
      "beds_count": "nÃºmero",
      "cover_image_url": "texto",
      "average_rating": "nÃºmero",
      "amenities": ["texto"]
    }
  ],
  "meta": {
    "current_page": "nÃºmero",
    "total_pages": "nÃºmero",
    "total_items": "nÃºmero"
  }
}
```

---

### `POST /api/v1/wishlists` â€” Guardar Favorito
*Permite a un turista guardar una finca en su lista de deseos.*

**AutenticaciÃ³n requerida:** `Bearer Token (TOURIST)`

**Cuerpo de solicitud:**
```json
{
  "property_id": "texto (requerido)"
}
```

**Respuesta exitosa â€” HTTP 201 Created:** `Acknowledge sin body.`

---

### `POST /api/v1/coupons/validate` â€” Validar CupÃ³n
*Verifica si un cupÃ³n es vÃ¡lido para una fecha y usuario antes de aplicar el descuento.*

**AutenticaciÃ³n requerida:** `Bearer Token (TOURIST, AGENCY_USER)`

**Cuerpo de solicitud:**
```json
{
  "code": "texto (requerido)",
  "property_id": "texto (requerido)"
}
```

**Respuesta exitosa â€” HTTP 200 OK:**
```json
{
  "data": {
    "valid": true,
    "discount_percentage": "nÃºmero (opcional)",
    "max_discount_amount": "nÃºmero (opcional, en centavos)"
  }
}
```

---

### `GET /api/v1/payouts` â€” Consultar Desembolsos
*El finquero visualiza el historial de dinero girado a su cuenta.*

**AutenticaciÃ³n requerida:** `Bearer Token (OWNER_API)`

**Respuesta exitosa â€” HTTP 200 OK:**
```json
{
  "data": [
    {
      "payout_id": "texto",
      "booking_id": "texto",
      "amount": "nÃºmero (centavos)",
      "currency": "texto",
      "status": "texto (PENDING, PROCESSING, PAID, FAILED)",
      "transaction_date": "fecha ISO-8601"
    }
  ]
}
```

---

## 2. EstÃ¡ndar de Errores Universal

Todo error del sistema devuelve la misma estructura, sin excepciones:

```json
{
  "error": {
    "code": "CÃ“DIGO_CONSTANTE_STRING",
    "message": "Mensaje descriptivo en espaÃ±ol.",
    "details": null
  }
}
```

| CÃ³digo HTTP | CÃ³digo Constante | DescripciÃ³n |
|---|---|---|
| `409` | `DATES_UNAVAILABLE` | Conflicto de fechas en reserva |
| `402` | `PAYMENT_DECLINED` | Pago rechazado por pasarela |
| `401` | `UNAUTHORIZED` | JWT ausente o expirado |
| `403` | `FORBIDDEN` | Acceso a recurso ajeno (IDOR) |
| `404` | `RESOURCE_NOT_FOUND` | Recurso no existe |
| `500` | `INTERNAL_SERVER_ERROR` | Error interno del servidor |

---

## ImplicaciÃ³n de Fase

- El contrato de comunicaciÃ³n estÃ¡ sellado. El equipo de Frontend puede construir Mock Servers con estas estructuras JSON mientras el Backend implementa la lÃ³gica real.
- Los `code` constantes del objeto de error son el contrato para la localizaciÃ³n i18n (D14): el Frontend usarÃ¡ `t('errors.DATES_UNAVAILABLE')` para mostrar el mensaje en el idioma del usuario.
- **Proceder a D10:** Matriz de Notificaciones y Eventos.

