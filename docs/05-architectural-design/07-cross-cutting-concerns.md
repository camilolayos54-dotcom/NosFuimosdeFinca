# Entregable 7 (D7): Cross-Cutting Concerns

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 5 â€” Architectural Design
**Estado:** Aprobado

*Backlink a Fase 4:* Las politicas de IAM de este documento formalizan tecnicamente los requerimientos de la matriz de Autorizacion (`[[PHASE_4_SYSTEM_MODELING/11.Authorization_and_Security/example_output_d11_security.md]]`).

---

## 2. IAM & Security Strategy

Las politicas de gestion de identidad y acceso perimetral para el Modular Monolith son:

- **Access Token:** JWT estandarizado (PostgreSQL GoTrue), con una duracion corta obligatoria de 1 hora.
- **Refresh Token:** Rotacion automatica gestionada por el SDK de PostgreSQL en cada uso. Si un token de refresco es interceptado, el intento de uso doble invalida inmediatamente la sesion completa del usuario.
- **Almacenamiento en Frontend:** Se usaran estrictamente **HttpOnly Cookies** implementadas mediante `spring-security` en Spring Boot. El uso de `LocalStorage` queda prohibido debido al riesgo de ataques XSS (robo de JWT via JavaScript).
- **Politica CORS (Cross-Origin Resource Sharing):** Dado que la aplicacion es un monolito servido desde un unico dominio (Frontend y API viven juntos en Railway/Render), la politica CORS base sera `SAMEORIGIN`. Se rechazaran peticiones de origenes externos para prevenir ataques CSRF. La unica excepcion explicita seran las rutas `/api/webhooks/*` (Wompi y WhatsApp), las cuales tendran CORS abierto pero validacion por firmas criptograficas HMAC.
- **Rate-Limiting (Proteccion Anti-DDoS/Abuso):** 
  - *Rutas Publicas (Catalogo):* 100 peticiones / minuto por IP.
  - *Rutas Criticas (Auth, Checkout):* 10 peticiones / minuto por IP.
  - *Respuesta:* HTTP `429 Too Many Requests` indicando el tiempo de espera en la cabecera `Retry-After`.

---

## 3. Observability, Error Handling & Caching Strategy

Para poder rastrear problemas transversales en el sistema, aplicaremos los siguientes estandares globales:

- **Formato de Logs:** Structured JSON Logging. Cada log emitido por la aplicacion debe ser un objeto JSON parseable por maquinas con, al menos, los campos: `timestamp` (ISO-8601), `level` (INFO, WARN, ERROR), `module` (Booking, Catalog, etc.), `message`, y `traceId` (UUID).
- **Captura de Excepciones (APM):** Utilizaremos **Sentry** acoplado al Railway/Render Edge y a los Spring MVC @RestController de Spring Boot (Java) para atrapar errores 500 no capturados y reportar trazas de ejecucion automaticamente.
- **Estructura de Error API:** Para garantizar que el Frontend reciba errores predecibles (y enlazando con la decision D9 de la Fase 4), todas las APIs deben retornar esta estructura exacta ante un fallo:
  ```json
  {
    "error": {
      "code": "STRING_CONST_CODE",
      "message": "Mensaje legible en espanol",
      "details": "Lista de errores de validacion (opcional)",
      "traceId": "uuid-for-sentry-correlation",
      "timestamp": "2026-07-13T12:00:00Z"
    }
  }
  ```

- **Capas de Cache e Invalidacion:**
  | Capa | Herramienta | Que cachea | Estrategia de Invalidacion |
  |---|---|---|---|
  | Assets / Media HD | Cloudinary / S3 para imagenes (CDN) | Fotos de fincas | Immutable: Cache-Control infinito. Se utiliza *versionado* en el nombre de archivo (ej. `finca_v2.jpg`) al cambiar la foto. |
  | Catalogo y APIs | Railway/Render Data Cache (Spring Cache (@Cacheable)) | Listado y detalles de Fincas | Hibrida: *On-Demand Revalidation* (por evento, cuando el Host modifica su finca) + *Time-based Revalidation* (TTL de 60s como respaldo seguro). |
  | Base de Datos | PostgreSQL Shared Buffers | Consultas repetitivas | Automatica. (No se anade Redis aun para evitar sobrecarga operativa, priorizando Time-to-Market). |

---

## 4. Downstream Consumers
Este entregable es input obligatorio para:
- **Phase 6 â€” D4 (Security Implementation & Middleware):** Obliga a los desarrolladores a programar el Middleware de Spring Boot (Java) (`SecurityConfig.java`) para inyectar los headers de CORS restrictivos, validar las HttpOnly Cookies y configurar el Rate-Limiting.
- **Phase 6 â€” D10 (Async Workers & Job Scheduling):** Establece como las funciones de invalidacion (Spring Cache (@Cacheable) On-Demand) se deben orquestar tras las escrituras en base de datos.
- **D8 (CI/CD & Environments Strategy):** Sentry debe ser configurado como paso obligatorio en el pipeline de CI/CD para cargar los Source Maps del codigo minificado en Produccion.

