# Wireframe Specifications: `/dashboard` (Resumen y Analíticas)

**Ruta UI:** `/dashboard/finanzas` (Hub Principal B2B)
**Requisitos Funcionales Inyectados:** `MOD-DASH` (Gráficos, Data Masking PII y Exportación Segura).

---

## Resultados
![Dashboard Finanzas - Wireframe Desktop.png](<Dashboard Finanzas - Wireframe Desktop.png>)
![Dashboard Finanzas - Wireframe Mobile.png](<Dashboard Finanzas - Wireframe Mobile.png>)

- **Diagnóstico:** El finquero entra aquí para ver si su negocio es rentable. Requiere una interfaz ultra-limpia, con tipografía clara y datos duros.
- **Patrón Principal:** `Sidebar Dashboard + KPI Cards`.
  - **Desktop:** Un menú lateral oscuro (`Sidebar`) a la izquierda para navegación (Dashboard, Mis Fincas, Reservas, Calendario). A la derecha, un fondo gris súper claro (`#F8F9FA`) que alberga tarjetas blancas (`KPI Cards`) con números grandes.
  - **Mobile:** El menú lateral se oculta tras un menú Hamburguesa (`Hamburger Menu`). Los gráficos deben colapsar elegantemente o permitir scroll horizontal nativo.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar el Dashboard:

### A. Átomos
- `SidebarLinkIcon`: Iconos de navegación (Casa, Dinero, Calendario).
- `KpiNumber`: Tipografía muy grande (H1 o H2) para mostrar dinero (Ej. "$15.000.000").
- `ExportIcon` **(Obligatorio por MOD-DASH)**: Icono de descarga o archivo Excel/CSV.

### B. Moléculas
- `SidebarNavItem`: Une (`SidebarLinkIcon` + Texto de la ruta). *Variante: `Active` (Resaltado azul).*
- `KpiCard`: Tarjeta blanca con sombra muy suave (`box-shadow`) que une (Título pequeño "Ingresos del Mes" + `KpiNumber` + Porcentaje de crecimiento verde/rojo).
- `ExportButton` **(Obligatorio por MOD-DASH)**: Botón secundario que une (`ExportIcon` + "Descargar Reporte"). *Variantes: `Default`, `Loading`.*

### C. Organismos
- `B2BSidebar`: Agrupación vertical de múltiples `SidebarNavItem`s y el botón de "Cerrar Sesión" al final.
- `RevenueChartCard` **(Obligatorio por MOD-DASH)**: Una tarjeta inmensa (Ancho completo) que contiene un gráfico de barras o líneas comparando los meses del año, además del selector de rango de fechas.
- `ExportModal` **(Obligatorio por MOD-DASH)**: Modal que pregunta "Selecciona el mes a exportar" y advierte sobre el enmascaramiento de datos.

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Skeleton Loaders de Analítica (Obligatorio por NFR-DASH-02):**
   - La Base de Datos puede demorar 1 segundo calculando 5 años de ingresos. Mientras carga, las `KpiCard` y el `RevenueChartCard` deben pintarse con una animación Skeleton gris. Si la pantalla se queda en blanco, el Finquero pensará que perdió todo su dinero.
2. **Confianza en la Exportación (Prevención PII - Data Masking):**
   - El `ExportModal` debe ser transparente sobre la seguridad: Debe incluir un texto legal que diga *"Por seguridad y cumplimiento Habeas Data, los correos electrónicos de los turistas serán parcialmente ocultos en este reporte (Ej. j***@gmail.com)"*.
3. **Empty State Motivacional (Obligatorio por MOD-DASH):**
   - Si el finquero es nuevo y la BD devuelve un Array vacío (`length === 0`), NO muestres un gráfico roto o en cero. Dibuja un Empty State amigable en medio del Dashboard que diga: *"Aún no tienes ventas este mes. ¡Asegúrate de que tus fincas tengan buenas fotos!"*.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/dashboard`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Layout `Sidebar` izquierdo. Contenido derecho con 4 `KpiCard`s en la primera fila y un gran `RevenueChartCard` abajo.
- `[ ]` **Mobile (390px):** Menú escondido. Tarjetas apiladas 1x1 hacia abajo.

### ✅ Estados Transitorios (Asincronía)
- `[ ]` **Loading Dashboard (Obligatorio por MOD-DASH):** Pantalla donde las tarjetas muestran `Skeletons` parpadeantes.
- `[ ]` **Botón Exportando (Obligatorio por MOD-DASH):** El usuario oprimió "Descargar". El `ExportButton` se pone gris con un spinner.

### ✅ Excepciones (Unhappy Paths)
- `[ ]` **Empty State Comercial (Obligatorio por MOD-DASH):** Pantalla para el usuario nuevo sin ventas. No hay gráfico, hay una ilustración amigable motivándolo.
