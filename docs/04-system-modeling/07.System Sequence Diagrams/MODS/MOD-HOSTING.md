# Modulo: MOD-HOSTING

### H-01: Proceso de Publicacion de Propiedad

Este diagrama modela la logica transaccional cuando un anfitrion crea una nueva finca (propiedad) y sube imagenes de la misma. Destaca la delegacion del almacenamiento de archivos estaticos (imagenes) a un servicio de terceros (ej. AWS S3 o Cloudinary) de forma asincrona o mediante firmas pre-aprobadas, y la posterior persistencia de las URLs en la base de datos principal.

```mermaid
sequenceDiagram
    autonumber
    actor H as Anfitrion
    participant C as Frontend
    participant API as Hosting API
    participant S3 as Storage Bucket (S3)
    participant DB as PostgreSQL

    H->>C: Llena Formulario y Sube Imagenes (Clic Publicar)
    C->>API: POST /api/properties (Datos + Multipart/form-data)
    
    alt Datos Invalidos
        API-->>C: HTTP 400 Bad Request (Validation Error)
        C-->>H: Mostrar Errores de Formulario
    else Validacion Exitosa
        API->>S3: Upload Images (Procesamiento Batch)
        alt Error Subiendo Archivos
            S3-->>API: 502 Bad Gateway
            API-->>C: HTTP 500 Internal Server Error (Storage)
            C-->>H: Mostrar Toast de Error "No se pudieron procesar las imagenes"
        else Imagenes Subidas
            S3-->>API: URLs (HD, Gallery, Thumb)
            API->>DB: INSERT INTO properties (Datos)
            DB-->>API: property_id
            
            API->>DB: INSERT INTO property_images (property_id, urls)
            DB-->>API: OK
            
            API-->>C: HTTP 201 Created (Property ID)
            C-->>H: Mostrar Mensaje de Exito y Redirigir a "Mis Propiedades"
        end
    end
```

---
### Implicaciones de Fase Especificas
- El backend requiere integracion con un SDK de almacenamiento en la nube, aumentando el tiempo de respuesta. El Frontend debe mantener el "Spinner" o barra de progreso activo durante este periodo.
- El esquema de base de datos (`property_images`) requiere que las imagenes esten asociadas obligatoriamente a un `property_id` valido.
