# Deliverable 4 (D4): Security Implementation & Middleware

## 1. Metadata Header
**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” Technical Design
**Estado:** Approved

*Backlink a Fase 4:* Este entregable implementa fÃ­sicamente los permisos y barreras teÃ³ricas definidas en la matriz de autorizaciÃ³n `[[PHASE_4_SYSTEM_MODELING/11.Authorization_and_Security/example_output_d11_authorization_matrix.md]]`.

---

## 2. EspecificaciÃ³n de CriptografÃ­a y Token

### 2.1 Cifrado y Hashing
- **Hashing de ContraseÃ±as:** Se utilizarÃ¡ **bcrypt** con factor de coste `saltRounds=10`. Esto es manejado de forma nativa por el motor de identidad del BaaS (Supabase GoTrue), ofreciendo resistencia comprobada contra ataques de fuerza bruta offline.
- **Cifrado de PII en Reposo (Encryption at Rest):** No se desarrollarÃ¡ cifrado simÃ©trico adicional a nivel de cÃ³digo de aplicaciÃ³n (ej. cifrar manualmente con llaves AWS KMS antes del `INSERT`). Nos apoyaremos en el cifrado AES-256 a nivel de volumen de disco fÃ­sico que provee la infraestructura (AWS/Supabase) y protegeremos el acceso lÃ³gico a la PII (`bank_account_number`, `document_number`) utilizando PostgreSQL Row Level Security (RLS) en el diseÃ±o de base de datos (Fase 6 D2).

### 2.2 Ciclo de Vida del Token (Session Lifecycle)
- **Proveedor:** JWT generado asimÃ©tricamente por Supabase Auth, firmado mediante `HS256`.
- **Estrategia de Almacenamiento Frontend:** Dado el framework Next.js con soporte Server-Side Rendering (SSR), el token se transmitirÃ¡ exclusivamente mediante **Cookies** con los flags `HttpOnly=true`, `Secure=true` y `SameSite=Lax`. **EstÃ¡ terminantemente prohibido almacenar tokens en `localStorage`**, eliminando asÃ­ la superficie de ataque para inyecciones de scripts (XSS).
- **Tiempos de ExpiraciÃ³n:**
  - `AccessToken` (Vida corta): 1 hora.
  - `RefreshToken` (SesiÃ³n prolongada): 7 dÃ­as.

---

## 3. PseudocÃ³digo / LÃ³gica de Middleware (Next.js Edge)

El archivo central de seguridad (Next.js `middleware.ts`) se ejecutarÃ¡ en la capa *Edge* antes de que cualquier request toque la base de datos o el frontend renderizado. Contiene dos barreras:

### 3.1 Estrategia de RevocaciÃ³n y AuthGuard (Identidad)
ValidaciÃ³n *Activa*. No nos confiaremos de la lectura en memoria del JWT. Usaremos la librerÃ­a `supabase/ssr` para verificar contra la BBDD si la sesiÃ³n sigue activa, permitiendo la revocaciÃ³n instantÃ¡nea (ej. si el usuario cambia la contraseÃ±a en otro equipo).

```text
1. INICIO: Request interceptado en el Edge de Vercel/Next.js.
2. Extraer cookie `sb-[project]-auth-token`.
3. Validar sesiÃ³n: await supabase.auth.getUser()
4. IF sesiÃ³n es INVÃLIDA (No hay token, expirado o revocado activamente):
     5. IF ruta es `/api/*` (Llamada REST interna):
          6. RETURN HTTP 401 Unauthorized.
     7. IF ruta es protegida web (`/host/*`, `/guest/*`, `/admin/*`):
          8. RETURN HTTP 302 Redirection -> `/login`.
9. ELSE (Identidad confirmada):
     10. Extraer `user.user_metadata.custom_role` (tourist | host | admin).
     11. Pasar el control a RoleGuard.
```

### 3.2 RoleGuard (AutorizaciÃ³n)
EvalÃºa los permisos segÃºn la Matriz de la Fase 4 D11.

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
25. RETURN next() (Permitir el paso al Server Action o la pÃ¡gina).
```

---

## 4. Downstream Consumers
Este entregable blinda al sistema contra intrusiones antes del inicio de cÃ³digo:
- **Phase 6 â€” D7 (API Contracts):** OpenApi.yml utilizarÃ¡ el requerimiento de Cookie de SesiÃ³n como el esquema de seguridad global estÃ¡ndar.
- **Phase 7 â€” D7 (Security & Middleware Implementation):** SerÃ¡ el manual directo de codificaciÃ³n del desarrollador encargado de escribir el archivo maestro `middleware.ts` del repositorio Next.js.

