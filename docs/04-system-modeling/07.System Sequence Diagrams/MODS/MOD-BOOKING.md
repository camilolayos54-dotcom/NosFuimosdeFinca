# Modulo: MOD-BOOKING

### S-01: Proceso de Reserva y Pago (Booking Checkout)

Este diagrama documenta la orquestacion sincrona y asincrona que ocurre cuando un Turista intenta reservar una finca, incluyendo la validacion concurrente (fechas ocupadas) y el cobro de la tarjeta de credito.

```mermaid
sequenceDiagram
    autonumber
    actor T as Turista
    participant C as Frontend (Browser)
    participant API as Booking API
    participant DB as PostgreSQL
    participant STR as Stripe API
    participant W as Async Worker

    T->>C: Clic "Reservar" (D5 Mockup)
    C->>API: POST /api/bookings (Fechas + Token Stripe)
    
    API->>DB: SELECT bookings ( Fechas Disponibles?)
    DB-->>API: Resultado
    
    alt Fechas Ocupadas (Concurrencia)
        API-->>C: HTTP 409 Conflict (Fechas no disponibles)
        C-->>T: Mostrar Inline Error Banner
    else Fechas Libres
        API->>STR: POST /v1/charges (Cobrar Tarjeta)
        
        alt Pago Declinado (Stripe rechaza)
            STR-->>API: 402 Payment Required
            API-->>C: HTTP 400 Bad Request
            C-->>T: Mostrar Toast de Error (Fondos Insuficientes)
        else Pago Exitoso
            STR-->>API: 200 OK (Charge ID)
            API->>DB: INSERT INTO bookings (Status: CONFIRMED)
            DB-->>API: Reservation ID
            
            %% Proceso Asincrono Delegado
            API-)W: Event: "Booking Confirmed" (Enviar Emails)
            W-)T: (Asincrono) Enviar Email Confirmacion
            
            %% Respuesta Inmediata al Usuario
            API-->>C: HTTP 201 Created
            C-->>T: Redirigir a Pantalla de "Recibo de Viaje"
        end
    end
```

---

### Phase Gate Implication
- El equipo Frontend ya sabe exactamente que Codigos HTTP esperar (201, 400, 409) para gatillar las pantallas disenadas en el D5.
- El equipo Backend ya sabe que enviar el correo es una tarea NO BLOQUEANTE (Background Worker).
- **Proceed to D8:** State Machine & Activity Diagrams.
