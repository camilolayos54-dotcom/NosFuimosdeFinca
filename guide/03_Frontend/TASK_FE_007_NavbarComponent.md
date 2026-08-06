- [x] TASK_FE_007 — Componente Navegacional Encabezado / Navbar Responsive 📅 2026-08-05 11:00
	- [x] Paso 1: Crear src/components/navbar.js y src/components/navbar.css
		- [x] Construir función renderNavbar() inyectando el encabezado HTML
		- [x] Evaluar sesión con auth.js para cambiar el menú dinámicamente según el rol
		- [x] Agregar listeners de eventos para desplegar el menú hamburguesa móvil
	- [x] Paso 2: Inyectar automáticamente en el DOM
		- [x] Buscar el contenedor <header id='main-header'> al cargar el DOM

# TASK_FE_007 — Componente Navegacional Encabezado / Navbar Responsive

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 25% -> 30%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Construye e inyecta dinámicamente la barra de navegación (30%). Adapta los enlaces expuestos según el estado de la sesión (Huésped, Anfitrión o Usuario Anónimo).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Manipulación del DOM en Vanilla JavaScript:** Uso de document.getElementById, querySelector e innerHTML para inyectar estructuras dinámicas.
* **Eventos de Interacción y Escuchadores (EventListeners):** Captura de eventos click en botones de navegación y menús hamburguesa.
* **Diseño Responsive con Media Queries CSS:** Ocultamiento y despliegue del menú de navegación mediante transiciones CSS en pantallas móviles.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/navbar.js` y `navbar.css`
1. Escribe la función `renderNavbar()` que seleccione `<header id="main-header">`.
2. Consulta `isAuthenticated()` y `getUserFromToken()` del servicio `auth.js`.
3. Si el usuario está logueado: genera HTML con su nombre, avatar, enlace a 'Mis Reservas' y botón 'Cerrar Sesión'. Si su rol es `OWNER_ROLE`, incluye el acceso a 'Panel Finquero'.
4. Si el usuario es anónimo: genera enlaces de navegación básica y botones 'Iniciar Sesión' y 'Registrarse'.
5. Registra el listener del menú hamburguesa para añadir o quitar la clase `.active` en el contenedor del menú móvil.

### Paso 2: Inicialización automática
1. Invoca `renderNavbar()` cuando el evento `DOMContentLoaded` se dispare.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
