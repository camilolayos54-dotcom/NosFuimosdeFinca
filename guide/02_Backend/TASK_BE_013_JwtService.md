# TASK BE-013 — JwtService
**Module:** backend/.../iam/services/
**Priority:** CRITICAL
**Depends On:** BE-010

## 1. Purpose
Generates and validates JWT AccessToken + RefreshToken using JJWT library and HMAC-SHA256.

## 2. Implementation Instructions
1. Create JwtService.java.
2. Implement generateAccessToken, generateRefreshToken, extractEmail, isTokenValid.
