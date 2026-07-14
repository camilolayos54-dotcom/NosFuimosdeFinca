 # Deliverable 9 (D9): Frontend MPA & State Management

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Technical Design
**Modulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4 y 6:* Este entregable mapea los Mockups de UI hacia el paradigma jerarquico de *Atomic Design*, y ata los componentes matematicamente a los endpoints descritos en los Contratos de API (`[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/7.API_Contracts.md]]`).

---

## 2. Arbol de Componentes y Props (Atomic Design)

### 2.1 Jerarquia Visual
El Modulo de Booking Engine posee dos paginas maestras en Spring Boot. Los componentes han sido desagregados priorizando la reusabilidad.

```text
**1. BookingCheckoutPage (Pagina)**
          BookingForm (Organismo)
                DateRangePicker (Molecula)
                      CalendarIcon (Atomo)
                      HiddenInput (Atomo)
                GuestCounter (Molecula)
                      IconButton (Atomo Importado del UI Kit)
                      CounterLabel (Atomo)
                CouponField (Molecula)
          BookingSummary (Organismo)
                PropertyMiniCard (Molecula)
                PriceLine (Molecula - Base, Limpieza, Fees, Total)
                Divider (Atomo Importado del UI Kit)
          CheckoutButton (Atomo Importado del UI Kit)

**2. MyBookingsPage (Pagina)**
          BookingFilters (Molecula)
                SelectTab (Atomo)
          BookingList (Organismo)
                EmptyState (Molecula - Wireframe State: Sin viajes)
                BookingCard (Molecula)
                    PropertyImage (Atomo)
                    StatusBadge (Atomo)
                    ActionMenu (Molecula - Opcion Cancelar/Pagar)
```

### 2.2 Contrato de Props (Java Interfaces)
Para evitar errores de runtime, los Organismos y Moleculas inteligentes exigiran el cumplimiento estricto de las siguientes props basadas en los Schemas de API:

```java
import { BookingResponse, CreateBookingRequest } from '@/shared/api/contracts/booking';

// --- BOOKING CHECKOUT --- //

interface BookingFormProps {
  propertyId: string;
  isSubmitting: boolean;
  unavailableDates: Date[]; // Fechas ya ocupadas a bloquear en el DatePicker
  // Omitimos propertyId porque lo maneja la pagina superior
  onSubmit: (data: Omit<CreateBookingRequest, 'propertyId'>) => void;
}

interface BookingSummaryProps {
  // Dumb Component. No recibe la entidad entera, solo los datos planos para pintar.
  basePrice: number;
  cleaningFee: number;
  platformFee: number;
  taxes: number;
  total: number;
  currency?: string; // Opcional. Predeterminado: 'COP'
}

// --- MY BOOKINGS --- //

interface BookingCardProps {
  booking: BookingResponse; // Entidad traida directamente de Gestionado desde el Backend Java (Spring Boot)
  onCancelClick?: (bookingId) => void; // Solo se activa si status === PENDING
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

### 3.3 Local State (HTML/JS (MPA) `useState`)
- Abierto/Cerrado del `DatePicker` (en `BookingForm`).
- Variables temporales del numero de huespedes.
- Abierto/Cerrado del modal de confirmacion de cancelacion (en `BookingCard`).

---

## 4. Downstream Consumers
- **Phase 7 D6 (Frontend UI & State Implementation):** El desarrollador de HTML/JS (MPA)/Spring Boot (Java) tomara este documento como su plano de construccion (Blueprint). Creara exactamente estos componentes, copiara y pegara las props tipadas, e instanciara los hooks de Gestionado desde el Backend Java (Spring Boot) con las `queryKeys` aqui escritas.

