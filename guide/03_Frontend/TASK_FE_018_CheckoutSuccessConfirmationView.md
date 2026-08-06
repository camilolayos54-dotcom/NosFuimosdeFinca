- [ ] TASK_FE_018 — Vista Confirmación de Reserva: Comprobante y Guía de Llegada 📅 2026-08-05 16:30
	- [ ] Paso 1: Crear el archivo src/pages/checkout-success/checkout-success.html
		- [ ] Diseñar tarjeta de confirmación con ícono de éxito y código de reserva
		- [ ] Mostrar desglose del viaje, datos de contacto del anfitrión e instrucciones de llegada
		- [ ] Agregar botones 'Ver Mis Reservas' y 'Imprimir / Descargar Comprobante'
	- [ ] Paso 2: Crear el controlador src/pages/checkout-success/checkout-success.js
		- [ ] Obtener bookingId de la URL y consultar GET /api/v1/bookings/{id} para cargar datos reales

# TASK_FE_018 — Vista Confirmación de Reserva: Comprobante y Guía de Llegada

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 78% -> 82%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Presenta el comprobante digital de reserva confirmada (82%), entregando al huésped su código de reserva, voucher y contacto directo del finquero.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Impresión y Generación de Comprobantes Web (window.print):** Uso de estilos CSS @media print para adaptar la vista de comprobante al formato de impresión en papel o PDF.
* **Manejo de Estados de Confirmación Transaccional:** Carga y visualización de detalles de órdenes procesadas para dar tranquilidad al usuario post-compra.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `checkout-success.html`
1. Diseña la tarjeta centradora de éxito con ícono de verificación verde en grande.
2. Muestra el código de reserva en formato destacado (ej: `NF-89421`).
3. Estructura los detalles del comprobante: Nombre de la Finca, Dirección/Vereda, Fechas de Check-in y Check-out, Nombre del Anfitrión y Teléfono de contacto directo.

### Paso 2: Crear `checkout-success.js`
1. Lee `bookingId` de la query string de la URL.
2. Consulta `apiGet('/bookings/' + bookingId)`.
3. Pobla los datos en el comprobante y asigna la acción `window.print()` al botón 'Imprimir Comprobante'.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
