# TASK BE-034 — Dashboard Module
**Module:** backend/.../dashboard/
**Priority:** HIGH
**Depends On:** BE-025

## 1. Purpose
DashboardController (GET /api/dashboard/metrics, /api/dashboard/macro-calendar). ExportController (POST /api/dashboard/export - CSV). DashboardService, CsvExportService (PII masking), MacroCalendarService (multi-property availability matrix).

## 2. Implementation Instructions
1. Create DashboardController, ExportController, DashboardService, CsvExportService, MacroCalendarService, MetricsResponse, MacroCalendarResponse, ExportRequest.
