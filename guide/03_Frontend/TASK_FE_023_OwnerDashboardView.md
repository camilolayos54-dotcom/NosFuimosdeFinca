- [ ] TASK_FE_023 — Vista Anfitrión: Dashboard de Control, Calendario de Disponibilidad e Ingresos 📅 2026-08-05 19:00
	- [ ] Paso 1: Crear el archivo src/pages/dashboard/dashboard.html
		- [ ] Diseñar sidebar de navegación: 'Resumen', 'Mis Fincas', 'Solicitudes de Reserva', 'Calendario'
		- [ ] Diseñar tarjetas métricas: Ingresos del Mes, Ocupación %, Reservas Pendientes
	- [ ] Paso 2: Crear el controlador src/pages/dashboard/dashboard.js
		- [ ] Consultar GET /api/v1/owner/metrics e inyectar datos reales
		- [ ] Implementar tabla de solicitudes con botones de 'Aprobar' y 'Rechazar'

# TASK_FE_023 — Vista Anfitrión: Dashboard de Control, Calendario de Disponibilidad e Ingresos

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 97% -> 99%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Proporciona al anfitrión su panel de administración comercial (99%) para controlar el estado de sus fincas, aprobar reservas y ver métricas financieras.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Visualización de Paneles de Control (Dashboards UI):** Disposición de métricas financieras e indicadores clave de rendimiento (KPIs) en paneles visuales de tarjetas.
* **Tablas de Datos Interactivos con Acciones:** Creación de filas de tabla con botones de acción dinámica ('Aprobar', 'Rechazar', 'Editar Tarifa') que modifican el estado de las entidades backend.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `dashboard.html`
1. Diseña la estructura de panel administrativo con sidebar lateral e interfaz principal.
2. Crea los bloques de tarjetas de indicadores clave (KPIs): Total Ganado, Reservas Confirmadas, Tasa de Ocupación.
3. Crea la tabla `#pending-requests-table` para la gestión de solicitudes.

### Paso 2: Crear `dashboard.js`
1. Valida que el usuario tenga el rol `OWNER_ROLE` o `ADMIN_ROLE`.
2. Consulta `apiGet('/owner/metrics')` para inyectar los datos en los KPIs.
3. Consulta `apiGet('/owner/bookings/pending')` e inyecta la lista de solicitudes pendientes enviando peticiones `apiPut` al presionar 'Aprobar' o 'Rechazar'.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
