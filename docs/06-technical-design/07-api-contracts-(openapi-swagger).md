 # Deliverable 7 (D7): API Contracts (OpenAPI)

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4 y 6:* Este documento fusiona las operaciones conceptuales del `[[PHASE_4_SYSTEM_MODELING/9.API_Conceptual_Design.md]]` con los DTOs estrictos definidos en el `[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/6.Data_Access.md]]` y el mecanismo de seguridad de `[[PHASE_6_TECHNICAL_DESIGN/4.Security_Implementation.md]]`. 

---

## 2. Especificacion OpenAPI YAML

> [!TIP]
> **Para el equipo Frontend:** Todos los endpoints requieren que la cookie `sb-[project]-auth-token` viaje en la peticion. Spring Boot (Java) y el navegador manejan esto automaticamente (credentials: 'include'), no hace falta adjuntar un header `Authorization` manualmente.

```yaml
openapi: 3.0.3
info:
  title: API Modulo Booking Engine
  version: 1.0.0
  description: Contrato oficial para orquestar reservas, resenas y favoritos.
  
paths:
  /api/bookings:
    post:
      tags: [Bookings]
      summary: Crear una nueva reserva (Turista)
      operationId: createBooking
      security: [{ cookieAuth: [] }]
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/CreateBookingRequest' }
      responses:
        '201':
          description: Reserva creada en estado PENDING.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/BookingResponse' }
        '400':
          description: Reglas de negocio violadas (ej. fechas cruzadas, capacidad excedida).
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
        '401':
          description: Sesion invalida o faltante.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
    get:
      tags: [Bookings]
      summary: Listar reservas asociadas al usuario actual
      operationId: listBookings
      security: [{ cookieAuth: [] }]
      parameters:
        - name: page
          in: query
          schema: { type: integer, default: 0 }
        - name: limit
          in: query
          schema: { type: integer, default: 20 }
      responses:
        '200':
          description: Array de reservas (Historico o Futuras).
          content:
            application/json:
              schema:
                type: array
                items: { $ref: '#/components/schemas/BookingResponse' }
        '401':
          description: Sesion invalida.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }

  /api/bookings/{id}/status:
    patch:
      tags: [Bookings]
      summary: Actualizar estado de la reserva (Finquero aprueba/cancela)
      operationId: updateBookingStatus
      security: [{ cookieAuth: [] }]
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string, format: uuid }
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/UpdateBookingStatusRequest' }
      responses:
        '200':
          description: Estado actualizado exitosamente.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/BookingResponse' }
        '401':
          description: Sesion invalida.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
        '403':
          description: Prohibido. El usuario no es dueno de la propiedad ni administrador.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }

  /api/reviews:
    post:
      tags: [Reviews]
      summary: Crear una resena para una propiedad
      operationId: createReview
      security: [{ cookieAuth: [] }]
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/CreateReviewRequest' }
      responses:
        '201':
          description: Resena guardada.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ReviewResponse' }
        '400':
          description: Error de validacion (ej. Rating fuera de rango 1-5).
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
        '401':
          description: Sesion invalida.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
        '403':
          description: Prohibido. El usuario no ha completado un viaje en esta finca.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
              
  /api/wishlists:
    post:
      tags: [Wishlists]
      summary: Agregar propiedad a favoritos
      operationId: addToWishlist
      security: [{ cookieAuth: [] }]
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/CreateWishlistRequest' }
      responses:
        '201':
          description: Agregado.
        '401':
          description: Sesion invalida.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }
              
  /api/wishlists/{propertyId}:
    delete:
      tags: [Wishlists]
      summary: Remover propiedad de favoritos
      operationId: removeFromWishlist
      security: [{ cookieAuth: [] }]
      parameters:
        - name: propertyId
          in: path
          required: true
          schema: { type: string, format: uuid }
      responses:
        '204':
          description: Eliminado exitosamente (Sin contenido).
        '401':
          description: Sesion invalida.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/ErrorResponse' }

components:
  securitySchemes:
    cookieAuth:
      type: apiKey
      in: cookie
      name: sb-project-auth-token
      description: Spring Boot (Java) SSR HttpOnly Cookie inyectada automaticamente.

  schemas:
    # --- REQUESTS ---
    CreateBookingRequest:
      type: object
      required: [propertyId, checkIn, checkOut, guestCount]
      properties:
        propertyId: { type: string, format: uuid }
        checkIn: { type: string, format: date, example: "2026-12-24" }
        checkOut: { type: string, format: date, example: "2026-12-31" }
        guestCount: { type: integer, minimum: 1, example: 4 }
        couponCode: { type: string }

    UpdateBookingStatusRequest:
      type: object
      required: [status]
      properties:
        status: { type: string, enum: [APPROVED, CANCELLED] }
        cancellationReason: { type: string }

    CreateReviewRequest:
      type: object
      required: [propertyId, rating]
      properties:
        propertyId: { type: string, format: uuid }
        rating: { type: integer, minimum: 1, maximum: 5, example: 5 }
        comment: { type: string, maxLength: 1000 }

    CreateWishlistRequest:
      type: object
      required: [propertyId]
      properties:
        propertyId: { type: string, format: uuid }

    # --- RESPONSES ---
    BookingResponse:
      type: object
      properties:
        id: { type: string, format: uuid }
        propertyId: { type: string, format: uuid }
        guestId: { type: string, format: uuid }
        status: { type: string, enum: [PENDING, APPROVED, CANCELLED, COMPLETED] }
        checkIn: { type: string, format: date-time }
        checkOut: { type: string, format: date-time }
        totalPrice: { type: integer, description: "Costo total en centavos" }

    ReviewResponse:
      type: object
      properties:
        id: { type: string, format: uuid }
        propertyId: { type: string, format: uuid }
        rating: { type: integer }
        comment: { type: string }

    # --- SHARED ENVELOPES ---
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code: { type: string, example: "VALIDATION_FAILED" }
            message: { type: string, example: "Mensaje descriptivo del error." }
```

---

## 3. Downstream Consumers
- **Phase 7 D5 (Backend API Implementation):** El desarrollador backend debe lograr que Spring Boot (Java) responda matematicamente identico a este YAML (mismos codigos HTTP, mismas keys en el JSON).
- **Phase 7 D6 (Frontend UI):** El desarrollador frontend usara este YAML (o generadores como `orval` / `openapi-java`) para crear las queries de **Gestionado desde el Backend Java (Spring Boot)** (`useMutation`, `useQuery`), logrando que el frontend este fuertemente tipado incluso antes de que el backend exista.

