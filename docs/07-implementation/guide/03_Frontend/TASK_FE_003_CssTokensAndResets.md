- [x] TASK_FE_003 — Sistema de Diseño CSS Base, Resets y Tokens HSL 📅 2026-08-05 09:00
	- [x] Paso 1: Crear el archivo src/styles/tokens.css
		- [x] Declarar variables HSL en :root para verde finca (--color-primary), naranja acento (--color-accent), superficies oscuras y estados
		- [x] Declarar escala de tipografía Inter/Outfit y espaciado modular en múltiplos de 4px
	- [x] Paso 2: Crear el archivo src/styles/global.css
		- [x] Importar Google Fonts ('Inter' y 'Outfit')
		- [x] Importar tokens.css mediante @import
		- [x] Aplicar Reset CSS universal (*, *::before, *::after)

# TASK_FE_003 — Sistema de Diseño CSS Base, Resets y Tokens HSL

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 8% -> 12%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Define el sistema de tokens visuales y la base de reseteo CSS (12%). Permite tematización coherente basada en variables HSL y estandarización tipográfica.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Modelo de Color HSL (Hue, Saturation, Lightness):** Comprensión de los ejes HSL para crear gamas armónicas, variaciones de tono (dark/light) y transparencias alpha.
* **Variables CSS Nativa (:root y var()):** Uso del pseudoclase :root para exponer propiedades personalizadas accesibles dinámicamente en todo el árbol DOM.
* **Reset CSS y Modelo de Caja (Box-Sizing):** Importancia de box-sizing: border-box para incluir padding y border dentro del cálculo de ancho y alto de los elementos HTML.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/styles/tokens.css`
1. Abre la regla `:root` y define los tokens de color HSL: `--color-primary: hsl(158, 64%, 40%)`, `--color-primary-dark`, `--color-primary-light`, `--color-accent: hsl(27, 95%, 55%)`, `--color-surface: hsl(220, 20%, 10%)`, `--color-surface-2`, `--color-surface-3`, `--color-text-primary`, `--color-text-secondary`, `--color-border`, `--color-success`, `--color-error`.
2. Define los tokens de fuente: `--font-body: 'Inter', sans-serif`, `--font-display: 'Outfit', sans-serif`.
3. Define la escala de espaciado modular en incrementos de 4px (`--spacing-1: 4px` hasta `--spacing-12: 48px`).
4. Define los bordes redondeados (`--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-full`).

### Paso 2: Crear `src/styles/global.css`
1. Carga las fuentes Google Fonts mediante `@import` para 'Inter' (400, 500, 600, 700) y 'Outfit' (600, 700, 800).
2. Importa `tokens.css` con `@import './tokens.css';`.
3. Aplica el Reset CSS universal: `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`.
4. Configura las reglas globales de `body`: tipografía base, color de fondo, color de texto principal, suavizado de fuentes y comportamiento de scroll.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
