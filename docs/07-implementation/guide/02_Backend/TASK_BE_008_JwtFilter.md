# TASK BE-008 — JwtAuthenticationFilter
**Module:** backend/.../shared/filter/
**Priority:** CRITICAL
**Depends On:** BE-004

## 1. Purpose
OncePerRequestFilter that extracts JWT from Authorization header, validates via JwtService, and sets SecurityContextHolder.

## 2. Implementation Instructions
1. Create JwtAuthenticationFilter.java extending OncePerRequestFilter.
2. Extract Bearer token from Authorization header.
3. If valid, populate SecurityContext with UsernamePasswordAuthenticationToken.
