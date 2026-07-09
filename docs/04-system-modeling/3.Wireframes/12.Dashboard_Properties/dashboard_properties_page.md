# Wireframe Specifications: `/dashboard/fincas` (Mis Fincas - Pipeline)

**Ruta UI:** `/dashboard/fincas` (y sub-rutas `/new`, `/edit`)
**Layout Padre:** Depende del *Sidebar Dashboard* definido en `/dashboard`. (El diseñador NO debe re-dibujar el menú lateral, solo el contenido derecho).
**Requisitos Funcionales Inyectados:** `MOD-PROP` (Pipeline de Creación de Finca y Soft-Delete).

---

# RESULTADOS
![Gestión de Fincas - Hub (Wireframe Desktop).png](Gesti%C3%B3n%20de%20Fincas%20-%20Hub%20%28Wireframe%20Desktop%29.png)
![Html → Body-1.png](Html%20%E2%86%92%20Body-1.png)
![Html → Body-2.png](Html%20%E2%86%92%20Body-2.png)
![Html → Body.png](Html%20%E2%86%92%20Body.png)


## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** Crear una finca en la plataforma requiere mucha información (Ubicación, Precios, Reglas, Fotos). Si le pedimos todo en una sola pantalla larga, el finquero abandonará el proceso (Fatiga Cognitiva).
- **Patrón Principal:** `Multi-Step Wizard + Draft Saving`.
  - El diseño debe partir la creación en 3 pasos: 1. Info Básica, 2. Reglas y Precios, 3. Galería de Fotos.
  - La pantalla principal (`/dashboard/fincas`) no es el wizard, sino una Tabla o Grilla (Hub) mostrando el listado de las fincas que el dueño posee, con "Píldoras de Estado" (Ej. `Publicada`, `Borrador`, `Inactiva`).

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar la gestión de fincas:

### A. Átomos
- `StatusPill`: Píldora de estado. *Variantes: `Draft` (Gris), `Published` (Verde), `Inactive` (Rojo).*
- `StepIndicator`: Círculos con números (1, 2, 3) unidos por una línea.
- `ToggleSwitch` **(Obligatorio por MOD-PROP)**: Interruptor para activar/desactivar (Soft Delete) una finca.

### B. Moléculas
- `PropertyRow`: Una fila en el Hub principal. Une (Foto Miniatura + Nombre + `StatusPill` + Botón "Editar" + `ToggleSwitch`).
- `WizardProgressHeader`: Une (Título de paso + `StepIndicator`).

### C. Organismos
- `PropertiesHubList`: Tabla o lista que contiene múltiples `PropertyRow`.
- `MediaUploadStep` **(Obligatorio por MOD-PROP)**: El bloque más complejo del Wizard. Une (`FileUploadArea` inmenso + Componentes transitorios de carga "Subiendo imagen 1/10...").

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Gestión de Carga Asíncrona (Imágenes pesadas):**
   - Según los Casos de Uso de `MOD-PROP`, el Finquero subirá fotos de 10MB desde su celular. El `MediaUploadStep` debe tener un diseño claro que le diga al usuario "Estamos procesando tus imágenes, puedes guardar y seguir".
2. **Protección de Datos (Soft-Delete B2B):**
   - El sistema NO PERMITE borrar fincas que tienen historial (Regla `NFR-PROP-01`). Por lo tanto, no diseñes un botón con el icono de "Papelera". Diseña un `ToggleSwitch` (Interruptor) que cambie el estado de la finca de `Activa` a `Inactiva`. Esto protegerá la integridad de la base de datos.
3. **Guardado Automático (Borradores):**
   - El botón principal del Wizard no debe decir "Siguiente", debe decir "Guardar y Continuar".

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard/fincas`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Hub Principal (`/dashboard/fincas`):** Dibuja la lista de fincas del dueño. En el `Layout Padre` del dashboard.
- `[ ]` **Wizard Paso 3 (`/dashboard/fincas/new#step3`) (Obligatorio por MOD-PROP):** Dibuja la pantalla donde se suben las fotos. Muestra cómo se ven los archivos subidos (como pequeñas miniaturas en cuadritos).

### ✅ Excepciones Legales (Unhappy Paths)
- `[ ]` **Error Soft-Delete (Obligatorio por MOD-PROP):** Dibuja la pantalla donde el Finquero intenta apagar (`ToggleSwitch`) una finca que tiene reservas pagadas para el próximo mes. Debe aparecer un Modal de Error de Negocio: *"No puedes ocultar esta finca porque tienes turistas agendados. Cancela las reservas primero"*.
