# -*- coding: utf-8 -*-
"""
Módulo 4: Banco Maestro de 25 Preguntas Trampa Teóricas (Quiz Rápido UAGRM)
Abarca todo el contenido evaluable de la cátedra de la Ing. Angélica Garzón:
Sintaxis Delphi, Cadenas, Ordenamientos, Modularidad y Números.
"""

def build_quiz_trampas_html():
    return """
  <!-- ======================================================================= -->
  <!-- SECCIÓN: BANCO MAESTRO DE 25 PREGUNTAS TRAMPA TEÓRICAS (QUIZ UAGRM)     -->
  <!-- ======================================================================= -->
  <section id="banco-quiz-teorico" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🧠 Banco Maestro: 25 Preguntas Trampa de Examen (Quiz UAGRM)</h2>
        <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; border-color: rgba(245, 158, 11, 0.3);">🏆 Asegura los 30 Puntos de Teoría</span>
      </div>

      <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin: 1rem 0;">
        Recopilación exhaustiva de las <strong>preguntas trampa teóricas reales</strong> que más puntos restan en los exámenes parciales y finales de la <strong>Ing. Angélica Garzón</strong>. Responde cada pregunta y obtén retroalimentación técnica inmediata:
      </p>

      <!-- BARRA DE PROGRESO Y FILTROS -->
      <div style="background: #0b1120; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; justify-content: space-between;">
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;" id="quizFilterButtons">
          <button class="delphi-btn-vcl active-quiz-filter" onclick="quizFiltrar('todas', this)" style="background: #0284c7; color: #fff; font-weight: 700; padding: 0.4rem 0.85rem; font-size: 0.82rem;">
            Todas (25)
          </button>
          <button class="delphi-btn-vcl" onclick="quizFiltrar('delphi', this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.4rem 0.85rem; font-size: 0.82rem;">
            Delphi &amp; Sintaxis (6)
          </button>
          <button class="delphi-btn-vcl" onclick="quizFiltrar('cadenas', this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.4rem 0.85rem; font-size: 0.82rem;">
            Cadenas (7)
          </button>
          <button class="delphi-btn-vcl" onclick="quizFiltrar('ordenamiento', this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.4rem 0.85rem; font-size: 0.82rem;">
            Ordenamiento (6)
          </button>
          <button class="delphi-btn-vcl" onclick="quizFiltrar('modularidad', this)" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.4rem 0.85rem; font-size: 0.82rem;">
            Modularidad &amp; Números (6)
          </button>
        </div>

        <div style="display: flex; align-items: center; gap: 1rem; font-family: 'Fira Code', monospace; font-size: 0.88rem;">
          <span style="color: #94a3b8;">Aciertos: <strong id="quizScoreText" style="color: #34d399;">0 / 0</strong></span>
          <button class="delphi-btn-vcl" onclick="quizReiniciar()" style="background: #334155; color: #f8fafc; font-size: 0.78rem; padding: 0.35rem 0.7rem;">
            🔄 Reiniciar
          </button>
        </div>
      </div>

      <!-- CONTENEDOR DE LA PREGUNTA ACTUAL -->
      <div id="quizCardScene" style="background: #0f172a; border: 2px solid #334155; border-radius: 10px; padding: 1.75rem; margin-bottom: 1.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.4);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <span id="quizBadgeCat" style="font-size: 0.75rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 3px 8px; border-radius: 4px; font-weight: 800; text-transform: uppercase;">
            DELPHI &amp; SINTAXIS
          </span>
          <span id="quizCounterText" style="font-size: 0.85rem; color: #94a3b8; font-family: 'Fira Code', monospace;">
            Pregunta 1 de 25
          </span>
        </div>

        <h3 id="quizQuestionText" style="color: #f8fafc; font-size: 1.15rem; line-height: 1.5; margin: 0.5rem 0 1.25rem 0;">
          ¿Por qué en Delphi una cadena tipo String se indexa a partir de 1 y no de 0?
        </h3>

        <!-- OPCIONES MULTIPLE CHOICE -->
        <div id="quizOptionsContainer" style="display: grid; gap: 0.75rem; margin-bottom: 1.5rem;">
          <!-- Opciones dinámicas -->
        </div>

        <!-- EXPLICACIÓN TÉCNICA / JUSTIFICACIÓN DE LA DOCENTE -->
        <div id="quizExplanationBox" style="display: none; background: #070a13; border-radius: 8px; padding: 1.25rem; border-left: 4px solid #10b981; margin-bottom: 1rem;">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem;">
            <span style="font-size: 1.2rem;">📖</span>
            <h4 style="color: #34d399; margin: 0; font-size: 0.95rem;">Justificación Teórica Oficial:</h4>
          </div>
          <p id="quizExplanationText" style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.5; margin: 0;"></p>
        </div>

        <!-- BOTONES DE NAVEGACIÓN -->
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <button class="delphi-btn-vcl" onclick="quizAnterior()" style="background: #1e293b; color: #cbd5e1; font-weight: 700; padding: 0.5rem 1rem;">
            ◀ Anterior
          </button>
          <button class="delphi-btn-vcl" onclick="quizSiguiente()" style="background: #0284c7; color: #fff; font-weight: 700; padding: 0.5rem 1.4rem;">
            Siguiente ▶
          </button>
        </div>

      </div>

    </div>
  </section>
  <!-- FIN SECCIÓN BANCO QUIZ -->
"""

