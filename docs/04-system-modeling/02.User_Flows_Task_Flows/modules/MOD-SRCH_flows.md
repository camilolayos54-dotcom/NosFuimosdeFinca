# User Flows: MOD-SRCH (Buscador B2C)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-SRCH
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Este es el primer punto de contacto del usuario con la plataforma. Exige una latencia minima y una alta disponibilidad.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Busqueda Parametrizada y Paginacion** | **User Flow** | Altamente dinamico. El usuario combina fechas, ubicacion y precios, y el Frontend debe responder con Skeleton Loaders, estados vacios ("No se encontraron fincas") o paginacion infinita. | Turista |

---

## 2. Screen Mapping (Cruce Topologico)

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Motor de Busqueda** | `/` (Landing Home) -> `/search?q=...` | **Empty State:** "Lo sentimos, no hay fincas con piscina en esas fechas". |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Busqueda Parametrizada y Empty States
Este flujo es vital para el Marketplace. Muestra como el Frontend debe reaccionar cuando la base de datos se demora o cuando los filtros del turista son tan estrictos que no existe una finca que cumpla con ellos.

```mermaid
flowchart TD
    %% Nodos UI
    HomeUI[Landing Page B2C<br>Ruta: /]
    SearchBarUI[Componente Search Bar<br>Input de Filtros]
    LoadingUI[Pantalla Skeleton Loaders<br>Buscando...]
    ResultsGridUI[Cuadricula de Fincas<br>Componente Card]
    EmptyStateUI[UI Sin Resultados<br>'Intenta borrar filtros']
    
    %% Nodos Asincronos
    SearchEngine((Motor SQL / Vectorial<br>Spring MVC @RestController))
    
    %% Decisiones
    FilterCheck{ El Turista<br>aplica filtros?}
    ResultCheck{ Count > 0?}

    %% Flujo de Busqueda
    HomeUI --> SearchBarUI
    SearchBarUI --> FilterCheck
    
    %% Busqueda Default vs Parametrizada
    FilterCheck -- No (Ver todas) --> LoadingUI
    FilterCheck -- Si (Ingresa Fechas/Precio) --> LoadingUI
    
    LoadingUI --> |Llamada AJAX| SearchEngine
    SearchEngine -.-> ResultCheck
    
    %% Unhappy Path (No hay fincas)
    ResultCheck -- No (0 Coincidencias) --> EmptyStateUI
    EmptyStateUI --> |Boton 'Limpiar Busqueda'| SearchBarUI
    
    %% Happy Path (Resultados y Scroll)
    ResultCheck -- Si --> ResultsGridUI
    ResultsGridUI --> |Scroll Abajo| InfiniteScroll(Paginacion Infinita AJAX)
    InfiniteScroll --> SearchEngine
```
