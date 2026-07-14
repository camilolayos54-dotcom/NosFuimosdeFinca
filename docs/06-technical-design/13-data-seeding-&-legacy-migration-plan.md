 # Deliverable 13 (D13): Data Seeding & Legacy Migration Plan

**Proyecto:** Nos Fuimos de Finca
**Fase:** 6 Diseno Tecnico
**Estado:** Aprobado

---

## 1. Catalogo de Datos Inmutables

Estas entidades seran inyectadas via script (`seed.ts` o `seed.sql`) durante el despliegue inicial a produccion. El sistema no puede funcionar sin ellas:

- **Roles:** `ADMIN`, `HOST`, `GUEST`
- **Estados de Reserva (Booking Statuses):** `PENDING`, `APPROVED`, `CANCELLED`, `COMPLETED`
- **Categorias de Propiedad Principales:** `FINCA_RECREATIVA`, `CABA A`, `GLAMPING`, `CHALET`
- **Comodidades Base (Amenities):** `PISCINA`, `WIFI`, `BBQ`, `PET_FRIENDLY`, `AIRE_ACONDICIONADO`, `JACUZZI`

---

## 2. Bootstrapping de Super-Admin

Para evitar un sistema inaccesible tras el primer despliegue, el script de inicializacion creara obligatoriamente un usuario maestro con los siguientes datos:
- **Email:** `admin@nosfuimosdefinca.com`
- **Rol:** `ADMIN`

**Restriccion de Seguridad:** La contrasena **jamas** debe ser incluida en el script. El script de base de datos debera leer la variable de entorno `ADMIN_SEED_PASSWORD`. Si la variable no existe en el momento del despliegue, la migracion de base de datos fallara explicitamente y detendra el proceso.

---

## 3. Datos Simulados (Mock Data) para Desarrollo

El equipo de Frontend (Fase 7) no puede desarrollar si el catalogo esta vacio. Utilizaremos la libreria `faker.js` combinada con nuestro cliente de base de datos para poblar los entornos locales y de QA.

- **Herramienta:** Script Typescript en `pom.xml` -> `mvn db:seed:mock`.
- **Volumenes Esperados:**
  - 50 Usuarios falsos (20% Hosts, 80% Guests).
  - 200 Propiedades asignadas aleatoriamente a los Hosts.
  - 1000 Reservas simulando todo el abanico de estados.
  - 3000 Resenas (Reviews).
- **Convenio de Desarrollo:** Todas las cuentas simuladas generadas por el script `faker.js` tendran la contrasena maestra temporal `password123`.

---

## 4. Plan de Migracion (Legacy ETL)

**No Aplica.** 
El proyecto *Nos Fuimos de Finca* es un desarrollo Greenfield (Nuevo). No existen sistemas heredados (Legacy Systems), tablas de Excel maestras, ni bases de datos de clientes antiguos que requieran ser inyectados en la nueva arquitectura. Por lo tanto, no se disenaran pipelines ETL.

