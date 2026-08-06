# TASK BE-014 — AuthService
**Module:** backend/.../iam/services/
**Priority:** CRITICAL
**Depends On:** BE-013

## 1. Purpose
Register (hash password, save user, send verification email), Login (validate credentials, generate tokens), Refresh (rotate refresh token).

## 2. Implementation Instructions
1. Create AuthService.java.
2. Use BCryptPasswordEncoder for password hashing.
