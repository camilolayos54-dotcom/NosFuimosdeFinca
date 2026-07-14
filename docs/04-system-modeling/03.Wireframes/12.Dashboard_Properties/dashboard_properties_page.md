# Wireframe Specifications: `/dashboard/fincas` (Mis Fincas - Pipeline)

**Ruta UI:** `/dashboard/fincas` (y sub-rutas `/new`, `/edit`)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (El disenador NO debe re-dibujar el menu lateral, solo el contenido derecho).
**Requisitos Funcionales Inyectados:** `MOD-PROP` (Pipeline de Creacion de Finca y Soft-Delete).

---

# RESULTADOS
![Gestion de Fincas - Hub (Wireframe Desktop).png](Gesti%C3%B3n%20de%20Fincas%20-%20Hub%20%28Wireframe%20Desktop%29.png)
![Html Body-1.png](Html%20%E2%86%92%20Body-1.png)
![Html Body-2.png](Html%20%E2%86%92%20Body-2.png)
![Html Body.png](Html%20%E2%86%92%20Body.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** Crear una finca en la plataforma requiere mucha informacion (Ubicacion, Precios, Reglas, Fotos). Si le pedimos todo en una sola pantalla larga, el finquero abandonara el proceso (Fatiga Cognitiva).
- **Patron Principal:** `Multi-Step Wizard + Draft Saving`.
  - El diseno debe partir la creacion en 3 pasos: 1. Info Basica, 2. Reglas y Precios, 3. Galeria de Fotos.
  - La pantalla principal (`/dashboard/fincas`) no es el wizard, sino una Tabla o Grilla (Hub) mostrando el listado de las fincas que el dueno posee, con "Pildoras de Estado" (Ej. `Publicada`, `Borrador`, `Inactiva`).

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la gestion de fincas:

### A. Atomos
- `StatusPill`: Pildora de estado. *Variantes: `Draft` (Gris), `Published` (Verde), `Inactive` (Rojo).*
- `StepIndicator`: Circulos con numeros (1, 2, 3) unidos por una linea.
- `ToggleSwitch` **(Obligatorio por MOD-PROP)**: Interruptor para activar/desactivar (Soft Delete) una finca.

### B. Moleculas
- `PropertyRow`: Una fila en el Hub principal. Une (Foto Miniatura + Nombre + `StatusPill` + Boton "Editar" + `ToggleSwitch`).
- `WizardProgressHeader`: Une (Titulo de paso + `StepIndicator`).

### C. Organismos
- `PropertiesHubList`: Tabla o lista que contiene multiples `PropertyRow`.
- `MediaUploadStep` **(Obligatorio por MOD-PROP)**: El bloque mas complejo del Wizard. Une (`FileUploadArea` inmenso + Componentes transitorios de carga "Subiendo imagen 1/10...").

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Gestion de Carga Asincrona (Imagenes pesadas):**
   - Segun los Casos de Uso de `MOD-PROP`, el Finquero subira fotos de 10MB desde su celular. El `MediaUploadStep` debe tener un diseno claro que le diga al usuario "Estamos procesando tus imagenes, puedes guardar y seguir".
2. **Proteccion de Datos (Soft-Delete B2B):**
   - El sistema NO PERMITE borrar fincas que tienen historial (Regla `NFR-PROP-01`). Por lo tanto, no disenes un boton con el icono de "Papelera". Disena un `ToggleSwitch` (Interruptor) que cambie el estado de la finca de `Activa` a `Inactiva`. Esto protegera la integridad de la base de datos.
3. **Guardado Automatico (Borradores):**
   - El boton principal del Wizard no debe decir "Siguiente", debe decir "Guardar y Continuar".

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/fincas`:

### Pantallas Base (Happy Path)
- `[ ]` **Hub Principal (`/dashboard/fincas`):** Dibuja la lista de fincas del dueno. En el `Layout Padre` del dashboard.
- `[ ]` **Wizard Paso 3 (`/dashboard/fincas/new#step3`) (Obligatorio por MOD-PROP):** Dibuja la pantalla donde se suben las fotos. Muestra como se ven los archivos subidos (como pequenas miniaturas en cuadritos).

### Excepciones Legales (Unhappy Paths)
- `[ ]` **Error Soft-Delete (Obligatorio por MOD-PROP):** Dibuja la pantalla donde el Finquero intenta apagar (`ToggleSwitch`) una finca que tiene reservas pagadas para el proximo mes. Debe aparecer un Modal de Error de Negocio: *"No puedes ocultar esta finca porque tienes turistas agendados. Cancela las reservas primero"*.
