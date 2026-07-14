# Wireframe Specifications: `/host` (Landing de Aliados B2B)

**Ruta UI:** `/host` (Venta Comercial para Captacion de Finqueros)
**Requisitos Funcionales Inyectados:** N/A (Pagina estatica informativa para conversion).

---

# RESULTADOS
![Host Landing - Wireframe Desktop.png](Host%20Landing%20-%20Wireframe%20Desktop.png)
![Host Landing - Wireframe Mobile.png](Host%20Landing%20-%20Wireframe%20Mobile.png)


## 1. Analisis Cognitivo y Patron UX Recomendado

- **Diagnostico:** Esta pantalla tiene una sola mision: Convencer a los duenos de fincas de que se registren en nuestra plataforma. El usuario (Finquero) es esceptico. Quiere saber cuanto le cobramos, como le pagamos y si es seguro.
- **Patron Principal:** `Long-Scroll Storytelling Landing`.
  - El diseno debe ser una narrativa descendente (Scroll largo). Comienza con un gran titulo (H1) que ataque el dolor principal ("Gana mas dinero sin preocuparte por el mercadeo"), seguido de bloques de contenido que expliquen el producto: *Como funciona, Precios (0% de inscripcion), Testimonios, y FAQs*.
  - Llamados a la Accion (CTA) flotantes: El boton de "Registrate ahora" debe estar repetido a lo largo de la pagina para atrapar al usuario en su momento de mayor calentamiento.

---

## 2. Inventario de UI (Atomic Design)

Disenador, asegurate de tener estos *Master Components* en Figma para ensamblar la pagina `/host`:

### A. Atomos
- `ValuePropIcon`: Icono vectorial para ilustrar beneficios (Ej. Un escudo, dinero, un calendario).
- `PrimaryButton`: Boton grande y brillante de conversion (Ej. "Comienza a publicar").
- `FaqAccordionArrow`: Icono de flecha `v` para expandir preguntas frecuentes.

### B. Moleculas
- `FeatureCard`: Une (`ValuePropIcon` + Titulo "Pagos Seguros" + Texto "Recibe tu dinero directo en tu cuenta gracias a Wompi").
- `TestimonialBlock`: Une (Foto del dueno + Texto "Desde que estoy en Nos Fuimos de Finca mis reservas subieron un 40%" + Estrellas).
- `FaqRow`: Une (Pregunta en negrita + `FaqAccordionArrow`).

### C. Organismos
- `HeroHostSection`: Une (Fotografia de un finquero real + Titulo H1 + Subtitulo + `PrimaryButton`).
- `ValuePropositionGrid`: Grilla de 3 o 4 `FeatureCard`s.
- `FaqAccordionGroup`: Agrupacion vertical de 5 `FaqRow`s para responder dudas tipicas ( Cuanto cuesta?, Quien paga el seguro?).

---

## 3. Heuristicas Espaciales y Accesibilidad (Layout Rules)

1. **Jerarquia Visual y Contraste (Call to Action):**
   - El `PrimaryButton` de esta pagina debe tener un color que resalte dramaticamente contra el resto del diseno (Ej. Naranja vibrante sobre fondo blanco/azul). No debe haber botones secundarios compitiendo con el.
2. **Ley de Proximidad en FAQs:**
   - En el `FaqAccordionGroup`, las respuestas deben tener suficiente `padding` para que el texto respire y el usuario en Mobile no se equivoque al tocar la pregunta correcta.

---

## 4. The Designer Checklist (Tareas para Figma)

Disenador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/host`:

### Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el *Long Scroll* intercalando fondos blancos y grises claros para separar secciones (Hero -> Features -> Testimonials -> FAQs).
- `[ ]` **Mobile (390px):** Layout colapsado a 1 columna. Asegurate de que el CTA principal aparezca en el primer "Pantallazo" (Above the Fold) sin hacer scroll.

### Mutaciones de Estado
- `[ ]` **FAQ Abierto:** Dibuja el estado de un `FaqRow` cuando el usuario hace clic y la respuesta se expande hacia abajo.
