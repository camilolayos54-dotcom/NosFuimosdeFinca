# TASK BE-002 — pom.xml
**Module:** backend/
**Priority:** CRITICAL
**Depends On:** None

## 1. Purpose
Declares Java 17 target, Spring Boot 3.x parent, all Maven dependencies.

## 2. Implementation Instructions
1. Create backend/pom.xml.
2. Set java.version 17.
3. Add starters: web, security, data-jpa, validation, mail.
4. Add: postgresql, flyway-core, jjwt-api/impl/jackson, spring-boot-starter-test, testcontainers.
