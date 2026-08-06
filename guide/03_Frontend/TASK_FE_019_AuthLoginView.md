- [x] TASK_FE_019 — Vista Autenticación: Formulario de Inicio de Sesión / Login 📅 2026-08-05 17:00
	- [x] Paso 1: Crear src/pages/auth/login.html y src/pages/auth/login.js
		- [x] Diseñar el formulario de ingreso con campos para Email y Contraseña
		- [x] Capturar submit y enviar POST /api/v1/auth/login mediante api.js
		- [x] Almacenar el token JWT con auth.js y redirigir al catálogo o dashboard según rol
	- [x] Paso 2: Crear la hoja de estilos src/pages/auth/login.css
		- [x] Diseñar tarjeta centradora con diseño glassmorphism

# TASK_FE_019 — Vista Autenticación: Formulario de Inicio de Sesión / Login

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 82% -> 86%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Autentica usuarios registrados (86%), procesando credenciales contra Spring Boot e iniciando la sesión cliente mediante almacenamiento de token JWT.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Manejo de Formularios de Credenciales y Seguridad:** Uso de inputs type='email' y type='password' con opción para conmutar la visibilidad de la contraseña.
* **Persistencia de Sesión JWT:** Almacenamiento del token devuelto en localStorage y actualización de la interfaz de usuario en consecuencia.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/auth/login.html` y `login.css`
1. Diseña la tarjeta de inicio de sesión centradora con el logotipo de NosFuimosdeFinca.
2. Estructura el formulario `#login-form` con campos para Correo Electrónico y Contraseña, además de la casilla 'Recordarme'.

### Paso 2: Crear `src/pages/auth/login.js`
1. Escucha el evento `submit` del formulario `#login-form`.
2. Extrae los valores de email y contraseña.
3. Realiza la petición `apiPost('/auth/login', { email, password })`.
4. Al recibir la respuesta exitosa conteniendo `{ token }`, invoca `setToken(token)` de `auth.js`.
5. Muestra un Toast de bienvenida y redirige al usuario a la página previa o a `/src/pages/catalog/catalog.html`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
