# TASK BE-024 — Booking Use Cases
**Module:** backend/.../booking/application/
**Priority:** CRITICAL
**Depends On:** BE-023

## 1. Purpose
CreateBookingUseCase (validate availability, create lock, persist). CancelBookingUseCase (validate policy, refund, release lock). BookingAppService (query facade).

## 2. Implementation Instructions
1. Create all 3 use case classes. Enforce business rules (no overbooking, cancellation policy).
