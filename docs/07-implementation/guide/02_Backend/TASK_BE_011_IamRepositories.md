# TASK BE-011 — IAM Repositories
**Module:** backend/.../iam/repositories/
**Priority:** HIGH
**Depends On:** BE-010

## 1. Purpose
JpaRepository interfaces for User, RefreshToken, EmailVerificationToken, PasswordResetToken.

## 2. Implementation Instructions
1. Create 4 repository interfaces extending JpaRepository<Entity, UUID>.
