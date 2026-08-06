# TASK BE-006 — GlobalExceptionHandler & Custom Exceptions
**Module:** backend/.../shared/exception/
**Priority:** HIGH
**Depends On:** BE-001

## 1. Purpose
Centralized @RestControllerAdvice. Custom exceptions: ResourceNotFoundException (404), ConflictException (409), UnauthorizedException (401), ForbiddenException (403), ValidationException (422).

## 2. Implementation Instructions
1. Create GlobalExceptionHandler.java with @ExceptionHandler for each.
2. Return standard JSON: timestamp, status, error, message.
