# Modulo: MOD-CALENDAR

### C-01: Sincronizacion y Bloqueo de Fechas

Este diagrama modela la logica en la cual un Anfitrion bloquea manualmente fechas en el calendario (o mediante iCal sync) para evitar que los Turistas reserven su propiedad en esos dias. Representa una escritura critica de base de datos para prevenir colisiones.

```mermaid
sequenceDiagram
    autonumber
    actor H as Anfitrion
    participant C as Frontend (Calendar UI)
    participant API as Calendar API
    participant DB as PostgreSQL

    H->>C: Selecciona Fechas y Clic "Bloquear"
    C->>API: POST /api/calendar/blocks (property_id, check_in, check_out)
    
    API->>DB: SELECT bookings WHERE dates_overlap
    DB-->>API: Overlapping Bookings Result
    
    alt Fechas Ya Reservadas
        API-->>C: HTTP 409 Conflict (Ya existe una reserva)
        C-->>H: Mostrar Error "No puedes bloquear fechas reservadas"
    else Fechas Libres
        API->>DB: INSERT INTO calendar_blocks
        DB-->>API: block_id
        API-->>C: HTTP 201 Created
        C-->>H: Pintar Fechas de Gris (Bloqueado)
    end
```

---
### Implicaciones de Fase Especificas
- Las sentencias `SELECT` de superposicion de fechas introducen un riesgo de condicion de carrera si el nivel de aislamiento de la base de datos no es correcto o si no se manejan bloqueos transaccionales (row-level locking).
- El Frontend espera que un 409 desencadene una recarga del estado del calendario para mostrar la reserva conflictiva al anfitrion.
