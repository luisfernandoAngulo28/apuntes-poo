# 🏛️ Portal Examen Final INF-110 · UAGRM (Versión React + Vite)

Plataforma interactiva SPA (Single Page Application) construida en **React 19 + TypeScript + Vite** para la preparación integral del Examen Final de **Introducción a la Informática (INF-110)** de la FICCT - UAGRM, cátedra de la **M.Sc. Ing. Angélica Garzón Cuéllar**.

---

## 🚀 Cómo Ejecutar en Modo Desarrollo

1. Abre tu terminal (PowerShell o CMD) en esta carpeta:
   ```bash
   cd d:\Introz2\practico07\portal-react
   ```
2. Ejecuta el servidor de desarrollo de Vite:
   ```bash
   npm run dev
   ```
3. Se abrirá automáticamente en tu navegador en:
   👉 **`http://localhost:5173`**

---

## 📦 Cómo Compilar para Producción (Build)

Para generar la versión optimizada lista para subir a Netlify, Vercel o GitHub Pages:
```bash
npm run build
```
Los archivos optimizados y minificados quedarán en la carpeta `dist/`.

---

## 👑 Arquitectura de Componentes

```
src/
 ├── components/
 │    ├── Navbar.tsx             # Barra superior con logo UAGRM y estado
 │    ├── Sidebar.tsx            # Menú lateral estilo Moodle con búsqueda y atajo Ctrl+B
 │    ├── CockpitTrilogia.tsx    # Simulador interactivo 3-en-1 (Series + Números + Cadenas)
 │    ├── PascalCodeBlock.tsx    # Visor de código Delphi Clean Code con botón copiar
 │    └── TrazaViewer.tsx        # Tabla dinámica para la Fase 4 (Prueba de Escritorio)
 ├── data/
 │    └── trilogiaData.ts        # Base de datos tipada con los ejercicios y fases
 ├── App.tsx                     # Orquestador del Layout y atajo Ctrl+B
 ├── main.tsx                    # Punto de entrada de React 19
 └── index.css                   # Sistema de diseño dark mode y tabs accesibles
```

---

## 🌟 Características Principales

- **Simulador Interactivo:** Puedes probar en tiempo real el cálculo de sumatorias, eliminación de dígitos repetidos e inversión de cadenas por mitades.
- **Metodología de 4 Fases:** Cada ejercicio cuenta con botones para ver:
  1. *Fase 1:* Análisis Metodológico
  2. *Fase 2:* Algoritmo / Pseudocódigo Formal
  3. *Fase 3:* Código Pascal / Delphi Clean Code con tipos fuertes
  4. *Fase 4:* Prueba de Escritorio (Traza tabular formal)
- **Atajo de Teclado:** Presiona `Ctrl + B` para alternar la barra lateral izquierda.
- **Accesibilidad según Modern Web Guidance:** Pestañas construidas con `role="tablist"`, `aria-selected`, e indicadores CSS compatibles con modos de alto contraste.

