# 🚀 GUÍA DE DESPLIEGUE WEB GRATUITO (100% LISTO PARA COMPARTIR)
## Portal Web de Preparación para el Examen Final · INF-110 (UAGRM - FICCT)
**Docente:** M.Sc. Ing. Angélica Garzón Cuéllar  
**Archivo Principal:** `index.html` (722 KB, autocontenido, offline y responsive)

---

## 🌟 OPCIÓN 1: Netlify Drop (La más rápida y recomendada - 30 Segundos)
> **Ventajas:** No requiere instalar nada, no necesitas Git ni consola. Te da un link HTTPS gratis e instantáneo para pasar por WhatsApp a tus compañeros.

### Pasos:
1. Abre tu navegador web (Chrome, Edge, Firefox, Brave) y entra a:
   👉 **[https://app.netlify.com/drop](https://app.netlify.com/drop)**
2. Abre el **Explorador de Archivos de Windows** y navega a:
   `D:\Introz2\`
3. **Arrastra la carpeta `practico07`** y suéltala dentro del círculo punteado en la página de Netlify.
4. En 5 segundos, Netlify cargará la web y te dará un enlace público automático como:
   `https://amazing-garzon-123456.netlify.app`
5. *(Opcional)* Haz clic en **"Site Configuration"** ➔ **"Change site name"** y cámbiale el nombre a algo profesional como:
   `https://inf110-uagrm-examenfinal.netlify.app`
6. ¡Listo! Ya puedes enviar ese enlace a tus compañeros y abrirlo desde cualquier celular, tablet o computadora.

---

## 🐙 OPCIÓN 2: GitHub Pages (Ideal para tu Currículum / Portafolio)
> **Ventajas:** Queda alojado para siempre bajo tu usuario de GitHub (`https://tu-usuario.github.io/...`).

### Pasos:
1. Inicia sesión en [GitHub](https://github.com/) y crea un repositorio nuevo llamado por ejemplo: `inf110-examen-final` (público).
2. Abre la consola de comandos (PowerShell) en la carpeta del práctico:
   ```powershell
   cd D:\Introz2\practico07
   git init
   git add index.html practico_poo.html *.docx *.pas
   git commit -m "Portal de Examen Final INF110 UAGRM con Sidebar y Cockpit Trilogía"
   git branch -M main
   git remote add origin https://github.com/TU-USUARIO/inf110-examen-final.git
   git push -u origin main
   ```
3. En la página de tu repositorio en GitHub:
   - Ve a **Settings** (Configuración) ➔ **Pages** (menú izquierdo).
   - En **Branch**, selecciona `main` y la carpeta `/ (root)`.
   - Haz clic en **Save** (Guardar).
4. En 1 minuto tendrás tu enlace activo:
   👉 `https://TU-USUARIO.github.io/inf110-examen-final/`

---

## ⚡ OPCIÓN 3: Vercel (Ultra rápido con Node.js o Drag & Drop)
> **Ventajas:** Servidores CDN globales ultra veloces.

### Opción A (Vía Web sin comandos):
1. Entra a **[https://vercel.com](https://vercel.com)** e inicia sesión con tu cuenta de GitHub o Google.
2. Arrastra la carpeta `D:\Introz2\practico07` a la sección de proyectos.
3. Haz clic en **Deploy**.

### Opción B (Vía Terminal con NPX):
```powershell
cd D:\Introz2\practico07
npx vercel deploy --prod
```

---

## 🌐 OPCIÓN 4: Surge.sh (1 Línea en la Consola)
> **Ventajas:** Se sube directamente desde tu terminal de PowerShell en un par de segundos.

```powershell
cd D:\Introz2\practico07
npx surge . inf110-uagrm-examen.surge.sh
```

---

## 🧭 ¿Qué incluye la nueva versión desplegada?

1. **Sidebar Izquierdo Idéntico al Campus UAGRM (Moodle):**
   - Icono institucional 🏛️ y cabecera de la materia (INF-110 · Ing. Garzón).
   - Botón hamburguesa `☰ Menú` en el navbar superior.
   - Atajo de teclado global: Presiona **`Ctrl + B`** en tu teclado para ocultar/mostrar el menú lateral en cualquier momento.
   - Cajón off-canvas con fondo oscuro y efecto blur en dispositivos móviles.
   - Buscador en tiempo real de secciones (`🔍 Filtrar sección...`).
   - Mosaicos organizados:
     - 👑 **Mosaico 1:** Trilogía Examen Final (Series 30p, Números 35p, Cadenas 35p).
     - 🏆 **Mosaico 2:** Banco Oficial de Exámenes (7 Finales 28 problemas + 7 Parciales).
     - 🧰 **Mosaico 3:** Hojas de Atajos (Cheat Sheets Pascal Clean Code).
     - 🔬 **Mosaico 4:** Laboratorios (Trazas Formales, Simulador 90 min, ASCII, Memoria).
     - 📚 **Mosaico 5:** Material Oficial (Apuntes, PDFs, 40 Preguntas POO).
     - 📥 **Mosaico 6:** Biblioteca de Descargas (.docx y .pas).

2. **Cockpit Trilogía 3-en-1:**
   - Permite evaluar en paralelo:
     - Una Serie Numérica (ej: Factorial / Doble).
     - Un Número Natural (ej: Capicúa, Inversión, Binario).
     - Una Cadena de Caracteres (ej: Inversión por mitades, ordenamiento consonantes).
   - Genera el veredicto en tiempo real con las 4 fases obligatorias de la cátedra:
     1. Análisis Metodológico (Entradas, Salidas, Ley de Formación).
     2. Algoritmo / Pseudocódigo formal.
     3. Código Pascal / Delphi Clean Code.
     4. Prueba de Escritorio / Traza tabular.

