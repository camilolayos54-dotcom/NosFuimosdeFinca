- [ ] TASK_FE_009 — Componente Sistema de Notificaciones Toast 📅 2026-08-05 12:00
	- [ ] Paso 1: Crear src/components/toast.js
		- [ ] Asegurar contenedor flotante div id='toast-container' en el body
		- [ ] Implementar la función showToast(message, type, duration)
		- [ ] Aplicar estilos visuales para clases toast-success, toast-error, toast-warning
		- [ ] Implementar temporizador de auto-destrucción del nodo DOM
	- [ ] Paso 2: Exportar funciones helpers de conveniencia
		- [ ] Exportar toastSuccess(msg), toastError(msg), toastWarning(msg)

# TASK_FE_009 — Componente Sistema de Notificaciones Toast

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 35% -> 40%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Proporciona un servicio visual de notificaciones emergentes (40%) para dar retroalimentación inmediata sobre acciones del usuario (errores, confirmaciones, advertencias).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Posicionamiento Fijo CSS (Fixed / Z-Index):** Uso de position: fixed, top/right y z-index elevado para mostrar alertas superpuestas sobre cualquier contenido.
* **Animaciones y Transiciones CSS (Keyframes / Transition):** Aplicación de transform: translateX() y opacity para suavizar la entrada y salida de notificaciones.
* **Gestión Asíncrona de Temporizadores (setTimeout):** Programación de la remoción de elementos del DOM tras el vencimiento de un intervalo de milisegundos.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/toast.js`
1. Crea una función privada `getOrCreateToastContainer()` que busque o inserte `<div id="toast-container">` fijo en la esquina superior derecha del viewport.
2. Escribe `showToast(message, type = 'info', duration = 4000)`.
3. Crea un nuevo elemento `div`, asígnale la clase `toast` y el modificador `toast-${type}` (success: verde, error: rojo, warning: amarillo, info: azul).
4. Añade un botón de cierre `×` para descartar manualmente la alerta.
5. Inserta la alerta en el contenedor y programa `setTimeout` para aplicar la clase `.fade-out` y remover el nodo del DOM pasados `duration` milisegundos.

### Paso 2: Exportar helpers
1. Exporta `toastSuccess(msg)`, `toastError(msg)`, `toastWarning(msg)`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
