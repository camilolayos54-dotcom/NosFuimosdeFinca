# TASK BE-028 — Wompi Integration
**Module:** backend/.../billing/
**Priority:** CRITICAL
**Depends On:** BE-027

## 1. Purpose
WompiHttpClient.java (REST calls to Wompi API). ProcessWompiWebhookUseCase.java (validate HMAC signature, update Payment status, trigger Payout). TriggerRefundUseCase.java (request refund via Wompi REST).

## 2. Implementation Instructions
1. Create WompiHttpClient using Java HttpClient.
2. Validate webhook HMAC-SHA256 signature before processing.
