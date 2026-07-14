# User Flows: MOD-DASH (Dashboard y Analíticas B2B)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-DASH
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Extraemos las acciones administrativas del Finquero y de la Agencia sobre el panel de control.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Carga de Métricas Dinámicas** | **Task Flow** | El usuario entra y el sistema carga las métricas (Ingresos, Ocupación). No hay bifurcaciones de decisión del usuario. | Finquero / Agencia |
| **Exportación de Reporte Financiero (CSV)** | **User Flow** | El usuario pide exportar datos. Requiere validación de seguridad (Data Masking de PII) por parte del servidor antes de entregar el archivo. | Finquero / Agencia |

---

## 2. Screen Mapping (Cruce Topológico)

Las acciones del módulo ocurren íntegramente dentro del Ecosistema Protegido (B2B Hub).

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Renderizado Analíticas** | `/dashboard/finanzas` | **Skeleton Loaders:** Se muestran mientras el Backend totaliza los datos. |
| **Exportación CSV** | `/dashboard/finanzas` | **Toast Notification:** "Descarga Iniciada" o "Error Generando Archivo". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. Task Flow: Renderizado de Métricas y Skeleton Loaders
Demuestra cómo el Frontend debe pintar "fantasmas" (Skeletons) para evitar una pantalla en blanco mientras la Base de Datos procesa sumatorias pesadas (COUNT, SUM).

```mermaid
flowchart TD
    %% Nodos UI
    SidebarUI[Navegación Menú Lateral<br>Ruta: /dashboard/*]
    SkeletonUI[Pantalla con Skeleton Loaders<br>Componente UI Transitorio]
    ChartsUI[Pantalla Renderizada (Gráficos)<br>Ruta: /dashboard/finanzas]
    ErrorToastUI[Toast Error<br>Fallo de Conexión]
    
    %% Nodos Asíncronos
    DB((Supabase DB<br>Agregación de Datos))
    
    %% Flujo Lineal B2B
    SidebarUI --> |Clic 'Finanzas'| SkeletonUI
    SkeletonUI --> |Fetch API Asíncrono| DB
    
    DB -.-> |Timeout / Error 500| ErrorToastUI
    ErrorToastUI --> ChartsUI
    
    DB -.-> |Data Array 200 OK| ChartsUI
    
    %% Nota: ChartsUI reemplaza a SkeletonUI en el DOM.
```

### 3.2. User Flow: Exportación Financiera y Data Masking (PII)
Este es un flujo condicional de seguridad. El Finquero solicita descargar un CSV con los datos de sus turistas, pero el sistema debe interceptar y enmascarar los correos electrónicos (Habeas Data) antes de entregar el archivo.

```mermaid
flowchart TD
    %% Nodos UI
    FinanzasUI[Panel de Finanzas B2B<br>Ruta: /dashboard/finanzas]
    ExportModalUI[Modal de Fechas<br>'Elegir Mes a Exportar']
    LoadingBtnUI[Botón de Descarga Girando<br>Estado 'Generando...']
    SuccessToastUI[Descarga en Navegador<br>Archivo CSV]
    
    %% Nodos Asíncronos
    BackendAPI((API Worker<br>Nos Fuimos de Finca))
    SecurityLayer((Módulo de Data Masking<br>Ofusca PII))
    
    %% Decisiones
    DataCheck{¿Existen registros<br>en ese mes?}

    %% Interacción del Usuario
    FinanzasUI --> |Clic 'Exportar Excel/CSV'| ExportModalUI
    ExportModalUI --> |Selecciona Fechas| LoadingBtnUI
    
    %% Proceso de Red
    LoadingBtnUI --> |POST /api/export| BackendAPI
    BackendAPI -.-> DataCheck
    
    %% Unhappy Path (Mes Vacío)
    DataCheck -- No (0 Filas) --> ErrorToastUI[Toast Warning<br>'No hay datos']
    ErrorToastUI --> ExportModalUI
    
    %% Happy Path y Seguridad
    DataCheck -- Sí (X Filas) --> SecurityLayer
    SecurityLayer -.-> |Aplica Máscara a Correos<br>juan***@gmail.com| SuccessToastUI
```
