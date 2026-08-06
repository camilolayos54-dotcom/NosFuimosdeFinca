import os

target_dir = r"c:\PROGRAMMING\PROJECTS\NosFuimosdeFinca\guide\03_Frontend"

# Ensure directory exists
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Detailed expanded tasks definition
tasks = [
    {
        "id": "TASK_FE_001",
        "file": "TASK_FE_001_MonorepoStructure.md",
        "title": "Inicialización del Monorepo Frontend y Estructura de Directorios",
        "status": "[x]",
        "prog": "0% -> 4%",
        "date": "2026-08-05 08:00",
        "p1": "Navegar al directorio raíz del proyecto frontend",
        "p1_subs": ["Acceder a la carpeta frontend/ en la raíz del repositorio de NosFuimosdeFinca"],
        "p2": "Crear la estructura física de carpetas",
        "p2_subs": ["Crear src/pages/, src/components/, src/services/, src/styles/, src/utils/, src/store/ y public/assets/"],
        "p3": "Inicializar el archivo package.json",
        "p3_subs": ["Ejecutar npm init -y", "Instalar Vite 5.x como dependencia de desarrollo", "Configurar scripts dev, build y preview"],
        "purpose": "Establece el punto de partida físico del cliente web (0%). Organiza la arquitectura de directorios separando la lógica de presentación, servicios HTTP, componentes reutilizables, utilidades y estado de la aplicación.",
        "prereqs": [
            ("Estructura de Monorepo y Modularidad Web", "Entender la separación de responsabilidades entre vistas (pages), componentes reusables (components), servicios de integración (services) y utilidades puras (utils)."),
            ("Administración de Dependencias con NPM", "Conocer el archivo package.json, la diferencia entre dependencies y devDependencies, y la ejecución de scripts npm."),
            ("Empaquetadores de Código (Bundlers) de Nueva Generación", "Comprender la función de Vite como servidor de desarrollo ultra-rápido basado en ESM nativo y empaquetador de producción basado en Rollup.")
        ],
        "steps": [
            ("Navegar al directorio raíz del proyecto frontend", [
                "Abre la consola de comandos en la raíz del repositorio de NosFuimosdeFinca.",
                "Ingresa al directorio `frontend/` mediante la terminal."
            ]),
            ("Crear la estructura física de directorios", [
                "Crea la carpeta `src/pages/` para albergar los subsistemas de vistas físicas independientes.",
                "Crea la carpeta `src/components/` dividida en subdirectorios `ui/` y `shared/` para módulos DOM reutilizables.",
                "Crea la carpeta `src/services/` para las capas de conexión HTTP Fetch y cliente JWT.",
                "Crea la carpeta `src/styles/` para las hojas de estilo CSS vanilla (Tokens, Reset y Componentes).",
                "Crea las carpetas `src/utils/` y `src/store/` para funciones auxiliares puras y estado global.",
                "Crea la carpeta `public/assets/` para almacenamiento de imágenes estáticas y favicons."
            ]),
            ("Inicializar `package.json` e instalar Vite", [
                "Ejecuta `npm init -y` para generar la configuración base del paquete.",
                "Ejecuta `npm install -D vite@latest` para incluir la herramienta de empaquetado Vite 5.x.",
                "Añade en la propiedad `scripts` los comandos: `\"dev\": \"vite\"`, `\"build\": \"vite build\"`, `\"preview\": \"vite preview\"`."
            ])
        ]
    },
    {
        "id": "TASK_FE_002",
        "file": "TASK_FE_002_ViteMpaConfig.md",
        "title": "Configuración Bundler Vite MPA y Servidor de Desarrollo",
        "status": "[x]",
        "prog": "4% -> 8%",
        "date": "2026-08-05 08:30",
        "p1": "Crear el archivo vite.config.js en la raíz de frontend/",
        "p1_subs": ["Importar la función resolve del módulo 'path' de Node.js"],
        "p2": "Configurar la opción build.rollupOptions.input para Multi-Page Application",
        "p2_subs": ["Registrar los 15 puntos de entrada HTML (home, catalog, property-detail, checkout, auth, dashboard, etc.)"],
        "p3": "Configurar el proxy de desarrollo local en server.proxy",
        "p3_subs": ["Mapear el prefijo '/api' redirigiendo hacia http://localhost:8080 con changeOrigin activado"],
        "purpose": "Configura Vite 5.x en modo Multi-Page Application (MPA). Garantiza que cada vista HTML sea procesada como un punto de entrada independiente y canaliza el tráfico `/api` al backend Spring Boot en puerto 8080.",
        "prereqs": [
            ("Arquitectura Multi-Page Application (MPA)", "Diferencia entre SPA y MPA. En MPA cada vista posee su propio archivo HTML nativo cargando scripts ES Modules dedicados."),
            ("Módulos Node.js y Resolución de Rutas Absolutas", "Uso del módulo path y __dirname para resolver rutas absolutas de archivos de forma multiplataforma (Windows/Linux/macOS)."),
            ("Configuración de Servidores Proxy de Desarrollo", "Concepto de proxy inverso local para redirigir peticiones HTTP de un puerto a otro evitando políticas de restricción de Origen Cruzado (CORS) durante el desarrollo.")
        ],
        "steps": [
            ("Crear vite.config.js", [
                "Crea el archivo `vite.config.js` en la raíz de `frontend/`.",
                "Importa `defineConfig` de `'vite'` y `resolve` del paquete integrado `'path'`."
            ]),
            ("Configurar los puntos de entrada MPA en Rollup", [
                "Define la propiedad `build.rollupOptions.input` dentro de la exportación del archivo.",
                "Registra las claves absolutas resueltas con `resolve(__dirname, 'src/pages/...')` para: main (home/index.html), catalog (catalog/catalog.html), property (property-detail/property.html), checkout (checkout/checkout.html), checkout_success (checkout-success/checkout-success.html), auth_login (auth/login.html), auth_register (auth/register.html), host_landing (host-landing/host-landing.html), onboarding (onboarding/onboarding.html), my_bookings (my-bookings/my-bookings.html), dashboard (dashboard/dashboard.html), error (error/error.html)."
            ]),
            ("Configurar el proxy inverso `/api`", [
                "Agrega la sección `server.proxy` mapeando el string `'/api'`.",
                "Asigna `target: 'http://localhost:8080'`, `changeOrigin: true` y asegura que las rutas preserven su estructura REST."
            ])
        ]
    },
    {
        "id": "TASK_FE_003",
        "file": "TASK_FE_003_CssTokensAndResets.md",
        "title": "Sistema de Diseño CSS Base, Resets y Tokens HSL",
        "status": "[x]",
        "prog": "8% -> 12%",
        "date": "2026-08-05 09:00",
        "p1": "Crear el archivo src/styles/tokens.css",
        "p1_subs": ["Declarar variables HSL en :root para verde finca (--color-primary), naranja acento (--color-accent), superficies oscuras y estados", "Declarar escala de tipografía Inter/Outfit y espaciado modular en múltiplos de 4px"],
        "p2": "Crear el archivo src/styles/global.css",
        "p2_subs": ["Importar Google Fonts ('Inter' y 'Outfit')", "Importar tokens.css mediante @import", "Aplicar Reset CSS universal (*, *::before, *::after)"],
        "purpose": "Define el sistema de tokens visuales y la base de reseteo CSS (12%). Permite tematización coherente basada en variables HSL y estandarización tipográfica.",
        "prereqs": [
            ("Modelo de Color HSL (Hue, Saturation, Lightness)", "Comprensión de los ejes HSL para crear gamas armónicas, variaciones de tono (dark/light) y transparencias alpha."),
            ("Variables CSS Nativa (:root y var())", "Uso del pseudoclase :root para exponer propiedades personalizadas accesibles dinámicamente en todo el árbol DOM."),
            ("Reset CSS y Modelo de Caja (Box-Sizing)", "Importancia de box-sizing: border-box para incluir padding y border dentro del cálculo de ancho y alto de los elementos HTML.")
        ],
        "steps": [
            ("Crear `src/styles/tokens.css`", [
                "Abre la regla `:root` y define los tokens de color HSL: `--color-primary: hsl(158, 64%, 40%)`, `--color-primary-dark`, `--color-primary-light`, `--color-accent: hsl(27, 95%, 55%)`, `--color-surface: hsl(220, 20%, 10%)`, `--color-surface-2`, `--color-surface-3`, `--color-text-primary`, `--color-text-secondary`, `--color-border`, `--color-success`, `--color-error`.",
                "Define los tokens de fuente: `--font-body: 'Inter', sans-serif`, `--font-display: 'Outfit', sans-serif`.",
                "Define la escala de espaciado modular en incrementos de 4px (`--spacing-1: 4px` hasta `--spacing-12: 48px`).",
                "Define los bordes redondeados (`--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-full`)."
            ]),
            ("Crear `src/styles/global.css`", [
                "Carga las fuentes Google Fonts mediante `@import` para 'Inter' (400, 500, 600, 700) y 'Outfit' (600, 700, 800).",
                "Importa `tokens.css` con `@import './tokens.css';`.",
                "Aplica el Reset CSS universal: `*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }`.",
                "Configura las reglas globales de `body`: tipografía base, color de fondo, color de texto principal, suavizado de fuentes y comportamiento de scroll."
            ])
        ]
    },
    {
        "id": "TASK_FE_004",
        "file": "TASK_FE_004_CssUtilityComponents.md",
        "title": "Biblioteca de Componentes CSS de Utilidad y Modificadores",
        "status": "[x]",
        "prog": "12% -> 16%",
        "date": "2026-08-05 09:30",
        "p1": "Crear el archivo src/styles/components.css",
        "p1_subs": ["Definir clases de botones (.btn, .btn-primary, .btn-accent, .btn-outline)", "Definir clases de tarjetas (.card, .card-body) y distintivos (.badge, .badge-success)", "Definir clases de inputs (.form-control, .input-group) y paneles glassmorphism (.glass-panel)"],
        "p2": "Vincular en global.css",
        "p2_subs": ["Importar components.css en global.css"],
        "purpose": "Construye una biblioteca reutilizable de clases CSS (16%) evitando la duplicación de estilos visuales en formularios, botones, tarjetas e insígnias.",
        "prereqs": [
            ("Metodología de Nombres BEM / Utility-First", "Creación de clases CSS modulares compuestas por bloque, elemento y modificador."),
            ("Efectos Visuales Glassmorphism", "Uso de backdrop-filter: blur(), transparencias HSL y bordes semitransparentes para lograr paneles de cristal sobre fondos oscuros."),
            ("Estados de Interacción (:hover, :focus, :active, :disabled)", "Diseño de retroalimentación visual inmediata ante eventos del usuario en botones y campos de entrada.")
        ],
        "steps": [
            ("Crear `src/styles/components.css`", [
                "Diseña las clases base `.btn` con display flex/inline-flex, alineación centrada, transiciones de color y cursor pointer.",
                "Crea variantes `.btn-primary` (fondo primario), `.btn-accent` (fondo naranja CTA) y `.btn-outline` (borde transparente y texto coloreado).",
                "Crea la clase `.card` con fondo de superficie elevación 2, bordes redondeados y sombras proyectadas.",
                "Crea `.form-control` para inputs y selects con bordes de foco resoplados en el color de acento.",
                "Crea `.glass-panel` aplicando `backdrop-filter: blur(12px)` y transparencia HSL de fondo."
            ]),
            ("Importar en `global.css`", [
                "Agrega `@import './components.css';` en `global.css`."
            ])
        ]
    },
    {
        "id": "TASK_FE_005",
        "file": "TASK_FE_005_HttpApiService.md",
        "title": "Servicio HTTP Fetch API y Manejo de Errores REST",
        "status": "[x]",
        "prog": "16% -> 20%",
        "date": "2026-08-05 10:00",
        "p1": "Crear el archivo src/services/api.js",
        "p1_subs": ["Implementar la función asíncrona apiRequest(endpoint, options)", "Inyectar la cabecera Authorization: Bearer <jwt> si existe token en localStorage", "Procesar respuestas HTTP de error (400, 401, 403, 500) y lanzar excepciones descriptivas"],
        "p2": "Exponer envoltorios HTTP helpers",
        "p2_subs": ["Exportar métodos apiGet, apiPost, apiPut, apiDelete"],
        "purpose": "Encapsula el cliente de peticiones HTTP REST (20%). Centraliza el envío de tokens JWT de autenticación y la captura unificada de errores del servidor.",
        "prereqs": [
            ("API Fetch Nativa y Promesas JavaScript", "Uso de async/await, manejo de objetos Response y conversión de flujos de datos a JSON mediante .json()."),
            ("Cabeceras HTTP de Autenticación (Bearer Token)", "Formato estándar 'Authorization: Bearer <token>' para el intercambio de tokens de sesión con APIs REST."),
            ("Manejo Centralizado de Excepciones HTTP", "Evaluación de la propiedad response.ok y captura de códigos de estado HTTP de error (4xx y 5xx).")
        ],
        "steps": [
            ("Crear `src/services/api.js`", [
                "Establece la constante base `API_BASE = '/api/v1'`. ",
                "Escribe la función asíncrona exportada `apiRequest(endpoint, options = {})`.",
                "Extrae el token JWT almacenado en `localStorage.getItem('token')`.",
                "Construye las cabeceras inyectando `'Content-Type': 'application/json'` y `'Authorization': 'Bearer ' + token` cuando esté presente.",
                "Ejecuta `fetch(API_BASE + endpoint, config)` y evalúa `response.ok`.",
                "Si la respuesta falla, lee el cuerpo JSON de error y lanza un objeto `Error` con el mensaje devuelto por Spring Boot."
            ]),
            ("Crear funciones de conveniencia HTTP", [
                "Exporta `apiGet(url)`, `apiPost(url, data)`, `apiPut(url, data)` y `apiDelete(url)` utilizando `apiRequest` internamente."
            ])
        ]
    },
    {
        "id": "TASK_FE_006",
        "file": "TASK_FE_006_JwtAuthStorageService.md",
        "title": "Módulo de Almacenamiento Local y Gestión de Sesión JWT",
        "status": "[x]",
        "prog": "20% -> 25%",
        "date": "2026-08-05 10:30",
        "p1": "Crear el archivo src/services/auth.js",
        "p1_subs": ["Implementar setToken(token), getToken(), removeToken()", "Implementar getUserFromToken() decodificando el payload JWT en base64", "Implementar isAuthenticated() y hasRole(role)"],
        "p2": "Implementar función logout()",
        "p2_subs": ["Remover token de localStorage y redirigir a la vista de inicio"],
        "purpose": "Administra el estado de la sesión cliente (25%). Almacena el token JWT, valida su tiempo de expiración y permite la verificación de roles (`GUEST_ROLE`, `OWNER_ROLE`, `ADMIN_ROLE`).",
        "prereqs": [
            ("Estructura de Tokens JWT (JSON Web Token)", "Formato Header.Payload.Signature. Decodificación de la parte Payload codificada en Base64URL sin requerir librerías externas."),
            ("API Web Storage (localStorage)", "Persistencia de cadenas de texto en el almacenamiento local del navegador entre recargas de página."),
            ("Control de Acceso Basado en Roles (RBAC)", "Lógica de verificación de roles del usuario activo para permitir o denegar el acceso a ciertas vistas o acciones UI.")
        ],
        "steps": [
            ("Crear `src/services/auth.js`", [
                "Implementa las funciones `setToken(token)`, `getToken()` y `removeToken()` interactuando con `localStorage` bajo la clave `'auth_token'`.",
                "Escribe `getUserFromToken()`: divide la cadena del token por los puntos `.`, toma la segunda sección (payload), decodifícala usando `atob()` y conviértela con `JSON.parse()`.",
                "Escribe `isAuthenticated()`: verifica si existe token y comprueba si la propiedad `exp` del payload decodificado es superior a la fecha actual (`Date.now() / 1000`).",
                "Escribe `hasRole(targetRole)`: comprueba si el array de roles del payload incluye el rol especificado."
            ]),
            ("Implementar `logout()`", [
                "Crea la función `logout()` que elimine el token de `localStorage` y redirija a `/src/pages/home/index.html`."
            ])
        ]
    },
    {
        "id": "TASK_FE_007",
        "file": "TASK_FE_007_NavbarComponent.md",
        "title": "Componente Navegacional Encabezado / Navbar Responsive",
        "status": "[x]",
        "prog": "25% -> 30%",
        "date": "2026-08-05 11:00",
        "p1": "Crear src/components/navbar.js y src/components/navbar.css",
        "p1_subs": ["Construir función renderNavbar() inyectando el encabezado HTML", "Evaluar sesión con auth.js para cambiar el menú dinámicamente según el rol", "Agregar listeners de eventos para desplegar el menú hamburguesa móvil"],
        "p2": "Inyectar automáticamente en el DOM",
        "p2_subs": ["Buscar el contenedor <header id='main-header'> al cargar el DOM"],
        "purpose": "Construye e inyecta dinámicamente la barra de navegación (30%). Adapta los enlaces expuestos según el estado de la sesión (Huésped, Anfitrión o Usuario Anónimo).",
        "prereqs": [
            ("Manipulación del DOM en Vanilla JavaScript", "Uso de document.getElementById, querySelector e innerHTML para inyectar estructuras dinámicas."),
            ("Eventos de Interacción y Escuchadores (EventListeners)", "Captura de eventos click en botones de navegación y menús hamburguesa."),
            ("Diseño Responsive con Media Queries CSS", "Ocultamiento y despliegue del menú de navegación mediante transiciones CSS en pantallas móviles.")
        ],
        "steps": [
            ("Crear `src/components/navbar.js` y `navbar.css`", [
                "Escribe la función `renderNavbar()` que seleccione `<header id=\"main-header\">`.",
                "Consulta `isAuthenticated()` y `getUserFromToken()` del servicio `auth.js`.",
                "Si el usuario está logueado: genera HTML con su nombre, avatar, enlace a 'Mis Reservas' y botón 'Cerrar Sesión'. Si su rol es `OWNER_ROLE`, incluye el acceso a 'Panel Finquero'.",
                "Si el usuario es anónimo: genera enlaces de navegación básica y botones 'Iniciar Sesión' y 'Registrarse'.",
                "Registra el listener del menú hamburguesa para añadir o quitar la clase `.active` en el contenedor del menú móvil."
            ]),
            ("Inicialización automática", [
                "Invoca `renderNavbar()` cuando el evento `DOMContentLoaded` se dispare."
            ])
        ]
    },
    {
        "id": "TASK_FE_008",
        "file": "TASK_FE_008_FooterComponent.md",
        "title": "Componente Pie de Página / Footer Reutilizable",
        "status": "[x]",
        "prog": "30% -> 35%",
        "date": "2026-08-05 11:30",
        "p1": "Crear src/components/footer.js y src/components/footer.css",
        "p1_subs": ["Construir función renderFooter() inyectando el pie de página HTML", "Incluir enlaces de navegación secundaria, términos legales y redes sociales", "Generar el año de copyright dinámico"],
        "p2": "Inyectar en el contenedor main-footer",
        "p2_subs": ["Buscar <footer id='main-footer'> al cargar la página"],
        "purpose": "Inyecta el pie de página global (35%) en todas las vistas HTML sin duplicar código, incluyendo datos de contacto, aviso legal y soporte.",
        "prereqs": [
            ("Reutilización de Módulos DOM", "Patrón de diseño donde un componente JS inyecta una sección compartida del layout en múltiples páginas físicas HTML."),
            ("Manejo Dinámico de Fechas en JS", "Uso del objeto Date para calcular el año actual sin dejar valores hardcodeados en el pie de página.")
        ],
        "steps": [
            ("Crear `src/components/footer.js` y `footer.css`", [
                "Escribe `renderFooter()` seleccionando el contenedor `<footer id=\"main-footer\">`.",
                "Genera el HTML organizado en 4 columnas: Marca NosFuimosdeFinca, Destinos Populares, Enlaces de Interés (Términos, Privacidad, FAQ) y Contacto (WhatsApp, Email).",
                "Calcula el año en curso con `new Date().getFullYear()` e inyéctalo en la barra de copyright inferior."
            ]),
            ("Inyección automática", [
                "Asigna la ejecución de `renderFooter()` en la carga de la página."
            ])
        ]
    },
    {
        "id": "TASK_FE_009",
        "file": "TASK_FE_009_ToastNotificationService.md",
        "title": "Componente Sistema de Notificaciones Toast",
        "status": "[ ]",
        "prog": "35% -> 40%",
        "date": "2026-08-05 12:00",
        "p1": "Crear src/components/toast.js",
        "p1_subs": ["Asegurar contenedor flotante div id='toast-container' en el body", "Implementar la función showToast(message, type, duration)", "Aplicar estilos visuales para clases toast-success, toast-error, toast-warning", "Implementar temporizador de auto-destrucción del nodo DOM"],
        "p2": "Exportar funciones helpers de conveniencia",
        "p2_subs": ["Exportar toastSuccess(msg), toastError(msg), toastWarning(msg)"],
        "purpose": "Proporciona un servicio visual de notificaciones emergentes (40%) para dar retroalimentación inmediata sobre acciones del usuario (errores, confirmaciones, advertencias).",
        "prereqs": [
            ("Posicionamiento Fijo CSS (Fixed / Z-Index)", "Uso de position: fixed, top/right y z-index elevado para mostrar alertas superpuestas sobre cualquier contenido."),
            ("Animaciones y Transiciones CSS (Keyframes / Transition)", "Aplicación de transform: translateX() y opacity para suavizar la entrada y salida de notificaciones."),
            ("Gestión Asíncrona de Temporizadores (setTimeout)", "Programación de la remoción de elementos del DOM tras el vencimiento de un intervalo de milisegundos.")
        ],
        "steps": [
            ("Crear `src/components/toast.js`", [
                "Crea una función privada `getOrCreateToastContainer()` que busque o inserte `<div id=\"toast-container\">` fijo en la esquina superior derecha del viewport.",
                "Escribe `showToast(message, type = 'info', duration = 4000)`.",
                "Crea un nuevo elemento `div`, asígnale la clase `toast` y el modificador `toast-${type}` (success: verde, error: rojo, warning: amarillo, info: azul).",
                "Añade un botón de cierre `×` para descartar manualmente la alerta.",
                "Inserta la alerta en el contenedor y programa `setTimeout` para aplicar la clase `.fade-out` y remover el nodo del DOM pasados `duration` milisegundos."
            ]),
            ("Exportar helpers", [
                "Exporta `toastSuccess(msg)`, `toastError(msg)`, `toastWarning(msg)`."
            ])
        ]
    },
    {
        "id": "TASK_FE_010",
        "file": "TASK_FE_010_HomePageHeroLayout.md",
        "title": "Vista Home: Maquetación HTML e Integración del Hero Search",
        "status": "[x]",
        "prog": "40% -> 45%",
        "date": "2026-08-05 12:30",
        "p1": "Crear src/pages/home/index.html",
        "p1_subs": ["Estructurar sección Hero Banner con fondo impactante y buscador principal", "Crear inputs de Municipio, Check-in, Check-out y Cantidad de Huéspedes"],
        "p2": "Crear src/pages/home/home.js y src/pages/home/home.css",
        "p2_subs": ["Capturar evento submit del formulario de búsqueda", "Validar fechas y redirigir a catalog.html con parámetros URLSearchParams"],
        "purpose": "Maqueta la vista de portada (45%) enfocada en la captación de usuarios mediante el formulario de búsqueda de fincas por destino y fechas.",
        "prereqs": [
            ("Semántica HTML5 y Estructuras de Formulario", "Uso de elementos form, label, input (date, number, text) y atributos de accesibilidad."),
            ("Manipulación de Parámetros de URL (URLSearchParams)", "Construcción de cadenas de consulta (query strings) para pasar parámetros de búsqueda entre páginas sin requerir estado global complexo."),
            ("Validación de Rango de Fechas en Cliente", "Verificación lógica para asegurar que la fecha de salida (check-out) sea estrictamente posterior a la fecha de entrada (check-in).")
        ],
        "steps": [
            ("Crear `src/pages/home/index.html`", [
                "Incluye las etiquetas `<header id=\"main-header\">` y `<footer id=\"main-footer\">`.",
                "Maqueta la sección `.hero-section` con titular destacado y subtítulo invitando al alquiler de fincas en Colombia.",
                "Estructura el formulario `<form id=\"search-hero-form\">` con campos: Municipio (select o input autocomplete), Fecha Check-in (input date), Fecha Check-out (input date) y Huéspedes (input number min 1)."
            ]),
            ("Crear `src/pages/home/home.js` y `home.css`", [
                "Importa `navbar.js` y `footer.js` para inicializar el encabezado y pie de página.",
                "Agrega un listener al evento `submit` del formulario `#search-hero-form`.",
                "Valida que `checkin` sea igual o mayor al día de hoy y que `checkout` sea posterior a `checkin`.",
                "Si la validación es correcta, construye los parámetros `new URLSearchParams({...})` y navega a `/src/pages/catalog/catalog.html?` más la query string."
            ])
        ]
    },
    {
        "id": "TASK_FE_011",
        "file": "TASK_FE_011_HomePageFeaturedProperties.md",
        "title": "Vista Home: Renderizado Dinámico de Fincas Destacadas y Categorías",
        "status": "[x]",
        "prog": "45% -> 50%",
        "date": "2026-08-05 13:00",
        "p1": "Actualizar src/pages/home/index.html",
        "p1_subs": ["Crear contenedor div id='featured-properties-container' para la grilla de fincas", "Crear contenedor div id='categories-container' para accesos por clima"],
        "p2": "Actualizar src/pages/home/home.js",
        "p2_subs": ["Invocar GET /api/v1/properties/featured mediante api.js", "Generar dinámicamente las tarjetas de fincas con foto, municipio, capacidad y tarifa", "Implementar Skeleton Loaders durante la carga asíncrona"],
        "purpose": "Conecta la portada con los servicios backend (50%) para renderizar la grilla de fincas populares y el carrusel de categorías (Clima Cálido, Piscina, Pet Friendly).",
        "prereqs": [
            ("Patrón de Carga Visual (Skeleton Loaders)", "Diseño de contenedores pulsantes grises que imitan la forma del contenido final para mejorar el tiempo percibido de carga (UX)."),
            ("Renderizado Dinámico de Listas mediante Plantillas de Cadena (Template Literals)", "Transformación de arrays de objetos JSON en cadenas HTML usando map() y join('')."),
            ("Formateo de Moneda Local (Intl.NumberFormat)", "Formateo de precios numéricos a moneda colombiana (COP) con separadores de miles.")
        ],
        "steps": [
            ("Actualizar `index.html`", [
                "Crea la sección `.featured-section` con el contenedor `<div id=\"featured-properties-container\" class=\"properties-grid\">`.",
                "Crea la sección `.categories-section` con el contenedor `<div id=\"categories-container\" class=\"categories-grid\">`."
            ]),
            ("Actualizar `home.js`", [
                "Antes de realizar la petición, inyecta tarjetas skeleton en `#featured-properties-container`.",
                "Consume la API REST `apiGet('/properties/featured')`.",
                "Itera el array de propiedades e inyecta las tarjetas conteniendo: foto principal, insignia de calificación promedio, municipio, capacidad máxima de personas y precio por noche formateado con `new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' })`.",
                "Agrega al hacer click en cualquier tarjeta la redirección a `/src/pages/property-detail/property.html?id=` + id de la finca."
            ])
        ]
    },
    {
        "id": "TASK_FE_012",
        "file": "TASK_FE_012_CatalogFilterSidebarLayout.md",
        "title": "Vista Catálogo: Layout de Búsqueda y Panel de Filtros Laterales",
        "status": "[ ]",
        "prog": "50% -> 55%",
        "date": "2026-08-05 13:30",
        "p1": "Crear el archivo src/pages/catalog/catalog.html",
        "p1_subs": ["Diseñar layout de 2 columnas: Sidebar de Filtros (izquierda) y Grilla de Resultados (derecha)", "Crear controles para Rango de Precio, Municipio, Capacidad de Huéspedes", "Crear checkboxes para amenidades (Piscina, Jacuzzi, BBQ, Pet Friendly, Wifi)"],
        "p2": "Crear la hoja de estilos src/pages/catalog/catalog.css",
        "p2_subs": ["Establecer disposición responsive en flex/grid adaptativa"],
        "purpose": "Maqueta el layout del catálogo de búsqueda (55%) dividiendo la interfaz entre el panel de filtrado por facetas a la izquierda y el área de resultados a la derecha.",
        "prereqs": [
            ("Layouts Complejos de Dos Columnas (CSS Grid)", "Creación de cuadrículas con fr (fracciones) y minmax() para fijar la barra lateral y hacer fluida la columna de resultados."),
            ("Elementos de Formulario Complejos (Range Sliders y Custom Checkboxes)", "Estilización de inputs tipo range, checkboxes y radios personalizados con var(--color-primary).")
        ],
        "steps": [
            ("Crear `src/pages/catalog/catalog.html`", [
                "Estructura el contenedor principal `.catalog-container` dividiéndolo en `<aside class=\"filter-sidebar\">` y `<main class=\"catalog-main\">`.",
                "En el sidebar, crea el formulario `#filters-form` con los grupos: Rango de Precio (slider con visualización de precio mínimo y máximo), Municipio (select desplegable), Capacidad (input number) y Amenidades (checkboxes para Piscina, Jacuzzi, BBQ, Wifi, Pet Friendly, Aire Acondicionado).",
                "En el área principal, crea el encabezado con el contador de fincas encontradas `<span id=\"results-count\">` y el selector de ordenamiento `<select id=\"sort-by\">`."
            ]),
            ("Crear `src/pages/catalog/catalog.css`", [
                "Define la cuadrícula Grid para escritorio y la disposición apilada móvil.",
                "Diseña el panel de filtros como una tarjeta flotante `glass-panel`."
            ])
        ]
    },
    {
        "id": "TASK_FE_013",
        "file": "TASK_FE_013_CatalogDynamicFilterLogic.md",
        "title": "Vista Catálogo: Lógica de Filtrado Dinámico y Paginación en Tiempo Real",
        "status": "[ ]",
        "prog": "55% -> 60%",
        "date": "2026-08-05 14:00",
        "p1": "Crear el script controlador src/pages/catalog/catalog.js",
        "p1_subs": ["Deserializar parámetros query de la URL al inicializar la vista", "Escuchar cambios en las entradas del formulario de filtros para actualizar los query params", "Invocar GET /api/v1/properties/search con api.js", "Renderizar tarjetas de fincas o mostrar mensaje amigable si no hay resultados"],
        "p2": "Implementar paginación de resultados",
        "p2_subs": ["Crear controles de cambio de página preservando los filtros aplicados"],
        "purpose": "Agrega la lógica de filtrado reactivo (60%), sincronizando los filtros seleccionados con la URL y realizando consultas dinámicas paginadas al servidor.",
        "prereqs": [
            ("Técnica de Limitación de Frecuencia (Debounce)", "Implementación de funciones de retardo (setTimeout) para diferir la ejecución de peticiones HTTP mientras el usuario desliza el rango de precios."),
            ("Manejo de Estados Vacíos (Empty States)", "Diseño de mensajes amigables con sugerencias para el usuario cuando una combinación de filtros no retorna resultados."),
            ("Sincronización Bidireccional de URL (history.pushState)", "Actualización de la query string en la barra de direcciones sin provocal un refresco de página completo.")
        ],
        "steps": [
            ("Crear `src/pages/catalog/catalog.js`", [
                "Al cargar, lee los parámetros de la URL mediante `new URLSearchParams(window.location.search)` y asigna los valores a los inputs del filtro.",
                "Escribe la función `fetchCatalogProperties()` que recopile los valores de todos los inputs y checkboxes marcados, construya los parámetros query y consulte `apiGet('/properties/search?' + queryParams)`.",
                "Aplica un debounce de 300ms al evento `input` del control de rango de precio.",
                "Escucha el evento `change` en los checkboxes y desplegables para desencadenar la búsqueda inmediatamente.",
                "Si la respuesta contiene propiedades, genera la grilla de tarjetas; si el array está vacío, inyecta la vista de estado vacío con un botón 'Limpiar Filtros'."
            ]),
            ("Implementar paginación", ["Genera los botones de cambio de página actualizando el parámetro `page` y ejecutando `fetchCatalogProperties()`."])
        ]
    },
    {
        "id": "TASK_FE_014",
        "file": "TASK_FE_014_PropertyDetailGalleryAndInfo.md",
        "title": "Vista Detalle de Finca: Galería Multimedia y Especificaciones",
        "status": "[ ]",
        "prog": "60% -> 65%",
        "date": "2026-08-05 14:30",
        "p1": "Crear el archivo src/pages/property-detail/property.html",
        "p1_subs": ["Diseñar encabezado con título, ubicación, botón de compartir y favoritos", "Diseñar cuadrícula de galería multimedia de imágenes (foto principal + miniaturas)", "Diseñar sección de descripción, capacidad de dormitorios, baños y lista de amenidades con íconos"],
        "p2": "Crear el controlador src/pages/property-detail/property.js",
        "p2_subs": ["Obtener id de la finca desde window.location.search", "Consultar GET /api/v1/properties/{id} mediante api.js y poblar los elementos DOM"],
        "purpose": "Construye la vista de detalle de la finca (65%), desplegando la galería multimedia, distribución de espacios, amenidades y normas del establecimiento.",
        "prereqs": [
            ("Galerías de Imágenes e Interacciones Modal Lightbox", "Manejo de click en imágenes miniaturas para intercambiar la imagen principal o abrir la vista de pantalla completa."),
            ("Parseo de IDs desde la Cadenas de Consulta URL", "Extracción segura de identificadores numéricos o UUIDs desde los query params de la página."),
            ("Inyección de Iconografía SVG / Font Icons", "Mapeo dinámico de nombres de amenidades ('PISCINA', 'BBQ', 'WIFI') hacia sus respectivos íconos visuales.")
        ],
        "steps": [
            ("Crear `src/pages/property-detail/property.html`", [
                "Estructura el contenedor de la galería `.gallery-grid` con 1 imagen principal grande a la izquierda y 4 imágenes secundarias a la derecha.",
                "Estructura la columna izquierda de información: Titular, Municipio/Vereda, Capacidad máxima, Número de alcobas, Número de baños, Descripción detallada, Lista de amenidades e Instrucciones de llegada.",
                "Agrega la sección de normas de la finca (horarios de check-in/out, prohibición de sonido excesivo, mascotas)."
            ]),
            ("Crear `src/pages/property-detail/property.js`", [
                "Extrae el parámetro `id` de `window.location.search`.",
                "Si no existe `id`, redirige a la página de error 404.",
                "Ejecuta `apiGet('/properties/' + id)`.",
                "Inyecta las URLs de fotos en la galería y agrega un listener a las miniaturas para cambiar la foto principal activa.",
                "Mapea el array de amenidades renderizando íconos con sus etiquetas correspondientes."
            ])
        ]
    },
    {
        "id": "TASK_FE_015",
        "file": "TASK_FE_015_PropertyDetailInteractiveQuoteWidget.md",
        "title": "Vista Detalle de Finca: Cotizador Interactivo de Fechas y Widget de Reserva",
        "status": "[ ]",
        "prog": "65% -> 70%",
        "date": "2026-08-05 15:00",
        "p1": "Actualizar src/pages/property-detail/property.html",
        "p1_subs": ["Crear widget flotante de reserva a la derecha del layout (sticky sidebar)", "Agregar selectores de fecha check-in/check-out y contador de huéspedes", "Crear contenedor de desglose financiero (noches x tarifa, depósito, tasa de servicio, total)"],
        "p2": "Actualizar src/pages/property-detail/property.js",
        "p2_subs": ["Escuchar cambios en las fechas para calcular número de noches", "Calcular el valor total dinámico y activar botón 'Reservar Ahora'"],
        "purpose": "Implementa el cotizador de reserva en tiempo real (70%), calculando costos exactos según noches seleccionadas e iniciando el checkout.",
        "prereqs": [
            ("Posicionamiento Sticky CSS (position: sticky)", "Fijación del widget flotante de reserva en la pantalla mientras el usuario hace scroll sobre la descripción de la finca."),
            ("Operaciones Matemáticas de Fechas en JS", "Cálculo preciso de diferencia en días entre dos fechas evitando desfasajes por zonas horarias."),
            ("Validación Dinámica de Formularios y Estados Habilitados/Deshabilitados", "Deshabilitar el botón de reserva hasta que se seleccione un rango válido de fechas.")
        ],
        "steps": [
            ("Actualizar `property.html`", [
                "Crea el widget de cotización flotante con la clase `.booking-widget-sticky`.",
                "Incluye el precio por noche destacado, las entradas de fecha de entrada y salida, el selector de huéspedes y el contenedor de desglose financiero `#price-breakdown`."
            ]),
            ("Actualizar `property.js`", [
                "Registra listeners `change` en las entradas de fechas.",
                "Al seleccionar ambas fechas, calcula el número de noches `(dateOut - dateIn) / (1000 * 60 * 60 * 24)`.",
                "Multiplica las noches por la tarifa por noche de la finca, agrega el depósito de garantía reembolsable y la tasa de servicio de la plataforma (10%).",
                "Muestra el desglose de precios en el DOM y habilita el botón `#btn-start-booking`.",
                "Al presionar `#btn-start-booking`, verifica si el usuario está autenticado; si no lo está, redirige a `login.html`; si lo está, redirige a `checkout.html` pasando la configuración de reserva por URL."
            ])
        ]
    },
    {
        "id": "TASK_FE_016",
        "file": "TASK_FE_016_PropertyDetailReviewsSection.md",
        "title": "Vista Detalle de Finca: Sección de Reseñas y Calificaciones",
        "status": "[ ]",
        "prog": "70% -> 74%",
        "date": "2026-08-05 15:30",
        "p1": "Actualizar src/pages/property-detail/property.html",
        "p1_subs": ["Crear sección div id='reviews-section' al final del contenido", "Diseñar desglose de puntuación por estrellas (limpieza, ubicación, servicio)", "Crear lista de comentarios de huéspedes y formulario para publicar opinión"],
        "p2": "Actualizar src/pages/property-detail/property.js",
        "p2_subs": ["Consultar GET /api/v1/properties/{id}/reviews y renderizar valoraciones", "Enviar POST /api/v1/properties/{id}/reviews al enviar el formulario"],
        "purpose": "Despliega la reputación y opiniones de la finca (74%), permitiendo consultar la puntuación promedio y enviar nuevas reseñas post-estadía.",
        "prereqs": [
            ("Componente de Puntuación por Estrellas (Star Rating)", "Creación de selectores de valoración interactivos con estrellas (1 a 5) manipulables mediante eventos mouseover/click."),
            ("Manejo de Contenido Generado por Usuario (Sanitización XSS)", "Escape de cadenas de texto de comentarios de usuarios antes de inyectarlas en el DOM para prevenir vulnerabilidades XSS.")
        ],
        "steps": [
            ("Actualizar `property.html`", [
                "Agrega la sección `#reviews-section` con barras de porcentaje para puntuaciones de Limpieza, Ubicación, Veracidad y Atención del Anfitrión.",
                "Agrega el contenedor de la lista de comentarios `#reviews-list`.",
                "Agrega el formulario `#add-review-form` visible solo para usuarios elegibles."
            ]),
            ("Actualizar `property.js`", [
                "Consume `apiGet('/properties/' + id + '/reviews')` e inyecta la lista de comentarios mostrando foto del usuario, fecha de estadía y texto sanitizado.",
                "Gestiona el envío del formulario de reseña mediante `apiPost('/properties/' + id + '/reviews', data)` y refresca la lista al completarse con éxito."
            ])
        ]
    },
    {
        "id": "TASK_FE_017",
        "file": "TASK_FE_017_CheckoutOrderSummaryAndForm.md",
        "title": "Vista Checkout: Formulario de Confirmación y Desglose de Pago",
        "status": "[ ]",
        "prog": "74% -> 78%",
        "date": "2026-08-05 16:00",
        "p1": "Crear el archivo src/pages/checkout/checkout.html",
        "p1_subs": ["Diseñar formulario de datos del titular (nombre, documento, teléfono, peticiones especiales)", "Diseñar selector de método de pago (Tarjeta, PSE, Nequi/Daviplata)", "Diseñar panel lateral con el resumen final de la reserva"],
        "p2": "Crear el controlador src/pages/checkout/checkout.js",
        "p2_subs": ["Cargar datos de la reserva desde los parámetros URLSearchParams", "Procesar solicitud POST /api/v1/bookings enviando datos de pago simulados", "Redirigir a checkout-success.html tras recibir la respuesta del servidor"],
        "purpose": "Gestiona la confirmación de la reserva y el proceso de pago (78%), recolectando información del titular y enviando la solicitud a Spring Boot.",
        "prereqs": [
            ("Validación Estricta de Formularios de Transacción", "Verificación de campos requeridos, formato de cédula/pasaporte, número de teléfono y selección de método de pago."),
            ("Integración con Pasarelas de Pago Simuladas", "Simulación del envío de tokens de pago (PSE, Tarjetas) contra endpoints backend transaccionales.")
        ],
        "steps": [
            ("Crear `src/pages/checkout/checkout.html`", [
                "Diseña la columna izquierda con el formulario `#checkout-form`: Datos Personales, Selección de Método de Pago (PSE, Tarjeta de Crédito, Transferencia bancaria) y aceptación de políticas de cancelación.",
                "Diseña la columna derecha con la tarjeta de resumen `#booking-summary-card`: Foto de la finca, título, fechas elegidas, cantidad de huéspedes y costo total final."
            ]),
            ("Crear `src/pages/checkout/checkout.js`", [
                "Verifica que el usuario esté autenticado con `auth.js`; de lo contrario, redirige a `login.html`.",
                "Lee los parámetros `propertyId`, `checkin`, `checkout`, `guests` de la URL.",
                "Al enviar `#checkout-form`, construye el payload JSON conteniendo los datos de la reserva y el método de pago seleccionado.",
                "Ejecuta `apiPost('/bookings', payload)`.",
                "Si la respuesta es exitosa (código 201 Created), redirige a `/src/pages/checkout-success/checkout-success.html?bookingId=` + response.id."
            ])
        ]
    },
    {
        "id": "TASK_FE_018",
        "file": "TASK_FE_018_CheckoutSuccessConfirmationView.md",
        "title": "Vista Confirmación de Reserva: Comprobante y Guía de Llegada",
        "status": "[ ]",
        "prog": "78% -> 82%",
        "date": "2026-08-05 16:30",
        "p1": "Crear el archivo src/pages/checkout-success/checkout-success.html",
        "p1_subs": ["Diseñar tarjeta de confirmación con ícono de éxito y código de reserva", "Mostrar desglose del viaje, datos de contacto del anfitrión e instrucciones de llegada", "Agregar botones 'Ver Mis Reservas' y 'Imprimir / Descargar Comprobante'"],
        "p2": "Crear el controlador src/pages/checkout-success/checkout-success.js",
        "p2_subs": ["Obtener bookingId de la URL y consultar GET /api/v1/bookings/{id} para cargar datos reales"],
        "purpose": "Presenta el comprobante digital de reserva confirmada (82%), entregando al huésped su código de reserva, voucher y contacto directo del finquero.",
        "prereqs": [
            ("Impresión y Generación de Comprobantes Web (window.print)", "Uso de estilos CSS @media print para adaptar la vista de comprobante al formato de impresión en papel o PDF."),
            ("Manejo de Estados de Confirmación Transaccional", "Carga y visualización de detalles de órdenes procesadas para dar tranquilidad al usuario post-compra.")
        ],
        "steps": [
            ("Crear `checkout-success.html`", [
                "Diseña la tarjeta centradora de éxito con ícono de verificación verde en grande.",
                "Muestra el código de reserva en formato destacado (ej: `NF-89421`).",
                "Estructura los detalles del comprobante: Nombre de la Finca, Dirección/Vereda, Fechas de Check-in y Check-out, Nombre del Anfitrión y Teléfono de contacto directo."
            ]),
            ("Crear `checkout-success.js`", [
                "Lee `bookingId` de la query string de la URL.",
                "Consulta `apiGet('/bookings/' + bookingId)`.",
                "Pobla los datos en el comprobante y asigna la acción `window.print()` al botón 'Imprimir Comprobante'."
            ])
        ]
    },
    {
        "id": "TASK_FE_019",
        "file": "TASK_FE_019_AuthLoginView.md",
        "title": "Vista Autenticación: Formulario de Inicio de Sesión / Login",
        "status": "[x]",
        "prog": "82% -> 86%",
        "date": "2026-08-05 17:00",
        "p1": "Crear src/pages/auth/login.html y src/pages/auth/login.js",
        "p1_subs": ["Diseñar el formulario de ingreso con campos para Email y Contraseña", "Capturar submit y enviar POST /api/v1/auth/login mediante api.js", "Almacenar el token JWT con auth.js y redirigir al catálogo o dashboard según rol"],
        "p2": "Crear la hoja de estilos src/pages/auth/login.css",
        "p2_subs": ["Diseñar tarjeta centradora con diseño glassmorphism"],
        "purpose": "Autentica usuarios registrados (86%), procesando credenciales contra Spring Boot e iniciando la sesión cliente mediante almacenamiento de token JWT.",
        "prereqs": [
            ("Manejo de Formularios de Credenciales y Seguridad", "Uso de inputs type='email' y type='password' con opción para conmutar la visibilidad de la contraseña."),
            ("Persistencia de Sesión JWT", "Almacenamiento del token devuelto en localStorage y actualización de la interfaz de usuario en consecuencia.")
        ],
        "steps": [
            ("Crear `src/pages/auth/login.html` y `login.css`", [
                "Diseña la tarjeta de inicio de sesión centradora con el logotipo de NosFuimosdeFinca.",
                "Estructura el formulario `#login-form` con campos para Correo Electrónico y Contraseña, además de la casilla 'Recordarme'."
            ]),
            ("Crear `src/pages/auth/login.js`", [
                "Escucha el evento `submit` del formulario `#login-form`.",
                "Extrae los valores de email y contraseña.",
                "Realiza la petición `apiPost('/auth/login', { email, password })`.",
                "Al recibir la respuesta exitosa conteniendo `{ token }`, invoca `setToken(token)` de `auth.js`.",
                "Muestra un Toast de bienvenida y redirige al usuario a la página previa o a `/src/pages/catalog/catalog.html`."
            ])
        ]
    },
    {
        "id": "TASK_FE_020",
        "file": "TASK_FE_020_AuthRegisterView.md",
        "title": "Vista Autenticación: Formulario de Registro de Usuario y Selección de Rol",
        "status": "[x]",
        "prog": "86% -> 90%",
        "date": "2026-08-05 17:30",
        "p1": "Crear src/pages/auth/register.html y src/pages/auth/register.js",
        "p1_subs": ["Diseñar formulario con campos: Nombre, Teléfono, Correo, Contraseña y Confirmación", "Agregar selector de tipo de cuenta: Huésped vs Anfitrión de Finca", "Enviar POST /api/v1/auth/register y redirigir a login.html"],
        "p2": "Crear la hoja de estilos src/pages/auth/register.css",
        "p2_subs": ["Diseñar tarjetas de selección de rol con resaltado de borde en el acento"],
        "purpose": "Registra nuevos usuarios en la plataforma (90%), permitiendo la elección entre el perfil de Huésped (`GUEST_ROLE`) y el de Propietario (`OWNER_ROLE`).",
        "prereqs": [
            ("Validación de Coincidencia de Contraseñas y Reglas de Complejidad", "Verificación de longitud mínima (8 caracteres) y coincidencia entre 'Contraseña' y 'Confirmar Contraseña'."),
            ("Selección de Roles en Formularios UI", "Uso de botones de radio estilizados tipo tarjeta para seleccionar el perfil de usuario antes del registro.")
        ],
        "steps": [
            ("Crear `src/pages/auth/register.html` y `register.css`", [
                "Diseña el formulario `#register-form` con los campos de datos personales.",
                "Incluye las opciones de selección de perfil: 'Quiero Alquilar Fincas (Huésped)' vs 'Tengo una Finca para Publicar (Anfitrión)'."
            ]),
            ("Crear `src/pages/auth/register.js`", [
                "Captura el submit del formulario `#register-form`.",
                "Comprueba que `password === confirmPassword`.",
                "Construye el payload JSON enviando `fullName`, `phone`, `email`, `password` y el rol seleccionado (`GUEST_ROLE` o `OWNER_ROLE`).",
                "Ejecuta `apiPost('/auth/register', payload)`.",
                "Muestra un Toast de confirmación de registro y redirige al usuario a `login.html`."
            ])
        ]
    },
    {
        "id": "TASK_FE_021",
        "file": "TASK_FE_021_HostLandingAndOnboardingWizard.md",
        "title": "Vista Anfitrión: Landing Informativa y Wizard de Onboarding de Fincas",
        "status": "[ ]",
        "prog": "90% -> 94%",
        "date": "2026-08-05 18:00",
        "p1": "Crear src/pages/host-landing/host-landing.html",
        "p1_subs": ["Diseñar landing promocional informando beneficios de publicar fincas", "Agregar botón CTA 'Publicar mi Finca' que lleve a onboarding.html"],
        "p2": "Crear src/pages/onboarding/onboarding.html y onboarding.js",
        "p2_subs": ["Diseñar formulario wizard por pasos (Paso 1: Ubicación, Paso 2: Amenidades, Paso 3: Fotos/Precios)", "Enviar POST /api/v1/properties al completar el wizard"],
        "purpose": "Promueve y facilita la captación de propietarios de finca (94%), mediante una landing informativa y un formulario guiado por pasos (wizard).",
        "prereqs": [
            ("Patrón de Formulario Multinivel (Wizard UI)", "Navegación entre pasos de formulario (Paso 1 -> Paso 2 -> Paso 3) ocultando y mostrando bloques DOM mientras se valida cada sección."),
            ("Carga y Previsualización de Imágenes en Cliente (FileReader API)", "Permitir la selección de fotos de la finca y mostrar vistas previas instantáneas antes de enviarlas al servidor.")
        ],
        "steps": [
            ("Crear `host-landing.html`", [
                "Diseña la landing explicativa destacando la rentabilidad, seguridad y soporte que ofrece NosFuimosdeFinca a los propietarios de finca."
            ]),
            ("Crear `onboarding.html` y `onboarding.js`", [
                "Implementa el formulario wizard por pasos:",
                "Paso 1: Nombre de la finca, Departamento, Municipio, Vereda e Instrucciones de llegada.",
                "Paso 2: Número de dormitorios, capacidad de huéspedes, número de baños y checkboxes de amenidades.",
                "Paso 3: Tarifa por noche en temporada baja/alta, depósito de garantía y selector de archivos de fotos.",
                "Al finalizar el Paso 3, envía `apiPost('/properties', formData)` y redirige al dashboard de anfitrión."
            ])
        ]
    },
    {
        "id": "TASK_FE_022",
        "file": "TASK_FE_022_GuestMyBookingsView.md",
        "title": "Vista Huésped: Panel Mis Reservas e Historial de Viajes",
        "status": "[ ]",
        "prog": "94% -> 97%",
        "date": "2026-08-05 18:30",
        "p1": "Crear src/pages/my-bookings/my-bookings.html",
        "p1_subs": ["Diseñar pestañas: 'Próximas Reservas', 'Completadas', 'Canceladas'", "Diseñar tarjeta de reserva con foto de finca, fechas, total pagado y estado"],
        "p2": "Crear el controlador src/pages/my-bookings/my-bookings.js",
        "p2_subs": ["Consultar GET /api/v1/bookings/my-bookings con api.js", "Agregar botón 'Cancelar Reserva' con modal de confirmación enviando DELETE /api/v1/bookings/{id}"],
        "purpose": "Entrega al huésped su centro de gestión de viajes (97%), permitiendo consultar reservas pasadas, imprimir vouchers y solicitar cancelaciones.",
        "prereqs": [
            ("Navegación por Pestañas (Tab Navigation)", "Filtrado de datos en el cliente o mediante peticiones parametrizadas al cambiar de pestaña activa."),
            ("Manejo de Modales de Confirmación de Acciones Críticas", "Creación de diálogos emergentes que soliciten confirmación explícita antes de proceder con una cancelación de reserva.")
        ],
        "steps": [
            ("Crear `my-bookings.html`", [
                "Diseña las pestañas horizontales `#tab-upcoming`, `#tab-completed`, `#tab-cancelled`.",
                "Crea el contenedor de la grilla de reservas `#my-bookings-container`."
            ]),
            ("Crear `my-bookings.js`", [
                "Verifica autenticación del usuario.",
                "Consume `apiGet('/bookings/my-bookings')` e inyecta las tarjetas de reserva mostrando estado, foto, municipio y fechas.",
                "Agrega la funcionalidad de cancelación mostrando un modal de confirmación que ejecute `apiDelete('/bookings/' + bookingId)`."
            ])
        ]
    },
    {
        "id": "TASK_FE_023",
        "file": "TASK_FE_023_OwnerDashboardView.md",
        "title": "Vista Anfitrión: Dashboard de Control, Calendario de Disponibilidad e Ingresos",
        "status": "[ ]",
        "prog": "97% -> 99%",
        "date": "2026-08-05 19:00",
        "p1": "Crear el archivo src/pages/dashboard/dashboard.html",
        "p1_subs": ["Diseñar sidebar de navegación: 'Resumen', 'Mis Fincas', 'Solicitudes de Reserva', 'Calendario'", "Diseñar tarjetas métricas: Ingresos del Mes, Ocupación %, Reservas Pendientes"],
        "p2": "Crear el controlador src/pages/dashboard/dashboard.js",
        "p2_subs": ["Consultar GET /api/v1/owner/metrics e inyectar datos reales", "Implementar tabla de solicitudes con botones de 'Aprobar' y 'Rechazar'"],
        "purpose": "Proporciona al anfitrión su panel de administración comercial (99%) para controlar el estado de sus fincas, aprobar reservas y ver métricas financieras.",
        "prereqs": [
            ("Visualización de Paneles de Control (Dashboards UI)", "Disposición de métricas financieras e indicadores clave de rendimiento (KPIs) en paneles visuales de tarjetas."),
            ("Tablas de Datos Interactivos con Acciones", "Creación de filas de tabla con botones de acción dinámica ('Aprobar', 'Rechazar', 'Editar Tarifa') que modifican el estado de las entidades backend.")
        ],
        "steps": [
            ("Crear `dashboard.html`", [
                "Diseña la estructura de panel administrativo con sidebar lateral e interfaz principal.",
                "Crea los bloques de tarjetas de indicadores clave (KPIs): Total Ganado, Reservas Confirmadas, Tasa de Ocupación.",
                "Crea la tabla `#pending-requests-table` para la gestión de solicitudes."
            ]),
            ("Crear `dashboard.js`", [
                "Valida que el usuario tenga el rol `OWNER_ROLE` o `ADMIN_ROLE`.",
                "Consulta `apiGet('/owner/metrics')` para inyectar los datos en los KPIs.",
                "Consulta `apiGet('/owner/bookings/pending')` e inyecta la lista de solicitudes pendientes enviando peticiones `apiPut` al presionar 'Aprobar' o 'Rechazar'."
            ])
        ]
    },
    {
        "id": "TASK_FE_024",
        "file": "TASK_FE_024_ErrorPagesAndBuildValidation.md",
        "title": "Vista Error y Fallback: Manejo de 404, 500 y Optimización Final",
        "status": "[ ]",
        "prog": "99% -> 100%",
        "date": "2026-08-05 19:30",
        "p1": "Crear src/pages/error/error.html y src/pages/error/error.js",
        "p1_subs": ["Diseñar vista amigable para errores 404 (Página No Encontrada) y 500 (Error del Servidor)", "Parsear el código de error desde la query string y mostrar el mensaje correspondiente"],
        "p2": "Verificación final del build de producción",
        "p2_subs": ["Ejecutar npm run build en frontend/ asegurando 0 errores de compilación"],
        "purpose": "Finaliza el desarrollo del cliente web al 100%. Garantiza una experiencia elegante ante enlaces rotos o caídas de servidor y confirma el empaquetado de producción.",
        "prereqs": [
            ("Manejo Formativo de Fallos de Aplicación (Graceful Degradation)", "Presentar alternativas amigables al usuario ante caídas imprevistas en lugar de pantallas en blanco o mensajes crudos."),
            ("Validación de Builds de Empaquetado Estático de Producción", "Verificación de que todos los assets (JS, CSS, HTML) se empaqueten limpiamente en el directorio dist/.")
        ],
        "steps": [
            ("Crear `error.html` y `error.js`", [
                "Diseña la interfaz centradora de error con una ilustración amigable y el botón de acción 'Volver a la Página Principal'.",
                "Escribe `error.js` leyendo `code` de la URL (`error.html?code=404`) para adaptar el texto entre 'Página no encontrada' o 'Servidor en mantenimiento'."
            ]),
            ("Validación Final del Proyecto 100%", [
                "Ejecuta `npm run build` en la carpeta `frontend/`.",
                "Confirma que Vite genere el directorio `dist/` conteniendo todos los archivos HTML y bundles optimizados sin errores."
            ])
        ]
    }
]

def generate_markdown(t):
    md = []
    # Checklist at top
    md.append(f"- {t['status']} {t['id']} — {t['title']} 📅 {t['date']}")
    md.append(f"\t- {t['status']} Paso 1: {t['p1']}")
    for sub in t['p1_subs']:
        md.append(f"\t\t- {t['status']} {sub}")
    md.append(f"\t- {t['status']} Paso 2: {t['p2']}")
    for sub in t['p2_subs']:
        md.append(f"\t\t- {t['status']} {sub}")
    if 'p3' in t:
        md.append(f"\t- {t['status']} Paso 3: {t['p3']}")
        for sub in t['p3_subs']:
            md.append(f"\t\t- {t['status']} {sub}")
    
    md.append("")
    md.append(f"# {t['id']} — {t['title']}")
    md.append("")
    md.append(f"**Módulo:** `frontend/`  ")
    md.append(f"**Porcentaje de Avance:** {t['prog']}  ")
    md.append(f"**Estado:** {'COMPLETADO' if t['status'] == '[x]' else 'PENDIENTE'}  ")
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
    md.append("## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave")
    md.append("")
    md.append("Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:")
    md.append("")
    for name, desc in t['prereqs']:
        md.append(f"* **{name}:** {desc}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Instrucciones de Implementación Paso a Paso")
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
    md.append("## 4. Criterios de Aceptación y Verificación")
    md.append("")
    md.append("| # | Criterio de Aceptación | Método de Verificación |")
    md.append("|---|---|---|")
    md.append("| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |")
    md.append("| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |")
    md.append("")
    return "\n".join(md)

# Clean out old task files in guide/03_Frontend
for f in os.listdir(target_dir):
    if f.startswith("TASK_FE_"):
        os.remove(os.path.join(target_dir, f))

# Write 24 tasks
for t in tasks:
    filepath = os.path.join(target_dir, t['file'])
    content = generate_markdown(t)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(tasks)} expanded task files for NosFuimosdeFinca.")
