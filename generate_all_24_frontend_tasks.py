import os

target_dir = r"c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide\03_Frontend"

tasks = [
    {
        "id": "TASK_FE_001",
        "file": "TASK_FE_001_MonorepoStructure.md",
        "title": "Inicialización del Monorepo Frontend y Estructura de Directorios",
        "prog": "0% -> 4%",
        "date": "2026-08-05 08:00",
        "p1": "Navegar al directorio raíz del proyecto frontend",
        "p1_subs": ["Acceder a la carpeta frontend/ en la raíz del repositorio de NosFuimosdeFinca"],
        "p2": "Crear la estructura física de carpetas",
        "p2_subs": ["Crear el directorio src/pages/", "Crear el directorio src/components/", "Crear el directorio src/services/", "Crear el directorio src/styles/", "Crear el directorio public/assets/"],
        "p3": "Inicializar el archivo package.json",
        "p3_subs": ["Ejecutar el comando de inicialización de npm", "Instalar Vite 5.x como dependencia de desarrollo", "Configurar los scripts dev, build y preview en package.json"],
        "purpose": "Establece el punto de partida físico del cliente web (0%). Se encarga de estructurar el directorio frontend/ dividiendo responsabilidades entre código fuente (src/), recursos estáticos (public/), estilos globales (src/styles/), componentes reutilizables (src/components/), servicios HTTP (src/services/) y vistas independientes (src/pages/).",
        "steps": [
            ("Navegar al directorio raíz del proyecto frontend", ["Dirígete a la raíz del repositorio de NosFuimosdeFinca.", "Ubícate dentro de la carpeta frontend/."]),
            ("Crear la estructura física de carpetas", ["Crea la carpeta src/pages/ donde residirán los subdirectorios de cada página de la aplicación.", "Crea la carpeta src/components/ para los módulos JS inyectables.", "Crea la carpeta src/services/ para llamadas HTTP Fetch y sesión JWT.", "Crea la carpeta src/styles/ para las hojas de estilo CSS vanilla.", "Crea la carpeta public/assets/ para imágenes estáticas y recursos."]),
            ("Inicializar el archivo package.json", ["Ejecuta la inicialización de paquete npm en modo por defecto.", "Instala Vite en su versión 5.x dentro de devDependencies.", "En el archivo package.json, agrega los scripts dev, build y preview."])
        ]
    },
    {
        "id": "TASK_FE_002",
        "file": "TASK_FE_002_ViteMpaConfig.md",
        "title": "Configuración Bundler Vite MPA y Servidor de Desarrollo",
        "prog": "4% -> 8%",
        "date": "2026-08-05 08:30",
        "p1": "Crear el archivo vite.config.js en la raíz de frontend/",
        "p1_subs": ["Importar la función resolve del módulo 'path' de Node.js"],
        "p2": "Configurar la opción build.rollupOptions.input para Multi-Page Application",
        "p2_subs": ["Registrar el punto de entrada 'main' apuntando a src/pages/home/index.html", "Registrar los puntos de entrada 'catalog', 'property', 'checkout', 'auth_login', 'dashboard' y demás HTMLs"],
        "p3": "Configurar el proxy de desarrollo local en server.proxy",
        "p3_subs": ["Configurar el prefijo '/api' redirigiendo hacia http://localhost:8080 con changeOrigin activado"],
        "purpose": "Configura Vite 5.x en modo Multi-Page Application (MPA). Cada página cuenta con un HTML físico independiente. Define los puntos de entrada de build y el proxy de desarrollo /api para comunicarse con Spring Boot en puerto 8080.",
        "steps": [
            ("Crear el archivo vite.config.js", ["Crea el archivo vite.config.js en la raíz de frontend/.", "Utiliza defineConfig de Vite y la función resolve del módulo estándar path de Node.js."]),
            ("Configurar build.rollupOptions.input", ["Dentro del objeto exportado, agrega la propiedad build.rollupOptions.input.", "Mapea las entradas HTML: main, catalog, property, checkout, checkout_success, auth_login, auth_register, host_landing, onboarding, my_bookings, dashboard, error."]),
            ("Configurar server.proxy", ["Agrega la opción server.proxy mapeando '/api'.", "Configura target hacia 'http://localhost:8080' y activa changeOrigin: true."])
        ]
    },
    {
        "id": "TASK_FE_003",
        "file": "TASK_FE_003_CssTokensAndResets.md",
        "title": "Sistema de Diseño CSS Base, Resets y Tokens HSL",
        "prog": "8% -> 12%",
        "date": "2026-08-05 09:00",
        "p1": "Crear el archivo src/styles/tokens.css",
        "p1_subs": ["Declarar variables HSL para color primario (--color-primary)", "Declarar variables HSL para acento, superficie oscura, bordes y estados", "Declarar variables de tipografía (--font-body, --font-display)", "Declarar escala de espaciado modular en múltiplos de 4px (--spacing-1 a --spacing-12)"],
        "p2": "Crear el archivo src/styles/global.css",
        "p2_subs": ["Importar las fuentes Google Fonts ('Inter' y 'Outfit')", "Importar tokens.css mediante @import", "Aplicar Reset CSS universal (*, *::before, *::after)"],
        "purpose": "Establece el sistema de diseño visual (12%). Define tokens HSL para colores, tipografías y espaciado modular, asegurando consistencia y eliminación de estilos predeterminados del navegador.",
        "steps": [
            ("Crear src/styles/tokens.css", ["Declara la regla :root con variables HSL para colores primario (Verde Finca), acento (Naranja CTA), superficies oscuras y estados.", "Define tokens de tipografía para 'Inter' (cuerpo) y 'Outfit' (titulares).", "Define variables de espaciado modular (múltiplos de 4px) y radios de borde."]),
            ("Crear src/styles/global.css", ["Importa Google Fonts ('Inter' y 'Outfit').", "Importa tokens.css al inicio del archivo.", "Aplica el Reset CSS universal estableciendo box-sizing: border-box, margin: 0, padding: 0.", "Configura los estilos globales del body (background-color, color, line-height)."])
        ]
    },
    {
        "id": "TASK_FE_004",
        "file": "TASK_FE_004_CssUtilityComponents.md",
        "title": "Biblioteca de Componentes CSS de Utilidad y Modificadores",
        "prog": "12% -> 16%",
        "date": "2026-08-05 09:30",
        "p1": "Crear el archivo src/styles/components.css",
        "p1_subs": ["Definir clases de botones reutilizables (.btn, .btn-primary, .btn-accent, .btn-outline)", "Definir clases de tarjetas e insignias (.card, .badge, .badge-success)", "Definir clases de formularios e inputs (.input-group, .form-control)", "Definir contenedores layout (.container, .grid-catalog)"],
        "p2": "Importar components.css en global.css",
        "p2_subs": ["Vincular componentes CSS para que estén disponibles en todo el proyecto"],
        "purpose": "Proporciona una biblioteca de clases CSS reutilizables (.btn, .card, .input, .badge, .glass-panel) previniendo estilos duplicados e inconsistentes en las vistas.",
        "steps": [
            ("Crear src/styles/components.css", ["Define clases de botones .btn-primary y .btn-accent utilizando var(--color-primary) y var(--color-accent).", "Define clases de contenedores de tarjetas .card con fondo de superficie y sombras suaves.", "Define clases de campos de entrada .form-control con bordes de foco resaltados.", "Define clases de insígnias .badge y paneles glassmorphism .glass-panel."]),
            ("Vincular en global.css", ["Agrega @import './components.css'; al final de global.css."])
        ]
    },
    {
        "id": "TASK_FE_005",
        "file": "TASK_FE_005_HttpApiService.md",
        "title": "Servicio HTTP Fetch API y Manejo de Errores REST",
        "prog": "16% -> 20%",
        "date": "2026-08-05 10:00",
        "p1": "Crear el archivo src/services/api.js",
        "p1_subs": ["Implementar la función genérica apiRequest(endpoint, options)", "Configurar cabecera Content-Type: application/json por defecto", "Inyectar la cabecera Authorization Bearer si existe token JWT en localStorage", "Manejar respuestas HTTP no exitosas (400, 401, 403, 500) procesando el JSON de error"],
        "p2": "Exponer envoltorios HTTP auxiliares",
        "p2_subs": ["Crear funciones genéricas para métodos GET, POST, PUT, DELETE"],
        "purpose": "Encapsula todas las llamadas a la API REST backend (20%). Maneja automáticamente cabeceras de autenticación JWT y errores HTTP de forma centralizada.",
        "steps": [
            ("Crear src/services/api.js", ["Define la constante API_BASE apuntando a '/api/v1'.", "Escribe la función asíncrona apiRequest con manejo de opciones HTTP.", "Lee el token JWT de localStorage e inyecta la cabecera 'Authorization: Bearer <token>'.", "Evalúa response.ok; si es falso, extrae el cuerpo de error JSON y lanza una Excepción con el mensaje recibido."]),
            ("Exponer métodos helper", ["Implementa y exporta funciones helpers: apiGet(url), apiPost(url, body), apiPut(url, body), apiDelete(url)."])
        ]
    },
    {
        "id": "TASK_FE_006",
        "file": "TASK_FE_006_JwtAuthStorageService.md",
        "title": "Módulo de Almacenamiento Local y Gestión de Sesión JWT",
        "prog": "20% -> 25%",
        "date": "2026-08-05 10:30",
        "p1": "Crear el archivo src/services/auth.js",
        "p1_subs": ["Implementar funciones setToken(token), getToken(), removeToken()", "Implementar función getUserFromToken() decodificando el payload JWT base64", "Implementar función isAuthenticated() verificando expiración de token", "Implementar función hasRole(role) para control de acceso por roles"],
        "p2": "Implementar flujo de Logout",
        "p2_subs": ["Escribir función logout() que limpie el almacenamiento local y redirija al usuario"],
        "purpose": "Administra la sesión del usuario en cliente (25%). Almacena el token JWT en localStorage, valida su fecha de expiración y decodifica los roles (GUEST, OWNER, ADMIN).",
        "steps": [
            ("Crear src/services/auth.js", ["Implementa las funciones de almacenamiento y recuperación de token JWT.", "Escribe una función de decodificación segura base64 para inspeccionar los Claims del payload JWT.", "Implementa isAuthenticated() comparando la fecha de expiración del token (exp) contra Date.now().", "Implementa hasRole(role) verificando la lista de roles del usuario."]),
            ("Implementar logout()", ["Escribe la función logout() que remueva el token y redirija a '/src/pages/home/index.html'."])
        ]
    },
    {
        "id": "TASK_FE_007",
        "file": "TASK_FE_007_NavbarComponent.md",
        "title": "Componente Navegacional Encabezado / Navbar Responsive",
        "prog": "25% -> 30%",
        "date": "2026-08-05 11:00",
        "p1": "Crear el archivo src/components/navbar.js",
        "p1_subs": ["Escribir la función de inyección DOM renderNavbar()", "Construir la estructura HTML del logotipo, menú de navegación principal y acciones de usuario", "Evaluar el estado de autenticación mediante el servicio auth.js para cambiar el menú dinámicamente", "Agregar listener al botón del menú hamburguesa para togglear la navegación móvil"],
        "p2": "Asegurar inyección en contenedor header",
        "p2_subs": ["Verificar la presencia de <header id='main-header'> en el DOM antes de inyectar"],
        "purpose": "Construye e inyecta dinámicamente la barra de navegación responsive (30%). Muestra opciones adaptadas según la sesión del usuario (Huésped vs Anfitrión vs Visitante).",
        "steps": [
            ("Crear src/components/navbar.js", ["Escribe la función renderNavbar() encargada de seleccionar el elemento DOM con id 'main-header'.", "Evalúa si el usuario está autenticado usando auth.js.", "Si está logueado: genera HTML con enlaces a 'Mis Reservas', avatar y botón 'Cerrar Sesión'. Si es Propietario, añade enlace a 'Panel Finquero'.", "Si no está logueado: genera botones para 'Iniciar Sesión' y 'Registrarse'.", "Agrega listener de evento click al botón hamburguesa móvil para desplegar el drawer."]),
            ("Inyección automática", ["Ejecuta renderNavbar() al cargar el evento DOMContentLoaded."])
        ]
    },
    {
        "id": "TASK_FE_008",
        "file": "TASK_FE_008_FooterComponent.md",
        "title": "Componente Pie de Página / Footer Reutilizable",
        "prog": "30% -> 35%",
        "date": "2026-08-05 11:30",
        "p1": "Crear el archivo src/components/footer.js",
        "p1_subs": ["Escribir la función de inyección DOM renderFooter()", "Construir enlaces a secciones de ayuda, términos legales y políticas de privacidad", "Agregar enlaces de contacto directo mediante WhatsApp y correo de soporte", "Inyectar aviso de derechos reservados con el año actual dinámico"],
        "p2": "Inyectar en contenedor footer",
        "p2_subs": ["Verificar la presencia de <footer id='main-footer'> en la vista HTML"],
        "purpose": "Inyecta el pie de página global (35%) en todas las vistas HTML sin duplicidad de código, incluyendo enlaces institucionales, legales y canales de atención.",
        "steps": [
            ("Crear src/components/footer.js", ["Escribe la función renderFooter() seleccionando el contenedor id 'main-footer'.", "Genera la estructura HTML dividida en columnas: Acerca de NosFuimosdeFinca, Enlaces Rápidos, Términos Legales y Redes Sociales.", "Utiliza new Date().getFullYear() para mantener dinámico el aviso de copyright."]),
            ("Inyección automática", ["Llama a renderFooter() en el evento DOMContentLoaded."])
        ]
    },
    {
        "id": "TASK_FE_009",
        "file": "TASK_FE_009_ToastNotificationService.md",
        "title": "Componente Sistema de Notificaciones Toast",
        "prog": "35% -> 40%",
        "date": "2026-08-05 12:00",
        "p1": "Crear el archivo src/components/toast.js",
        "p1_subs": ["Crear contenedor dinámico div id='toast-container' en el body si no existe", "Implementar la función showToast(message, type, duration)", "Aplicar estilos visuales según el tipo de notificación (success, error, warning, info)", "Implementar temporizador de auto-remoción del elemento toast tras transcurrir el tiempo especificado"],
        "p2": "Exponer funciones helpers de conveniencia",
        "p2_subs": ["Crear métodos toastSuccess, toastError, toastWarning"],
        "purpose": "Proporciona un sistema de alertas flotantes efímeras (40%) para informar al usuario sobre el resultado de operaciones (reserva creada, error de login, cambios guardados).",
        "steps": [
            ("Crear src/components/toast.js", ["Asegura la existencia de un contenedor div flotante fijo en la esquina superior derecha del viewport.", "Escribe la función showToast(message, type = 'info', duration = 4000).", "Crea un elemento DOM para la alerta con la clase correspondiente a su tipo.", "Usa setTimeout para desvanecer y remover la alerta del DOM automáticamente tras la duración indicada."]),
            ("Exportar helpers", ["Exporta funciones auxiliares: toastSuccess(msg), toastError(msg), toastWarning(msg)."])
        ]
    },
    {
        "id": "TASK_FE_010",
        "file": "TASK_FE_010_HomePageHeroLayout.md",
        "title": "Vista Home: Maquetación HTML e Integración del Hero Search",
        "prog": "40% -> 45%",
        "date": "2026-08-05 12:30",
        "p1": "Crear la estructura HTML en src/pages/home/index.html",
        "p1_subs": ["Incluir etiquetas <header id='main-header'> y <footer id='main-footer'>", "Diseñar la sección Hero con título impactante y formulario de búsqueda rápida", "Crear campos de entrada para Municipio/Ubicación, Fecha de Entrada, Fecha de Salida y Cantidad de Huéspedes"],
        "p2": "Crear el script controlador src/pages/home/home.js",
        "p2_subs": ["Agregar listener al evento submit del formulario de búsqueda rápida", "Capturar los valores del formulario y redirigir a catalog.html con los query params correspondientes"],
        "purpose": "Construye el layout principal de la página de inicio (45%) enfocado en la conversión inmediata a través del formulario de búsqueda rápida de fincas.",
        "steps": [
            ("Crear src/pages/home/index.html", ["Incluye los contenedores header y footer para la inyección de componentes.", "Estructura la sección Hero Banner con fondo atractivo y panel flotante de búsqueda.", "Agrega inputs para selección de municipio, selector de rango de fechas y contador de huéspedes."]),
            ("Crear src/pages/home/home.js", ["Importa los componentes navbar y footer para su inicialización.", "Captura el submit del formulario de búsqueda, extrae los valores e instruye la navegación a '/src/pages/catalog/catalog.html?location=...&checkin=...&checkout=...&guests=...'."])
        ]
    },
    {
        "id": "TASK_FE_011",
        "file": "TASK_FE_011_HomePageFeaturedProperties.md",
        "title": "Vista Home: Renderizado Dinámico de Fincas Destacadas y Categorías",
        "prog": "45% -> 50%",
        "date": "2026-08-05 13:00",
        "p1": "Actualizar src/pages/home/index.html",
        "p1_subs": ["Crear contenedor div id='featured-properties-container' para la grilla de fincas", "Crear contenedor div id='categories-container' para los accesos directos por tipo de clima"],
        "p2": "Actualizar src/pages/home/home.js",
        "p2_subs": ["Invocar la API REST GET /api/v1/properties/featured usando api.js", "Generar dinámicamente las tarjetas HTML de fincas destacadas con foto, título, municipio y precio por noche", "Manejar estado de carga (skeleton loader) mientras se obtienen los datos"],
        "purpose": "Conecta la vista Home con el backend (50%) para renderizar dinámicamente las fincas más populares y las categorías por clima (cálido, templado, frío).",
        "steps": [
            ("Actualizar index.html", ["Agrega la sección 'Fincas Destacadas' con su contenedor correspondiente.", "Agrega la sección 'Explora por Categorías' (Fincas con Piscina, Clima Cálido, Pet Friendly)."]),
            ("Actualizar home.js", ["Llama a la API GET '/properties/featured'.", "Itera el array de propiedades devuelto e inyecta las tarjetas de finca con imagen de portada, calificación promedio, capacidad y precio por noche.", "Implementa un estado de carga visual tipo Skeleton Loader mientras la petición está en curso."])
        ]
    },
    {
        "id": "TASK_FE_012",
        "file": "TASK_FE_012_CatalogFilterSidebarLayout.md",
        "title": "Vista Catálogo: Layout de Búsqueda y Panel de Filtros Laterales",
        "prog": "50% -> 55%",
        "date": "2026-08-05 13:30",
        "p1": "Crear el archivo src/pages/catalog/catalog.html",
        "p1_subs": ["Diseñar layout de 2 columnas: Sidebar de Filtros (izquierda) y Grilla de Resultados (derecha)", "Crear controles de filtro: Rango de Precio (slider), Municipio (select), Capacidad de Huéspedes (number)", "Crear checkboxes para amenidades (Piscina, Jacuzzi, BBQ, Wifi, Pet Friendly, Aire Acondicionado)"],
        "p2": "Crear la hoja de estilos src/pages/catalog/catalog.css",
        "p2_subs": ["Establecer disposición responsive en grilla flex/grid adaptada a móviles"],
        "purpose": "Maqueta la estructura de la página de catálogo (55%) proporcionando un panel lateral de filtrado avanzado para afinar la búsqueda de fincas.",
        "steps": [
            ("Crear src/pages/catalog/catalog.html", ["Estructura la vista en dos columnas principales mediante CSS Grid.", "Diseña el sidebar de filtros con controles para precio mínimo/máximo, municipio, capacidad e insígnias de amenidades.", "Crea el área principal de resultados con contador de propiedades encontradas y menú de ordenamiento (precio menor a mayor, mejor valoradas)."]),
            ("Crear catalog.css", ["Aplica estilos para el panel lateral flotante y la cuadrícula adaptativa de tarjetas."])
        ]
    },
    {
        "id": "TASK_FE_013",
        "file": "TASK_FE_013_CatalogDynamicFilterLogic.md",
        "title": "Vista Catálogo: Lógica de Filtrado Dinámico y Paginación en Tiempo Real",
        "prog": "55% -> 60%",
        "date": "2026-08-05 14:00",
        "p1": "Crear el script controlador src/pages/catalog/catalog.js",
        "p1_subs": ["Leer y deserializar parámetros query de la URL al cargar la página", "Escuchar cambios en las entradas del panel de filtros para reconstruir los query params", "Invocar GET /api/v1/properties/search enviando los filtros mediante api.js", "Renderizar la grilla de fincas o mostrar mensaje amigable de 'No se encontraron resultados'"],
        "p2": "Implementar paginación de resultados",
        "p2_subs": ["Generar botones de paginación anterior/siguiente y número de página activa"],
        "purpose": "Añade interactividad al catálogo (60%). Aplica filtros en tiempo real, sincroniza la URL y realiza búsquedas dinámicas hacia el backend.",
        "steps": [
            ("Crear src/pages/catalog/catalog.js", ["Al iniciar, parsea URLSearchParams para rellenar los valores iniciales de los filtros.", "Define la función executeSearch() que recopila todos los filtros activos y consulta la API backend.", "Implementa debounce en las entradas de texto/rango de precio para evitar peticiones excesivas al servidor.", "Mapea los resultados renderizando las tarjetas de fincas o el estado vacío (Empty State)."]),
            ("Implementar paginación", ["Agrega controles para cambiar de página manteniendo los filtros aplicados actualmente."])
        ]
    },
    {
        "id": "TASK_FE_014",
        "file": "TASK_FE_014_PropertyDetailGalleryAndInfo.md",
        "title": "Vista Detalle de Finca: Galería Multimedia y Especificaciones",
        "prog": "60% -> 65%",
        "date": "2026-08-05 14:30",
        "p1": "Crear el archivo src/pages/property-detail/property.html",
        "p1_subs": ["Diseñar la cabecera con título de la finca, ubicación, botón de compartir y favoritos", "Diseñar la cuadrícula de galería multimedia de fotos (imagen principal + miniaturas)", "Diseñar la sección de descripción, capacidad de dormitorios, baños y lista de amenidades"],
        "p2": "Crear el controlador src/pages/property-detail/property.js",
        "p2_subs": ["Extraer el parámetro 'id' de la propiedad desde la URL", "Consultar GET /api/v1/properties/{id} mediante api.js y poblar la información en el DOM"],
        "purpose": "Construye la vista detallada de la finca (65%), presentando la galería de fotos, capacidad, descripción completa y lista de servicios.",
        "steps": [
            ("Crear property.html", ["Diseña el encabezado de la propiedad y la cuadrícula de imágenes destacadas.", "Estructura el cuerpo de la página detallando número de habitaciones, camas, baños, normas de la finca y amenidades con íconos."]),
            ("Crear property.js", ["Obtén el ID de la propiedad de la URL.", "Realiza la petición GET a '/api/v1/properties/' + id.", "Inyecta las imágenes en la galería y actualiza la información detallada en los elementos DOM."])
        ]
    },
    {
        "id": "TASK_FE_015",
        "file": "TASK_FE_015_PropertyDetailInteractiveQuoteWidget.md",
        "title": "Vista Detalle de Finca: Cotizador Interactivo de Fechas y Widget de Reserva",
        "prog": "65% -> 70%",
        "date": "2026-08-05 15:00",
        "p1": "Actualizar src/pages/property-detail/property.html",
        "p1_subs": ["Crear el widget de cotización flotante (sidebar fijo a la derecha)", "Agregar inputs de fecha de check-in, check-out y número de huéspedes", "Crear contenedor de desglose de costos (noches x tarifa, depósito, tasa de servicio, total)"],
        "p2": "Actualizar src/pages/property-detail/property.js",
        "p2_subs": ["Escuchar cambios en las fechas seleccionadas para calcular la cantidad de noches", "Calcular el precio total dinámico e integrar el botón 'Reservar Ahora' para redirigir a checkout.html"],
        "purpose": "Implementa la calculadora de tarifas en tiempo real (70%), permitiendo seleccionar fechas y pasar al proceso de reserva con el resumen financiero listo.",
        "steps": [
            ("Actualizar property.html", ["Agrega la tarjeta flotante de reserva a la derecha de la pantalla con precio por noche prominente."]),
            ("Actualizar property.js", ["Agrega listeners a los selectores de fecha.", "Calcula la diferencia de días entre check-in y check-out.", "Calcula el costo subtotal, aplica depósito de garantía y tasa de servicio.", "Al presionar 'Reservar Ahora', valida autenticación y redirige a '/src/pages/checkout/checkout.html?propertyId=...&checkin=...&checkout=...'."])
        ]
    },
    {
        "id": "TASK_FE_016",
        "file": "TASK_FE_016_PropertyDetailReviewsSection.md",
        "title": "Vista Detalle de Finca: Sección de Reseñas y Calificaciones",
        "prog": "70% -> 74%",
        "date": "2026-08-05 15:30",
        "p1": "Actualizar src/pages/property-detail/property.html",
        "p1_subs": ["Crear contenedor div id='reviews-section' al final de la vista", "Diseñar resumen de puntuación por estrellas (limpieza, ubicación, comunicación, veracidad)", "Crear lista de comentarios de huéspedes y formulario para publicar nueva reseña"],
        "p2": "Actualizar src/pages/property-detail/property.js",
        "p2_subs": ["Consultar GET /api/v1/properties/{id}/reviews y renderizar comentarios", "Enviar POST /api/v1/properties/{id}/reviews al enviar el formulario de opinión"],
        "purpose": "Muestra la prueba social y reputación de la finca (74%), permitiendo consultar experiencias de otros huéspedes y publicar valoraciones.",
        "steps": [
            ("Actualizar property.html", ["Agrega la sección de comentarios con barras de promedio por categoría."]),
            ("Actualizar property.js", ["Consulta las reseñas de la finca e inyéctalas en el DOM.", "Habilita el formulario de reseña solo para usuarios que tengan reservas pasadas confirmadas en la finca."])
        ]
    },
    {
        "id": "TASK_FE_017",
        "file": "TASK_FE_017_CheckoutOrderSummaryAndForm.md",
        "title": "Vista Checkout: Formulario de Confirmación y Desglose de Pago",
        "prog": "74% -> 78%",
        "date": "2026-08-05 16:00",
        "p1": "Crear el archivo src/pages/checkout/checkout.html",
        "p1_subs": ["Diseñar formulario de datos del titular (nombre, documento, teléfono, peticiones especiales)", "Diseñar sección de selección de método de pago (Tarjeta de Crédito, PSE, Transferencia Nequi/Daviplata)", "Diseñar panel lateral con el resumen final de la reserva y la propiedad elegida"],
        "p2": "Crear el controlador src/pages/checkout/checkout.js",
        "p2_subs": ["Cargar la información de la reserva desde los parámetros de URL", "Procesar la solicitud mediante POST /api/v1/bookings enviando los datos de pago simulados", "Redirigir a checkout-success.html tras la respuesta exitosa del servidor"],
        "purpose": "Gestione la transacción y confirmación de reserva (78%), solicitando datos del huésped y procesando la reserva contra el backend.",
        "steps": [
            ("Crear checkout.html", ["Diseña el formulario de pago y el resumen lateral de la reserva."]),
            ("Crear checkout.js", ["Valida que el usuario esté autenticado.", "Al enviar el formulario, ejecuta POST '/api/v1/bookings'.", "Si la reserva es exitosa, navega a '/src/pages/checkout-success/checkout-success.html?bookingId=' + response.id."])
        ]
    },
    {
        "id": "TASK_FE_018",
        "file": "TASK_FE_018_CheckoutSuccessConfirmationView.md",
        "title": "Vista Confirmación de Reserva: Comprobante y Guía de Llegada",
        "prog": "78% -> 82%",
        "date": "2026-08-05 16:30",
        "p1": "Crear el archivo src/pages/checkout-success/checkout-success.html",
        "p1_subs": ["Diseñar mensaje de éxito prominente con ícono de check", "Mostrar código de confirmación de reserva, fechas reservadas y datos del anfitrión", "Agregar instrucciones de llegada a la finca y botón para descargar comprobante PDF/Imprimir"],
        "p2": "Crear el controlador src/pages/checkout-success/checkout-success.js",
        "p2_subs": ["Obtener bookingId de la URL y consultar GET /api/v1/bookings/{id} para validar la reserva"],
        "purpose": "Presenta la confirmación formal de la reserva (82%), entregando al cliente su código de voucher y datos de contacto del anfitrión.",
        "steps": [
            ("Crear checkout-success.html", ["Diseña el voucher de reserva con los datos del viaje."]),
            ("Crear checkout-success.js", ["Consulta los datos finales de la reserva creada y muéstralos en pantalla."])
        ]
    },
    {
        "id": "TASK_FE_019",
        "file": "TASK_FE_019_AuthLoginView.md",
        "title": "Vista Autenticación: Formulario de Inicio de Sesión / Login",
        "prog": "82% -> 86%",
        "date": "2026-08-05 17:00",
        "p1": "Crear el archivo src/pages/auth/login.html",
        "p1_subs": ["Diseñar el formulario de ingreso con campos para Correo Electrónico y Contraseña", "Agregar opciones de 'Recordarme' y enlace a '¿Olvidaste tu contraseña?'", "Agregar enlace de redirección hacia la página de registro (register.html)"],
        "p2": "Crear el controlador src/pages/auth/login.js",
        "p2_subs": ["Capturar el evento submit del formulario y enviar POST /api/v1/auth/login", "Almacenar el token JWT recibido mediante auth.js y redirigir al origen o al catálogo"],
        "purpose": "Permite el acceso a usuarios registrados (86%), autenticando credenciales contra el backend e iniciando la sesión cliente mediante JWT.",
        "steps": [
            ("Crear login.html", ["Diseña la tarjeta centrada de inicio de sesión."]),
            ("Crear login.js", ["Al enviar el formulario, ejecuta POST '/api/v1/auth/login' enviando email y password.", "Usa auth.js para guardar el token JWT.", "Muestra un Toast de éxito y redirige al usuario a la página de catálogo o al panel de anfitrión según su rol."])
        ]
    },
    {
        "id": "TASK_FE_020",
        "file": "TASK_FE_020_AuthRegisterView.md",
        "title": "Vista Autenticación: Formulario de Registro de Usuario y Selección de Rol",
        "prog": "86% -> 90%",
        "date": "2026-08-05 17:30",
        "p1": "Crear el archivo src/pages/auth/register.html",
        "p1_subs": ["Diseñar formulario con campos: Nombre Completo, Teléfono, Correo, Contraseña y Confirmación", "Agregar selector de tipo de cuenta: 'Quiero Reservar Fincas (Huésped)' vs 'Quiero Publicar mi Finca (Anfitrión)'", "Agregar checkbox de aceptación de Términos y Condiciones"],
        "p2": "Crear el controlador src/pages/auth/register.js",
        "p2_subs": ["Validar coincidencia de contraseñas y fortaleza mínima antes de enviar", "Enviar POST /api/v1/auth/register con el rol seleccionado y redirigir a login.html"],
        "purpose": "Permite la creación de nuevas cuentas (90%), distinguiendo entre roles de Huésped (`GUEST_ROLE`) y Propietario (`OWNER_ROLE`).",
        "steps": [
            ("Crear register.html", ["Diseña el formulario de registro con la selección explícita del tipo de usuario."]),
            ("Crear register.js", ["Valida que las contraseñas coincidan.", "Envía POST a '/api/v1/auth/register'.", "Muestra notificación Toast y redirige al inicio de sesión."])
        ]
    },
    {
        "id": "TASK_FE_021",
        "file": "TASK_FE_021_HostLandingAndOnboardingWizard.md",
        "title": "Vista Anfitrión: Landing Informativa y Wizard de Onboarding de Fincas",
        "prog": "90% -> 94%",
        "date": "2026-08-05 18:00",
        "p1": "Crear src/pages/host-landing/host-landing.html",
        "p1_subs": ["Diseñar landing promocional informando las ventajas de alquilar fincas en la plataforma", "Agregar botón principal CTA 'Publicar mi Finca Ahora' que redirija a onboarding.html"],
        "p2": "Crear src/pages/onboarding/onboarding.html y onboarding.js",
        "p2_subs": ["Diseñar wizard en 3 pasos: Paso 1 (Datos Básicos/Ubicación), Paso 2 (Amenidades/Capacidad), Paso 3 (Fotos/Precios)", "Enviar la información registrada a POST /api/v1/properties al completar el wizard"],
        "purpose": "Facilita la captación y registro de nuevas propiedades (94%) a través de un proceso guiado paso a paso para propietarios.",
        "steps": [
            ("Crear host-landing.html", ["Diseña la página informativa para propietarios de finca."]),
            ("Crear onboarding.html y onboarding.js", ["Implementa el formulario wizard por pasos.", "Captura fotos y detalles de la finca.", "Envía POST a '/api/v1/properties' para dar de alta la finca en la plataforma."])
        ]
    },
    {
        "id": "TASK_FE_022",
        "file": "TASK_FE_022_GuestMyBookingsView.md",
        "title": "Vista Huésped: Panel Mis Reservas e Historial de Viajes",
        "prog": "94% -> 97%",
        "date": "2026-08-05 18:30",
        "p1": "Crear el archivo src/pages/my-bookings/my-bookings.html",
        "p1_subs": ["Diseñar la vista con pestañas: 'Próximas Reservas', 'Historial Completado', 'Canceladas'", "Diseñar la tarjeta de reserva con foto de finca, fechas del viaje, precio pagado y estado de la reserva"],
        "p2": "Crear el controlador src/pages/my-bookings/my-bookings.js",
        "p2_subs": ["Consultar GET /api/v1/bookings/my-bookings mediante api.js", "Agregar botón de 'Cancelar Reserva' con modal de confirmación enviando DELETE /api/v1/bookings/{id}"],
        "purpose": "Permite al cliente gestionar sus viajes (97%), consultar comprobantes anteriores y gestionar solicitudes de cancelación de forma autónoma.",
        "steps": [
            ("Crear my-bookings.html", ["Diseña la interfaz de gestión de reservas personales."]),
            ("Crear my-bookings.js", ["Consulta las reservas del usuario y muéstralas organizadas por estado.", "Permite solicitar la cancelación de reservas próximas dentro del marco permitido."])
        ]
    },
    {
        "id": "TASK_FE_023",
        "file": "TASK_FE_023_OwnerDashboardView.md",
        "title": "Vista Anfitrión: Dashboard de Control, Calendario de Disponibilidad e Ingresos",
        "prog": "97% -> 99%",
        "date": "2026-08-05 19:00",
        "p1": "Crear el archivo src/pages/dashboard/dashboard.html",
        "p1_subs": ["Diseñar panel administrativo con sidebar de navegación: 'Resumen', 'Mis Fincas', 'Reservas Recibidas', 'Calendario'", "Crear tarjetas métricas: Ingresos del Mes, Tasa de Ocupación, Reservas Pendientes por Aprobar"],
        "p2": "Crear el controlador src/pages/dashboard/dashboard.js",
        "p2_subs": ["Consultar GET /api/v1/owner/metrics e inyectar métricas financieras", "Implementar tabla de solicitudes de reserva recibidas con botones 'Aprobar' y 'Rechazar'"],
        "purpose": "Entrega al propietario el centro de control operacional (99%) para administrar sus propiedades, controlar reservas recibidas y monitorear ingresos.",
        "steps": [
            ("Crear dashboard.html", ["Diseña el panel de administración para finqueros."]),
            ("Crear dashboard.js", ["Carga estadísticas de rendimiento financiero.", "Permite aceptar o rechazar solicitudes de reserva recibidas."])
        ]
    },
    {
        "id": "TASK_FE_024",
        "file": "TASK_FE_024_ErrorPagesAndBuildValidation.md",
        "title": "Vista Error y Fallback: Manejo de 404, 500 y Optimización Final",
        "prog": "99% -> 100%",
        "date": "2026-08-05 19:30",
        "p1": "Crear el archivo src/pages/error/error.html",
        "p1_subs": ["Diseñar vista amigable para errores 404 (Página no encontrada) y 500 (Error de Servidor)", "Incluir ilustración de finca y botón directo 'Volver al Inicio'"],
        "p2": "Crear el controlador src/pages/error/error.js",
        "p2_subs": ["Parsear el código de error recibido por URL parameter (ej: error.html?code=404)"],
        "p3": "Verificación final del proceso de build del cliente",
        "p3_subs": ["Ejecutar npm run build en la carpeta frontend/ verificando compilación limpia en la carpeta dist/ sin errores"],
        "purpose": "Finaliza el desarrollo del cliente frontend al 100%. Garantiza una experiencia sin caídas ante rutas inexistentes y valida que el paquete de producción compile limpiamente.",
        "steps": [
            ("Crear error.html y error.js", ["Diseña la página de fallback visual para errores HTTP."]),
            ("Validar Build de Producción 100%", ["Ejecuta 'npm run build' dentro de frontend/.", "Comprueba que todos los puntos de entrada HTML hayan generado sus assets optimizados dentro del directorio dist/."])
        ]
    }
]

def generate_markdown(t):
    md = []
    # Checklist at top
    md.append(f"- [ ] {t['id']} — {t['title']} 📅 {t['date']}")
    md.append(f"\t- [ ] Paso 1: {t['p1']}")
    for sub in t['p1_subs']:
        md.append(f"\t\t- [ ] {sub}")
    md.append(f"\t- [ ] Paso 2: {t['p2']}")
    for sub in t['p2_subs']:
        md.append(f"\t\t- [ ] {sub}")
    if 'p3' in t:
        md.append(f"\t- [ ] Paso 3: {t['p3']}")
        for sub in t['p3_subs']:
            md.append(f"\t\t- [ ] {sub}")
    
    md.append("")
    md.append(f"# {t['id']} — {t['title']}")
    md.append("")
    md.append(f"**Módulo:** `frontend/`  ")
    md.append(f"**Porcentaje de Avance:** {t['prog']}  ")
    md.append(f"**Prioridad:** ALTA  ")
    md.append(f"**Depende de:** Tareas previas de la secuencia  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Propósito y Justificación Técnica")
    md.append("")
    md.append(t['purpose'])
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Instrucciones de Implementación Paso a Paso")
    md.append("")
    
    step_num = 1
    for step_title, sub_steps in t['steps']:
        md.append(f"### Paso {step_num}: {step_title}")
        for idx, s in enumerate(sub_steps, 1):
            md.append(f"{idx}. {s}")
        md.append("")
        step_num += 1

    md.append("---")
    md.append("")
    md.append("## 3. Criterios de Aceptación y Verificación")
    md.append("")
    md.append("| # | Criterio de Aceptación | Método de Verificación |")
    md.append("|---|---|---|")
    md.append("| 1 | Estructura implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo |")
    md.append("| 2 | Cero errores en consola de desarrollo | Verificar consola F12 limpia de excepciones |")
    md.append("")
    return "\n".join(md)

# Clean out directory first
for f in os.listdir(target_dir):
    if f.startswith("TASK_FE_"):
        os.remove(os.path.join(target_dir, f))

# Write 24 files
for t in tasks:
    filepath = os.path.join(target_dir, t['file'])
    content = generate_markdown(t)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(tasks)} detailed frontend task files.")
