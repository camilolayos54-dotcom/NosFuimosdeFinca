# TASK OPS-003 — `.github/workflows/ci-backend.yml` & `ci-frontend.yml`

**Module:** `.github/workflows/`  
**File Type:** GitHub Actions Workflow Configuration  
**Priority:** HIGH  
**Depends On:** OPS-002  
**Blocks:** Automated PR checks  

---

## 1. Purpose
Automates Maven build/test for Spring Boot backend and Vite build verification for frontend on pull requests.

## 2. Implementation Instructions
1. Create `.github/workflows/ci-backend.yml` running `./mvnw test`.
2. Create `.github/workflows/ci-frontend.yml` running `npm run build`.

## 3. Verification Command
Validate YAML format.
