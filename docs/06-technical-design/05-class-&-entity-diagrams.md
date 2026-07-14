# Deliverable 5 (D5): Class & Entity Diagrams

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 3 y 5:* Este entregable toma las entidades puras del ERD y les inyecta las Reglas de Negocio definidas en el `[[PHASE_3_REQUIREMENTS_ENGINEERING/7.Module_Specification.md]]`, logrando un Dominio Rico (Rich Domain Model) que serÃ¡ codificado mediante clases de TypeScript bajo los principios de *Clean Architecture* decididos en la Fase 5.

---

## 2. Diagrama de Clases UML (TypeScript Abstraction)

> [!NOTE]
> Las propiedades marcadas con `-` son privadas y **no pueden ser alteradas directamente** desde controladores externos. Deben usarse los mÃ©todos pÃºblicos (`+`) provistos, garantizando que ninguna factura se emita con valores matemÃ¡ticos incorrectos y que no se viole la mÃ¡quina de estados.

```mermaid
classDiagram
    class BookingStatus {
        <<enumeration>>
        PENDING
        APPROVED
        CANCELLED
        COMPLETED
    }

    class Booking {
        -id: string
        +propertyId: string
        +guestId: string
        +couponId: string | null
        +checkIn: Date
        +checkOut: Date
        +guestCount: number
        -basePriceAmount: number
        -cleaningFeeAmount: number
        -platformFeeAmount: number
        -taxesAmount: number
        -totalPrice: number
        -status: BookingStatus
        +cancellationReason: string | null
        
        +calculateTotal() number
        +approve() void
        +cancel(reason: string) void
        +applyCoupon(discountPercent: number, maxAmount: number) void
        +getStatus() BookingStatus
        +getTotalPrice() number
    }

    class Review {
        -id: string
        +propertyId: string
        +guestId: string
        -rating: number
        +comment: string
        
        +updateRating(newRating: number) void
        +getRating() number
    }

    class Wishlist {
        <<interface>>
        +id: string
        +userId: string
        +propertyId: string
    }

    Booking ..> BookingStatus : uses
```

---

## 3. JustificaciÃ³n Anti-AnÃ©mica

Para evitar el antipatrÃ³n del *Modelo de Dominio AnÃ©mico* (donde la lÃ³gica crÃ­tica queda dispersa en mÃºltiples archivos tipo *Service*), la clase **Booking** concentra todas las validaciones financieras internamente:

1. **`calculateTotal()`:** Unifica matemÃ¡ticamente el valor en centavos (`basePriceAmount` + `cleaningFeeAmount` + `platformFeeAmount` + `taxesAmount`). NingÃºn programador podrÃ¡ calcular totales "a mano" en la UI o en un endpoint HTTP.
2. **`approve()` / `cancel()`:** MÃ¡quina de estados blindada. El mÃ©todo `cancel()` verificarÃ¡ internamente que el status actual sea `PENDING` o `APPROVED` y lanzarÃ¡ un error si se intenta cancelar una reserva `COMPLETED`. 
3. **`Wishlist` como Interfaz:** La lista de deseos es deliberadamente anÃ©mica (declarada como `<<interface>>`) porque, funcionalmente, es solo un Data Transfer Object (DTO) que une al usuario con una finca. No tiene reglas de validaciÃ³n complejas, por lo tanto no requiere encapsulamiento.

---

## 4. Downstream Consumers
Este diseÃ±o es la semilla para el cÃ³digo real del Backend:
- **Phase 6 â€” D6 (Data Access & Repositories):** Los repositorios de Supabase deberÃ¡n devolver instancias reales (new Booking) en lugar de JSONs genÃ©ricos, respetando este contrato.
- **Phase 7 â€” D5 (Backend API Implementation):** Los desarrolladores transcribirÃ¡n este diagrama literal en archivos `.ts` (ej. `src/modules/booking/domain/Booking.ts`).

