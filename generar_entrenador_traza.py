# -*- coding: utf-8 -*-
"""
Módulo 3: Entrenador Interactivo de Prueba de Escritorio («Modo Llenar Tabla de Examen»)
Permite al estudiante rellenar manualmente las celdas de la tabla de traza
y auto-calificarse con feedback verde/rojo instantáneo.
"""

def build_entrenador_traza_html():
    return """
    <!-- ======================================================================= -->
    <!-- SUB-MÓDULO 4: ENTRENADOR DE PRUEBA DE ESCRITORIO (MODO LLENAR TABLA)   -->
    <!-- ======================================================================= -->
    <div id="toolSection-entrenador" class="tool-subpanel" style="display: none; margin-top: 1.5rem;">
      <div class="card" style="border: 2px solid #a855f7;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
          <h3 style="color: #c084fc; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>✏️</span> Entrenador de Prueba de Escritorio (Modo Llenar Tabla de Examen)
          </h3>
          <span style="font-size: 0.8rem; background: rgba(168, 85, 247, 0.15); color: #c084fc; padding: 0.25rem 0.6rem; border-radius: 4px; border: 1px solid rgba(168, 85, 247, 0.3);">
            Autocorrección Instantánea • Formato Parcial UAGRM
          </span>
        </div>

        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.5; margin-bottom: 1.25rem;">
          En el examen con la Ing. Angélica Garzón, la tabla de traza vale la mitad de la nota. <strong>Rellena las casillas vacías</strong> con los valores que van tomando las variables en cada paso y presiona «Calificar» para verificar tus respuestas:
        </p>

        <!-- SELECTOR DE EJERCICIO DE ENTRENAMIENTO -->
        <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; justify-content: space-between;">
          <div style="flex: 1; min-width: 250px;">
            <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.35rem;">Seleccionar Ejercicio para Practicar:</label>
            <select id="trainExSelect" class="delphi-form-edit" onchange="trainCargarEjercicio()" style="width: 100%; color: #c084fc !important; background: #0f172a !important; border: 1.5px solid #a855f7 !important; padding: 0.5rem 0.75rem; border-radius: 6px; font-weight: 700;">
              <option value="vocales">1. Contar Vocales (cad = 'casa')</option>
              <option value="burbuja">2. Pizarra: Ordenar Burbuja (cad = '321')</option>
              <option value="invertir">3. Invertir Cadena (cad = 'sol')</option>
              <option value="primos">4. Números: Sumar Dígitos Primos (n = 352)</option>
            </select>
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button class="delphi-btn-vcl" onclick="trainCalificar()" style="background: #10b981; color: #022c22; font-weight: 800; padding: 0.55rem 1.4rem; border-color: #059669; box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);">
              ✅ Calificar mi Traza
            </button>
            <button class="delphi-btn-vcl" onclick="trainRevelar()" style="background: #334155; color: #f8fafc; font-weight: 700; padding: 0.55rem 1rem;">
              👁️ Ver Solución Oficial
            </button>
            <button class="delphi-btn-vcl" onclick="trainLimpiar()" style="background: #1e293b; color: #94a3b8; font-weight: 700; padding: 0.55rem 0.85rem;">
              🧹 Limpiar
            </button>
          </div>
        </div>

        <!-- ENUNCIADO Y CÓDIGO DEL EJERCICIO -->
        <div style="background: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 1rem; margin-bottom: 1.25rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span id="trainEnunciadoTitle" style="color: #38bdf8; font-weight: 800; font-size: 0.95rem;">
              Ejercicio: Contar Vocales en 'casa'
            </span>
            <span id="trainPuntajeBadge" style="font-size: 0.82rem; font-weight: 800; color: #94a3b8;">
              Puntuación: Pendiente
            </span>
          </div>
          <pre id="trainCodeSnippet" style="background: #070a13; border: 1px solid #1e293b; border-radius: 4px; padding: 0.75rem; color: #f8fafc; font-family: 'Fira Code', monospace; font-size: 0.82rem; margin: 0; overflow-x: auto;"></pre>
        </div>

        <!-- TABLA DE TRAZA RELLENABLE -->
        <div style="overflow-x: auto; border: 1.5px solid #334155; border-radius: 8px; margin-bottom: 1.25rem;">
          <table class="traza-table" style="margin: 0; width: 100%;">
            <thead id="trainThead">
              <!-- Encabezados dinámicos -->
            </thead>
            <tbody id="trainTbody">
              <!-- Celdas con inputs generadas dinámicamente -->
            </tbody>
          </table>
        </div>

        <!-- MENSAJE DE FEEDBACK DE CALIFICACIÓN -->
        <div id="trainFeedbackBox" style="display: none; background: #070a13; border-radius: 6px; padding: 1rem; border-left: 4px solid #10b981;">
          <div id="trainFeedbackTitle" style="font-weight: 800; font-size: 1rem; color: #34d399; margin-bottom: 0.35rem;"></div>
          <div id="trainFeedbackDesc" style="font-size: 0.88rem; color: #cbd5e1;"></div>
        </div>

      </div>
    </div>
"""

