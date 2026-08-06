- [ ] TASK_FE_015 — Vista Detalle de Finca: Cotizador Interactivo de Fechas y Widget de Reserva 📅 2026-08-05 15:00
	- [ ] Paso 1: Actualizar src/pages/property-detail/property.html
		- [ ] Crear widget flotante de reserva a la derecha del layout (sticky sidebar)
		- [ ] Agregar selectores de fecha check-in/check-out y contador de huéspedes
		- [ ] Crear contenedor de desglose financiero (noches x tarifa, depósito, tasa de servicio, total)
	- [ ] Paso 2: Actualizar src/pages/property-detail/property.js
		- [ ] Escuchar cambios en las fechas para calcular número de noches
		- [ ] Calcular el valor total dinámico y activar botón 'Reservar Ahora'

# TASK_FE_015 — Vista Detalle de Finca: Cotizador Interactivo de Fechas y Widget de Reserva

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 65% -> 70%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Implementa el cotizador de reserva en tiempo real (70%), calculando costos exactos según noches seleccionadas e iniciando el checkout.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Posicionamiento Sticky CSS (position: sticky):** Fijación del widget flotante de reserva en la pantalla mientras el usuario hace scroll sobre la descripción de la finca.
* **Operaciones Matemáticas de Fechas en JS:** Cálculo preciso de diferencia en días entre dos fechas evitando desfasajes por zonas horarias.
* **Validación Dinámica de Formularios y Estados Habilitados/Deshabilitados:** Deshabilitar el botón de reserva hasta que se seleccione un rango válido de fechas.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Actualizar `property.html`
1. Crea el widget de cotización flotante con la clase `.booking-widget-sticky`.
2. Incluye el precio por noche destacado, las entradas de fecha de entrada y salida, el selector de huéspedes y el contenedor de desglose financiero `#price-breakdown`.

### Paso 2: Actualizar `property.js`
1. Registra listeners `change` en las entradas de fechas.
2. Al seleccionar ambas fechas, calcula el número de noches `(dateOut - dateIn) / (1000 * 60 * 60 * 24)`.
3. Multiplica las noches por la tarifa por noche de la finca, agrega el depósito de garantía reembolsable y la tasa de servicio de la plataforma (10%).
4. Muestra el desglose de precios en el DOM y habilita el botón `#btn-start-booking`.
5. Al presionar `#btn-start-booking`, verifica si el usuario está autenticado; si no lo está, redirige a `login.html`; si lo está, redirige a `checkout.html` pasando la configuración de reserva por URL.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
