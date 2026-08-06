- [x] TASK_FE_008 — Componente Pie de Página / Footer Reutilizable 📅 2026-08-05 11:30
	- [x] Paso 1: Crear src/components/footer.js y src/components/footer.css
		- [x] Construir función renderFooter() inyectando el pie de página HTML
		- [x] Incluir enlaces de navegación secundaria, términos legales y redes sociales
		- [x] Generar el año de copyright dinámico
	- [x] Paso 2: Inyectar en el contenedor main-footer
		- [x] Buscar <footer id='main-footer'> al cargar la página

# TASK_FE_008 — Componente Pie de Página / Footer Reutilizable

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 30% -> 35%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Inyecta el pie de página global (35%) en todas las vistas HTML sin duplicar código, incluyendo datos de contacto, aviso legal y soporte.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Reutilización de Módulos DOM:** Patrón de diseño donde un componente JS inyecta una sección compartida del layout en múltiples páginas físicas HTML.
* **Manejo Dinámico de Fechas en JS:** Uso del objeto Date para calcular el año actual sin dejar valores hardcodeados en el pie de página.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/footer.js` y `footer.css`
1. Escribe `renderFooter()` seleccionando el contenedor `<footer id="main-footer">`.
2. Genera el HTML organizado en 4 columnas: Marca NosFuimosdeFinca, Destinos Populares, Enlaces de Interés (Términos, Privacidad, FAQ) y Contacto (WhatsApp, Email).
3. Calcula el año en curso con `new Date().getFullYear()` e inyéctalo en la barra de copyright inferior.

### Paso 2: Inyección automática
1. Asigna la ejecución de `renderFooter()` en la carga de la página.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
