 # Deliverable 6 (D6): Data Access & Repositories

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 6, D5:* Este entregable define las interfaces de comunicacion con la base de datos (PostgreSQL via Spring Data JPA) para persistir las entidades protegidas disenadas en el `[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/5.Class_Diagrams.md]]`.

---

## 2. Interfaces de Repositorio y Queries Complejas (Spring Data JPA)

Aplicando Domain-Driven Design, hemos creado repositorios unicamente para las *Aggregate Roots* (`Booking`, `Review`, `Wishlist`).

### 2.1 IBookingRepository
```java
import com.nosfuimosdefinica.booking.domain.Booking;
import com.nosfuimosdefinica.booking.infrastructure.dto.*;

public interface IBookingRepository {
  // Operaciones CRUD Estandar
  create(CreateBookingDTO data: CreateBookingDTO): Booking;
  findById(id): Optional<Booking>;
  update(String id, UpdateBookingDTO): Booking;
  delete(id): void; // (Solo aplicable pre-pago por seguridad financiera)
  
  // NFR: Listado Generico con Paginacion
  findAll(params: { page: number; limit: number; String sortBy; String String }): List<Booking>;
  
  // --- CONSULTAS COMPLEJAS (Spring Data JPA) ---

  // 1. Prevencion de Doble Reserva (Validacion antes de Crear)
  findOverlappingBookings(propertyId: string, checkIn: Date, checkOut: Date): List<Booking {
    var results = // JPA query
      // find via repository'bookings')
      // .findAll()'*')
      .eq('property_id', propertyId)
      .in('status', ['PENDING', 'APPROVED'])
      // Logica de cruce temporal en Postgres:
      .or(`and(check_in.lte.${checkOut.toISOString()},check_out.gte.${checkIn.toISOString()})`);
    
    // Spring Data JPA throws DataAccessException
    return results;
  }

  // 2. Dashboard del Finquero (Mis Huespedes) - Inner Join Invertido
  findBookingsByHost(hostId: string, params: PaginationParams): List<Booking {
    var results = // JPA query
      // find via repository'bookings')
      // Relacion implicita configurada en BD: properties!inner
      // .findAll()'*, properties!inner(host_id)')
      .eq('properties.host_id', hostId)
      .order(params.sortBy || 'created_at', { ascending: params.order === 'asc' })
      .range(params.page * params.limit, (params.page + 1) * params.limit - 1);
      
    // Spring Data JPA throws DataAccessException
    return results;
  }

  // 3. Mis Viajes (Dashboard del Turista)
  findBookingsByGuest(guestId): List<Booking {
    var results = // JPA query
      // find via repository'bookings')
      // .findAll()'*')
      .eq('guest_id', guestId)
      .order('check_in', { ascending: false });
      
    // Spring Data JPA throws DataAccessException
    return results;
  }
}
```

### 2.2 IReviewRepository & IWishlistRepository
```java
public interface IReviewRepository {
  Review create(CreateReviewDTO data);
  Optional<Review> findById(String id);
  List<Review> findAll(PaginationParams params);
  Review update(String id, UpdateReviewDTO data);
  void delete(String id);
}

public interface IWishlistRepository {
  Wishlist create(CreateWishlistDTO data);
  List<Wishlist> findAll(PaginationParams params);
  void delete(String id);
}
```


---

## 3. Definiciones de DTO (Data Transfer Objects)

> [!WARNING]
> La seguridad de Mass Assignment reside aqui. Ningun DTO expone los atributos financieros (`totalPrice`, `taxesAmount`) de la base de datos hacia el cliente. El backend debe recalcularlos asincronamente en base al catalogo maestro en el momento de crear la reserva.

```java
// ==========================================
// BOOKING DTOs
// ==========================================

interface CreateBookingDTO {
  propertyId: string; // UUID valido, requerido (Llave hacia Catalogo)
  checkIn: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor o igual a HOY
  checkOut: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor a checkIn
  guestCount: number; // Entero positivo >= 1
  couponCode?: string; // Opcional. String alfanumerico.
  
  // BLOQUEADO: 'status', 'totalPrice', 'basePriceAmount' y 'id' NO se aceptan.
}

interface UpdateBookingDTO {
  // Las modificaciones a una reserva son acciones de estado, no escrituras libres.
  status?: 'APPROVED' | 'CANCELLED'; 
  cancellationReason?: string;
}

// ==========================================
// REVIEW DTOs
// ==========================================

interface CreateReviewDTO {
  propertyId: string; // UUID valido
  rating: number; // Entero obligatorio, restringido al rango 1 - 5
  comment?: string; // Texto, maximo 1000 caracteres
  
  // BLOQUEADO: 'guestId' NO se acepta del cliente. El backend lo inyectara extrayendolo del JWT por seguridad.
}

// ==========================================
// WISHLIST DTOs
// ==========================================

interface CreateWishlistDTO {
  propertyId: string; // UUID valido
  
  // BLOQUEADO: 'userId' lo inyecta el AuthGuard a partir de la cookie de sesion.
}
```

---

## 4. Downstream Consumers
- **Phase 6 D7 (API Contracts):** Este documento entregara la estructura JSON exacta que se plasmara en Swagger/OpenAPI (Los DTOs definen los `Request Bodies`).
- **Phase 7 D5 (Backend API Implementation):** Los desarrolladores usaran estas interfaces y las consultas literales de Spring Data JPA para escribir el codigo fuente del proyecto Spring Boot (Java) (`com.nosfuimosdefinica.booking/infrastructure/PostgreSQLBookingRepository.ts`).

