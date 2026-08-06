- [x] TASK_FE_020 — Vista Autenticación: Formulario de Registro de Usuario y Selección de Rol 📅 2026-08-05 17:30
	- [x] Paso 1: Crear src/pages/auth/register.html y src/pages/auth/register.js
		- [x] Diseñar formulario con campos: Nombre, Teléfono, Correo, Contraseña y Confirmación
		- [x] Agregar selector de tipo de cuenta: Huésped vs Anfitrión de Finca
		- [x] Enviar POST /api/v1/auth/register y redirigir a login.html
	- [x] Paso 2: Crear la hoja de estilos src/pages/auth/register.css
		- [x] Diseñar tarjetas de selección de rol con resaltado de borde en el acento

# TASK_FE_020 — Vista Autenticación: Formulario de Registro de Usuario y Selección de Rol

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 86% -> 90%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Registra nuevos usuarios en la plataforma (90%), permitiendo la elección entre el perfil de Huésped (`GUEST_ROLE`) y el de Propietario (`OWNER_ROLE`).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Validación de Coincidencia de Contraseñas y Reglas de Complejidad:** Verificación de longitud mínima (8 caracteres) y coincidencia entre 'Contraseña' y 'Confirmar Contraseña'.
* **Selección de Roles en Formularios UI:** Uso de botones de radio estilizados tipo tarjeta para seleccionar el perfil de usuario antes del registro.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/auth/register.html` y `register.css`
1. Diseña el formulario `#register-form` con los campos de datos personales.
2. Incluye las opciones de selección de perfil: 'Quiero Alquilar Fincas (Huésped)' vs 'Tengo una Finca para Publicar (Anfitrión)'.

### Paso 2: Crear `src/pages/auth/register.js`
1. Captura el submit del formulario `#register-form`.
2. Comprueba que `password === confirmPassword`.
3. Construye el payload JSON enviando `fullName`, `phone`, `email`, `password` y el rol seleccionado (`GUEST_ROLE` o `OWNER_ROLE`).
4. Ejecuta `apiPost('/auth/register', payload)`.
5. Muestra un Toast de confirmación de registro y redirige al usuario a `login.html`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
