- [ ] TASK_FE_022 — Vista Huésped: Panel Mis Reservas e Historial de Viajes 📅 2026-08-05 18:30
	- [ ] Paso 1: Crear src/pages/my-bookings/my-bookings.html
		- [ ] Diseñar pestañas: 'Próximas Reservas', 'Completadas', 'Canceladas'
		- [ ] Diseñar tarjeta de reserva con foto de finca, fechas, total pagado y estado
	- [ ] Paso 2: Crear el controlador src/pages/my-bookings/my-bookings.js
		- [ ] Consultar GET /api/v1/bookings/my-bookings con api.js
		- [ ] Agregar botón 'Cancelar Reserva' con modal de confirmación enviando DELETE /api/v1/bookings/{id}

# TASK_FE_022 — Vista Huésped: Panel Mis Reservas e Historial de Viajes

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 94% -> 97%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Entrega al huésped su centro de gestión de viajes (97%), permitiendo consultar reservas pasadas, imprimir vouchers y solicitar cancelaciones.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Navegación por Pestañas (Tab Navigation):** Filtrado de datos en el cliente o mediante peticiones parametrizadas al cambiar de pestaña activa.
* **Manejo de Modales de Confirmación de Acciones Críticas:** Creación de diálogos emergentes que soliciten confirmación explícita antes de proceder con una cancelación de reserva.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `my-bookings.html`
1. Diseña las pestañas horizontales `#tab-upcoming`, `#tab-completed`, `#tab-cancelled`.
2. Crea el contenedor de la grilla de reservas `#my-bookings-container`.

### Paso 2: Crear `my-bookings.js`
1. Verifica autenticación del usuario.
2. Consume `apiGet('/bookings/my-bookings')` e inyecta las tarjetas de reserva mostrando estado, foto, municipio y fechas.
3. Agrega la funcionalidad de cancelación mostrando un modal de confirmación que ejecute `apiDelete('/bookings/' + bookingId)`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
