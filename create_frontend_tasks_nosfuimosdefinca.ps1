# Script to generate granular 24 Frontend Tasks for NosFuimosdeFinca

$targetDir = "c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide\03_Frontend"

# Ensure directory exists
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

# Task 2
@'
- [ ] TASK FE-002 — Configuración Bundler Vite MPA y Servidor de Desarrollo 📅 2026-08-05 08:30
	- [ ] Paso 1: Crear el archivo vite.config.js en la raíz de frontend/
		- [ ] Importar la función resolve del módulo 'path' de Node.js
	- [ ] Paso 2: Configurar la opción build.rollupOptions.input para Multi-Page Application
		- [ ] Registrar el punto de entrada 'main' apuntando a src/pages/home/index.html
		- [ ] Registrar el punto de entrada 'catalog' apuntando a src/pages/catalog/catalog.html
		- [ ] Registrar el punto de entrada 'property' apuntando a src/pages/property-detail/property.html
		- [ ] Registrar el punto de entrada 'checkout' apuntando a src/pages/checkout/checkout.html
		- [ ] Registrar el punto de entrada 'checkout_success' apuntando a src/pages/checkout-success/checkout-success.html
		- [ ] Registrar el punto de entrada 'auth_login' apuntando a src/pages/auth/login.html
		- [ ] Registrar el punto de entrada 'auth_register' apuntando a src/pages/auth/register.html
		- [ ] Registrar el punto de entrada 'host_landing' apuntando a src/pages/host-landing/host-landing.html
		- [ ] Registrar el punto de entrada 'onboarding' apuntando a src/pages/onboarding/onboarding.html
		- [ ] Registrar el punto de entrada 'my_bookings' apuntando a src/pages/my-bookings/my-bookings.html
		- [ ] Registrar el punto de entrada 'dashboard' apuntando a src/pages/dashboard/dashboard.html
		- [ ] Registrar el punto de entrada 'error' apuntando a src/pages/error/error.html
	- [ ] Paso 3: Configurar el proxy de desarrollo local en server.proxy
		- [ ] Configurar el prefijo '/api' redirigiendo hacia 'http://localhost:8080' con changeOrigin activado

# TASK FE-002 — Configuración Bundler Vite MPA y Servidor de Desarrollo (`vite.config.js`)

**Módulo:** `frontend/`  
**Tipo de Archivo:** Configuración de Bundler Vite 5.x  
**Porcentaje de Avance:** 5% -> 10%  
**Prioridad:** CRÍTICA  
**Depende de:** `TASK_FE_001`  
**Bloquea:** Compilación y empaquetado de producción de todas las páginas  

---

## 1. Propósito y Justificación Técnica

Configura **Vite 5.x** en modo **Multi-Page Application (MPA)**. A diferencia de una Single Page Application (SPA), la arquitectura de NosFuimosdeFinca utiliza archivos `.html` físicos nativos por cada módulo visual. El archivo `vite.config.js` le indica al empaquetador Rollup cómo mapear cada HTML de origen y cómo canalizar las peticiones `/api` al backend Spring Boot en puerto 8080 evitando bloqueos de CORS en desarrollo.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo `vite.config.js` en la raíz de `frontend/`
1. En la carpeta `frontend/`, crea un archivo denominado `vite.config.js`.
2. Utiliza la función `defineConfig` de Vite y la utilidad `resolve` del módulo estándar `path` de Node.js.

### Paso 2: Configurar la opción `build.rollupOptions.input` para Multi-Page Application
1. Dentro del objeto retornado por `defineConfig`, agrega la propiedad `build`.
2. Especifica `rollupOptions` conteniendo el objeto `input`.
3. Define una clave por cada página del sistema asignando su ruta física resuelta con `resolve(__dirname, 'src/pages/...')`:
   - `main`: `src/pages/home/index.html`
   - `catalog`: `src/pages/catalog/catalog.html`
   - `property`: `src/pages/property-detail/property.html`
   - `checkout`: `src/pages/checkout/checkout.html`
   - `checkout_success`: `src/pages/checkout-success/checkout-success.html`
   - `auth_login`: `src/pages/auth/login.html`
   - `auth_register`: `src/pages/auth/register.html`
   - `host_landing`: `src/pages/host-landing/host-landing.html`
   - `onboarding`: `src/pages/onboarding/onboarding.html`
   - `my_bookings`: `src/pages/my-bookings/my-bookings.html`
   - `dashboard`: `src/pages/dashboard/dashboard.html`
   - `error`: `src/pages/error/error.html`

### Paso 3: Configurar el proxy de desarrollo local en `server.proxy`
1. Agrega el bloque `server` al objeto de configuración de Vite.
2. Define la propiedad `proxy` mapeando la clave `'/api'`.
3. Configura la propiedad `target` hacia `'http://localhost:8080'`.
4. Activa `changeOrigin: true` y asegura que las rutas `/api` mantengan su prefijo original.

---

## 3. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Entradas HTML correctamente registradas en `rollupOptions.input` | Probar ejecucion de `npx vite build` sin advertencias de rutas |
| 2 | Proxy `/api` redirigiendo a puerto 8080 | Realizar un `fetch('/api/v1/health')` en la consola de dev server |
'@ | Out-File -FilePath "$targetDir\TASK_FE_002_DesignTokens.md" -Encoding utf8

# Task 3
@'
- [ ] TASK FE-003 — Sistema de Diseño CSS Base, Resets y Tokens HSL 📅 2026-08-05 09:00
	- [ ] Paso 1: Crear el archivo src/styles/tokens.css
		- [ ] Declarar variables HSL para color primario (--color-primary: hsl(158, 64%, 40%))
		- [ ] Declarar variables HSL para color secundario y acento CTA (--color-accent)
		- [ ] Declarar variables HSL para superficies oscuras, bordes y estados
		- [ ] Declarar variables de tipografía (--font-body: 'Inter', --font-display: 'Outfit')
		- [ ] Declarar variables de espaciado modular de 4px (--spacing-1 a --spacing-12)
		- [ ] Declarar variables de elevación, sombras y bordes redondeados
	- [ ] Paso 2: Crear el archivo src/styles/global.css
		- [ ] Importar las fuentes Google Fonts ('Inter' y 'Outfit') mediante @import
		- [ ] Importar el archivo tokens.css en la cabecera
		- [ ] Aplicar Reset CSS global (*, *::before, *::after) estableciendo box-sizing: border-box
		- [ ] Establecer estilos base para tag body (background-color, color, line-height)

# TASK FE-003 — Sistema de Diseño CSS Base, Resets y Tokens HSL (`tokens.css` & `global.css`)

**Módulo:** `frontend/src/styles/`  
**Tipo de Archivo:** Hoja de Estilos CSS Vanilla  
**Porcentaje de Avance:** 10% -> 15%  
**Prioridad:** CRÍTICA  
**Depende de:** `TASK_FE_001`  
**Bloquea:** Estilos visuales de todos los componentes y vistas  

---

## 1. Propósito y Justificación Técnica

Crea la base del sistema de diseño unificado del proyecto (15%). Define la paleta cromática basada exclusivamente en **HSL** (Hue, Saturation, Lightness) para permitir tematización dinámica y modos oscuros/glassmorphism sin acoplamiento. Establece las normas de tipografía, escala de espacios en múltiplos de 4px y un Reset CSS estricto que elimina las inconsistencias de renderizado por defecto de los distintos navegadores.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el archivo `src/styles/tokens.css`
1. Crea el archivo `tokens.css` dentro de `src/styles/`.
2. Abre el bloque selector `:root {}`.
3. Define los tokens cromáticos HSL:
   - Verde Finca (Primario): `--color-primary` (hsl 158, 64%, 40%), variantes `--color-primary-dark` y `--color-primary-light`.
   - Naranja Atardecer (Acento CTA): `--color-accent` (hsl 27, 95%, 55%) y variante `--color-accent-dark`.
   - Superficies Oscuras Glassmorphism: `--color-surface` (hsl 220, 20%, 10%), `--color-surface-2`, `--color-surface-3`.
   - Colores de Estado: `--color-success`, `--color-warning`, `--color-error`.
   - Colores de Texto: `--color-text-primary`, `--color-text-secondary`, `--color-text-muted`.
   - Bordes: `--color-border`.
4. Define los tokens de tipografía:
   - `--font-body`: `'Inter', sans-serif`.
   - `--font-display`: `'Outfit', sans-serif`.
5. Define la escala de espaciado modular en múltiplos de 4px (`--spacing-1: 4px`, `--spacing-2: 8px`, `--spacing-3: 12px`, `--spacing-4: 16px`, `--spacing-6: 24px`, `--spacing-8: 32px`, `--spacing-12: 48px`).
6. Define border-radius (`--radius-sm: 4px`, `--radius-md: 8px`, `--radius-lg: 16px`, `--radius-full: 9999px`) y sombras.

### Paso 2: Crear el archivo `src/styles/global.css`
1. Crea el archivo `global.css` en `src/styles/`.
2. Agrega la directiva `@import` al inicio para cargar las fuentes desde Google Fonts: `'Inter'` (pesos 400, 500, 600, 700) y `'Outfit'` (pesos 600, 700, 800).
3. Importa `tokens.css` mediante `@import './tokens.css';`.
4. Aplica el Reset CSS universal:
   - Selector `*, *::before, *::after` con `box-sizing: border-box`, `margin: 0`, `padding: 0`.
5. Define los estilos globales de `body`:
   - `font-family: var(--font-body)`.
   - `background-color: var(--color-surface)`.
   - `color: var(--color-text-primary)`.
   - `line-height: 1.5`.
   - `overflow-x: hidden`.

---

## 3. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Variables `:root` disponibles globalmente | Inspeccionar `:root` en DevTools de cualquier página |
| 2 | Cero valores numéricos de color en código CSS posterior | Auditar que se usen exclusivamente `var(--color-...)` |
| 3 | Reset CSS activo | Comprobar que elementos `h1`, `p`, `ul` no tengan márgenes default |
'@ | Out-File -FilePath "$targetDir\TASK_FE_003_NavbarFooter.md" -Encoding utf8

Write-Host "Tasks generated successfully."
