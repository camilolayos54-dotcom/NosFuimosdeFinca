# TASK OPS-002 — `backend/Dockerfile`

**Module:** `backend/`  
**File Type:** Multi-stage Dockerfile  
**Priority:** HIGH  
**Depends On:** OPS-001  
**Blocks:** Production deployment on Railway/Render  

---

## 1. Purpose
Creates multi-stage Docker build for Spring Boot 3.x using Eclipse Temurin JDK 17 for build and JRE 17 for runtime.

## 2. Implementation Instructions
1. Create `backend/Dockerfile`.
2. Stage 1 (`build`): `FROM eclipse-temurin:17-jdk-alpine`, `./mvnw package -DskipTests`.
3. Stage 2 (`runtime`): `FROM eclipse-temurin:17-jre-alpine`, `COPY --from=build /app/target/*.jar app.jar`, `EXPOSE 8080`, `ENTRYPOINT ["java", "-jar", "app.jar"]`.

## 3. Verification Command
```bash
docker build -t nosfuimosdefinca-backend backend/
```
