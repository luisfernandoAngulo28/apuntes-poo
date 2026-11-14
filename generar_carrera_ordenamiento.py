# -*- coding: utf-8 -*-
"""
Módulo 1: Carrera en Vivo de los 5 Métodos de Ordenamiento
(Burbuja vs Selección vs Inserción vs Shell vs QuickSort)
Visualizador interactivo con barras de progreso y estadísticas en tiempo real:
- Comparaciones
- Intercambios (Swaps)
- Estado de ordenamiento
"""

def build_carrera_ordenamiento_html():
    return """
      <!-- ======================================================================= -->
      <!-- SUB-SECCIÓN: SIMULADOR VISUAL - CARRERA DE LOS 5 MÉTODOS DE ORDENACIÓN  -->
      <!-- ======================================================================= -->
      <div style="margin-top: 2.5rem; background: rgba(15, 23, 42, 0.95); border: 2px solid #38bdf8; border-radius: 12px; padding: 1.5rem; box-shadow: 0 8px 30px rgba(0,0,0,0.5);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
          <h3 style="color: #38bdf8; margin: 0; font-size: 1.25rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🏁</span> Carrera Visual en Vivo: Los 5 Métodos de Ordenación
          </h3>
          <span style="font-size: 0.8rem; background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 0.25rem 0.6rem; border-radius: 4px; border: 1px solid rgba(56, 189, 248, 0.3);">
            Burbuja • Selección • Inserción • Shell • QuickSort
          </span>
        </div>
        <p style="color: #94a3b8; font-size: 0.92rem; line-height: 1.5; margin-bottom: 1.25rem;">
          Compara el comportamiento en tiempo real de los 5 algoritmos sobre el <strong>mismo vector de prueba</strong>. Observa cómo QuickSort y ShellSort reducen drásticamente la cantidad de comparaciones respecto a Burbuja.
        </p>

        <!-- PANEL DE CONTROL DE LA CARRERA -->
        <div style="background: #070a13; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end; justify-content: space-between;">
          <div style="flex: 1; min-width: 240px;">
            <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.35rem;">Vector de Entrada (números separados por comas):</label>
            <input type="text" id="raceInputVector" value="4, 5, 1, 2, 3" style="width: 100%; font-family: 'Fira Code', monospace; color: #ffffff !important; background: #0f172a !important; border: 1.5px solid #38bdf8 !important; padding: 0.5rem 0.75rem; font-size: 1rem; font-weight: 700; border-radius: 6px;">
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button class="delphi-btn-vcl" onclick="raceCargarVector('4, 5, 1, 2, 3')" style="background: #1e293b; color: #94a3b8; font-size: 0.8rem; padding: 0.45rem 0.75rem;">
              📋 Pizarra: [4,5,1,2,3]
            </button>
            <button class="delphi-btn-vcl" onclick="raceGenerarAleatorio(8)" style="background: #1e293b; color: #38bdf8; font-size: 0.8rem; padding: 0.45rem 0.75rem;">
              🎲 8 Aleatorios
            </button>
            <button class="delphi-btn-vcl" onclick="raceGenerarAleatorio(15)" style="background: #1e293b; color: #a855f7; font-size: 0.8rem; padding: 0.45rem 0.75rem;">
              ⚡ 15 Aleatorios
            </button>
          </div>
          <div>
            <button class="delphi-btn-vcl" id="btnRaceStart" onclick="raceIniciarCarrera()" style="background: #10b981; color: #022c22; font-weight: 800; font-size: 1rem; padding: 0.6rem 1.6rem; border-color: #059669; box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);">
              🚀 Iniciar Carrera
            </button>
          </div>
        </div>

        <!-- PISTAS DE CARRERA (LOS 5 ALGORITMOS) -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
          
          <!-- PISTA 1: BURBUJA -->
          <div style="background: #0b1120; border: 1.5px solid #10b981; border-radius: 8px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #34d399; font-weight: 800; font-size: 0.95rem;">🫧 1. Burbuja</span>
              <span id="raceStatus-burbuja" style="font-size: 0.75rem; color: #94a3b8;">Listo</span>
            </div>
            <div id="raceBars-burbuja" style="display: flex; gap: 3px; align-items: flex-end; height: 90px; background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 0.75rem; overflow-x: auto;">
              <!-- Barras generadas por JS -->
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.8rem;">
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Comp:</span> <strong id="raceComp-burbuja" style="color: #38bdf8;">0</strong>
              </div>
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Swaps:</span> <strong id="raceSwap-burbuja" style="color: #fbbf24;">0</strong>
              </div>
            </div>
          </div>

          <!-- PISTA 2: SELECCIÓN -->
          <div style="background: #0b1120; border: 1.5px solid #38bdf8; border-radius: 8px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #38bdf8; font-weight: 800; font-size: 0.95rem;">🎯 2. Selección</span>
              <span id="raceStatus-seleccion" style="font-size: 0.75rem; color: #94a3b8;">Listo</span>
            </div>
            <div id="raceBars-seleccion" style="display: flex; gap: 3px; align-items: flex-end; height: 90px; background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 0.75rem; overflow-x: auto;"></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.8rem;">
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Comp:</span> <strong id="raceComp-seleccion" style="color: #38bdf8;">0</strong>
              </div>
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Swaps:</span> <strong id="raceSwap-seleccion" style="color: #fbbf24;">0</strong>
              </div>
            </div>
          </div>

          <!-- PISTA 3: INSERCIÓN -->
          <div style="background: #0b1120; border: 1.5px solid #c084fc; border-radius: 8px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #c084fc; font-weight: 800; font-size: 0.95rem;">🃏 3. Inserción</span>
              <span id="raceStatus-insercion" style="font-size: 0.75rem; color: #94a3b8;">Listo</span>
            </div>
            <div id="raceBars-insercion" style="display: flex; gap: 3px; align-items: flex-end; height: 90px; background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 0.75rem; overflow-x: auto;"></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.8rem;">
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Comp:</span> <strong id="raceComp-insercion" style="color: #38bdf8;">0</strong>
              </div>
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Swaps:</span> <strong id="raceSwap-insercion" style="color: #fbbf24;">0</strong>
              </div>
            </div>
          </div>

          <!-- PISTA 4: SHELL -->
          <div style="background: #0b1120; border: 1.5px solid #f59e0b; border-radius: 8px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #fbbf24; font-weight: 800; font-size: 0.95rem;">🐚 4. Shell Sort</span>
              <span id="raceStatus-shell" style="font-size: 0.75rem; color: #94a3b8;">Listo</span>
            </div>
            <div id="raceBars-shell" style="display: flex; gap: 3px; align-items: flex-end; height: 90px; background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 0.75rem; overflow-x: auto;"></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.8rem;">
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Comp:</span> <strong id="raceComp-shell" style="color: #38bdf8;">0</strong>
              </div>
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Swaps:</span> <strong id="raceSwap-shell" style="color: #fbbf24;">0</strong>
              </div>
            </div>
          </div>

          <!-- PISTA 5: QUICKSORT -->
          <div style="background: #0b1120; border: 1.5px solid #ec4899; border-radius: 8px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="color: #f472b6; font-weight: 800; font-size: 0.95rem;">⚡ 5. QuickSort</span>
              <span id="raceStatus-quicksort" style="font-size: 0.75rem; color: #94a3b8;">Listo</span>
            </div>
            <div id="raceBars-quicksort" style="display: flex; gap: 3px; align-items: flex-end; height: 90px; background: #070a13; border: 1px solid #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 0.75rem; overflow-x: auto;"></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-family: 'Fira Code', monospace; font-size: 0.8rem;">
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Comp:</span> <strong id="raceComp-quicksort" style="color: #38bdf8;">0</strong>
              </div>
              <div style="background: #070a13; padding: 4px 8px; border-radius: 4px; border: 1px solid #1e293b;">
                <span style="color: #94a3b8;">Swaps:</span> <strong id="raceSwap-quicksort" style="color: #fbbf24;">0</strong>
              </div>
            </div>
          </div>

        </div>

        <!-- CUADRO DE CONCLUSIÓN COMPARATIVA EN VIVO -->
        <div id="raceVerdictBox" style="margin-top: 1rem; background: #070a13; border-left: 4px solid #10b981; border-radius: 6px; padding: 0.85rem 1.25rem; font-size: 0.88rem; color: #cbd5e1;">
          Presiona <strong>«Iniciar Carrera»</strong> para ver competir los 5 algoritmos y comparar la cantidad de operaciones requeridas.
        </div>
      </div>
"""

