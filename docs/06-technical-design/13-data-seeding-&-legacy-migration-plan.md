# Deliverable 13 (D13): Data Seeding & Legacy Migration Plan

**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 â€” DiseÃ±o TÃ©cnico
**Estado:** Aprobado

---

## 1. CatÃ¡logo de Datos Inmutables

Estas entidades serÃ¡n inyectadas vÃ­a script (`seed.ts` o `seed.sql`) durante el despliegue inicial a producciÃ³n. El sistema no puede funcionar sin ellas:

- **Roles:** `ADMIN`, `HOST`, `GUEST`
- **Estados de Reserva (Booking Statuses):** `PENDING`, `APPROVED`, `CANCELLED`, `COMPLETED`
- **CategorÃ­as de Propiedad Principales:** `FINCA_RECREATIVA`, `CABAÃ‘A`, `GLAMPING`, `CHALET`
- **Comodidades Base (Amenities):** `PISCINA`, `WIFI`, `BBQ`, `PET_FRIENDLY`, `AIRE_ACONDICIONADO`, `JACUZZI`

---

## 2. Bootstrapping de Super-Admin

Para evitar un sistema inaccesible tras el primer despliegue, el script de inicializaciÃ³n crearÃ¡ obligatoriamente un usuario maestro con los siguientes datos:
- **Email:** `admin@nosfuimosdefinca.com`
- **Rol:** `ADMIN`

**RestricciÃ³n de Seguridad:** La contraseÃ±a **jamÃ¡s** debe ser incluida en el script. El script de base de datos deberÃ¡ leer la variable de entorno `ADMIN_SEED_PASSWORD`. Si la variable no existe en el momento del despliegue, la migraciÃ³n de base de datos fallarÃ¡ explÃ­citamente y detendrÃ¡ el proceso.

---

## 3. Datos Simulados (Mock Data) para Desarrollo

El equipo de Frontend (Fase 7) no puede desarrollar si el catÃ¡logo estÃ¡ vacÃ­o. Utilizaremos la librerÃ­a `faker.js` combinada con nuestro cliente de base de datos para poblar los entornos locales y de QA.

- **Herramienta:** Script Typescript en `package.json` -> `npm run db:seed:mock`.
- **VolÃºmenes Esperados:**
  - 50 Usuarios falsos (20% Hosts, 80% Guests).
  - 200 Propiedades asignadas aleatoriamente a los Hosts.
  - 1000 Reservas simulando todo el abanico de estados.
  - 3000 ReseÃ±as (Reviews).
- **Convenio de Desarrollo:** Todas las cuentas simuladas generadas por el script `faker.js` tendrÃ¡n la contraseÃ±a maestra temporal `password123`.

---

## 4. Plan de MigraciÃ³n (Legacy ETL)

**No Aplica.** 
El proyecto *Nos Fuimos de Finca* es un desarrollo Greenfield (Nuevo). No existen sistemas heredados (Legacy Systems), tablas de Excel maestras, ni bases de datos de clientes antiguos que requieran ser inyectados en la nueva arquitectura. Por lo tanto, no se diseÃ±arÃ¡n pipelines ETL.

