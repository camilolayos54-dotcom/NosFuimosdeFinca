# Índice Maestro de Tareas: Backend (Java 17 / Spring Boot 3.x) — Nos Fuimos de Finca

**Proyecto:** Nos Fuimos de Finca  
**Capa:** Backend Core Java 17 LTS (`Spring Boot 3.x`, `Spring MVC`, `Spring Security`, `Spring Data JPA`)  
**Estructura Base:** `backend/src/main/java/com/nosfuimosdefinica/`  

---

## Descripción General de la Capa Backend

El backend se organiza en arquitectura modular basada en paquetes de dominio DDD (`iam`, `catalog`, `booking`, `billing`, `search`, `dashboard`, `calendar`, `reviews`, `wishlist`, `notifications`, `shared`).

---

## Catálogo Detallado de Tareas

### Sprint 1: Scaffolding, Maven & Configuración Base

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-001** | [`TASK_BE_001`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_001_NosFuimosDeFincaApplication.md) | **Punto de entrada Spring Boot:** Clase principal `NosFuimosDeFincaApplication.java` anotada con `@SpringBootApplication`, `@EnableScheduling` (para ejecuciones en segundo plano) y `@EnableJpaAuditing` (para timestamping automático). Arranca el contexto Spring. | CRÍTICA | pom.xml |
| **BE-002** | [`TASK_BE_002`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_002_PomXml.md) | **Manifiesto de dependencias Maven:** Archivo `pom.xml` configurado para Java 17 LTS con starters de Spring Boot (`web`, `security`, `data-jpa`, `validation`, `mail`), driver `postgresql`, `flyway-core`, JJWT (`jjwt-api`, `jjwt-impl`, `jjwt-jackson`), y librerías de pruebas JUnit 5 / Testcontainers. | CRÍTICA | Ninguna |
| **BE-003** | [`TASK_BE_003`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_003_ApplicationYml.md) | **Configuración de ambiente:** Archivo `application.yml` cargando propiedades de conexión a PostgreSQL (HikariCP max-pool=10), Flyway migration path, expiración de tokens JWT (1h accesstoken, 7d refreshtoken), credenciales Wompi API, WhatsApp Business API y Cloudinary vía variables de entorno. | CRÍTICA | BE-002 |

---

### Sprint 2: Seguridad & Componentes Compartidos (`shared/`)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-004** | [`TASK_BE_004`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_004_SecurityConfig.md) | **Cadena de filtros de seguridad Spring Security:** Clase `SecurityConfig.java` declarando `SecurityFilterChain`. Configura manejo de sesiones `STATELESS`, rutas públicas permitidas (`/api/v1/auth/**`, `/api/v1/webhooks/wompi`, `/api/v1/properties/search`), y restricción por roles `OWNER_API` y `AGENCY_USER` para el panel. | CRÍTICA | BE-001 |
| **BE-005** | [`TASK_BE_005`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_005_JpaAndCorsConfig.md) | **Configuración de CORS, DataSource y JPA:** Clases `JpaConfig.java` (auditoría de fechas), `CorsConfig.java` (lista blanca de orígenes permitidos `localhost:5173` y dominio productivo), y `DataSourceConfig.java`. | ALTA | BE-001 |
| **BE-006** | [`TASK_BE_006`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_006_ExceptionHandling.md) | **Manejador global de excepciones:** `GlobalExceptionHandler.java` anotado con `@RestControllerAdvice`. Captura excepciones y genera respuestas JSON con formato estándar (status, error, message, timestamp) para 404 (`ResourceNotFoundException`), 409 (`ConflictException`), 401 (`UnauthorizedException`), 403 (`ForbiddenException`) y 422 (`ValidationException`). | ALTA | BE-001 |
| **BE-007** | [`TASK_BE_007`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_007_SharedUtils.md) | **Utilidades compartidas:** `DateUtils.java` (cálculo exacto de noches entre fechas check-in/out y validación de superposición) y `MoneyUtils.java` (conversión bidireccional entre centavos `BIGINT` y BigDecimal en pesos COP). | ALTA | BE-001 |
| **BE-008** | [`TASK_BE_008`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_008_JwtFilter.md) | **Filtro de autenticación JWT:** `JwtAuthenticationFilter.java` heredando de `OncePerRequestFilter`. Intercepta peticiones HTTP, extrae el token Bearer del header `Authorization`, valida la firma con `JwtService` y establece la autenticación en el `SecurityContextHolder`. | CRÍTICA | BE-004 |

---

### Sprint 3: Módulo IAM (Autenticación, Usuarios y KYC)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-009** | [`TASK_BE_009`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_009_IamEnums.md) | **Enums de identidad:** Enums `UserRole` (`TOURIST`, `AGENCY_USER`, `OWNER_API`) y `KycStatus` (`PENDING`, `VERIFIED`, `REJECTED`). | ALTA | BE-001 |
| **BE-010** | [`TASK_BE_010`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_010_UserEntity.md) | **Entidades de persistencia IAM:** `User.java` (mapea tabla `users`), `RefreshToken.java`, `EmailVerificationToken.java`, y `PasswordResetToken.java`. Incluyen auditoría y soft-delete. | ALTA | BE-009 |
| **BE-011** | [`TASK_BE_011`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_011_IamRepositories.md) | **Repositorios Spring Data IAM:** Interfaces `UserRepository` (búsqueda por email), `RefreshTokenRepository`, `EmailVerificationTokenRepository`, y `PasswordResetTokenRepository`. | ALTA | BE-010 |
| **BE-012** | [`TASK_BE_012`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_012_IamDTOs.md) | **DTOs de autenticación y perfil:** Records Java `LoginRequest`, `RegisterRequest`, `AuthResponse`, `ForgotPasswordRequest`, `ResetPasswordRequest`, `UserProfileDTO`, y `KycUploadResponse`. | ALTA | BE-009 |
| **BE-013** | [`TASK_BE_013`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_013_JwtService.md) | **Servicio de tokens JWT:** `JwtService.java` encargado de firmar y verificar tokens de acceso (1h) y tokens de refresco (7d) utilizando `io.jsonwebtoken`. | CRÍTICA | BE-010 |
| **BE-014** | [`TASK_BE_014`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_014_AuthService.md) | **Servicio de lógica de autenticación:** `AuthService.java` implementando registro de usuarios con hash de contraseña BCrypt, inicio de sesión con validación de credenciales, y rotación segura de refresh tokens. | CRÍTICA | BE-013 |
| **BE-015** | [`TASK_BE_015`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_015_UserAndKycServices.md) | **Servicios de perfil, KYC y recuperación:** `UserService.java` (actualización de perfil), `KycService.java` (subida de RUT a Cloudinary y actualización de estado KYC), `PasswordResetService.java`, `EmailVerificationService.java` (doble opt-in) y `RateLimitService.java`. | ALTA | BE-014 |
| **BE-016** | [`TASK_BE_016`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_016_IamControllers.md) | **Controladores REST IAM:** `AuthController.java` (POST `/api/v1/auth/register`, `/login`, `/refresh`, `/logout`), `UserProfileController.java` (GET/PATCH `/api/v1/users/me`), `KycController.java` (POST `/api/v1/kyc/upload`) y `PasswordResetController.java`. | ALTA | BE-015 |

---

### Sprint 4: Módulo Catálogo (Fincas y Propiedades)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-017** | [`TASK_BE_017`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_017_CatalogEntities.md) | **Entidades del catálogo de fincas:** `Property.java` (mapea tabla `properties` con geolocalización y precios base), `PropertyImage.java`, `PropertyAmenity.java`, `PropertyRules.java` (horarios 1:1), `PropertyAvailability.java` (bloqueos) y `SeasonalPrice.java`. | ALTA | BE-005 |
| **BE-018** | [`TASK_BE_018`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_018_CatalogRepositories.md) | **Repositorios del catálogo:** Interfaces `PropertyRepository`, `PropertyImageRepository` y `SeasonalPriceRepository` con consultas personalizadas por anfitrión y rango de fechas. | ALTA | BE-017 |
| **BE-019** | [`TASK_BE_019`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_019_CatalogDTOs.md) | **DTOs del catálogo:** Records `PropertyDTO` (detalle completo público), `PropertySummaryDTO` (tarjeta liviana para grillas) y `CreatePropertyRequest`. | ALTA | BE-017 |
| **BE-020** | [`TASK_BE_020`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_020_CatalogServices.md) | **Servicios de catálogo e imágenes:** `PropertyService.java` (gestión del catálogo y filtrado) y `PropertyImageService.java` (subida de fotografías HD a Cloudinary y ordenamiento de galería). | ALTA | BE-018 |
| **BE-021** | [`TASK_BE_021`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_021_CatalogControllers.md) | **Controladores REST de propiedades:** `PropertyController.java` (rutas `/api/v1/properties/**` para listar, ver detalle y crear finca) y `PropertyImageController.java` (endpoints de carga de archivos). | ALTA | BE-020 |

---

### Sprint 5: Módulo de Reservas (`booking/`)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-022** | [`TASK_BE_022`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_022_BookingEnumsAndEntities.md) | **Modelo de dominio de reservas:** Enum `BookingStatus` (`PENDING_PAYMENT`, `PENDING_APPROVAL`, `CONFIRMED`, `COMPLETED`, `CANCELLED`) y entidad JPA `Booking.java` con desglose estricto de tarifa base, aseo, plataforma y total. | ALTA | BE-017 |
| **BE-023** | [`TASK_BE_023`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_023_BookingDTOs.md) | **DTOs y Mappers de reserva:** Records `BookingDTO`, `CreateBookingRequest` y la clase `BookingMapper.java` para transformar centavos `BIGINT` a montos legibles en pesos COP. | ALTA | BE-022 |
| **BE-024** | [`TASK_BE_024`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_024_BookingUseCases.md) | **Casos de uso de negocio de reservas:** `CreateBookingUseCase.java` (valida disponibilidad sin superposición de fechas, aplica cupones, calcula desglose de precio y persiste reserva en `PENDING_PAYMENT`), `CancelBookingUseCase.java` (ejecuta política de cancelación) y `BookingAppService.java`. | CRÍTICA | BE-023 |
| **BE-025** | [`TASK_BE_025`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_025_BookingController.md) | **Controlador REST y Repositorio de reservas:** `BookingController.java` (endpoints `/api/v1/bookings/**` para crear reserva, ver mis reservas y cancelar) y `BookingRepository.java`. | ALTA | BE-024 |

---

### Sprint 6: Módulo de Pagos y Pasarela Wompi (`billing/`)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-026** | [`TASK_BE_026`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_026_BillingEnumsAndEntities.md) | **Modelo de pagos y desembolsos:** Enums `PaymentStatus` y `PayoutStatus`. Entidades JPA `Payment.java` (referencia Wompi) y `Payout.java` (desembolso bancario al finquero deduciendo comisión). | ALTA | BE-022 |
| **BE-027** | [`TASK_BE_027`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_027_BillingRepositories.md) | **Repositorios de facturación:** Interfaces `PaymentRepository` (búsqueda por referencia Wompi) y `PayoutRepository`. | ALTA | BE-026 |
| **BE-028** | [`TASK_BE_028`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_028_WompiIntegration.md) | **Integración con Pasarela Wompi:** `WompiHttpClient.java` (comunicación HTTP con Wompi), `ProcessWompiWebhookUseCase.java` (valida la firma criptográfica HMAC del webhook de Wompi, actualiza el estado del pago a `APPROVED`, confirma la reserva y genera la orden de desembolso en `Payout`) y `TriggerRefundUseCase.java`. | CRÍTICA | BE-027 |
| **BE-029** | [`TASK_BE_029`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_029_WompiWebhookController.md) | **Controlador de Webhooks:** `WompiWebhookController.java` exponiendo la ruta pública `POST /api/v1/webhooks/wompi` para recibir notificaciones asíncronas de pago. | ALTA | BE-028 |

---

### Sprint 7: Búsqueda Facetada, Calendario, Reseñas y Favoritos

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-030** | [`TASK_BE_030`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_030_SearchModule.md) | **Motor de búsqueda de fincas:** `SearchController.java` (`GET /api/v1/search`), `SearchService.java` (búsqueda facetada con filtros de fechas check-in/out, número de huéspedes, precio mínimo/máximo y amenidades con algoritmo de recomendación) y `SearchQueryBuilder.java` (construcción segura de SQL dinámico). | ALTA | BE-017 |
| **BE-031** | [`TASK_BE_031`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_031_CalendarModule.md) | **Gestión de calendario y precios de temporada:** `CalendarController.java`, `AvailabilityService.java` (bloqueo/desbloqueo manual de fechas por el finquero) y `SeasonalPricingService.java` (sobreescritura de precio por noche para fechas especiales). | ALTA | BE-017 |
| **BE-032** | [`TASK_BE_032`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_032_ReviewsModule.md) | **Módulo de evaluaciones:** `Review.java` (entidad JPA con restricción de 1 sola reseña por reserva completada), `ReviewService.java` y `ReviewController.java` (`POST /api/v1/reviews`). | MEDIA | BE-022 |
| **BE-033** | [`TASK_BE_033`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_033_WishlistModule.md) | **Módulo de lista de favoritos:** `Wishlist.java` (entidad JPA con índice UNIQUE user-property), `WishlistService.java` y `WishlistController.java` (`POST/DELETE /api/v1/wishlists`). | MEDIA | BE-017 |

---

### Sprint 8: Panel Dashboard, Notificaciones y Tareas Programadas

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-034** | [`TASK_BE_034`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_034_DashboardModule.md) | **Módulo de Dashboard e informes:** `DashboardController.java` (`GET /api/v1/dashboard/metrics`, `GET /api/v1/dashboard/macro-calendar`), `DashboardService.java` (agregación de métricas de ocupación e ingresos con SQL GROUP BY), `CsvExportService.java` (exportación CSV con ofuscación de datos sensibles PII) y `MacroCalendarService.java`. | ALTA | BE-025 |
| **BE-035** | [`TASK_BE_035`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_035_NotificationsModule.md) | **Módulo multicanal de notificaciones:** `Notification.java`, `NotificationService.java` (orquestador por tipo EMAIL/WHATSAPP), `WhatsAppService.java` (envío vía API REST de WhatsApp Business) y `EmailService.java` (envío SMTP con `JavaMailSender`). | ALTA | BE-010 |
| **BE-036** | [`TASK_BE_036`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_036_ScheduledJobs.md) | **Tareas automatizadas en segundo plano:** `CancelExpiredBookingsJob.java` (tarea `@Scheduled` ejecutada cada hora para cancelar reservas `PENDING_PAYMENT` con más de 24 horas sin pago) y `SendPreCheckinRemindersJob.java` (remitente diario a las 14:00 COT con instrucciones de llegada vía WhatsApp). | MEDIA | BE-024, BE-035 |
| **BE-037** | [`TASK_BE_037`](file:///c:/PROGRAMMING/PROJECTS/NosFuimosdeFincaNo/guide/02_Backend/TASK_BE_037_EventDispatcher.md) | **Despachador interno de eventos de reserva:** `BookingEventPayload.java` y `BookingEventDispatcher.java` para desacoplar el flujo de reservas de las notificaciones push/email. | MEDIA | BE-035 |
