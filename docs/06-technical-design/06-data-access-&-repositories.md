# Deliverable 6 (D6): Data Access & Repositories

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 6, D5:* Este entregable define las interfaces de comunicaciÃ³n con la base de datos (PostgreSQL vÃ­a Supabase JS) para persistir las entidades protegidas diseÃ±adas en el `[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/5.Class_Diagrams.md]]`.

---

## 2. Interfaces de Repositorio y Queries Complejas (Supabase JS)

Aplicando Domain-Driven Design, hemos creado repositorios Ãºnicamente para las *Aggregate Roots* (`Booking`, `Review`, `Wishlist`).

### 2.1 IBookingRepository
```typescript
import { Booking } from '../domain/Booking';
import { CreateBookingDTO, UpdateBookingDTO } from './dtos';

export interface IBookingRepository {
  // Operaciones CRUD EstÃ¡ndar
  create(data: CreateBookingDTO): Promise<Booking>;
  findById(id: string): Promise<Booking | null>;
  update(id: string, data: UpdateBookingDTO): Promise<Booking>;
  delete(id: string): Promise<void>; // (Solo aplicable pre-pago por seguridad financiera)
  
  // NFR: Listado GenÃ©rico con PaginaciÃ³n
  findAll(params: { page: number; limit: number; sortBy?: string; order?: 'asc' | 'desc' }): Promise<Booking[]>;
  
  // --- CONSULTAS COMPLEJAS (Supabase JS) ---

  // 1. PrevenciÃ³n de Doble Reserva (ValidaciÃ³n antes de Crear)
  async findOverlappingBookings(propertyId: string, checkIn: Date, checkOut: Date): Promise<Booking[]> {
    const { data, error } = await supabase
      .from('bookings')
      .select('*')
      .eq('property_id', propertyId)
      .in('status', ['PENDING', 'APPROVED'])
      // LÃ³gica de cruce temporal en Postgres:
      .or(`and(check_in.lte.${checkOut.toISOString()},check_out.gte.${checkIn.toISOString()})`);
    
    if (error) throw error;
    return data.map(mapToBookingEntity);
  }

  // 2. Dashboard del Finquero (Mis HuÃ©spedes) - Inner Join Invertido
  async findBookingsByHost(hostId: string, params: PaginationParams): Promise<Booking[]> {
    const { data, error } = await supabase
      .from('bookings')
      // RelaciÃ³n implicita configurada en BD: properties!inner
      .select('*, properties!inner(host_id)')
      .eq('properties.host_id', hostId)
      .order(params.sortBy || 'created_at', { ascending: params.order === 'asc' })
      .range(params.page * params.limit, (params.page + 1) * params.limit - 1);
      
    if (error) throw error;
    return data.map(mapToBookingEntity);
  }

  // 3. Mis Viajes (Dashboard del Turista)
  async findBookingsByGuest(guestId: string): Promise<Booking[]> {
    const { data, error } = await supabase
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
```typescript
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
> La seguridad de Mass Assignment reside aquÃ­. NingÃºn DTO expone los atributos financieros (`totalPrice`, `taxesAmount`) de la base de datos hacia el cliente. El backend debe recalcularlos asÃ­ncronamente en base al catÃ¡logo maestro en el momento de crear la reserva.

```typescript
// ==========================================
// BOOKING DTOs
// ==========================================

export interface CreateBookingDTO {
  propertyId: string; // UUID vÃ¡lido, requerido (Llave hacia CatÃ¡logo)
  checkIn: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor o igual a HOY
  checkOut: string; // Fecha ISO YYYY-MM-DD, requerida, debe ser mayor a checkIn
  guestCount: number; // Entero positivo >= 1
  couponCode?: string; // Opcional. String alfanumÃ©rico.
  
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
  propertyId: string; // UUID vÃ¡lido
  rating: number; // Entero obligatorio, restringido al rango 1 - 5
  comment?: string; // Texto, mÃ¡ximo 1000 caracteres
  
  // â›” BLOQUEADO: 'guestId' NO se acepta del cliente. El backend lo inyectarÃ¡ extrayÃ©ndolo del JWT por seguridad.
}

// ==========================================
// WISHLIST DTOs
// ==========================================

export interface CreateWishlistDTO {
  propertyId: string; // UUID vÃ¡lido
  
  // â›” BLOQUEADO: 'userId' lo inyecta el AuthGuard a partir de la cookie de sesiÃ³n.
}
```

---

## 4. Downstream Consumers
- **Phase 6 â€” D7 (API Contracts):** Este documento entregarÃ¡ la estructura JSON exacta que se plasmarÃ¡ en Swagger/OpenAPI (Los DTOs definen los `Request Bodies`).
- **Phase 7 â€” D5 (Backend API Implementation):** Los desarrolladores usarÃ¡n estas interfaces y las consultas literales de Supabase JS para escribir el cÃ³digo fuente del proyecto Next.js (`src/modules/booking/infrastructure/SupabaseBookingRepository.ts`).

