# Deliverable 12 (D12): i18n Technical Implementation

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved (Global Deliverable)

*Backlink a Fase 4:* Este documento aterriza los requisitos de idioma y regionalizacion plasmados en la `Localization Strategy` (Fase 4, D14) a codigo ejecutable, determinando librerias, estructuras y protocolos de fallo.

---

## 2. Libreria y Mecanismo de Cambio de Idioma

### 2.1 Libreria Seleccionada
Para alinearnos con nuestra decision de usar Spring Boot REST API (Vite + JavaScript (frontend) Spring MVC @RestController), utilizaremos la libreria **`next-intl`**.
- **Justificacion:** A diferencia de `react-i18next`, `next-intl` soporta traducciones del lado del servidor nativamente sin necesidad de forzar los componentes a ser `use client`, protegiendo nuestro rendimiento y tamano del bundle.

### 2.2 Estrategia de Resolucion de Idioma (Prioridad)
No adivinaremos magicamente el idioma. Seguiremos esta estricta cadena de mando:

1. **Prioridad 1 (Prefijo URL):** Si la ruta explicitamente dice `/en/checkout`, el sistema **debe** renderizar en Ingles. Esto es obligatorio para habilitar el SEO multi-idioma.
2. **Prioridad 2 (Cookie `NEXT_LOCALE`):** Si un Turista entro ayer a la raiz `/` y selecciono manualmente Ingles, el sistema guardo esta cookie. Al volver a entrar a `/`, sera redirigido inmediatamente a `/en`.
3. **Prioridad 3 (Header `Accept-Language`):** Para visitantes primerizos sin cookies. Si su navegador pide ingles, Spring Security Filter Chain los intercepta y los manda a `/en`.
4. **Prioridad 4 (Fallback - Default):** Si el idioma que piden no lo soportamos (ej. Japones), el sistema cae en gracia al espanol (`es`).

---

## 3. Estructura de Archivos y Convencion de Keys

Tener un archivo gigante `translations.json` de 5,000 lineas crea cuellos de botella para el equipo. La estructura de carpetas sera dividida por Modulo de Negocio (Domain-Driven).

### 3.1 Estructura en el Repositorio
```text
src/
â””â”€â”€ locales/
    â”œâ”€â”€ es/
    â”‚   â”œâ”€â”€ common.json      # Botones (Aceptar, Cerrar), Navbar generico.
    â”‚   â”œâ”€â”€ auth.json        # Modulo Auth (Login, Registro).
    â”‚   â”œâ”€â”€ catalog.json     # Modulo Catalogo (Busqueda, Filtros).
    â”‚   â””â”€â”€ booking.json     # Modulo Booking Engine.
    â””â”€â”€ en/
        â”œâ”€â”€ common.json
        â”œâ”€â”€ auth.json
        â”œâ”€â”€ catalog.json
        â””â”€â”€ booking.json
```

### 3.2 Convencion de Keys
Las claves deben estar anidadas logicamente y en `camelCase`. Prohibido usar _flat structures_.

```json
// CORRECTO (booking.json)
{
  "checkoutForm": {
    "title": "Confirma tu reserva",
    "labels": {
      "checkIn": "Fecha de llegada",
      "checkOut": "Fecha de salida"
    },
    "guestCountMessage": "{count, plural, =1 {1 huesped} other {# huespedes}}"
  }
}

// INCORRECTO (Prohibido)
{
  "checkoutFormTitle": "Confirma tu reserva",
  "checkoutFormCheckInLabel": "Fecha de llegada"
}
```

> [!CAUTION]
> **Cero Llaves Huerfanas:** Un pipeline de GitHub Actions se encargara de comprobar que cada llave que exista en `/es/archivo.json` deba existir exactamente con el mismo path en `/en/archivo.json`. Si un desarrollador olvida traducir una llave, el PR sera bloqueado.

---

## 4. Protocolo de Errores Localizables del Backend

El backend no sabe de idiomas. El backend solo habla "Codigos".

### 4.1 Contrato del Backend
Cuando una regla de negocio falla, la API debe devolver `code` en formato `DOMINIO_MOTIVO` (`UPPER_SNAKE_CASE`). El atributo `message` adjunto estara en ingles tecnico solo para consumo de desarrolladores en la consola/Sentry.

```json
{
  "error": {
    "code": "BOOKING_DATES_OVERLAP",
    "message": "The requested dates overlap with an existing approved booking."
  }
}
```

### 4.2 Resolucion en Frontend
El Frontend alojara un archivo `errors.json` en ambas carpetas (`es`, `en`). En tiempo de ejecucion, el frontend utilizara el `code` devuelto por el servidor como llave para extraer la frase humana amigable.

```json
// src/locales/es/errors.json
{
  "BOOKING_DATES_OVERLAP": "Las fechas seleccionadas ya estan ocupadas. Por favor intenta con otras.",
  "AUTH_USER_SUSPENDED": "Tu cuenta se encuentra suspendida temporalmente."
}
```

**Ejemplo de implementacion (Frontend):**
```tsx
const { error } = await createBooking(data);
// âŒ PROHIBIDO: 
// toast(error.message); 
// âœ… CORRECTO: 
toast( t(`errors.${error.code}`) );
```

---

## 5. Downstream Consumers
- **Phase 7 â€” D6 (Frontend UI Implementation):** El desarrollador de UI configurara `next-intl` en el `SecurityConfig.java` de Spring Boot (Java) obedeciendo estrictamente el orden de prioridad listado en la seccion 2.2.
- **Phase 7 â€” D5 (Backend API Implementation):** El desarrollador backend debe configurar su manejador global de excepciones para asegurar que ningun error nativo (ej. `PostgresError`) se filtre como un string crudo, envolviendolos todos en codigos `UPPER_SNAKE_CASE`.

