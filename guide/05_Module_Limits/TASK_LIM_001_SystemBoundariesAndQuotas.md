# TASK LIM-001 — Operational Boundaries & Quota Enforcement

**Module:** Global System Constraints  
**File Type:** System Limit Contract Specification  
**Priority:** HIGH  
**Depends On:** `limits.md`  
**Blocks:** Production validation  

---

## 1. Purpose
Defines maximum operational limits: 10MB photo upload ceiling per Cloudinary upload, 24h PENDING_PAYMENT booking auto-expiration job, and 100 properties per agency account limit.

## 2. Implementation Instructions
1. Enforce max photo size check in `PropertyImageService.java`.
2. Enforce 24h expiration in `CancelExpiredBookingsJob.java`.
