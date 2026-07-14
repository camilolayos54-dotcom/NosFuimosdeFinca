# Deliverable 6 (D6): Data Access & Repositories

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 6, D5:* Este entregable define las interfaces de comunicacion con la base de datos (PostgreSQL via PostgreSQL JS) para persistir las entidades protegidas disenadas en el `[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/5.Class_Diagrams.md]]`.

---

## 2. Interfaces de Repositorio y Queries Complejas (PostgreSQL JS)

Aplicando Domain-Driven Design, hemos creado repositorios unicamente para las *Aggregate Roots* (`Booking`, `Review`, `Wishlist`).

### 2.1 IBookingRepository
```java
import { Booking } from '../domain/Booking';
import { CreateBookingDTO, UpdateBookingDTO } from './dtos';

export interface IBookingRepository {
  // Operaciones CRUD Estandar
  create(data: CreateBookingDTO): Promise<Booking>;
  findById(id: string): Promise<Booking | null>;
  update(id: string, data: UpdateBookingDTO): Promise<Booking>;
  delete(id: string): Promise<void>; // (Solo aplicable pre-pago por seguridad financiera)
  
  // NFR: Listado Generico con Paginacion
  findAll(params: { page: number; limit: number; sortBy?: string; order?: 'asc' | 'desc' }): Promise<Booking[]>;
  
  // --- CONSULTAS COMPLEJAS (PostgreSQL JS) ---

  // 1. Prevencion de Doble Reserva (Validacion antes de Crear)
  async findOverlappingBookings(propertyId: string, checkIn: Date, checkOut: Date): Promise<Booking[]> {
    const { data, error } = await postgresql
      .from('bookings')
      .select('*')
      .eq('property_id', propertyId)
      .in('status', ['PENDING', 'APPROVED'])
      // Logica de cruce temporal en Postgres:
      .or(`and(check_in.lte.${checkOut.toISOString()},check_out.gte.${checkIn.toISOString()})`);
    
    if (error) throw error;
    return data.map(mapToBookingEntity);
  }

  // 2. Dashboard del Finquero (Mis Huespedes) - Inner Join Invertido
  async findBookingsByHost(hostId: string, params: PaginationParams): Promise<Booking[]> {
    const { data, error } = await postgresql
      .from('bookings')
      // Relacion implicita configurada en BD: properties!inner
      .select('*, properties!inner(host_id)')
      .eq('properties.host_id', hostId)
      .order(params.sortBy || 'created_at', { ascending: params.order === 'asc' })
      .range(params.page * params.limit, (params.page + 1) * params.limit - 1);
      
    if (error) throw error;
    return data.map(mapToBookingEntity);
  }

  // 3. Mis Viajes (Dashboard del Turista)
  async findBookingsByGuest(guestId: string): Promise<Booking[]> {
    const { data, error } = await postgresql
      .from('bookings')
      .select('*')
      .eq('guest_id', guestId)
      .order('check_in', { ascending: false });
      
    if (error) throw error;
    return data.map(mapToBookingEntity);
  }
}
```

### 2.2 IReviewRepository & IWishlistRepository
```java
export interface IReviewRepository {
  create(data: CreateReviewDTO): Promise<Review>;
  findById(id: string): Promise<Review | null>;
  findAll(params: { page: number; limit: number; sortBy?: string; order?: 'asc' | 'desc' }): Promise<Review[]>;
  update(id: string, data: UpdateReviewDTO): Promise<Review>;
  delete(id: string): Promise<void>;
}

export interface IWishlistRepository {
  create(data: CreateWishlistDTO): Promise<Wishlist>;
  findAll(params: { page: number; limit: number; sortBy?: string; order?: 'asc' | 'desc' }): Promise<Wishlist[]>;
  delete(id: string): Promise<void>;
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

export interface CreateBookingDTO {
  propertyId: string; // UUID valido, requerido (Llave hacia Catalogo)
  checkIn: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor o igual a HOY
  checkOut: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor a checkIn
  guestCount: number; // Entero positivo >= 1
  couponCode?: string; // Opcional. String alfanumerico.
  
  // â›” BLOQUEADO: 'status', 'totalPrice', 'basePriceAmount' y 'id' NO se aceptan.
}

export interface UpdateBookingDTO {
  // Las modificaciones a una reserva son acciones de estado, no escrituras libres.
  status?: 'APPROVED' | 'CANCELLED'; 
  cancellationReason?: string;
}

// ==========================================
// REVIEW DTOs
// ==========================================

export interface CreateReviewDTO {
  propertyId: string; // UUID valido
  rating: number; // Entero obligatorio, restringido al rango 1 - 5
  comment?: string; // Texto, maximo 1000 caracteres
  
  // â›” BLOQUEADO: 'guestId' NO se acepta del cliente. El backend lo inyectara extrayendolo del JWT por seguridad.
}

// ==========================================
// WISHLIST DTOs
// ==========================================

export interface CreateWishlistDTO {
  propertyId: string; // UUID valido
  
  // â›” BLOQUEADO: 'userId' lo inyecta el AuthGuard a partir de la cookie de sesion.
}
```

---

## 4. Downstream Consumers
- **Phase 6 â€” D7 (API Contracts):** Este documento entregara la estructura JSON exacta que se plasmara en Swagger/OpenAPI (Los DTOs definen los `Request Bodies`).
- **Phase 7 â€” D5 (Backend API Implementation):** Los desarrolladores usaran estas interfaces y las consultas literales de PostgreSQL JS para escribir el codigo fuente del proyecto Spring Boot (Java) (`com.nosfuimosdefinica.booking/infrastructure/PostgreSQLBookingRepository.ts`).

