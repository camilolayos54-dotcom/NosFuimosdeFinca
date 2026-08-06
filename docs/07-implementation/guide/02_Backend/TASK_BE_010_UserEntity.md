# TASK BE-010 — IAM JPA Entities
**Module:** backend/.../iam/models/
**Priority:** HIGH
**Depends On:** BE-009

## 1. Purpose
User.java, RefreshToken.java, EmailVerificationToken.java, PasswordResetToken.java JPA entities mapped to users, refresh_tokens tables.

## 2. Implementation Instructions
1. Create all 4 entity classes with @Entity, @Table annotations.
2. User.java maps all columns from V001 migration.
