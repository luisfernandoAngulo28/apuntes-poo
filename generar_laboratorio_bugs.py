# -*- coding: utf-8 -*-
"""
Módulo 2: Laboratorio Interactivo «Detecta y Corrige el Bug de Examen»
(Las 6 Trampas Clásicas de la Ing. Angélica Garzón en Exámenes Parciales)
"""

def build_laboratorio_bugs_html():
    return """
  <!-- ======================================================================= -->
  <!-- SECCIÓN: LABORATORIO INTERACTIVO DETECTA EL BUG DE EXAMEN              -->
  <!-- ======================================================================= -->
  <section id="laboratorio-bugs-examen" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🧪 Laboratorio Interactivo: «Detecta y Corrige el Bug de Examen»</h2>
        <span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #f87171; border-color: rgba(239, 68, 68, 0.3);">⚠️ Pregunta Típica de Parcial • INF110-Z2</span>
      </div>

      <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin: 1rem 0;">
        En los exámenes de la <strong>M.Sc. Ing. Angélica Garzón</strong> es común que te den fragmentos de código con <strong>errores conceptuales o sintácticos intencionales</strong> para evaluar si realmente entiendes la memoria y el compilador de Delphi. Pon a prueba tu ojo clínico seleccionando el error en cada caso:
      </p>

      <!-- BOTONERA DE CASOS DE BUGS -->
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;" id="bugNavButtons">
        <button class="delphi-btn-vcl active-bug-btn" onclick="bugCargarCaso(0, this)" style="background: #0284c7; color: #fff; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 1: Bucle Infinito
        </button>
        <button class="delphi-btn-vcl" onclick="bugCargarCaso(1, this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 2: Índice Cero (cad[0])
        </button>
        <button class="delphi-btn-vcl" onclick="bugCargarCaso(2, this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 3: Punto y Coma en ELSE
        </button>
        <button class="delphi-btn-vcl" onclick="bugCargarCaso(3, this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 4: Función sin Result
        </button>
        <button class="delphi-btn-vcl" onclick="bugCargarCaso(4, this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 5: Variable sin Inicializar
        </button>
        <button class="delphi-btn-vcl" onclick="bugCargarCaso(5, this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.5rem 1rem;">
          Bug 6: Swap Destructivo sin Aux
        </button>
      </div>

      <!-- VISOR DEL CASO ACTUAL -->
      <div style="background: #0b1120; border: 2px solid #334155; border-radius: 10px; padding: 1.5rem; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
          <h3 id="bugTitle" style="color: #f87171; margin: 0; font-size: 1.15rem;">
            Caso 1: ¿Por qué este algoritmo cuelga la computadora?
          </h3>
          <span id="bugBadge" style="font-size: 0.75rem; background: rgba(239, 68, 68, 0.2); color: #f87171; padding: 3px 8px; border-radius: 4px; font-weight: 800;">
            ERROR DE EJECUCIÓN (HANG)
          </span>
        </div>

        <p id="bugPrompt" style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 1rem;">
          Analiza el siguiente código escrito por un estudiante y encuentra cuál es la línea fatal:
        </p>

        <!-- CÓDIGO CON LÍNEAS CLICKEABLES -->
        <div id="bugCodeContainer" style="background: #070a13; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; font-family: 'Fira Code', monospace; font-size: 0.88rem; overflow-x: auto; margin-bottom: 1.25rem;">
          <!-- Código inyectado dinámicamente -->
        </div>

        <!-- OPCIONES DE RESPUESTA INTERACTIVAS -->
        <div style="margin-bottom: 1.25rem;">
          <div style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.6rem;">
            ¿Cuál es el diagnóstico correcto del problema?
          </div>
          <div id="bugOptionsGrid" style="display: grid; gap: 0.6rem;">
            <!-- Opciones generadas por JS -->
          </div>
        </div>

        <!-- CAJA DE EXPLICACIÓN Y SOLUCIÓN OFICIAL (OCULTA INICIALMENTE) -->
        <div id="bugExplanationBox" style="display: none; background: #070a13; border-radius: 8px; padding: 1.25rem; border-left: 4px solid #10b981;">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="font-size: 1.2rem;">💡</span>
            <h4 id="bugFeedbackTitle" style="color: #34d399; margin: 0; font-size: 1rem;">¡Exacto! Esa es la trampa del examen</h4>
          </div>
          <p id="bugFeedbackText" style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.5; margin-bottom: 0.75rem;">
            <!-- Explicación -->
          </p>
          <div style="background: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 0.85rem;">
            <span style="font-size: 0.78rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">Código Oficial Corregido:</span>
            <pre id="bugCorrectCode" style="color: #34d399; font-family: 'Fira Code', monospace; font-size: 0.82rem; margin: 0.4rem 0 0 0; overflow-x: auto;"></pre>
          </div>
        </div>

      </div>

    </div>
  </section>
  <!-- FIN SECCIÓN LABORATORIO BUGS -->
"""

