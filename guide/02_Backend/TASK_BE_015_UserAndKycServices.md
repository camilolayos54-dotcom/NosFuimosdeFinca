# TASK BE-015 — User, KYC, PasswordReset, EmailVerification, RateLimit Services
**Module:** backend/.../iam/services/
**Priority:** HIGH
**Depends On:** BE-014

## 1. Purpose
UserService (profile CRUD), KycService (RUT upload to S3/Cloudinary), PasswordResetService (token generation/validation), EmailVerificationService (double opt-in), RateLimitService (failed login counter).

## 2. Implementation Instructions
1. Create all 5 service classes per backend.md spec.
