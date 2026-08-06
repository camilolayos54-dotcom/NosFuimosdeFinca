- [x] TASK_FE_011 — Vista Home: Renderizado Dinámico de Fincas Destacadas y Categorías 📅 2026-08-05 13:00
	- [x] Paso 1: Actualizar src/pages/home/index.html
		- [x] Crear contenedor div id='featured-properties-container' para la grilla de fincas
		- [x] Crear contenedor div id='categories-container' para accesos por clima
	- [x] Paso 2: Actualizar src/pages/home/home.js
		- [x] Invocar GET /api/v1/properties/featured mediante api.js
		- [x] Generar dinámicamente las tarjetas de fincas con foto, municipio, capacidad y tarifa
		- [x] Implementar Skeleton Loaders durante la carga asíncrona

# TASK_FE_011 — Vista Home: Renderizado Dinámico de Fincas Destacadas y Categorías

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 45% -> 50%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Conecta la portada con los servicios backend (50%) para renderizar la grilla de fincas populares y el carrusel de categorías (Clima Cálido, Piscina, Pet Friendly).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Patrón de Carga Visual (Skeleton Loaders):** Diseño de contenedores pulsantes grises que imitan la forma del contenido final para mejorar el tiempo percibido de carga (UX).
* **Renderizado Dinámico de Listas mediante Plantillas de Cadena (Template Literals):** Transformación de arrays de objetos JSON en cadenas HTML usando map() y join('').
* **Formateo de Moneda Local (Intl.NumberFormat):** Formateo de precios numéricos a moneda colombiana (COP) con separadores de miles.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Actualizar `index.html`
1. Crea la sección `.featured-section` con el contenedor `<div id="featured-properties-container" class="properties-grid">`.
2. Crea la sección `.categories-section` con el contenedor `<div id="categories-container" class="categories-grid">`.

### Paso 2: Actualizar `home.js`
1. Antes de realizar la petición, inyecta tarjetas skeleton en `#featured-properties-container`.
2. Consume la API REST `apiGet('/properties/featured')`.
3. Itera el array de propiedades e inyecta las tarjetas conteniendo: foto principal, insignia de calificación promedio, municipio, capacidad máxima de personas y precio por noche formateado con `new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' })`.
4. Agrega al hacer click en cualquier tarjeta la redirección a `/src/pages/property-detail/property.html?id=` + id de la finca.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
