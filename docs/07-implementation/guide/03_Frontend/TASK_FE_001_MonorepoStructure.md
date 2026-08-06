- [x] TASK_FE_001 — Inicialización del Monorepo Frontend y Estructura de Directorios 📅 2026-08-05 08:00
	- [x] Paso 1: Navegar al directorio raíz del proyecto frontend
		- [x] Acceder a la carpeta frontend/ en la raíz del repositorio de NosFuimosdeFinca
	- [x] Paso 2: Crear la estructura física de carpetas
		- [x] Crear src/pages/, src/components/, src/services/, src/styles/, src/utils/, src/store/ y public/assets/
	- [x] Paso 3: Inicializar el archivo package.json
		- [x] Ejecutar npm init -y
		- [x] Instalar Vite 5.x como dependencia de desarrollo
		- [x] Configurar scripts dev, build y preview

# TASK_FE_001 — Inicialización del Monorepo Frontend y Estructura de Directorios

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 0% -> 4%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Establece el punto de partida físico del cliente web (0%). Organiza la arquitectura de directorios separando la lógica de presentación, servicios HTTP, componentes reutilizables, utilidades y estado de la aplicación.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Estructura de Monorepo y Modularidad Web:** Entender la separación de responsabilidades entre vistas (pages), componentes reusables (components), servicios de integración (services) y utilidades puras (utils).
* **Administración de Dependencias con NPM:** Conocer el archivo package.json, la diferencia entre dependencies y devDependencies, y la ejecución de scripts npm.
* **Empaquetadores de Código (Bundlers) de Nueva Generación:** Comprender la función de Vite como servidor de desarrollo ultra-rápido basado en ESM nativo y empaquetador de producción basado en Rollup.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Navegar al directorio raíz del proyecto frontend
1. Abre la consola de comandos en la raíz del repositorio de NosFuimosdeFinca.
2. Ingresa al directorio `frontend/` mediante la terminal.

### Paso 2: Crear la estructura física de directorios
1. Crea la carpeta `src/pages/` para albergar los subsistemas de vistas físicas independientes.
2. Crea la carpeta `src/components/` dividida en subdirectorios `ui/` y `shared/` para módulos DOM reutilizables.
3. Crea la carpeta `src/services/` para las capas de conexión HTTP Fetch y cliente JWT.
4. Crea la carpeta `src/styles/` para las hojas de estilo CSS vanilla (Tokens, Reset y Componentes).
5. Crea las carpetas `src/utils/` y `src/store/` para funciones auxiliares puras y estado global.
6. Crea la carpeta `public/assets/` para almacenamiento de imágenes estáticas y favicons.

### Paso 3: Inicializar `package.json` e instalar Vite
1. Ejecuta `npm init -y` para generar la configuración base del paquete.
2. Ejecuta `npm install -D vite@latest` para incluir la herramienta de empaquetado Vite 5.x.
3. Añade en la propiedad `scripts` los comandos: `"dev": "vite"`, `"build": "vite build"`, `"preview": "vite preview"`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
