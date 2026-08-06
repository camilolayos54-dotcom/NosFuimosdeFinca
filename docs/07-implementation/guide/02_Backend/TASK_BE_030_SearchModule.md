# TASK BE-030 — Search Module
**Module:** backend/.../search/
**Priority:** HIGH
**Depends On:** BE-017

## 1. Purpose
SearchController (GET /api/search with query params: checkin, checkout, guests, amenities, price). SearchService (faceted search + cross-selling soft-match). SearchQueryBuilder (dynamic SQL with whitelist sorting).

## 2. Implementation Instructions
1. Create SearchController, SearchService, SearchQueryBuilder, SearchRequest, SearchResponse.
