# TASK BE-004 — SecurityConfig.java
**Module:** backend/.../shared/config/
**Priority:** CRITICAL
**Depends On:** BE-001

## 1. Purpose
Configures Spring Security filter chain, public/private route rules, stateless sessions, JWT filter registration.

## 2. Implementation Instructions
1. Create SecurityConfig.java.
2. Permit /api/v1/auth/**, /api/v1/webhooks/wompi.
3. Require auth for all other /api/** routes.
