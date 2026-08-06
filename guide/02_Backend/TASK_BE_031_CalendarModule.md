# TASK BE-031 — Calendar Module
**Module:** backend/.../calendar/
**Priority:** HIGH
**Depends On:** BE-017

## 1. Purpose
CalendarController (GET/POST /api/properties/{id}/availability). AvailabilityService (manual date blocking by host). SeasonalPricingService (override base price for date ranges).

## 2. Implementation Instructions
1. Create CalendarController, AvailabilityService, SeasonalPricingService, AvailabilityRequest/Response, PropertyAvailabilityRepository.
