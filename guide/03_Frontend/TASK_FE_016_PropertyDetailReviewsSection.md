- [ ] TASK_FE_016 — Vista Detalle de Finca: Sección de Reseñas y Calificaciones 📅 2026-08-05 15:30
	- [ ] Paso 1: Actualizar src/pages/property-detail/property.html
		- [ ] Crear sección div id='reviews-section' al final del contenido
		- [ ] Diseñar desglose de puntuación por estrellas (limpieza, ubicación, servicio)
		- [ ] Crear lista de comentarios de huéspedes y formulario para publicar opinión
	- [ ] Paso 2: Actualizar src/pages/property-detail/property.js
		- [ ] Consultar GET /api/v1/properties/{id}/reviews y renderizar valoraciones
		- [ ] Enviar POST /api/v1/properties/{id}/reviews al enviar el formulario

# TASK_FE_016 — Vista Detalle de Finca: Sección de Reseñas y Calificaciones

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 70% -> 74%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Despliega la reputación y opiniones de la finca (74%), permitiendo consultar la puntuación promedio y enviar nuevas reseñas post-estadía.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Componente de Puntuación por Estrellas (Star Rating):** Creación de selectores de valoración interactivos con estrellas (1 a 5) manipulables mediante eventos mouseover/click.
* **Manejo de Contenido Generado por Usuario (Sanitización XSS):** Escape de cadenas de texto de comentarios de usuarios antes de inyectarlas en el DOM para prevenir vulnerabilidades XSS.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Actualizar `property.html`
1. Agrega la sección `#reviews-section` con barras de porcentaje para puntuaciones de Limpieza, Ubicación, Veracidad y Atención del Anfitrión.
2. Agrega el contenedor de la lista de comentarios `#reviews-list`.
3. Agrega el formulario `#add-review-form` visible solo para usuarios elegibles.

### Paso 2: Actualizar `property.js`
1. Consume `apiGet('/properties/' + id + '/reviews')` e inyecta la lista de comentarios mostrando foto del usuario, fecha de estadía y texto sanitizado.
2. Gestiona el envío del formulario de reseña mediante `apiPost('/properties/' + id + '/reviews', data)` y refresca la lista al completarse con éxito.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
