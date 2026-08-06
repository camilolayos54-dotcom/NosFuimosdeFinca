---
project: 1.NosFuimosDeFincaFrontend
---


- [ ] TASK_FE_002 — Configuración Bundler Vite MPA y Servidor de Desarrollo 📅 2026-08-05 08:30
	- [ ] Paso 1: Crear el archivo vite.config.js en la raíz de frontend/
		- [ ] Importar la función resolve del módulo 'path' de Node.js
	- [ ] Paso 2: Configurar la opción build.rollupOptions.input para Multi-Page Application
		- [ ] Registrar los 15 puntos de entrada HTML (home, catalog, property-detail, checkout, auth, dashboard, etc.)
	- [ ] Paso 3: Configurar el proxy de desarrollo local en server.proxy
		- [ ] Mapear el prefijo '/api' redirigiendo hacia http://localhost:8080 con changeOrigin activado

# TASK_FE_002 — Configuración Bundler Vite MPA y Servidor de Desarrollo

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 4% -> 8%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Configura Vite 5.x en modo Multi-Page Application (MPA). Garantiza que cada vista HTML sea procesada como un punto de entrada independiente y canaliza el tráfico `/api` al backend Spring Boot en puerto 8080.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Arquitectura Multi-Page Application (MPA):** Diferencia entre SPA y MPA. En MPA cada vista posee su propio archivo HTML nativo cargando scripts ES Modules dedicados.
* **Módulos Node.js y Resolución de Rutas Absolutas:** Uso del módulo path y __dirname para resolver rutas absolutas de archivos de forma multiplataforma (Windows/Linux/macOS).
* **Configuración de Servidores Proxy de Desarrollo:** Concepto de proxy inverso local para redirigir peticiones HTTP de un puerto a otro evitando políticas de restricción de Origen Cruzado (CORS) durante el desarrollo.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear vite.config.js
1. Crea el archivo `vite.config.js` en la raíz de `frontend/`.
2. Importa `defineConfig` de `'vite'` y `resolve` del paquete integrado `'path'`.

### Paso 2: Configurar los puntos de entrada MPA en Rollup
1. Define la propiedad `build.rollupOptions.input` dentro de la exportación del archivo.
2. Registra las claves absolutas resueltas con `resolve(__dirname, 'src/pages/...')` para: main (home/index.html), catalog (catalog/catalog.html), property (property-detail/property.html), checkout (checkout/checkout.html), checkout_success (checkout-success/checkout-success.html), auth_login (auth/login.html), auth_register (auth/register.html), host_landing (host-landing/host-landing.html), onboarding (onboarding/onboarding.html), my_bookings (my-bookings/my-bookings.html), dashboard (dashboard/dashboard.html), error (error/error.html).

### Paso 3: Configurar el proxy inverso `/api`
1. Agrega la sección `server.proxy` mapeando el string `'/api'`.
2. Asigna `target: 'http://localhost:8080'`, `changeOrigin: true` y asegura que las rutas preserven su estructura REST.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
