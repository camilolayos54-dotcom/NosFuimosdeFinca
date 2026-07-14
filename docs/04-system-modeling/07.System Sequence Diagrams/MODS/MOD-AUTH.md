# Modulo: MOD-AUTH

### A-01: Proceso de Autenticacion (Login)

Este diagrama modela el flujo sincrono de inicio de sesion de un usuario, la validacion de credenciales en la base de datos y la subsecuente generacion de un JSON Web Token (JWT) firmado por el servidor para manejar la sesion en el cliente.

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
        C-->>U: Mostrar Error Generico
    else Usuario Existe
        API->>API: Verificar Password Hash
        alt Hash No Coincide
            API-->>C: HTTP 401 Unauthorized
            C-->>U: Mostrar Error Generico
        else Hash Coincide
            API->>API: Generar JWT (Access Token)
            API-->>C: HTTP 200 OK (Set-Cookie: jwt)
            C-->>U: Redirigir a Dashboard/Inicio
        end
    end
```

---
### Implicaciones de Fase Especificas
- El equipo Frontend debe configurar sus peticiones subsecuentes para incluir credentials y leer el estado desde el middleware.
- El Backend debe estandarizar el error 401 devolviendo un mensaje generico para no revelar si fallo el email o la contrasena por motivos de seguridad (Prevencion de Enumeracion).
