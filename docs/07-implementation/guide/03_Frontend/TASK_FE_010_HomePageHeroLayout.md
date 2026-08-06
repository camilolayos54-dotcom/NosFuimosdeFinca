- [x] TASK_FE_010 — Vista Home: Maquetación HTML e Integración del Hero Search 📅 2026-08-05 12:30
	- [x] Paso 1: Crear src/pages/home/index.html
		- [x] Estructurar sección Hero Banner con fondo impactante y buscador principal
		- [x] Crear inputs de Municipio, Check-in, Check-out y Cantidad de Huéspedes
	- [x] Paso 2: Crear src/pages/home/home.js y src/pages/home/home.css
		- [x] Capturar evento submit del formulario de búsqueda
		- [x] Validar fechas y redirigir a catalog.html con parámetros URLSearchParams

# TASK_FE_010 — Vista Home: Maquetación HTML e Integración del Hero Search

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 40% -> 45%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Maqueta la vista de portada (45%) enfocada en la captación de usuarios mediante el formulario de búsqueda de fincas por destino y fechas.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Semántica HTML5 y Estructuras de Formulario:** Uso de elementos form, label, input (date, number, text) y atributos de accesibilidad.
* **Manipulación de Parámetros de URL (URLSearchParams):** Construcción de cadenas de consulta (query strings) para pasar parámetros de búsqueda entre páginas sin requerir estado global complexo.
* **Validación de Rango de Fechas en Cliente:** Verificación lógica para asegurar que la fecha de salida (check-out) sea estrictamente posterior a la fecha de entrada (check-in).

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/home/index.html`
1. Incluye las etiquetas `<header id="main-header">` y `<footer id="main-footer">`.
2. Maqueta la sección `.hero-section` con titular destacado y subtítulo invitando al alquiler de fincas en Colombia.
3. Estructura el formulario `<form id="search-hero-form">` con campos: Municipio (select o input autocomplete), Fecha Check-in (input date), Fecha Check-out (input date) y Huéspedes (input number min 1).

### Paso 2: Crear `src/pages/home/home.js` y `home.css`
1. Importa `navbar.js` y `footer.js` para inicializar el encabezado y pie de página.
2. Agrega un listener al evento `submit` del formulario `#search-hero-form`.
3. Valida que `checkin` sea igual o mayor al día de hoy y que `checkout` sea posterior a `checkin`.
4. Si la validación es correcta, construye los parámetros `new URLSearchParams({...})` y navega a `/src/pages/catalog/catalog.html?` más la query string.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
