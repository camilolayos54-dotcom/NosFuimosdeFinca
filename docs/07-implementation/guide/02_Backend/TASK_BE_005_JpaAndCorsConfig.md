# TASK BE-005 — JpaConfig, CorsConfig, DataSourceConfig
**Module:** backend/.../shared/config/
**Priority:** HIGH
**Depends On:** BE-001

## 1. Purpose
JpaConfig enables @CreatedDate/@LastModifiedDate auditing. CorsConfig whitelists localhost:5173 and prod domain. DataSourceConfig configures HikariCP.

## 2. Implementation Instructions
1. Create JpaConfig.java with @EnableJpaAuditing.
2. Create CorsConfig.java with allowed origins.
3. Create DataSourceConfig.java.
