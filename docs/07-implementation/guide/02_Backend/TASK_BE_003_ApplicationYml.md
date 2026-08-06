# TASK BE-003 — application.yml
**Module:** backend/src/main/resources/
**Priority:** CRITICAL
**Depends On:** BE-002

## 1. Purpose
Configures datasource (env vars), HikariCP pool, JPA validate, Flyway, JWT secret/expirations, Wompi keys, WhatsApp API, Cloudinary.

## 2. Implementation Instructions
1. Create application.yml per backend.md section 2.2.
2. All secrets via env vars. Never hardcode.
