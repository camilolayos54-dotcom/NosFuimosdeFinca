# Deliverable 9 (D9): Frontend Component & State Architecture

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**MÃ³dulo:** MOD-Booking
**Estado:** Approved

*Backlink a Fase 4 y 6:* Este entregable mapea los Mockups de UI hacia el paradigma jerÃ¡rquico de *Atomic Design*, y ata los componentes matemÃ¡ticamente a los endpoints descritos en los Contratos de API (`[[PHASE_6_TECHNICAL_DESIGN/modules/MOD-Booking/7.API_Contracts.md]]`).

---

## 2. Ãrbol de Componentes y Props (Atomic Design)

### 2.1 JerarquÃ­a Visual
El MÃ³dulo de Booking Engine posee dos pÃ¡ginas maestras en Next.js. Los componentes han sido desagregados priorizando la reusabilidad.

```text
**1. BookingCheckoutPage (PÃ¡gina)**
â”œâ”€â”€ BookingForm (Organismo)
â”‚   â”œâ”€â”€ DateRangePicker (MolÃ©cula)
â”‚   â”‚   â”œâ”€â”€ CalendarIcon (Ãtomo)
â”‚   â”‚   â””â”€â”€ HiddenInput (Ãtomo)
â”‚   â”œâ”€â”€ GuestCounter (MolÃ©cula)
â”‚   â”‚   â”œâ”€â”€ IconButton (Ãtomo â€” Importado del UI Kit)
â”‚   â”‚   â””â”€â”€ CounterLabel (Ãtomo)
â”‚   â””â”€â”€ CouponField (MolÃ©cula)
â”œâ”€â”€ BookingSummary (Organismo)
â”‚   â”œâ”€â”€ PropertyMiniCard (MolÃ©cula)
â”‚   â”œâ”€â”€ PriceLine (MolÃ©cula - Base, Limpieza, Fees, Total)
â”‚   â””â”€â”€ Divider (Ãtomo â€” Importado del UI Kit)
â””â”€â”€ CheckoutButton (Ãtomo â€” Importado del UI Kit)

**2. MyBookingsPage (PÃ¡gina)**
â”œâ”€â”€ BookingFilters (MolÃ©cula)
â”‚   â””â”€â”€ SelectTab (Ãtomo)
â”œâ”€â”€ BookingList (Organismo)
â”‚   â”œâ”€â”€ EmptyState (MolÃ©cula - Wireframe State: Sin viajes)
â”‚   â””â”€â”€ BookingCard (MolÃ©cula)
â”‚       â”œâ”€â”€ PropertyImage (Ãtomo)
â”‚       â”œâ”€â”€ StatusBadge (Ãtomo)
â”‚       â””â”€â”€ ActionMenu (MolÃ©cula - OpciÃ³n Cancelar/Pagar)
```

### 2.2 Contrato de Props (TypeScript Interfaces)
Para evitar errores de runtime, los Organismos y MolÃ©culas inteligentes exigirÃ¡n el cumplimiento estricto de las siguientes props basadas en los Schemas de API:

```typescript
import { BookingResponse, CreateBookingRequest } from '@/shared/api/contracts/booking';

// --- BOOKING CHECKOUT --- //

export interface BookingFormProps {
  propertyId: string;
  isSubmitting: boolean;
  unavailableDates: Date[]; // Fechas ya ocupadas a bloquear en el DatePicker
  // Omitimos propertyId porque lo maneja la pÃ¡gina superior
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
  booking: BookingResponse; // Entidad traÃ­da directamente de React Query
  onCancelClick?: (bookingId: string) => void; // Solo se activa si status === PENDING
}
```

---

## 3. Definiciones de GestiÃ³n de Estado

Siguiendo las mejores prÃ¡cticas modernas, **no utilizaremos Global State (Zustand) para almacenar las reservas ni las fechas temporales**. Mezclar el cachÃ© de servidor con estado global conduce a problemas graves de sincronizaciÃ³n.

### 3.1 Server State (React Query / SWR)
Toda la data persistente que viene del backend vive aquÃ­.

- **Hook:** `useBookings()`
  - **QueryKey:** `['bookings', 'my-trips', page]`
  - **Uso:** Importado a nivel de la pÃ¡gina `MyBookingsPage` y pasado hacia abajo.
  
- **Mutation:** `useCreateBooking()`
  - **OnSuccess Behavior:** Llama a `queryClient.invalidateQueries(['bookings'])` para asegurar que, si el turista regresa a su listado, vea la nueva reserva inmediatamente sin tener que refrescar la pÃ¡gina.

### 3.2 Global State (Zustand)
- **NO SE USA** en este mÃ³dulo. 
- *DecisiÃ³n ArquitectÃ³nica:* Evitamos usar un `BookingSlice` para mover la finca o fechas escogidas hacia el Checkout. En su lugar usaremos **Deep Linking / URL Params** (ej. `/checkout?propertyId=123&checkIn=2026-12-01`). Esto permite que el Turista comparta el enlace con su pareja o recargue la pÃ¡gina sin perder los datos de reserva.

### 3.3 Local State (React `useState`)
- Abierto/Cerrado del `DatePicker` (en `BookingForm`).
- Variables temporales del nÃºmero de huÃ©spedes.
- Abierto/Cerrado del modal de confirmaciÃ³n de cancelaciÃ³n (en `BookingCard`).

---

## 4. Downstream Consumers
- **Phase 7 â€” D6 (Frontend UI & State Implementation):** El desarrollador de React/Next.js tomarÃ¡ este documento como su plano de construcciÃ³n (Blueprint). CrearÃ¡ exactamente estos componentes, copiarÃ¡ y pegarÃ¡ las props tipadas, e instanciarÃ¡ los hooks de React Query con las `queryKeys` aquÃ­ escritas.

