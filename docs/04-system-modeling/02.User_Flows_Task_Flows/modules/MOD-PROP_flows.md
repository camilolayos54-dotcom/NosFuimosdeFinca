# User Flows: MOD-PROP (Gestion de Propiedades)

**Project:** Nos Fuimos de Finca
**Phase:** 4 System Modeling (D2)
**Module:** MOD-PROP
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heuristico)

Extraemos como el Finquero nutre el catalogo de la plataforma y como el Turista lo consume.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificacion UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Pipeline de Creacion de Finca** | **User Flow** | Extremadamente complejo. Un formulario gigante dividido en multiples pasos (Wizard) con subida de imagenes asincrona, generacion de slugs y estado borrador/publicado. | Finquero |
| **Visualizacion Perfil Publico** | **Task Flow** | El turista navega por la URL publica para ver la finca. Flujo de lectura lineal, altamente optimizado en LCP (Largest Contentful Paint). | Turista |

---

## 2. Screen Mapping (Cruce Topologico)

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Creacion Wizard (B2B)** | `/dashboard/fincas/new` -> `/dashboard/fincas/[id]/edit` | **Skeleton / Progress Bar:** "Subiendo 20 imagenes... 45%". |
| **Perfil Finca (B2C)** | `/finca/[slug]` | **Galeria Modal:** Visor de imagenes expandido en pantalla completa. |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Wizard de Creacion de Finca (Pipeline B2B)
Ensenar al Finquero a usar la plataforma requiere dividir el trabajo. Si le mostramos un formulario con 50 campos, se ira. Modelamos un *Wizard* donde la Finca se crea inmediatamente en la DB como "Borrador" y el Finquero puede ir completando pasos a su ritmo.

```mermaid
flowchart TD
    %% Nodos UI
    HubUI[Dashboard Catalogo<br>Ruta: /dashboard/fincas]
    Step1UI[Paso 1: Info Basica<br>Ruta: /dashboard/fincas/new]
    Step2UI[Paso 2: Amenidades y Precios<br>Ruta: /dashboard/fincas/123/edit]
    Step3UI[Paso 3: Galeria Fotos<br>Sube multiples archivos]
    UploadToastUI[Componente Progreso<br>'Subiendo 1/20...']
    PublishModalUI[Modal ' Listo para publicar?']
    
    %% Nodos Asincronos
    DB((PostgreSQL DB))
    Storage((AWS S3<br>Compresion WebP))
    SlugService((Generador de Slug<br>Backend))
    
    %% Decisiones
    IsDraftCheck{ Datos<br>Obligatorios<br>Completos?}

    %% Flujo Inicial (Draft)
    HubUI --> |Clic 'Crear Finca'| Step1UI
    Step1UI --> |Guardar| DB
    DB -.-> |Devuelve ID Borrador| Step2UI
    
    %% Proceso de Medios
    Step2UI --> |Guardar| Step3UI
    Step3UI --> |Sube JPGs| UploadToastUI
    UploadToastUI --> Storage
    Storage -.-> Step3UI
    
    %% Publicacion Final
    Step3UI --> |Clic 'Publicar Finca'| IsDraftCheck
    IsDraftCheck -- No (Faltan fotos) --> ErrorToastUI[Toast Error<br>Sube al menos 5 fotos]
    ErrorToastUI --> Step3UI
    
    IsDraftCheck -- Si --> SlugService
    SlugService -.-> |Asigna slug-unico| DB
    DB -.-> |Estado: PUBLISHED| HubUI
```

### 3.2. Task Flow: Visualizacion Perfil Publico (Turista)
El flujo mas importante del Marketplace. El turista lee la finca y navega la galeria de fotos.

```mermaid
flowchart TD
    %% Nodos UI
    SearchUI[Resultados Buscador<br>Ruta: /]
    ProfileUI[Perfil de la Finca<br>Ruta: /finca/slug]
    GalleryModalUI[Visor de Fotos Fullscreen<br>Componente UI]
    CheckoutHookUI[Seccion Inferior<br>Widget de Reserva MOD-CAL]
    
    %% Nodos Asincronos
    CDN((Cloudflare CDN<br>Imagenes Cacheadas))
    
    %% Flujo Lineal de Lectura
    SearchUI --> |Clickea en una Tarjeta| ProfileUI
    ProfileUI -.-> |Lazy Load de Fotos| CDN
    
    %% Acciones Atomicas en la misma vista
    ProfileUI --> |Clic 'Ver todas las fotos'| GalleryModalUI
    GalleryModalUI --> |Cerrar Modal| ProfileUI
    
    ProfileUI --> |Scroll Abajo| CheckoutHookUI
```
