# Wireframe Specifications: `/dashboard` (Resumen y Analiticas)

**Ruta UI:** `/dashboard/finanzas` (Hub Principal B2B)
**Requisitos Funcionales Inyectados:** `MOD-DASH` (Graficos, Data Masking PII y Exportacion Segura).

---

## Resultados
![Dashboard Finanzas - Wireframe Desktop.png](Dashboard%20Finanzas%20-%20Wireframe%20Desktop.png)
![Dashboard Finanzas - Wireframe Mobile.png](Dashboard%20Finanzas%20-%20Wireframe%20Mobile.png)

- **Diagnostico:** El finquero entra aqui para ver si su negocio es rentable. Requiere una interfaz ultra-limpia, con tipografia clara y datos duros.
- **Patron Principal:** `Sidebar Dashboard + KPI Cards`.
  - **Desktop:** Un menu lateral oscuro (`Sidebar`) a la izquierda para navegacion (Dashboard, Mis Fincas, Reservas, Calendario). A la derecha, un fondo gris super claro (`#F8F9FA`) que alberga tarjetas blancas (`KPI Cards`) con numeros grandes.
  - **Mobile:** El menu lateral se oculta tras un menu Hamburguesa (`Hamburger Menu`). Los graficos deben colapsar elegantemente o permitir scroll horizontal nativo.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar el Dashboard:

### A. Atomos
- `SidebarLinkIcon`: Iconos de navegacion (Casa, Dinero, Calendario).
- `KpiNumber`: Tipografia muy grande (H1 o H2) para mostrar dinero (Ej. "$15.000.000").
- `ExportIcon` **(Obligatorio por MOD-DASH)**: Icono de descarga o archivo Excel/CSV.

### B. Moleculas
- `SidebarNavItem`: Une (`SidebarLinkIcon` + Texto de la ruta). *Variante: `Active` (Resaltado azul).*
- `KpiCard`: Tarjeta blanca con sombra muy suave (`box-shadow`) que une (Titulo pequeno "Ingresos del Mes" + `KpiNumber` + Porcentaje de crecimiento verde/rojo).
- `ExportButton` **(Obligatorio por MOD-DASH)**: Boton secundario que une (`ExportIcon` + "Descargar Reporte"). *Variantes: `Default`, `Loading`.*

### C. Organismos
- `B2BSidebar`: Agrupacion vertical de multiples `SidebarNavItem`s y el boton de "Cerrar Sesion" al final.
- `RevenueChartCard` **(Obligatorio por MOD-DASH)**: Una tarjeta inmensa (Ancho completo) que contiene un grafico de barras o lineas comparando los meses del ano, ademas del selector de rango de fechas.
- `ExportModal` **(Obligatorio por MOD-DASH)**: Modal que pregunta "Selecciona el mes a exportar" y advierte sobre el enmascaramiento de datos.

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Skeleton Loaders de Analitica (Obligatorio por NFR-DASH-02):**
   - La Base de Datos puede demorar 1 segundo calculando 5 anos de ingresos. Mientras carga, las `KpiCard` y el `RevenueChartCard` deben pintarse con una animacion Skeleton gris. Si la pantalla se queda en blanco, el Finquero pensara que perdio todo su dinero.
2. **Confianza en la Exportacion (Prevencion PII - Data Masking):**
   - El `ExportModal` debe ser transparente sobre la seguridad: Debe incluir un texto legal que diga *"Por seguridad y cumplimiento Habeas Data, los correos electronicos de los turistas seran parcialmente ocultos en este reporte (Ej. j***@gmail.com)"*.
3. **Empty State Motivacional (Obligatorio por MOD-DASH):**
   - Si el finquero es nuevo y la BD devuelve un Array vacio (`length === 0`), NO muestres un grafico roto o en cero. Dibuja un Empty State amigable en medio del Dashboard que diga: *"Aun no tienes ventas este mes. Asegurate de que tus fincas tengan buenas fotos!"*.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Layout `Sidebar` izquierdo. Contenido derecho con 4 `KpiCard`s en la primera fila y un gran `RevenueChartCard` abajo.
- `[ ]` **Mobile (390px):** Menu escondido. Tarjetas apiladas 1x1 hacia abajo.

### Estados Transitorios (Asincronia)
- `[ ]` **Loading Dashboard (Obligatorio por MOD-DASH):** Pantalla donde las tarjetas muestran `Skeletons` parpadeantes.
- `[ ]` **Boton Exportando (Obligatorio por MOD-DASH):** El usuario oprimio "Descargar". El `ExportButton` se pone gris con un spinner.

### Excepciones (Unhappy Paths)
- `[ ]` **Empty State Comercial (Obligatorio por MOD-DASH):** Pantalla para el usuario nuevo sin ventas. No hay grafico, hay una ilustracion amigable motivandolo.
