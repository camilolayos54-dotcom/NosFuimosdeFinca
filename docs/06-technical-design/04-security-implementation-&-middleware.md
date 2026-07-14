# Deliverable 4 (D4): Security Implementation & Middleware

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved

*Backlink a Fase 4:* Este entregable implementa fisicamente los permisos y barreras teoricas definidas en la matriz de autorizacion `[[PHASE_4_SYSTEM_MODELING/11.Authorization_and_Security/example_output_d11_authorization_matrix.md]]`.

---

## 2. Especificacion de Criptografia y Token

### 2.1 Cifrado y Hashing
- **Hashing de Contrasenas:** Se utilizara **bcrypt** con factor de coste `saltRounds=10`. Esto es manejado de forma nativa por el motor de identidad del PostgreSQL + Spring Boot (PostgreSQL GoTrue), ofreciendo resistencia comprobada contra ataques de fuerza bruta offline.
- **Cifrado de PII en Reposo (Encryption at Rest):** No se desarrollara cifrado simetrico adicional a nivel de codigo de aplicacion (ej. cifrar manualmente con llaves AWS KMS antes del `INSERT`). Nos apoyaremos en el cifrado AES-256 a nivel de volumen de disco fisico que provee la infraestructura (AWS/PostgreSQL) y protegeremos el acceso logico a la PII (`bank_account_number`, `document_number`) utilizando PostgreSQL Row Level Security (Spring Security + Row-Level Filtering) en el diseno de base de datos (Fase 6 D2).

### 2.2 Ciclo de Vida del Token (Session Lifecycle)
- **Proveedor:** JWT generado asimetricamente por Spring Security + JWT, firmado mediante `HS256`.
- **Estrategia de Almacenamiento Frontend:** Dado el framework Spring Boot (Java) con soporte Server-Side Rendering (SSR), el token se transmitira exclusivamente mediante **Cookies** con los flags `HttpOnly=true`, `Secure=true` y `SameSite=Lax`. **Esta terminantemente prohibido almacenar tokens en `localStorage`**, eliminando asi la superficie de ataque para inyecciones de scripts (XSS).
- **Tiempos de Expiracion:**
  - `AccessToken` (Vida corta): 1 hora.
  - `RefreshToken` (Sesion prolongada): 7 dias.

---

## 3. Pseudocodigo / Logica de Middleware (Spring Boot (Java) Edge)

El archivo central de seguridad (Spring Boot (Java) `SecurityConfig.java`) se ejecutara en la capa *Edge* antes de que cualquier request toque la base de datos o el frontend renderizado. Contiene dos barreras:

### 3.1 Estrategia de Revocacion y AuthGuard (Identidad)
Validacion *Activa*. No nos confiaremos de la lectura en memoria del JWT. Usaremos la libreria `postgresql/ssr` para verificar contra la BBDD si la sesion sigue activa, permitiendo la revocacion instantanea (ej. si el usuario cambia la contrasena en otro equipo).

```text
1. INICIO: Request interceptado en el Edge de Railway/Render/Spring Boot (Java).
2. Extraer cookie `sb-[project]-auth-token`.
3. Validar sesion: await postgresql.auth.getUser()
4. IF sesion es INVÃLIDA (No hay token, expirado o revocado activamente):
     5. IF ruta es `/api/*` (Llamada REST interna):
          6. RETURN HTTP 401 Unauthorized.
     7. IF ruta es protegida web (`/host/*`, `/guest/*`, `/admin/*`):
          8. RETURN HTTP 302 Redirection -> `/login`.
9. ELSE (Identidad confirmada):
     10. Extraer `user.user_metadata.custom_role` (tourist | host | admin).
     11. Pasar el control a RoleGuard.
```

### 3.2 RoleGuard (Autorizacion)
Evalua los permisos segun la Matriz de la Fase 4 D11.

```text
12. INICIO ROLEGUARD.
13. Determinar el contexto de la ruta solicitada.
14. IF ruta inicia con `/host/`:
      15. IF rol_del_usuario !== 'host' AND !== 'admin':
          16. RETURN HTTP 403 Forbidden. (No tiene permiso de propietario)
17. IF ruta inicia con `/admin/`:
      18. IF rol_del_usuario !== 'admin':
          19. RETURN HTTP 403 Forbidden.
20. IF ruta es Webhook Externo (ej. `/api/wompi-webhook`):
      21. (Bypass de AuthGuard regular)
      22. Validar firma SHA-256 contra el body con `WOMPI_WEBHOOK_SECRET` de D3.
      23. IF firma NO COINCIDE:
          24. RETURN HTTP 403 Forbidden.
25. RETURN next() (Permitir el paso al Spring Boot Service Method o la pagina).
```

---

## 4. Downstream Consumers
Este entregable blinda al sistema contra intrusiones antes del inicio de codigo:
- **Phase 6 â€” D7 (API Contracts):** OpenApi.yml utilizara el requerimiento de Cookie de Sesion como el esquema de seguridad global estandar.
- **Phase 7 â€” D7 (Security & Middleware Implementation):** Sera el manual directo de codificacion del desarrollador encargado de escribir el archivo maestro `SecurityConfig.java` del repositorio Spring Boot (Java).

