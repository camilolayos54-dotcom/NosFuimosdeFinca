- [ ] TASK_FE_014 — Vista Detalle de Finca: Galería Multimedia y Especificaciones 📅 2026-08-05 14:30
	- [ ] Paso 1: Crear el archivo src/pages/property-detail/property.html
		- [ ] Diseñar encabezado con título, ubicación, botón de compartir y favoritos
		- [ ] Diseñar cuadrícula de galería multimedia de imágenes (foto principal + miniaturas)
		- [ ] Diseñar sección de descripción, capacidad de dormitorios, baños y lista de amenidades con íconos
	- [ ] Paso 2: Crear el controlador src/pages/property-detail/property.js
		- [ ] Obtener id de la finca desde window.location.search
		- [ ] Consultar GET /api/v1/properties/{id} mediante api.js y poblar los elementos DOM

# TASK_FE_014 — Vista Detalle de Finca: Galería Multimedia y Especificaciones

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 60% -> 65%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Construye la vista de detalle de la finca (65%), desplegando la galería multimedia, distribución de espacios, amenidades y normas del establecimiento.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Galerías de Imágenes e Interacciones Modal Lightbox:** Manejo de click en imágenes miniaturas para intercambiar la imagen principal o abrir la vista de pantalla completa.
* **Parseo de IDs desde la Cadenas de Consulta URL:** Extracción segura de identificadores numéricos o UUIDs desde los query params de la página.
* **Inyección de Iconografía SVG / Font Icons:** Mapeo dinámico de nombres de amenidades ('PISCINA', 'BBQ', 'WIFI') hacia sus respectivos íconos visuales.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/property-detail/property.html`
1. Estructura el contenedor de la galería `.gallery-grid` con 1 imagen principal grande a la izquierda y 4 imágenes secundarias a la derecha.
2. Estructura la columna izquierda de información: Titular, Municipio/Vereda, Capacidad máxima, Número de alcobas, Número de baños, Descripción detallada, Lista de amenidades e Instrucciones de llegada.
3. Agrega la sección de normas de la finca (horarios de check-in/out, prohibición de sonido excesivo, mascotas).

### Paso 2: Crear `src/pages/property-detail/property.js`
1. Extrae el parámetro `id` de `window.location.search`.
2. Si no existe `id`, redirige a la página de error 404.
3. Ejecuta `apiGet('/properties/' + id)`.
4. Inyecta las URLs de fotos en la galería y agrega un listener a las miniaturas para cambiar la foto principal activa.
5. Mapea el array de amenidades renderizando íconos con sus etiquetas correspondientes.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
