- [ ] TASK_FE_021 — Vista Anfitrión: Landing Informativa y Wizard de Onboarding de Fincas 📅 2026-08-05 18:00
	- [ ] Paso 1: Crear src/pages/host-landing/host-landing.html
		- [ ] Diseñar landing promocional informando beneficios de publicar fincas
		- [ ] Agregar botón CTA 'Publicar mi Finca' que lleve a onboarding.html
	- [ ] Paso 2: Crear src/pages/onboarding/onboarding.html y onboarding.js
		- [ ] Diseñar formulario wizard por pasos (Paso 1: Ubicación, Paso 2: Amenidades, Paso 3: Fotos/Precios)
		- [ ] Enviar POST /api/v1/properties al completar el wizard

# TASK_FE_021 — Vista Anfitrión: Landing Informativa y Wizard de Onboarding de Fincas

**Módulo:** `frontend/`  
**Porcentaje de Avance:** 90% -> 94%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Promueve y facilita la captación de propietarios de finca (94%), mediante una landing informativa y un formulario guiado por pasos (wizard).

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Patrón de Formulario Multinivel (Wizard UI):** Navegación entre pasos de formulario (Paso 1 -> Paso 2 -> Paso 3) ocultando y mostrando bloques DOM mientras se valida cada sección.
* **Carga y Previsualización de Imágenes en Cliente (FileReader API):** Permitir la selección de fotos de la finca y mostrar vistas previas instantáneas antes de enviarlas al servidor.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `host-landing.html`
1. Diseña la landing explicativa destacando la rentabilidad, seguridad y soporte que ofrece NosFuimosdeFinca a los propietarios de finca.

### Paso 2: Crear `onboarding.html` y `onboarding.js`
1. Implementa el formulario wizard por pasos:
2. Paso 1: Nombre de la finca, Departamento, Municipio, Vereda e Instrucciones de llegada.
3. Paso 2: Número de dormitorios, capacidad de huéspedes, número de baños y checkboxes de amenidades.
4. Paso 3: Tarifa por noche en temporada baja/alta, depósito de garantía y selector de archivos de fotos.
5. Al finalizar el Paso 3, envía `apiPost('/properties', formData)` y redirige al dashboard de anfitrión.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
