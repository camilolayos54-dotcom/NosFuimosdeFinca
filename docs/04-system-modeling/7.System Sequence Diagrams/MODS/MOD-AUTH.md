# Módulo: MOD-AUTH

### A-01: Proceso de Autenticación (Login)

Este diagrama modela el flujo síncrono de inicio de sesión de un usuario, la validación de credenciales en la base de datos y la subsecuente generación de un JSON Web Token (JWT) firmado por el servidor para manejar la sesión en el cliente.

```mermaid
sequenceDiagram
    autonumber
    actor U as Usuario
    participant C as Frontend (Browser)
    participant API as Auth API
    participant DB as PostgreSQL

    U->>C: Ingresa Credenciales y Clic "Login"
    C->>API: POST /api/auth/login (email, password)
    
    API->>DB: SELECT user WHERE email = ?
    DB-->>API: User Data (Hashed Password)
    
    alt Usuario No Encontrado
        API-->>C: HTTP 401 Unauthorized
        C-->>U: Mostrar Error Genérico
    else Usuario Existe
        API->>API: Verificar Password Hash
        alt Hash No Coincide
            API-->>C: HTTP 401 Unauthorized
            C-->>U: Mostrar Error Genérico
        else Hash Coincide
            API->>API: Generar JWT (Access Token)
            API-->>C: HTTP 200 OK (Set-Cookie: jwt)
            C-->>U: Redirigir a Dashboard/Inicio
        end
    end
```

---
### Implicaciones de Fase Específicas
- El equipo Frontend debe configurar sus peticiones subsecuentes para incluir credentials y leer el estado desde el middleware.
- El Backend debe estandarizar el error 401 devolviendo un mensaje genérico para no revelar si falló el email o la contraseña por motivos de seguridad (Prevención de Enumeración).
