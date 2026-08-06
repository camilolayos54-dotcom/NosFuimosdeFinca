- [ ] TASK_FE_013 — Vista Catálogo: Lógica de Filtrado Dinámico y Paginación en Tiempo Real 📅 2026-08-05 14:00
	- [ ] Paso 1: Crear el script controlador src/pages/catalog/catalog.js
		- [ ] Deserializar parámetros query de la URL al inicializar la vista
		- [ ] Escuchar cambios en las entradas del formulario de filtros para actualizar los query params
		- [ ] Invocar GET /api/v1/properties/search con api.js
		- [ ] Renderizar tarjetas de fincas o mostrar mensaje amigable si no hay resultados
	- [ ] Paso 2: Implementar paginación de resultados
		- [ ] Crear controles de cambio de página preservando los filtros aplicados

# TASK_FE_013 — Vista Catálogo: Lógica de Filtrado Dinámico y Paginación en Tiempo Real

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 55% -> 60%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Agrega la lógica de filtrado reactivo (60%), sincronizando los filtros seleccionados con la URL y realizando consultas dinámicas paginadas al servidor.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Técnica de Limitación de Frecuencia (Debounce):** Implementación de funciones de retardo (setTimeout) para diferir la ejecución de peticiones HTTP mientras el usuario desliza el rango de precios.
* **Manejo de Estados Vacíos (Empty States):** Diseño de mensajes amigables con sugerencias para el usuario cuando una combinación de filtros no retorna resultados.
* **Sincronización Bidireccional de URL (history.pushState):** Actualización de la query string en la barra de direcciones sin provocal un refresco de página completo.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/catalog/catalog.js`
1. Al cargar, lee los parámetros de la URL mediante `new URLSearchParams(window.location.search)` y asigna los valores a los inputs del filtro.
2. Escribe la función `fetchCatalogProperties()` que recopile los valores de todos los inputs y checkboxes marcados, construya los parámetros query y consulte `apiGet('/properties/search?' + queryParams)`.
3. Aplica un debounce de 300ms al evento `input` del control de rango de precio.
4. Escucha el evento `change` en los checkboxes y desplegables para desencadenar la búsqueda inmediatamente.
5. Si la respuesta contiene propiedades, genera la grilla de tarjetas; si el array está vacío, inyecta la vista de estado vacío con un botón 'Limpiar Filtros'.

### Paso 2: Implementar paginación
1. Genera los botones de cambio de página actualizando el parámetro `page` y ejecutando `fetchCatalogProperties()`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
