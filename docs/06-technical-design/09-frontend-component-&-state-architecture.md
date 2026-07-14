# Deliverable 9 (D9): Frontend Component & State Architecture

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4 y 6:* Este entregable mapea los Mockups de UI hacia el paradigma jerarquico de *Atomic Design*, y ata los componentes matematicamente a los endpoints descritos en los Contratos de API (`[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/7.API_Contracts.md]]`).

---

## 2. Ãrbol de Componentes y Props (Atomic Design)

### 2.1 Jerarquia Visual
El Modulo de Booking Engine posee dos paginas maestras en Spring Boot. Los componentes han sido desagregados priorizando la reusabilidad.

```text
**1. BookingCheckoutPage (Pagina)**
â”œâ”€â”€ BookingForm (Organismo)
â”‚   â”œâ”€â”€ DateRangePicker (Molecula)
â”‚   â”‚   â”œâ”€â”€ CalendarIcon (Ãtomo)
â”‚   â”‚   â””â”€â”€ HiddenInput (Ãtomo)
â”‚   â”œâ”€â”€ GuestCounter (Molecula)
â”‚   â”‚   â”œâ”€â”€ IconButton (Ãtomo â€” Importado del UI Kit)
â”‚   â”‚   â””â”€â”€ CounterLabel (Ãtomo)
â”‚   â””â”€â”€ CouponField (Molecula)
â”œâ”€â”€ BookingSummary (Organismo)
â”‚   â”œâ”€â”€ PropertyMiniCard (Molecula)
â”‚   â”œâ”€â”€ PriceLine (Molecula - Base, Limpieza, Fees, Total)
â”‚   â””â”€â”€ Divider (Ãtomo â€” Importado del UI Kit)
â””â”€â”€ CheckoutButton (Ãtomo â€” Importado del UI Kit)

**2. MyBookingsPage (Pagina)**
â”œâ”€â”€ BookingFilters (Molecula)
â”‚   â””â”€â”€ SelectTab (Ãtomo)
â”œâ”€â”€ BookingList (Organismo)
â”‚   â”œâ”€â”€ EmptyState (Molecula - Wireframe State: Sin viajes)
â”‚   â””â”€â”€ BookingCard (Molecula)
â”‚       â”œâ”€â”€ PropertyImage (Ãtomo)
â”‚       â”œâ”€â”€ StatusBadge (Ãtomo)
â”‚       â””â”€â”€ ActionMenu (Molecula - Opcion Cancelar/Pagar)
```

### 2.2 Contrato de Props (Java Interfaces)
Para evitar errores de runtime, los Organismos y Moleculas inteligentes exigiran el cumplimiento estricto de las siguientes props basadas en los Schemas de API:

```java
import { BookingResponse, CreateBookingRequest } from '@/shared/api/contracts/booking';

// --- BOOKING CHECKOUT --- //

export interface BookingFormProps {
  propertyId: string;
  isSubmitting: boolean;
  unavailableDates: Date[]; // Fechas ya ocupadas a bloquear en el DatePicker
  // Omitimos propertyId porque lo maneja la pagina superior
  onSubmit: (data: Omit<CreateBookingRequest, 'propertyId'>) => void;
}

export interface BookingSummaryProps {
  // Dumb Component. No recibe la entidad entera, solo los datos planos para pintar.
  basePrice: number;
  cleaningFee: number;
  platformFee: number;
  taxes: number;
  total: number;
  currency?: string; // Opcional. Predeterminado: 'COP'
}

// --- MY BOOKINGS --- //

export interface BookingCardProps {
  booking: BookingResponse; // Entidad traida directamente de Gestionado desde el Backend Java (Spring Boot)
  onCancelClick?: (bookingId: string) => void; // Solo se activa si status === PENDING
}
```

---

## 3. Definiciones de Gestion de Estado

Siguiendo las mejores practicas modernas, **no utilizaremos Global State (Estado de sesion via Spring Security + JWT Cookie) para almacenar las reservas ni las fechas temporales**. Mezclar el cache de servidor con estado global conduce a problemas graves de sincronizacion.

### 3.1 Server State (Gestionado desde el Backend Java (Spring Boot) / SWR)
Toda la data persistente que viene del backend vive aqui.

- **Hook:** `useBookings()`
  - **QueryKey:** `['bookings', 'my-trips', page]`
  - **Uso:** Importado a nivel de la pagina `MyBookingsPage` y pasado hacia abajo.
  
- **Mutation:** `useCreateBooking()`
  - **OnSuccess Behavior:** Llama a `queryClient.invalidateQueries(['bookings'])` para asegurar que, si el turista regresa a su listado, vea la nueva reserva inmediatamente sin tener que refrescar la pagina.

### 3.2 Global State (Estado de sesion via Spring Security + JWT Cookie)
- **NO SE USA** en este modulo. 
- *Decision Arquitectonica:* Evitamos usar un `BookingSlice` para mover la finca o fechas escogidas hacia el Checkout. En su lugar usaremos **Deep Linking / URL Params** (ej. `/checkout?propertyId=123&checkIn=2026-12-01`). Esto permite que el Turista comparta el enlace con su pareja o recargue la pagina sin perder los datos de reserva.

### 3.3 Local State (Vite + JavaScript (frontend) `useState`)
- Abierto/Cerrado del `DatePicker` (en `BookingForm`).
- Variables temporales del numero de huespedes.
- Abierto/Cerrado del modal de confirmacion de cancelacion (en `BookingCard`).

---

## 4. Downstream Consumers
- **Phase 7 â€” D6 (Frontend UI & State Implementation):** El desarrollador de Vite + JavaScript (frontend)/Spring Boot (Java) tomara este documento como su plano de construccion (Blueprint). Creara exactamente estos componentes, copiara y pegara las props tipadas, e instanciara los hooks de Gestionado desde el Backend Java (Spring Boot) con las `queryKeys` aqui escritas.

