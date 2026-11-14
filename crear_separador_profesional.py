# -*- coding: utf-8 -*-
"""
Generador del Separador Profesional de Temas inspirado en la plataforma oficial Moodle UAGRM:
1. Banner Académico Oficial [2-2026] Introducción a la Programación - Z2 (M.Sc. Ing. Angélica Garzón Cuéllar).
2. Barra Segmentada de 5 Categorías Principales + Buscador en Tiempo Real.
3. Menú Drawer Reorganizado en Acordeones Oficiales de la Materia.
"""

import sys, shutil
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HTML_FILE = 'teoria_programacion_modular.html'
BAK_FILE = 'teoria_programacion_modular.html.bak'

shutil.copyfile(HTML_FILE, BAK_FILE)

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. BANNER ACADÉMICO MOODLE UAGRM ───
BANNER_HTML = '''  <!-- ========================================================================= -->
  <!-- BANNER ACADÉMICO OFICIAL UAGRM - FICCT (INF110-Z2)                       -->
  <!-- ========================================================================= -->
  <div class="moodle-banner-container" style="margin-bottom: 1.5rem;">
    <!-- Encabezado superior estilo Moodle -->
    <div style="background: #0f172a; border: 1px solid #1e293b; border-bottom: none; border-radius: 12px 12px 0 0; padding: 0.8rem 1.4rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.8rem;">
      <div style="display: flex; align-items: center; gap: 0.8rem;">
        <span style="background: #2563eb; color: #fff; font-weight: 800; font-size: 0.78rem; padding: 0.25rem 0.6rem; border-radius: 6px; letter-spacing: 0.05em;">UAGRM • FICCT</span>
        <span style="color: #cbd5e1; font-weight: 700; font-size: 0.95rem; letter-spacing: -0.01em;">[2-2026] INTRODUCCIÓN A LA PROGRAMACIÓN - Z2</span>
      </div>
      <div style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.82rem; color: #94a3b8;">
        <span>Docente: <strong style="color: #fff;">M.Sc. Ing. Angélica Garzón Cuéllar</strong></span>
      </div>
    </div>

    <!-- Franja distintiva institucional (Rojo Guinda y Azul UAGRM) -->
    <div style="background: linear-gradient(90deg, #991b1b 0%, #b91c1c 40%, #1e3a8a 100%); padding: 1.1rem 1.5rem; color: #fff; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
      <div style="display: flex; align-items: center; gap: 1rem;">
        <div style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: 8px; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
          🏛️
        </div>
        <div>
          <div style="font-size: 1.15rem; font-weight: 900; letter-spacing: 0.02em; text-transform: uppercase;">
            Introducción a la Programación INF-110 Z2
          </div>
          <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9); font-weight: 500;">
            Portal Oficial de Estudio • Semestre 2-2026 • Santa Cruz de la Sierra, Bolivia
          </div>
        </div>
      </div>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
        <span style="background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.25); color: #fff; font-size: 0.78rem; font-weight: 700; padding: 0.35rem 0.75rem; border-radius: 999px;">
          ⚡ 21 Módulos Integrados
        </span>
      </div>
    </div>

    <!-- 3 Tarjetas de Acceso Rápido estilo Plataforma -->
    <div style="background: #0b1120; border: 1px solid #1e293b; border-top: none; border-radius: 0 0 12px 12px; padding: 1rem 1.2rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.8rem;">
      
      <div onclick="filtrarCategoria('practicos')" style="background: rgba(30,41,59,0.7); border: 1px solid rgba(56,189,248,0.3); border-radius: 8px; padding: 0.8rem 1rem; display: flex; align-items: center; gap: 0.8rem; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.borderColor='#38bdf8';this.style.background='rgba(56,189,248,0.1)'" onmouseout="this.style.borderColor='rgba(56,189,248,0.3)';this.style.background='rgba(30,41,59,0.7)'">
        <span style="font-size: 1.6rem;">📂</span>
        <div>
          <div style="font-size: 0.88rem; font-weight: 800; color: #fff;">Prácticos Oficiales</div>
          <div style="font-size: 0.75rem; color: #38bdf8;">Prácticos #6, #7 y #8 (65+ Ej.) ➜</div>
        </div>
      </div>

      <div onclick="filtrarCategoria('examenes')" style="background: rgba(30,41,59,0.7); border: 1px solid rgba(245,158,11,0.3); border-radius: 8px; padding: 0.8rem 1rem; display: flex; align-items: center; gap: 0.8rem; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.borderColor='#f59e0b';this.style.background='rgba(245,158,11,0.1)'" onmouseout="this.style.borderColor='rgba(245,158,11,0.3)';this.style.background='rgba(30,41,59,0.7)'">
        <span style="font-size: 1.6rem;">🏆</span>
        <div>
          <div style="font-size: 0.88rem; font-weight: 800; color: #fff;">Exámenes & Modelos</div>
          <div style="font-size: 0.75rem; color: #fbbf24;">Examen Final 40p + 11 Modelos ➜</div>
        </div>
      </div>

      <div onclick="filtrarCategoria('herramientas')" style="background: rgba(30,41,59,0.7); border: 1px solid rgba(16,185,129,0.3); border-radius: 8px; padding: 0.8rem 1rem; display: flex; align-items: center; gap: 0.8rem; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.borderColor='#10b981';this.style.background='rgba(16,185,129,0.1)'" onmouseout="this.style.borderColor='rgba(16,185,129,0.3)';this.style.background='rgba(30,41,59,0.7)'">
        <span style="font-size: 1.6rem;">🔬</span>
        <div>
          <div style="font-size: 0.88rem; font-weight: 800; color: #fff;">Herramientas & Traza</div>
          <div style="font-size: 0.75rem; color: #10b981;">Generador de Traza & Series ➜</div>
        </div>
      </div>

    </div>
  </div>
'''

# ─── 2. SEPARADOR Y FILTRADOR PROFESIONAL DE CATEGORÍAS ───
SEPARADOR_BAR_HTML = '''  <!-- ========================================================================= -->
  <!-- SEPARADOR PROFESIONAL DE TEMAS (FILTRO POR CATEGORÍAS & BUSCADOR)        -->
  <!-- ========================================================================= -->
  <div class="topic-separator-wrapper" style="background: rgba(15,23,42,0.9); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem 1.25rem; margin-bottom: 1.25rem; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
    
    <!-- Barra superior: Título del separador y buscador rápido -->
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.8rem; margin-bottom: 0.9rem;">
      <div style="display: flex; align-items: center; gap: 0.6rem;">
        <span style="font-size: 1.3rem;">🗂️</span>
        <span style="font-weight: 800; color: #fff; font-size: 1rem; letter-spacing: -0.01em;">Separador de Temas de la Materia</span>
        <span id="filtroCountBadge" style="background: rgba(56,189,248,0.15); color: #38bdf8; font-size: 0.75rem; font-weight: 700; padding: 0.15rem 0.55rem; border-radius: 999px;">
          21 Temas
        </span>
      </div>

      <!-- Buscador en tiempo real de temas -->
      <div style="position: relative; min-width: 260px; flex: 1; max-width: 380px;">
        <input type="text" id="topicSearchInput" placeholder="🔍 Buscar tema (ej. cadena, primo, examen, traza...)" oninput="buscarTemasEnVivo()" style="width: 100%; padding: 0.45rem 0.8rem 0.45rem 2.2rem; background: #070a13; border: 1px solid #334155; border-radius: 999px; color: #fff; font-size: 0.82rem; transition: border-color 0.2s;" onfocus="this.style.borderColor='#38bdf8'" onblur="this.style.borderColor='#334155'">
        <span style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); font-size: 0.85rem; color: #64748b; pointer-events: none;">🔍</span>
      </div>
    </div>

    <!-- Pestañas de categorías principales (Estilo Chips) -->
    <div class="category-chips-bar" style="display: flex; gap: 0.5rem; overflow-x: auto; padding-bottom: 0.25rem; scrollbar-width: none;">
      <button class="cat-chip-btn active" data-cat="all" onclick="filtrarCategoria('all')">
        🌟 Todos (21)
      </button>
      <button class="cat-chip-btn" data-cat="practicos" onclick="filtrarCategoria('practicos')">
        📂 Prácticos Oficiales (3)
      </button>
      <button class="cat-chip-btn" data-cat="tareas" onclick="filtrarCategoria('tareas')">
        📝 Tareas &amp; Pizarra (2)
      </button>
      <button class="cat-chip-btn" data-cat="examenes" onclick="filtrarCategoria('examenes')">
        🏆 Exámenes &amp; Simulacros (5)
      </button>
      <button class="cat-chip-btn" data-cat="herramientas" onclick="filtrarCategoria('herramientas')">
        🔬 Herramientas &amp; Series (4)
      </button>
      <button class="cat-chip-btn" data-cat="fundamentos" onclick="filtrarCategoria('fundamentos')">
        📖 Fundamentos &amp; Teoría (7)
      </button>
    </div>
  </div>
'''

# ─── 3. NAV TABS CATEGORIZADOS (data-cat) ───
NEW_NAV_TABS = '''  <nav class="nav-tabs">
    <!-- CATEGORÍA: PRÁCTICOS OFICIALES -->
    <button class="nav-btn active" data-cat="practicos" onclick="switchTab('solucion-practico7')">💻 1. Práctico #7: Programación Modular (25 Ej.)</button>
    <button class="nav-btn" data-cat="practicos" onclick="switchTab('solucion-practico8')">🔤 2. Práctico #8: Cadenas (40 Ej. &amp; Delphi Form)</button>
    <button class="nav-btn" data-cat="practicos" onclick="switchTab('practico6-naturales')">🔢 3. Práctico #6: Números Naturales</button>

    <!-- CATEGORÍA: EXÁMENES Y SIMULACROS -->
    <button class="nav-btn" data-cat="examenes" onclick="switchTab('examen-final-oficial')">🏆 Examen Final Oficial 2-2020 (40/40 Ptos)</button>
    <button class="nav-btn" data-cat="examenes" onclick="switchTab('cadenas-exam-kit')">🎯 Kit Examen Cadenas (5 Módulos)</button>
    <button class="nav-btn" data-cat="examenes" onclick="switchTab('modelos-examen')">🎯 Modelos de Examen (11 Ejercicios)</button>
    <button class="nav-btn" data-cat="examenes" onclick="switchTab('simulacro-examen')">⏱️ Simulacro con Cronómetro</button>
    <button class="nav-btn" data-cat="examenes" onclick="switchTab('trampas-delphi')">🧠 Trampas Clásicas &amp; Errores de Examen</button>

    <!-- CATEGORÍA: TAREAS & PIZARRA -->
    <button class="nav-btn" data-cat="tareas" onclick="switchTab('ejercicios-pizarra')">📋 Tarea de Clase (Pizarra &amp; Delphi Form)</button>
    <button class="nav-btn" data-cat="tareas" onclick="switchTab('series-y-herramientas')">📈 Metodología de los 5 Pasos &amp; Series</button>

    <!-- CATEGORÍA: HERRAMIENTAS & SERIES -->
    <button class="nav-btn" data-cat="herramientas" onclick="switchTab('traza-escritorio')">🧪 Prueba de Escritorio (Trace en Vivo)</button>
    <button class="nav-btn" data-cat="herramientas" onclick="switchTab('hoja-atajos')">⚡ Hoja de Atajos (Cheat Sheet F7/F8)</button>
    <button class="nav-btn" data-cat="herramientas" onclick="switchTab('diagramas-flujo')">📊 Diagramas de Flujo ANSI</button>
    <button class="nav-btn" data-cat="herramientas" onclick="switchTab('conversion-bases')">🔢 Conversión de Bases Numéricas</button>

    <!-- CATEGORÍA: FUNDAMENTOS & TEORÍA -->
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('fundamentos-historia')">📖 Fundamentos Teóricos &amp; PDFs</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('diferencia-func-proc')">⚖️ Función vs Procedimiento</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('delphi-vcl-form')">🖥️ Delphi Form (Clase Docente)</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('buenas-practicas')">💡 Buenas Prácticas &amp; Clean Code</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('puente-poo')">🚀 Puente hacia POO (Objetos)</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('preguntas')">❓ Cuestionario de 20 Preguntas</button>
    <button class="nav-btn" data-cat="fundamentos" onclick="switchTab('evaluacion-quiz')">📝 Mini Test de Autoevaluación</button>
  </nav>'''

# ─── 4. DRAWER LATERAL REORGANIZADO EN ACORDEONES OFICIALES ───
NEW_DRAWER_CONTENT = '''    <div class="drawer-title" style="padding: 1.1rem 1.4rem; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
      <div>
        <div style="font-weight: 800; color: #fff; font-size: 1.05rem;">📚 Temario Oficial INF110-Z2</div>
        <div style="font-size: 0.78rem; color: #94a3b8;">M.Sc. Ing. Angélica Garzón Cuéllar</div>
      </div>
      <button class="mobile-btn-action" onclick="toggleMobileDrawer()" style="padding: 0.35rem 0.75rem; font-size: 0.8rem; background: rgba(244,63,94,0.15); color: #fb7185; border: 1px solid rgba(244,63,94,0.3); border-radius: 6px;">✕ Cerrar</button>
    </div>

    <!-- Buscador móvil dentro del Drawer -->
    <div style="padding: 0.75rem 1.25rem 0.25rem 1.25rem;">
      <input type="text" id="drawerSearchInput" placeholder="🔍 Filtrar sección..." oninput="buscarDrawerEnVivo()" style="width: 100%; padding: 0.45rem 0.8rem; background: #070a13; border: 1px solid #334155; border-radius: 8px; color: #fff; font-size: 0.82rem;">
    </div>

    <div class="drawer-scrollable" style="padding: 0.8rem 1.25rem 2rem 1.25rem; overflow-y: auto; max-height: calc(85vh - 120px);">

      <!-- GRUPO 1: PRÁCTICOS OFICIALES S2-2026 -->
      <div class="drawer-group" style="margin-bottom: 1.1rem;">
        <div style="font-size: 0.75rem; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: space-between;">
          <span>📂 PRACTICO S2-2026</span>
          <span style="background: rgba(56,189,248,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">3</span>
        </div>
        <div class="drawer-grid">
          <div class="drawer-item" onclick="selectDrawerTab('solucion-practico7')">
            <span>💻 Práctico #7: Programación Modular (25 Ej.)</span>
            <span style="color: var(--accent-blue);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('solucion-practico8')">
            <span>🔤 Práctico #8: Cadenas (40 Ejercicios &amp; Form)</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('practico6-naturales')">
            <span>🔢 Práctico #6: Números Naturales</span>
            <span style="color: var(--accent-blue);">➜</span>
          </div>
        </div>
      </div>

      <!-- GRUPO 2: TAREAS DE CLASE S2-2026 -->
      <div class="drawer-group" style="margin-bottom: 1.1rem;">
        <div style="font-size: 0.75rem; font-weight: 800; color: #10b981; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: space-between;">
          <span>📝 TAREA S2-2026 &amp; PIZARRA</span>
          <span style="background: rgba(16,185,129,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">2</span>
        </div>
        <div class="drawer-grid">
          <div class="drawer-item" onclick="selectDrawerTab('ejercicios-pizarra')">
            <span>📋 Tarea de Clase (Pizarra &amp; Delphi Form)</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('series-y-herramientas')">
            <span>📈 Metodología 5 Pasos &amp; Series</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
        </div>
      </div>

      <!-- GRUPO 3: EVALUACIONES Y EXÁMENES -->
      <div class="drawer-group" style="margin-bottom: 1.1rem;">
        <div style="font-size: 0.75rem; font-weight: 800; color: #f59e0b; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: space-between;">
          <span>🏆 EVALUACIONES Y EXAMEN FINAL</span>
          <span style="background: rgba(245,158,11,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">5</span>
        </div>
        <div class="drawer-grid">
          <div class="drawer-item" onclick="selectDrawerTab('examen-final-oficial')">
            <span>🏆 Examen Final Oficial 2-2020 (40 Ptos)</span>
            <span style="color: var(--accent-rose);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('cadenas-exam-kit')">
            <span>🎯 Kit Examen Cadenas (5 Módulos)</span>
            <span style="color: var(--accent-amber);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('modelos-examen')">
            <span>🎯 Modelos de Examen (11 Ejercicios)</span>
            <span style="color: var(--accent-rose);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('simulacro-examen')">
            <span>⏱️ Simulacro con Cronómetro</span>
            <span style="color: var(--accent-purple);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('trampas-delphi')">
            <span>🧠 Trampas Clásicas &amp; Errores</span>
            <span style="color: var(--accent-rose);">➜</span>
          </div>
        </div>
      </div>

      <!-- GRUPO 4: LABORATORIOS & HERRAMIENTAS INTERACTIVAS -->
      <div class="drawer-group" style="margin-bottom: 1.1rem;">
        <div style="font-size: 0.75rem; font-weight: 800; color: #a855f7; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: space-between;">
          <span>🔬 LABORATORIOS &amp; HERRAMIENTAS</span>
          <span style="background: rgba(168,85,247,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">4</span>
        </div>
        <div class="drawer-grid">
          <div class="drawer-item" onclick="selectDrawerTab('traza-escritorio')">
            <span>🧪 Prueba de Escritorio (Trace en Vivo)</span>
            <span style="color: var(--accent-purple);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('hoja-atajos')">
            <span>⚡ Hoja de Atajos (Cheat Sheet F7/F8)</span>
            <span style="color: var(--accent-amber);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('diagramas-flujo')">
            <span>📊 Diagramas de Flujo ANSI</span>
            <span style="color: var(--accent-cyan);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('conversion-bases')">
            <span>🔢 Conversión de Bases Numéricas</span>
            <span style="color: var(--accent-blue);">➜</span>
          </div>
        </div>
      </div>

      <!-- GRUPO 5: FUNDAMENTOS DE PROGRAMACIÓN -->
      <div class="drawer-group" style="margin-bottom: 0.5rem;">
        <div style="font-size: 0.75rem; font-weight: 800; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; display: flex; align-items: center; justify-content: space-between;">
          <span>📖 FUNDAMENTOS DE PROGRAMACIÓN</span>
          <span style="background: rgba(203,213,225,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">7</span>
        </div>
        <div class="drawer-grid">
          <div class="drawer-item" onclick="selectDrawerTab('fundamentos-historia')">
            <span>📖 Fundamentos Teóricos &amp; PDFs</span>
            <span style="color: #cbd5e1;">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('diferencia-func-proc')">
            <span>⚖️ Función vs Procedimiento</span>
            <span style="color: var(--accent-amber);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('delphi-vcl-form')">
            <span>🖥️ Delphi Form (Clase Docente)</span>
            <span style="color: var(--accent-blue);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('buenas-practicas')">
            <span>💡 Buenas Prácticas &amp; Clean Code</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('puente-poo')">
            <span>🚀 Puente hacia POO (Objetos)</span>
            <span style="color: var(--accent-purple);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('preguntas')">
            <span>❓ Cuestionario de 20 Preguntas</span>
            <span style="color: var(--accent-amber);">➜</span>
          </div>
          <div class="drawer-item" onclick="selectDrawerTab('evaluacion-quiz')">
            <span>📝 Mini Test de Autoevaluación</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
        </div>
      </div>

    </div>'''

# ─── 5. CSS DEL SEPARADOR PROFESIONAL Y CHIPS ───
SEPARATOR_CSS = '''
    /* ==========================================================================
       ESTILOS DEL SEPARADOR PROFESIONAL DE TEMAS (MOODLE UAGRM STYLE)
       ========================================================================== */
    .cat-chip-btn {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #94a3b8;
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .cat-chip-btn:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      color: #fff;
    }
    .cat-chip-btn.active {
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border-color: #38bdf8;
      color: #fff;
      font-weight: 800;
      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
    }
    .nav-btn.hidden-by-category {
      display: none !important;
    }
'''

# ─── 6. JAVASCRIPT DE FILTRADO Y BÚSQUEDA ───
SEPARATOR_JS = '''
  // ===========================================================================
  //      MOTOR DEL SEPARADOR PROFESIONAL DE TEMAS (MOODLE UAGRM)
  // ===========================================================================
  let categoriaActualFiltro = 'all';

  function filtrarCategoria(cat) {
    categoriaActualFiltro = cat;

    // Actualizar estado activo en los botones chips
    const chips = document.querySelectorAll('.cat-chip-btn');
    chips.forEach(chip => {
      if (chip.getAttribute('data-cat') === cat) {
        chip.classList.add('active');
      } else {
        chip.classList.remove('active');
      }
    });

    // Limpiar input de búsqueda para no mezclar filtros
    const searchInput = document.getElementById('topicSearchInput');
    if (searchInput) searchInput.value = '';

    // Filtrar botones de navegacion en nav-tabs
    const navBtns = document.querySelectorAll('.nav-tabs .nav-btn');
    let visibles = 0;
    navBtns.forEach(btn => {
      const btnCat = btn.getAttribute('data-cat') || '';
      if (cat === 'all' || btnCat === cat) {
        btn.classList.remove('hidden-by-category');
        btn.style.display = '';
        visibles++;
      } else {
        btn.classList.add('hidden-by-category');
        btn.style.display = 'none';
      }
    });

    const badge = document.getElementById('filtroCountBadge');
    if (badge) {
      badge.innerText = `${visibles} Tema${visibles!==1?'s':''}`;
    }

    showMobileToast(`Mostrando: ${cat === 'all' ? 'Todos los temas' : cat.toUpperCase()}`);
  }

  function buscarTemasEnVivo() {
    const q = (document.getElementById('topicSearchInput').value || '').toLowerCase().trim();
    const navBtns = document.querySelectorAll('.nav-tabs .nav-btn');
    let visibles = 0;

    navBtns.forEach(btn => {
      const text = btn.innerText.toLowerCase();
      const cat = btn.getAttribute('data-cat') || '';
      const coincideCat = (categoriaActualFiltro === 'all' || cat === categoriaActualFiltro);
      const coincideBusqueda = (q === '' || text.includes(q));

      if (coincideCat && coincideBusqueda) {
        btn.classList.remove('hidden-by-category');
        btn.style.display = '';
        visibles++;
      } else {
        btn.classList.add('hidden-by-category');
        btn.style.display = 'none';
      }
    });

    const badge = document.getElementById('filtroCountBadge');
    if (badge) {
      badge.innerText = `${visibles} Encontrado${visibles!==1?'s':''}`;
    }
  }

  function buscarDrawerEnVivo() {
    const q = (document.getElementById('drawerSearchInput').value || '').toLowerCase().trim();
    const items = document.querySelectorAll('#mobileDrawer .drawer-item');
    items.forEach(item => {
      const text = item.innerText.toLowerCase();
      if (q === '' || text.includes(q)) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  }
'''

# ─── REALIZAR REEMPLAZOS EN EL HTML ───

# 1. Insertar BANNER antes de <header>
if 'class="moodle-banner-container"' not in html:
    pos_header = html.find('<header>')
    if pos_header != -1:
        html = html[:pos_header] + BANNER_HTML + '\n' + html[pos_header:]
        print('✓ Banner académico Moodle UAGRM insertado antes de <header>.')

# 2. Insertar CSS de separador antes de </style>
if '.cat-chip-btn' not in html:
    pos_style = html.find('</style>')
    if pos_style != -1:
        html = html[:pos_style] + SEPARATOR_CSS + '\n' + html[pos_style:]
        print('✓ Estilos del separador profesional insertados en <style>.')

# 3. Insertar SEPARADOR_BAR antes de <nav class="nav-tabs">
if 'class="topic-separator-wrapper"' not in html:
    pos_nav = html.find('<nav class="nav-tabs">')
    if pos_nav != -1:
        html = html[:pos_nav] + SEPARADOR_BAR_HTML + '\n' + html[pos_nav:]
        print('✓ Barra del separador de temas insertada antes de nav-tabs.')

# 4. Reemplazar <nav class="nav-tabs">...</nav> con NEW_NAV_TABS
pos_nav_start = html.find('<nav class="nav-tabs">')
if pos_nav_start != -1:
    pos_nav_end = html.find('</nav>', pos_nav_start) + len('</nav>')
    html = html[:pos_nav_start] + NEW_NAV_TABS + html[pos_nav_end:]
    print('✓ Nav tabs reorganizado y etiquetado con data-cat.')

# 5. Reorganizar el Drawer
pos_drw = html.find('id="mobileDrawer"')
if pos_drw != -1:
    pos_drw_title = html.find('<div class="drawer-title"', pos_drw)
    pos_drw_end = html.find('</aside>', pos_drw)
    if pos_drw_end == -1: pos_drw_end = html.find('</div>\n  </div>', pos_drw)
    if pos_drw_title != -1:
        # Reemplazar desde drawer-title hasta el cierre
        pos_close = html.find('</div>', pos_drw) # Cierre del primer div interno
        # Encontremos la etiqueta de cierre del drawer
        pos_aside_end = html.find('</div>\n  <!-- BOTÓN FLOTANTE', pos_drw)
        if pos_aside_end == -1:
            pos_aside_end = html.find('</div>\n\n  <!-- BOTÓN FLOTANTE', pos_drw)
        if pos_aside_end == -1:
            # Buscar el final de drawer-grid
            pos_grid_end = html.find('</div>', html.find('class="drawer-grid"', pos_drw)) + len('</div>')
            pos_aside_end = html.find('</div>', pos_grid_end)
        
        # Enfoque seguro: reemplazar el interior del drawer después de drawer-handle
        pos_handle = html.find('class="drawer-handle"></div>', pos_drw)
        if pos_handle != -1:
            ins_point = pos_handle + len('class="drawer-handle"></div>')
            # Buscar el cierre de mobileDrawer
            end_point = html.find('</div>\n  </div>', ins_point)
            if end_point == -1: end_point = html.find('</div>\n    </div>', ins_point)
            if end_point != -1:
                end_point += len('</div>\n  </div>')
                html = html[:ins_point] + '\n' + NEW_DRAWER_CONTENT + '\n  </div>' + html[end_point:]
                print('✓ Menú Drawer lateral reorganizado con acordeones oficiales.')

# 6. Insertar JavaScript antes del último </script>
if 'categoriaActualFiltro' not in html:
    pos_last_script = html.rfind('</script>')
    if pos_last_script != -1:
        html = html[:pos_last_script] + '\n\n' + SEPARATOR_JS.strip() + '\n\n' + html[pos_last_script:]
        print('✓ Motor JavaScript del separador insertado antes de </script>.')

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Separador profesional integrado con éxito: {HTML_FILE} ({len(html):,} bytes, {len(html.splitlines()):,} líneas)")
