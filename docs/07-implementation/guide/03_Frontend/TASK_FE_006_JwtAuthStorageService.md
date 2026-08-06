- [x] TASK_FE_006 — Módulo de Almacenamiento Local y Gestión de Sesión JWT 📅 2026-08-05 10:30
	- [x] Paso 1: Crear el archivo src/services/auth.js
		- [x] Implementar setToken(token), getToken(), removeToken()
		- [x] Implementar getUserFromToken() decodificando el payload JWT en base64
		- [x] Implementar isAuthenticated() y hasRole(role)
	- [x] Paso 2: Implementar función logout()
		- [x] Remover token de localStorage y redirigir a la vista de inicio

# TASK_FE_006 — Módulo de Almacenamiento Local y Gestión de Sesión JWT

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 20% -> 25%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Administra el estado de la sesión cliente (25%). Almacena el token JWT, valida su tiempo de expiración y permite la verificación de roles (`GUEST_ROLE`, `OWNER_ROLE`, `ADMIN_ROLE`).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Estructura de Tokens JWT (JSON Web Token):** Formato Header.Payload.Signature. Decodificación de la parte Payload codificada en Base64URL sin requerir librerías externas.
* **API Web Storage (localStorage):** Persistencia de cadenas de texto en el almacenamiento local del navegador entre recargas de página.
* **Control de Acceso Basado en Roles (RBAC):** Lógica de verificación de roles del usuario activo para permitir o denegar el acceso a ciertas vistas o acciones UI.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/services/auth.js`
1. Implementa las funciones `setToken(token)`, `getToken()` y `removeToken()` interactuando con `localStorage` bajo la clave `'auth_token'`.
2. Escribe `getUserFromToken()`: divide la cadena del token por los puntos `.`, toma la segunda sección (payload), decodifícala usando `atob()` y conviértela con `JSON.parse()`.
3. Escribe `isAuthenticated()`: verifica si existe token y comprueba si la propiedad `exp` del payload decodificado es superior a la fecha actual (`Date.now() / 1000`).
4. Escribe `hasRole(targetRole)`: comprueba si el array de roles del payload incluye el rol especificado.

### Paso 2: Implementar `logout()`
1. Crea la función `logout()` que elimine el token de `localStorage` y redirija a `/src/pages/home/index.html`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
