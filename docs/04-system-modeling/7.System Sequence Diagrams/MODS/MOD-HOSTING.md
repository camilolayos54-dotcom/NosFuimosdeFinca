# Módulo: MOD-HOSTING

### H-01: Proceso de Publicación de Propiedad

Este diagrama modela la lógica transaccional cuando un anfitrión crea una nueva finca (propiedad) y sube imágenes de la misma. Destaca la delegación del almacenamiento de archivos estáticos (imágenes) a un servicio de terceros (ej. AWS S3 o Cloudinary) de forma asíncrona o mediante firmas pre-aprobadas, y la posterior persistencia de las URLs en la base de datos principal.

```mermaid
sequenceDiagram
    autonumber
    actor H as Anfitrión
    participant C as Frontend
    participant API as Hosting API
    participant S3 as Storage Bucket (S3)
    participant DB as PostgreSQL

    H->>C: Llena Formulario y Sube Imágenes (Clic Publicar)
    C->>API: POST /api/properties (Datos + Multipart/form-data)
    
    alt Datos Inválidos
        API-->>C: HTTP 400 Bad Request (Validation Error)
        C-->>H: Mostrar Errores de Formulario
    else Validación Exitosa
        API->>S3: Upload Images (Procesamiento Batch)
        alt Error Subiendo Archivos
            S3-->>API: 502 Bad Gateway
            API-->>C: HTTP 500 Internal Server Error (Storage)
            C-->>H: Mostrar Toast de Error "No se pudieron procesar las imágenes"
        else Imágenes Subidas
            S3-->>API: URLs (HD, Gallery, Thumb)
            API->>DB: INSERT INTO properties (Datos)
            DB-->>API: property_id
            
            API->>DB: INSERT INTO property_images (property_id, urls)
            DB-->>API: OK
            
            API-->>C: HTTP 201 Created (Property ID)
            C-->>H: Mostrar Mensaje de Éxito y Redirigir a "Mis Propiedades"
        end
    end
```

---
### Implicaciones de Fase Específicas
- El backend requiere integración con un SDK de almacenamiento en la nube, aumentando el tiempo de respuesta. El Frontend debe mantener el "Spinner" o barra de progreso activo durante este periodo.
- El esquema de base de datos (`property_images`) requiere que las imágenes estén asociadas obligatoriamente a un `property_id` válido.
