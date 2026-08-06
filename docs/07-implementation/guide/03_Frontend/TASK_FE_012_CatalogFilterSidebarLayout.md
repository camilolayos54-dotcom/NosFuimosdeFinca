- [ ] TASK_FE_012 — Vista Catálogo: Layout de Búsqueda y Panel de Filtros Laterales 📅 2026-08-05 13:30
	- [ ] Paso 1: Crear el archivo src/pages/catalog/catalog.html
		- [ ] Diseñar layout de 2 columnas: Sidebar de Filtros (izquierda) y Grilla de Resultados (derecha)
		- [ ] Crear controles para Rango de Precio, Municipio, Capacidad de Huéspedes
		- [ ] Crear checkboxes para amenidades (Piscina, Jacuzzi, BBQ, Pet Friendly, Wifi)
	- [ ] Paso 2: Crear la hoja de estilos src/pages/catalog/catalog.css
		- [ ] Establecer disposición responsive en flex/grid adaptativa

# TASK_FE_012 — Vista Catálogo: Layout de Búsqueda y Panel de Filtros Laterales

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 50% -> 55%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Maqueta el layout del catálogo de búsqueda (55%) dividiendo la interfaz entre el panel de filtrado por facetas a la izquierda y el área de resultados a la derecha.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Layouts Complejos de Dos Columnas (CSS Grid):** Creación de cuadrículas con fr (fracciones) y minmax() para fijar la barra lateral y hacer fluida la columna de resultados.
* **Elementos de Formulario Complejos (Range Sliders y Custom Checkboxes):** Estilización de inputs tipo range, checkboxes y radios personalizados con var(--color-primary).

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/catalog/catalog.html`
1. Estructura el contenedor principal `.catalog-container` dividiéndolo en `<aside class="filter-sidebar">` y `<main class="catalog-main">`.
2. En el sidebar, crea el formulario `#filters-form` con los grupos: Rango de Precio (slider con visualización de precio mínimo y máximo), Municipio (select desplegable), Capacidad (input number) y Amenidades (checkboxes para Piscina, Jacuzzi, BBQ, Wifi, Pet Friendly, Aire Acondicionado).
3. En el área principal, crea el encabezado con el contador de fincas encontradas `<span id="results-count">` y el selector de ordenamiento `<select id="sort-by">`.

### Paso 2: Crear `src/pages/catalog/catalog.css`
1. Define la cuadrícula Grid para escritorio y la disposición apilada móvil.
2. Diseña el panel de filtros como una tarjeta flotante `glass-panel`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
