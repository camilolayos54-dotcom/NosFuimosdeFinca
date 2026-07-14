# Deliverable 12 (D12): i18n Technical Implementation

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved (Global Deliverable)

*Backlink a Fase 4:* Este documento aterriza los requisitos de idioma y regionalizaciÃ³n plasmados en la `Localization Strategy` (Fase 4, D14) a cÃ³digo ejecutable, determinando librerÃ­as, estructuras y protocolos de fallo.

---

## 2. LibrerÃ­a y Mecanismo de Cambio de Idioma

### 2.1 LibrerÃ­a Seleccionada
Para alinearnos con nuestra decisiÃ³n de usar Next.js App Router (React Server Components), utilizaremos la librerÃ­a **`next-intl`**.
- **JustificaciÃ³n:** A diferencia de `react-i18next`, `next-intl` soporta traducciones del lado del servidor nativamente sin necesidad de forzar los componentes a ser `use client`, protegiendo nuestro rendimiento y tamaÃ±o del bundle.

### 2.2 Estrategia de ResoluciÃ³n de Idioma (Prioridad)
No adivinaremos mÃ¡gicamente el idioma. Seguiremos esta estricta cadena de mando:

1. **Prioridad 1 (Prefijo URL):** Si la ruta explÃ­citamente dice `/en/checkout`, el sistema **debe** renderizar en InglÃ©s. Esto es obligatorio para habilitar el SEO multi-idioma.
2. **Prioridad 2 (Cookie `NEXT_LOCALE`):** Si un Turista entrÃ³ ayer a la raÃ­z `/` y seleccionÃ³ manualmente InglÃ©s, el sistema guardÃ³ esta cookie. Al volver a entrar a `/`, serÃ¡ redirigido inmediatamente a `/en`.
3. **Prioridad 3 (Header `Accept-Language`):** Para visitantes primerizos sin cookies. Si su navegador pide inglÃ©s, Next.js Middleware los intercepta y los manda a `/en`.
4. **Prioridad 4 (Fallback - Default):** Si el idioma que piden no lo soportamos (ej. JaponÃ©s), el sistema cae en gracia al espaÃ±ol (`es`).

---

## 3. Estructura de Archivos y ConvenciÃ³n de Keys

Tener un archivo gigante `translations.json` de 5,000 lÃ­neas crea cuellos de botella para el equipo. La estructura de carpetas serÃ¡ dividida por MÃ³dulo de Negocio (Domain-Driven).

### 3.1 Estructura en el Repositorio
```text
src/
â””â”€â”€ locales/
    â”œâ”€â”€ es/
    â”‚   â”œâ”€â”€ common.json      # Botones (Aceptar, Cerrar), Navbar genÃ©rico.
    â”‚   â”œâ”€â”€ auth.json        # MÃ³dulo Auth (Login, Registro).
    â”‚   â”œâ”€â”€ catalog.json     # MÃ³dulo CatÃ¡logo (BÃºsqueda, Filtros).
    â”‚   â””â”€â”€ booking.json     # MÃ³dulo Booking Engine.
    â””â”€â”€ en/
        â”œâ”€â”€ common.json
        â”œâ”€â”€ auth.json
        â”œâ”€â”€ catalog.json
        â””â”€â”€ booking.json
```

### 3.2 ConvenciÃ³n de Keys
Las claves deben estar anidadas lÃ³gicamente y en `camelCase`. Prohibido usar _flat structures_.

```json
// CORRECTO (booking.json)
{
  "checkoutForm": {
    "title": "Confirma tu reserva",
    "labels": {
      "checkIn": "Fecha de llegada",
      "checkOut": "Fecha de salida"
    },
    "guestCountMessage": "{count, plural, =1 {1 huÃ©sped} other {# huÃ©spedes}}"
  }
}

// INCORRECTO (Prohibido)
{
  "checkoutFormTitle": "Confirma tu reserva",
  "checkoutFormCheckInLabel": "Fecha de llegada"
}
```

> [!CAUTION]
> **Cero Llaves HuÃ©rfanas:** Un pipeline de GitHub Actions se encargarÃ¡ de comprobar que cada llave que exista en `/es/archivo.json` deba existir exactamente con el mismo path en `/en/archivo.json`. Si un desarrollador olvida traducir una llave, el PR serÃ¡ bloqueado.

---

## 4. Protocolo de Errores Localizables del Backend

El backend no sabe de idiomas. El backend solo habla "CÃ³digos".

### 4.1 Contrato del Backend
Cuando una regla de negocio falla, la API debe devolver `code` en formato `DOMINIO_MOTIVO` (`UPPER_SNAKE_CASE`). El atributo `message` adjunto estarÃ¡ en inglÃ©s tÃ©cnico solo para consumo de desarrolladores en la consola/Sentry.

```json
{
  "error": {
    "code": "BOOKING_DATES_OVERLAP",
    "message": "The requested dates overlap with an existing approved booking."
  }
}
```

### 4.2 ResoluciÃ³n en Frontend
El Frontend alojarÃ¡ un archivo `errors.json` en ambas carpetas (`es`, `en`). En tiempo de ejecuciÃ³n, el frontend utilizarÃ¡ el `code` devuelto por el servidor como llave para extraer la frase humana amigable.

```json
// src/locales/es/errors.json
{
  "BOOKING_DATES_OVERLAP": "Las fechas seleccionadas ya estÃ¡n ocupadas. Por favor intenta con otras.",
  "AUTH_USER_SUSPENDED": "Tu cuenta se encuentra suspendida temporalmente."
}
```

**Ejemplo de implementaciÃ³n (Frontend):**
```tsx
const { error } = await createBooking(data);
// âŒ PROHIBIDO: 
// toast(error.message); 
// âœ… CORRECTO: 
toast( t(`errors.${error.code}`) );
```

---

## 5. Downstream Consumers
- **Phase 7 â€” D6 (Frontend UI Implementation):** El desarrollador de UI configurarÃ¡ `next-intl` en el `middleware.ts` de Next.js obedeciendo estrictamente el orden de prioridad listado en la secciÃ³n 2.2.
- **Phase 7 â€” D5 (Backend API Implementation):** El desarrollador backend debe configurar su manejador global de excepciones para asegurar que ningÃºn error nativo (ej. `PostgresError`) se filtre como un string crudo, envolviÃ©ndolos todos en cÃ³digos `UPPER_SNAKE_CASE`.

