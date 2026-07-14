# Entregable 7 (D7): Cross-Cutting Concerns

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4:* Las polÃ­ticas de IAM de este documento formalizan tÃ©cnicamente los requerimientos de la matriz de AutorizaciÃ³n (`[[PHASE_4_SYSTEM_MODELING/11.Authorization_and_Security/example_output_d11_security.md]]`).

---

## 2. IAM & Security Strategy

Las polÃ­ticas de gestiÃ³n de identidad y acceso perimetral para el Modular Monolith son:

- **Access Token:** JWT estandarizado (Supabase GoTrue), con una duraciÃ³n corta obligatoria de 1 hora.
- **Refresh Token:** RotaciÃ³n automÃ¡tica gestionada por el SDK de Supabase en cada uso. Si un token de refresco es interceptado, el intento de uso doble invalida inmediatamente la sesiÃ³n completa del usuario.
- **Almacenamiento en Frontend:** Se usarÃ¡n estrictamente **HttpOnly Cookies** implementadas mediante `@supabase/ssr` en Next.js. El uso de `LocalStorage` queda prohibido debido al riesgo de ataques XSS (robo de JWT vÃ­a JavaScript).
- **PolÃ­tica CORS (Cross-Origin Resource Sharing):** Dado que la aplicaciÃ³n es un monolito servido desde un Ãºnico dominio (Frontend y API viven juntos en Vercel), la polÃ­tica CORS base serÃ¡ `SAMEORIGIN`. Se rechazarÃ¡n peticiones de orÃ­genes externos para prevenir ataques CSRF. La Ãºnica excepciÃ³n explÃ­cita serÃ¡n las rutas `/api/webhooks/*` (Wompi y WhatsApp), las cuales tendrÃ¡n CORS abierto pero validaciÃ³n por firmas criptogrÃ¡ficas HMAC.
- **Rate-Limiting (ProtecciÃ³n Anti-DDoS/Abuso):** 
  - *Rutas PÃºblicas (CatÃ¡logo):* 100 peticiones / minuto por IP.
  - *Rutas CrÃ­ticas (Auth, Checkout):* 10 peticiones / minuto por IP.
  - *Respuesta:* HTTP `429 Too Many Requests` indicando el tiempo de espera en la cabecera `Retry-After`.

---

## 3. Observability, Error Handling & Caching Strategy

Para poder rastrear problemas transversales en el sistema, aplicaremos los siguientes estÃ¡ndares globales:

- **Formato de Logs:** Structured JSON Logging. Cada log emitido por la aplicaciÃ³n debe ser un objeto JSON parseable por mÃ¡quinas con, al menos, los campos: `timestamp` (ISO-8601), `level` (INFO, WARN, ERROR), `module` (Booking, Catalog, etc.), `message`, y `traceId` (UUID).
- **Captura de Excepciones (APM):** Utilizaremos **Sentry** acoplado al Vercel Edge y a los Server Components de Next.js para atrapar errores 500 no capturados y reportar trazas de ejecuciÃ³n automÃ¡ticamente.
- **Estructura de Error API:** Para garantizar que el Frontend reciba errores predecibles (y enlazando con la decisiÃ³n D9 de la Fase 4), todas las APIs deben retornar esta estructura exacta ante un fallo:
  ```json
  {
    "error": {
      "code": "STRING_CONST_CODE",
      "message": "Mensaje legible en espaÃ±ol",
      "details": "Lista de errores de validaciÃ³n (opcional)",
      "traceId": "uuid-for-sentry-correlation",
      "timestamp": "2026-07-13T12:00:00Z"
    }
  }
  ```

- **Capas de CachÃ© e InvalidaciÃ³n:**
  | Capa | Herramienta | QuÃ© cachea | Estrategia de InvalidaciÃ³n |
  |---|---|---|---|
  | Assets / Media HD | Supabase Storage (CDN) | Fotos de fincas | Immutable: Cache-Control infinito. Se utiliza *versionado* en el nombre de archivo (ej. `finca_v2.jpg`) al cambiar la foto. |
  | CatÃ¡logo y APIs | Vercel Data Cache (ISR) | Listado y detalles de Fincas | HÃ­brida: *On-Demand Revalidation* (por evento, cuando el Host modifica su finca) + *Time-based Revalidation* (TTL de 60s como respaldo seguro). |
  | Base de Datos | PostgreSQL Shared Buffers | Consultas repetitivas | AutomÃ¡tica. (No se aÃ±ade Redis aÃºn para evitar sobrecarga operativa, priorizando Time-to-Market). |

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 â€” D4 (Security Implementation & Middleware):** Obliga a los desarrolladores a programar el Middleware de Next.js (`middleware.ts`) para inyectar los headers de CORS restrictivos, validar las HttpOnly Cookies y configurar el Rate-Limiting.
- **Phase 6 â€” D10 (Async Workers & Job Scheduling):** Establece cÃ³mo las funciones de invalidaciÃ³n (ISR On-Demand) se deben orquestar tras las escrituras en base de datos.
- **D8 (CI/CD & Environments Strategy):** Sentry debe ser configurado como paso obligatorio en el pipeline de CI/CD para cargar los Source Maps del cÃ³digo minificado en ProducciÃ³n.

