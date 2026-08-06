# Índice Maestro de Tareas: DevOps & CI/CD — Nos Fuimos de Finca

**Proyecto:** Nos Fuimos de Finca  
**Capa:** Infraestructura, Docker y CI/CD (`Docker Compose`, `GitHub Actions`, `Railway / Render`)  

---

## Catálogo Detallado de Tareas

| ID Tarea | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **OPS-001** | [`TASK_OPS_001`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/04_CICD_Docker/TASK_OPS_001_DockerCompose.md) | **Orquestación de entorno local:** Archivo `docker-compose.yml` en la raíz del repositorio. Levanta un contenedor con `postgres:15-alpine` expuesto en el puerto `5432` con volumen de almacenamiento persistente `postgres_data` y credenciales de desarrollo. | CRÍTICA | Ninguna |
| **OPS-002** | [`TASK_OPS_002`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/04_CICD_Docker/TASK_OPS_002_BackendDockerfile.md) | **Empaquetamiento en contenedor productivo:** Archivo `backend/Dockerfile`. Construye una imagen Docker optimizada de dos etapas (multi-stage build): Etapa 1 compila el JAR con `eclipse-temurin:17-jdk-alpine`, Etapa 2 empaqueta el runtime liviano con `eclipse-temurin:17-jre-alpine` expuesto en el puerto `8080`. | ALTA | OPS-001 |
| **OPS-003** | [`TASK_OPS_003`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/04_CICD_Docker/TASK_OPS_003_GitHubActions.md) | **Pipeline de integración continua (CI):** Workflows `.github/workflows/ci-backend.yml` y `ci-frontend.yml`. Ejecuta pruebas unitarias e integración en Maven y valida el build de producción en Vite en cada Pull Request antes de fusionar a la rama `main`. | ALTA | OPS-002 |
