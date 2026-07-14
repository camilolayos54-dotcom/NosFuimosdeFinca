# Entregable 11 (D11): Matriz de AutorizaciÃ³n y Seguridad

**Proyecto:** Nos Fuimos de Finca
**Fase:** 4 â€” Modelado del Sistema
**Estado:** Aprobado

---

## 1. ConfiguraciÃ³n Global de Seguridad (AuthN)

*Backlink a Fase 3:* Estas polÃ­ticas de seguridad (incluyendo JWT, Roles de Usuario y RLS) implementan las directivas obligatorias de los NFRs y los Actores identificados en `[[PHASE_3_REQUIREMENTS_ENGINEERING/2.Actor_and_Role_Definition]]`.

- **Proveedor:** Spring Security + JWT.
- **Mecanismo:** JWT (gestionado por Spring Security).
- **Cabecera HTTP:** `Authorization: Bearer <postgresql_jwt>`
- **Access Token TTL:** 1 hora (manejado por Spring Security).
- **Refresh Token:** Manejado automÃ¡ticamente por el Spring Security.
- **RotaciÃ³n:** PostgreSQL rota los Refresh Tokens en cada uso.

**Whitelist â€” Rutas Exentas del RLS/Middleware:**
| Ruta | MÃ©todo | Mecanismo Alternativo |
|---|---|---|
| `/api/v1/auth/*` | POST | Spring Security REST Auth |
| `/api/v1/properties` | GET | Ninguno â€” catÃ¡logo pÃºblico (Anon Key) |
| `/api/v1/properties/*` | GET | Ninguno â€” catÃ¡logo pÃºblico (Anon Key) |
| `/api/v1/webhooks/wompi` | POST | ValidaciÃ³n HMAC-SHA256 de Wompi |

---

## 2. Matriz de Visibilidad UI (Frontend)

| Ruta Frontend | Public (AnÃ³n) | TOURIST | OWNER_API | AGENCY_USER |
|:---|:---|:---|:---|:---|
| `/` (Marketplace) | Leer | Leer | Leer | Leer |
| `/finca/[slug]` | Leer | Leer | Leer | Leer |
| `/checkout/[id]` | Leer (c/Soft-Lock) | Leer | Redirigir â†’ `/` | Leer |
| `/login`, `/register` | Leer | Redirigir â†’ `/` | Redirigir â†’ `/dashboard` | Redirigir â†’ `/dashboard` |
| `/onboarding` (KYC) | Redirigir â†’ `/login` | Redirigir â†’ `/login` | Leer (si pending) | N/A |
| `/dashboard/*` | Oculto (403) | Oculto (403) | Modificar | Modificar |
| `/admin/*` | Oculto (403) | Oculto (403) | Oculto (403) | Oculto (403) |
| `/terminos`, `/privacidad` | Leer | Leer | Leer | Leer |
| `/404`, `/403`, `/500` | Leer | Leer | Leer | Leer |

---

## 3. Matriz de Acceso API y Spring Security (Backend)

**Leyenda:**
- `Allow (OWN)`: Spring Security verifica que el JWT `userId` coincide con el campo de propiedad.
- `Allow (ALL)`: Sin verificaciÃ³n de RLS.
- `Deny (403)`: PolÃ­tica RLS bloquea o middleware rechaza la peticiÃ³n.

| Endpoint / Tabla | MÃ©todo | Public | TOURIST | OWNER_API | AGENCY_USER |
|:---|:---|:---|:---|:---|:---|
| `/auth/*` | POST | Allow (ALL) | Allow (ALL) | Allow (ALL) | Allow (ALL) |
| `/properties` | GET | Allow (ALL) | Allow (ALL) | Allow (ALL) | Allow (ALL) |
| `/properties/:id` | GET | Allow (ALL) | Allow (ALL) | Allow (ALL) | Allow (ALL) |
| `/properties` | POST | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |
| `/properties/:id` | PATCH | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |
| `/properties/:id` | DELETE | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |
| `/properties/:id/images` | POST | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |
| `/bookings` | POST | Deny (403) | Allow (OWN) | Deny (403) | Allow (OWN) |
| `/bookings` | GET | Deny (403) | Allow (OWN) | Allow (OWN) | Allow (OWN) |
| `/bookings/:id` | PATCH | Deny (403) | Allow (OWN) | Allow (OWN) | Allow (OWN) |
| `/payouts` | GET | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |
| `/wishlists` | GET, POST, DELETE | Deny (403) | Allow (OWN) | Deny (403) | Deny (403) |
| `/coupons/validate` | POST | Deny (403) | Allow (ALL) | Allow (ALL) | Allow (ALL) |
| `/properties/:id/seasonal-prices` | POST, PATCH | Deny (403) | Deny (403) | Allow (OWN) | Deny (403) |

**ImplementaciÃ³n de RLS (Row Level Security) en PostgreSQL:**
- `bookings` (TOURIST / AGENCY_USER): `(userId del JWT = guest_id)`
- `bookings` (OWNER_API): `(EXISTS (SELECT 1 FROM properties WHERE properties.id = bookings.property_id AND properties.host_id = userId del JWT))`
- `properties` (OWNER_API): `(userId del JWT = host_id)`
- `payouts` (OWNER_API): `(userId del JWT = host_id)`
- `wishlists` (TOURIST): `(userId del JWT = user_id)`
- `seasonal_prices` (OWNER_API): `(EXISTS (SELECT 1 FROM properties WHERE properties.id = seasonal_prices.property_id AND properties.host_id = userId del JWT))`
- `coupons`: `(auth.role() = 'service_role')` (Solo admin puede crearlos, validaciÃ³n es vÃ­a Stored Procedure).

---

## ImplicaciÃ³n de Fase

- El equipo de Frontend (Track A) puede condicionar la navegaciÃ³n con PostgreSQL SDK (ej. `jwtTokenUtil.getUser(request)`) y proteger rutas B2B (Dashboard).
- El equipo de Base de Datos y Backend (Track B) no necesita programar middlewares manuales extensos; solo aplica las polÃ­ticas RLS directamente en la base de datos PostgreSQL de PostgreSQL.
- **Proceder a D12:** SÃ­ntesis de SeÃ±ales ArquitectÃ³nicas.

