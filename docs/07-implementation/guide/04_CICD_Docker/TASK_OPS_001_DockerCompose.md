# TASK OPS-001 — `docker-compose.yml`

**Module:** `nos-fuimos-de-finca/`  
**File Type:** Docker Compose Configuration  
**Priority:** CRITICAL  
**Depends On:** Docker Desktop installed  
**Blocks:** Local database execution  

---

## 1. Purpose
Defines local container topology for PostgreSQL 15 (port 5432) with persistent volume.

## 2. Implementation Instructions
1. Create `docker-compose.yml` in project root.
2. Configure `postgres:15-alpine` service with environment variables (`POSTGRES_DB=nosfuimosdefinca`, `POSTGRES_USER=postgres`, `POSTGRES_PASSWORD=postgres`).
3. Map port `5432:5432`.

## 3. Verification Command
```bash
docker compose up -d
```
