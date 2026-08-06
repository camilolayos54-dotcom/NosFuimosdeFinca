- [x] TASK_FE_005 — Servicio HTTP Fetch API y Manejo de Errores REST 📅 2026-08-05 10:00
	- [x] Paso 1: Crear el archivo src/services/api.js
		- [x] Implementar la función asíncrona apiRequest(endpoint, options)
		- [x] Inyectar la cabecera Authorization: Bearer <jwt> si existe token en localStorage
		- [x] Procesar respuestas HTTP de error (400, 401, 403, 500) y lanzar excepciones descriptivas
	- [x] Paso 2: Exponer envoltorios HTTP helpers
		- [x] Exportar métodos apiGet, apiPost, apiPut, apiDelete

# TASK_FE_005 — Servicio HTTP Fetch API y Manejo de Errores REST

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 16% -> 20%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Encapsula el cliente de peticiones HTTP REST (20%). Centraliza el envío de tokens JWT de autenticación y la captura unificada de errores del servidor.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **API Fetch Nativa y Promesas JavaScript:** Uso de async/await, manejo de objetos Response y conversión de flujos de datos a JSON mediante .json().
* **Cabeceras HTTP de Autenticación (Bearer Token):** Formato estándar 'Authorization: Bearer <token>' para el intercambio de tokens de sesión con APIs REST.
* **Manejo Centralizado de Excepciones HTTP:** Evaluación de la propiedad response.ok y captura de códigos de estado HTTP de error (4xx y 5xx).

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/services/api.js`
1. Establece la constante base `API_BASE = '/api/v1'`. 
2. Escribe la función asíncrona exportada `apiRequest(endpoint, options = {})`.
3. Extrae el token JWT almacenado en `localStorage.getItem('token')`.
4. Construye las cabeceras inyectando `'Content-Type': 'application/json'` y `'Authorization': 'Bearer ' + token` cuando esté presente.
5. Ejecuta `fetch(API_BASE + endpoint, config)` y evalúa `response.ok`.
6. Si la respuesta falla, lee el cuerpo JSON de error y lanza un objeto `Error` con el mensaje devuelto por Spring Boot.

### Paso 2: Crear funciones de conveniencia HTTP
1. Exporta `apiGet(url)`, `apiPost(url, data)`, `apiPut(url, data)` y `apiDelete(url)` utilizando `apiRequest` internamente.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
