- [ ] TASK_FE_017 — Vista Checkout: Formulario de Confirmación y Desglose de Pago 📅 2026-08-05 16:00
	- [ ] Paso 1: Crear el archivo src/pages/checkout/checkout.html
		- [ ] Diseñar formulario de datos del titular (nombre, documento, teléfono, peticiones especiales)
		- [ ] Diseñar selector de método de pago (Tarjeta, PSE, Nequi/Daviplata)
		- [ ] Diseñar panel lateral con el resumen final de la reserva
	- [ ] Paso 2: Crear el controlador src/pages/checkout/checkout.js
		- [ ] Cargar datos de la reserva desde los parámetros URLSearchParams
		- [ ] Procesar solicitud POST /api/v1/bookings enviando datos de pago simulados
		- [ ] Redirigir a checkout-success.html tras recibir la respuesta del servidor

# TASK_FE_017 — Vista Checkout: Formulario de Confirmación y Desglose de Pago

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 74% -> 78%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Gestiona la confirmación de la reserva y el proceso de pago (78%), recolectando información del titular y enviando la solicitud a Spring Boot.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Validación Estricta de Formularios de Transacción:** Verificación de campos requeridos, formato de cédula/pasaporte, número de teléfono y selección de método de pago.
* **Integración con Pasarelas de Pago Simuladas:** Simulación del envío de tokens de pago (PSE, Tarjetas) contra endpoints backend transaccionales.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/checkout/checkout.html`
1. Diseña la columna izquierda con el formulario `#checkout-form`: Datos Personales, Selección de Método de Pago (PSE, Tarjeta de Crédito, Transferencia bancaria) y aceptación de políticas de cancelación.
2. Diseña la columna derecha con la tarjeta de resumen `#booking-summary-card`: Foto de la finca, título, fechas elegidas, cantidad de huéspedes y costo total final.

### Paso 2: Crear `src/pages/checkout/checkout.js`
1. Verifica que el usuario esté autenticado con `auth.js`; de lo contrario, redirige a `login.html`.
2. Lee los parámetros `propertyId`, `checkin`, `checkout`, `guests` de la URL.
3. Al enviar `#checkout-form`, construye el payload JSON conteniendo los datos de la reserva y el método de pago seleccionado.
4. Ejecuta `apiPost('/bookings', payload)`.
5. Si la respuesta es exitosa (código 201 Created), redirige a `/src/pages/checkout-success/checkout-success.html?bookingId=` + response.id.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
