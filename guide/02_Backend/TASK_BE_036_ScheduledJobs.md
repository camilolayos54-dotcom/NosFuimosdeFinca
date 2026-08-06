# TASK BE-036 — Scheduled Jobs
**Module:** backend/.../shared/scheduler/
**Priority:** MEDIUM
**Depends On:** BE-024, BE-035

## 1. Purpose
CancelExpiredBookingsJob (@Scheduled every hour - cancels PENDING bookings older than 24h). SendPreCheckinRemindersJob (@Scheduled daily 14:00 COT - WhatsApp check-in reminders).

## 2. Implementation Instructions
1. Create CancelExpiredBookingsJob.java and SendPreCheckinRemindersJob.java.
2. Use @Scheduled(cron = ...) annotations.
