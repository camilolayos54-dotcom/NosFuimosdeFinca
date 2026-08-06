# TASK BE-007 — DateUtils, MoneyUtils
**Module:** backend/.../shared/utils/
**Priority:** HIGH
**Depends On:** BE-001

## 1. Purpose
DateUtils: calculate nights between dates, validate date ranges. MoneyUtils: convert centavos COP to pesos and back.

## 2. Implementation Instructions
1. Create DateUtils.java with calculateNights(LocalDate checkIn, LocalDate checkOut).
2. Create MoneyUtils.java with toPesos(long centavos) and toCentavos(BigDecimal pesos).
