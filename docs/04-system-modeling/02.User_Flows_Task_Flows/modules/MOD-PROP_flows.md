# User Flows: MOD-PROP (Gestión de Propiedades)

**Project:** Nos Fuimos de Finca
**Phase:** 4 — System Modeling (D2)
**Module:** MOD-PROP
**Status:** Approved

---

## 1. Flow Inventory (Inventario Heurístico)

Extraemos cómo el Finquero nutre el catálogo de la plataforma y cómo el Turista lo consume.

| Caso de Uso Origen (Fase 3) | Tipo de Flujo | Justificación UX (Regla Aplicada) | Actor |
| :--- | :--- | :--- | :--- |
| **Pipeline de Creación de Finca** | **User Flow** | Extremadamente complejo. Un formulario gigante dividido en múltiples pasos (Wizard) con subida de imágenes asíncrona, generación de slugs y estado borrador/publicado. | Finquero |
| **Visualización Perfil Público** | **Task Flow** | El turista navega por la URL pública para ver la finca. Flujo de lectura lineal, altamente optimizado en LCP (Largest Contentful Paint). | Turista |

---

## 2. Screen Mapping (Cruce Topológico)

| Flujo | Nodos UI Involucrados (Rutas Reales) | Estado UI Transaccional (Si aplica) |
| :--- | :--- | :--- |
| **Creación Wizard (B2B)** | `/dashboard/fincas/new` -> `/dashboard/fincas/[id]/edit` | **Skeleton / Progress Bar:** "Subiendo 20 imágenes... 45%". |
| **Perfil Finca (B2C)** | `/finca/[slug]` | **Galería Modal:** Visor de imágenes expandido en pantalla completa. |

---

## 3. Visual Flow Modeling (Mermaid)

### 3.1. User Flow: Wizard de Creación de Finca (Pipeline B2B)
Enseñar al Finquero a usar la plataforma requiere dividir el trabajo. Si le mostramos un formulario con 50 campos, se irá. Modelamos un *Wizard* donde la Finca se crea inmediatamente en la DB como "Borrador" y el Finquero puede ir completando pasos a su ritmo.

```mermaid
flowchart TD
    %% Nodos UI
    HubUI[Dashboard Catálogo<br>Ruta: /dashboard/fincas]
    Step1UI[Paso 1: Info Básica<br>Ruta: /dashboard/fincas/new]
    Step2UI[Paso 2: Amenidades y Precios<br>Ruta: /dashboard/fincas/123/edit]
    Step3UI[Paso 3: Galería Fotos<br>Sube múltiples archivos]
    UploadToastUI[Componente Progreso<br>'Subiendo 1/20...']
    PublishModalUI[Modal '¿Listo para publicar?']
    
    %% Nodos Asíncronos
    DB((Supabase DB))
    Storage((AWS S3<br>Compresión WebP))
    SlugService((Generador de Slug<br>Backend))
    
    %% Decisiones
    IsDraftCheck{¿Datos<br>Obligatorios<br>Completos?}

    %% Flujo Inicial (Draft)
    HubUI --> |Clic 'Crear Finca'| Step1UI
    Step1UI --> |Guardar| DB
    DB -.-> |Devuelve ID Borrador| Step2UI
    
    %% Proceso de Medios
    Step2UI --> |Guardar| Step3UI
    Step3UI --> |Sube JPGs| UploadToastUI
    UploadToastUI --> Storage
    Storage -.-> Step3UI
    
    %% Publicación Final
    Step3UI --> |Clic 'Publicar Finca'| IsDraftCheck
    IsDraftCheck -- No (Faltan fotos) --> ErrorToastUI[Toast Error<br>Sube al menos 5 fotos]
    ErrorToastUI --> Step3UI
    
    IsDraftCheck -- Sí --> SlugService
    SlugService -.-> |Asigna slug-unico| DB
    DB -.-> |Estado: PUBLISHED| HubUI
```

### 3.2. Task Flow: Visualización Perfil Público (Turista)
El flujo más importante del Marketplace. El turista lee la finca y navega la galería de fotos.

```mermaid
flowchart TD
    %% Nodos UI
    SearchUI[Resultados Buscador<br>Ruta: /]
    ProfileUI[Perfil de la Finca<br>Ruta: /finca/slug]
    GalleryModalUI[Visor de Fotos Fullscreen<br>Componente UI]
    CheckoutHookUI[Sección Inferior<br>Widget de Reserva MOD-CAL]
    
    %% Nodos Asíncronos
    CDN((Cloudflare CDN<br>Imágenes Cacheadas))
    
    %% Flujo Lineal de Lectura
    SearchUI --> |Clickea en una Tarjeta| ProfileUI
    ProfileUI -.-> |Lazy Load de Fotos| CDN
    
    %% Acciones Atómicas en la misma vista
    ProfileUI --> |Clic 'Ver todas las fotos'| GalleryModalUI
    GalleryModalUI --> |Cerrar Modal| ProfileUI
    
    ProfileUI --> |Scroll Abajo| CheckoutHookUI
```
