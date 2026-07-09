# Wireframe Specifications: `/host` (Landing de Aliados B2B)

**Ruta UI:** `/host` (Venta Comercial para Captación de Finqueros)
**Requisitos Funcionales Inyectados:** N/A (Página estática informativa para conversión).

---

# RESULTADOS
![Host Landing - Wireframe Desktop.png](<Host Landing - Wireframe Desktop.png>)
![Host Landing - Wireframe Mobile.png](<Host Landing - Wireframe Mobile.png>)


## 1. Análisis Cognitivo y Patrón UX Recomendado

- **Diagnóstico:** Esta pantalla tiene una sola misión: Convencer a los dueños de fincas de que se registren en nuestra plataforma. El usuario (Finquero) es escéptico. Quiere saber cuánto le cobramos, cómo le pagamos y si es seguro.
- **Patrón Principal:** `Long-Scroll Storytelling Landing`.
  - El diseño debe ser una narrativa descendente (Scroll largo). Comienza con un gran título (H1) que ataque el dolor principal ("Gana más dinero sin preocuparte por el mercadeo"), seguido de bloques de contenido que expliquen el producto: *Cómo funciona, Precios (0% de inscripción), Testimonios, y FAQs*.
  - Llamados a la Acción (CTA) flotantes: El botón de "Regístrate ahora" debe estar repetido a lo largo de la página para atrapar al usuario en su momento de mayor calentamiento.

---

## 2. Inventario de UI (Atomic Design)

Diseñador, asegúrate de tener estos *Master Components* en Figma para ensamblar la página `/host`:

### A. Átomos
- `ValuePropIcon`: Icono vectorial para ilustrar beneficios (Ej. Un escudo, dinero, un calendario).
- `PrimaryButton`: Botón grande y brillante de conversión (Ej. "Comienza a publicar").
- `FaqAccordionArrow`: Icono de flecha `v` para expandir preguntas frecuentes.

### B. Moléculas
- `FeatureCard`: Une (`ValuePropIcon` + Título "Pagos Seguros" + Texto "Recibe tu dinero directo en tu cuenta gracias a Wompi").
- `TestimonialBlock`: Une (Foto del dueño + Texto "Desde que estoy en Nos Fuimos de Finca mis reservas subieron un 40%" + Estrellas).
- `FaqRow`: Une (Pregunta en negrita + `FaqAccordionArrow`).

### C. Organismos
- `HeroHostSection`: Une (Fotografía de un finquero real + Título H1 + Subtítulo + `PrimaryButton`).
- `ValuePropositionGrid`: Grilla de 3 o 4 `FeatureCard`s.
- `FaqAccordionGroup`: Agrupación vertical de 5 `FaqRow`s para responder dudas típicas (¿Cuánto cuesta?, ¿Quién paga el seguro?).

---

## 3. Heurísticas Espaciales y Accesibilidad (Layout Rules)

1. **Jerarquía Visual y Contraste (Call to Action):**
   - El `PrimaryButton` de esta página debe tener un color que resalte dramáticamente contra el resto del diseño (Ej. Naranja vibrante sobre fondo blanco/azul). No debe haber botones secundarios compitiendo con él.
2. **Ley de Proximidad en FAQs:**
   - En el `FaqAccordionGroup`, las respuestas deben tener suficiente `padding` para que el texto respire y el usuario en Mobile no se equivoque al tocar la pregunta correcta.

---

## 4. The Designer Checklist (Tareas para Figma)

Diseñador, marca con `[x]` cuando hayas dibujado estas mesas de trabajo (`Artboards`) para la ruta `/host`:

### ✅ Pantallas Base (Happy Path)
- `[ ]` **Desktop (1440px):** Dibuja el *Long Scroll* intercalando fondos blancos y grises claros para separar secciones (Hero -> Features -> Testimonials -> FAQs).
- `[ ]` **Mobile (390px):** Layout colapsado a 1 columna. Asegúrate de que el CTA principal aparezca en el primer "Pantallazo" (Above the Fold) sin hacer scroll.

### ✅ Mutaciones de Estado
- `[ ]` **FAQ Abierto:** Dibuja el estado de un `FaqRow` cuando el usuario hace clic y la respuesta se expande hacia abajo.
