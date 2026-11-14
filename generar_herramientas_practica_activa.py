# -*- coding: utf-8 -*-
"""
Generador del Módulo de Práctica Activa para Rendir Exámenes (INF110 - UAGRM)
Docente: M.Sc. Ing. Angélica Garzón Cuéllar
"""

import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def build_practica_activa_html():
    out = []
    
    out.append('''
  <!-- ========================================================================= -->
  <!-- SECCIÓN: PRÁCTICA ACTIVA PARA EXÁMENES (TRAZA, FLASHCARDS & PARCIAL REAL) -->
  <!-- ========================================================================= -->
  <section id="practica-activa-examenes" class="section-content">
    
    <!-- ENCABEZADO PRINCIPAL DE LA SECCIÓN -->
    <div class="card" style="border-left: 5px solid #10b981; background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(6, 78, 59, 0.15));">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">⚡ Laboratorio de Práctica Activa para Exámenes</h2>
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3);">
          ENTRENAMIENTO UAGRM • INF110-Z2
        </span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem; color: #cbd5e1; line-height: 1.6;">
        Entorno interactivo diseñado específicamente para rendir y aprobar los exámenes de la <strong>M.Sc. Angélica Garzón Cuéllar</strong>. 
        Pon a prueba tus conocimientos con el <strong>Animador de Memoria en Vivo</strong>, domina conceptos clave con las <strong>Flashcards móviles</strong> y simula un <strong>Examen Parcial Real con Cronómetro</strong>.
      </p>

      <!-- SELECTOR DE HERRAMIENTAS ACTIVAS -->
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.25rem;">
        <button class="btn-print active-herramienta" id="btnToolTraza" onclick="switchToolActive('traza', this)" style="font-size: 0.9rem; padding: 0.6rem 1.2rem; display: flex; align-items: center; gap: 0.5rem; background: #10b981; color: #022c22; font-weight: 800; border-color: #059669;">
          <span>🧪 1. Animador de Memoria &amp; Traza</span>
        </button>
        <button class="btn-print" id="btnToolFlashcards" onclick="switchToolActive('flashcards', this)" style="font-size: 0.9rem; padding: 0.6rem 1.2rem; display: flex; align-items: center; gap: 0.5rem; background: #0f172a; color: #38bdf8; font-weight: 700; border: 1px solid #0284c7;">
          <span>🎴 2. Flashcards de Examen (Anki)</span>
        </button>
        <button class="btn-print" id="btnToolExamen" onclick="switchToolActive('examen', this)" style="font-size: 0.9rem; padding: 0.6rem 1.2rem; display: flex; align-items: center; gap: 0.5rem; background: #0f172a; color: #f59e0b; font-weight: 700; border: 1px solid #d97706;">
          <span>📝 3. Simulador de Parcial Imprimible</span>
        </button>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- SUB-MÓDULO 1: SIMULADOR DE TRAZA Y ANIMADOR DE MEMORIA EN VIVO          -->
    <!-- ======================================================================= -->
    <div id="toolSection-traza" class="tool-subpanel" style="display: block; margin-top: 1.5rem;">
      <div class="card" style="border: 1px solid rgba(16, 185, 129, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
          <h3 style="color: #34d399; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>🧪</span> Animador de Traza de Escritorio en Tiempo Real
          </h3>
          <span style="font-size: 0.8rem; background: rgba(52, 211, 153, 0.1); color: #34d399; padding: 0.25rem 0.6rem; border-radius: 4px; border: 1px solid rgba(52, 211, 153, 0.2);">
            Metodología Oficial: while i &lt;= n
          </span>
        </div>
        <p style="font-size: 0.92rem; color: #94a3b8; margin-bottom: 1.25rem;">
          Observa cómo se desplaza el puntero <code>i</code> posición por posición, cómo se actualiza la memoria RAM de variables y cómo se genera la tabla de traza idéntica a la que la docente exige en las hojas de examen.
        </p>

        <!-- PANEL DE CONTROL DEL ALGORITMO -->
        <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.2rem; margin-bottom: 1.5rem;">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; align-items: end;">
            
            <!-- SELECTOR DE ALGORITMO -->
            <div>
              <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.4rem;">Seleccionar Algoritmo a Animar:</label>
              <select id="animAlgSelect" class="delphi-form-edit" onchange="animCambiarAlgoritmo()" style="width: 100%; font-weight: 700; color: #34d399; background: #0f172a; border: 2px solid #059669; padding: 0.6rem 0.85rem; border-radius: 6px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);">
                <option value="vocales">1. Contar Vocales (cad: String; n, i: Byte)</option>
                <option value="elimEspacios">2. Eliminar Espacios en Blanco (cad: String; n, i: Byte)</option>
                <option value="contarPalabras">3. Contar Palabras con Bandera (enPalabra: Boolean)</option>
                <option value="invertir">4. Invertir Cadena (Recorrido Regresivo i := n downto 1)</option>
                <option value="buscarLetra">5. Buscar Carácter con Salida Anticipada (encontrado = true)</option>
                <option value="paresVocales">6. Contar 2 Vocales Juntas Contiguas (cad[i] y cad[i+1])</option>
                <option value="numDigitos">7. Números: Sumar Dígitos Primos (n mod 10 y n div 10)</option>
              </select>
            </div>

            <!-- ENTRADA DE TEXTO O NÚMERO -->
            <div>
              <label id="animInputLabel" style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.4rem;">Cadena de Entrada (cad):</label>
              <input type="text" id="animInputCad" class="delphi-form-edit" value="hola mundo" style="width: 100%; font-family: 'Fira Code', monospace; color: #ffffff !important; background: #0f172a !important; border: 2px solid #38bdf8 !important; padding: 0.6rem 0.85rem !important; font-size: 1.15rem !important; font-weight: 700 !important; border-radius: 6px !important; box-shadow: 0 0 10px rgba(56, 189, 248, 0.25) !important;">
            </div>

            <!-- PARÁMETRO EXTRA (OCULTO SEGÚN ALGORITMO) -->
            <div id="animExtraCol" style="display: none;">
              <label id="animExtraLabel" style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 0.4rem;">Carácter a Buscar:</label>
              <input type="text" id="animInputExtra" class="delphi-form-edit" value="o" maxlength="1" style="width: 100%; text-align: center; font-weight: 900; font-size: 1.2rem; color: #fbbf24 !important; background: #0f172a !important; border: 2px solid #f59e0b !important; padding: 0.6rem 0.85rem !important; border-radius: 6px !important; box-shadow: 0 0 10px rgba(245, 158, 11, 0.25) !important;">
            </div>

          </div>

          <!-- BOTONERA DE CONTROL PASO A PASO -->
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.25rem; align-items: center; justify-content: space-between;">
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
              <button class="delphi-btn-vcl" onclick="animReset()" style="background: #334155; color: #f8fafc; font-weight: 700; padding: 0.5rem 1rem;">
                ⏮ Reiniciar
              </button>
              <button class="delphi-btn-vcl" id="btnAnimStep" onclick="animPasoSiguiente()" style="background: #10b981; color: #022c22; font-weight: 800; padding: 0.5rem 1.4rem; border-color: #059669; box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);">
                ⏭ Paso Siguiente (F8)
              </button>
              <button class="delphi-btn-vcl" id="btnAnimAuto" onclick="animToggleAuto()" style="background: #0284c7; color: #f0fdf4; font-weight: 700; padding: 0.5rem 1.2rem;">
                ▶ Auto Ejecutar
              </button>
            </div>

            <!-- INDICADOR DE VELOCIDAD -->
            <div style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.82rem; color: #94a3b8;">
              <span>Velocidad:</span>
              <select id="animSpeedSelect" class="delphi-form-edit" style="padding: 0.35rem 0.65rem; font-size: 0.82rem; font-weight: 600; color: #f8fafc !important; background: #0f172a !important; border: 1.5px solid #475569 !important; border-radius: 4px;">
                <option value="1200">Lenta (1.2s)</option>
                <option value="600" selected>Media (0.6s)</option>
                <option value="250">Rápida (0.25s)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- CINTA VISUAL DE MEMORIA (CHARACTER TAPE) -->
        <div style="margin-bottom: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.05em;">
              📼 Cinta de Memoria: cad[1..n] &amp; Puntero Activo i
            </span>
            <span id="animTapeStatus" style="font-size: 0.82rem; color: #34d399; font-weight: 600;">
              Longitud n = 10
            </span>
          </div>

          <!-- CONTENEDOR DE CELDAS CON DESPLAZAMIENTO -->
          <div id="animTapeContainer" style="display: flex; gap: 8px; overflow-x: auto; padding: 1.85rem 0.75rem 1.25rem 0.75rem; background: #070a13; border: 1.5px solid #1e293b; border-radius: 8px; min-height: 105px; align-items: center;">
            <!-- Celdas generadas dinámicamente por JS -->
          </div>
        </div>

        <!-- PANEL DE VARIABLES (RAM INSPECTOR) Y LÍNEA DE CÓDIGO -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
          
          <!-- VARIABLES EN MEMORIA -->
          <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #38bdf8; text-transform: uppercase; margin-bottom: 0.75rem; display: flex; justify-content: space-between;">
              <span>💾 Estado de Variables (RAM)</span>
              <span id="animPasoCounter" style="color: #94a3b8;">Paso: 0</span>
            </div>
            <div id="animVarsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.65rem;">
              <!-- Tarjetas de variables dinámicas -->
            </div>
          </div>

          <!-- EVALUACIÓN LÓGICA Y LÍNEA DE CÓDIGO ACTUAL -->
          <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="font-size: 0.8rem; font-weight: 800; color: #fbbf24; text-transform: uppercase; margin-bottom: 0.5rem;">
                ⚙️ Condición / Expresión Evaluada
              </div>
              <div id="animCondText" style="font-family: 'Fira Code', monospace; font-size: 0.9rem; padding: 0.6rem; background: #070a13; border-radius: 4px; border: 1px solid #334155; color: #f8fafc; min-height: 42px; display: flex; align-items: center;">
                Esperando inicio de simulación...
              </div>
            </div>
            <div style="margin-top: 0.75rem;">
              <span style="font-size: 0.75rem; color: #94a3b8;">Explicación del paso:</span>
              <p id="animStepExplanation" style="font-size: 0.85rem; color: #cbd5e1; margin: 0.25rem 0 0 0; line-height: 1.4;">
                Haz clic en «Paso Siguiente» para inicializar las variables con <code>i := 1;</code>.
              </p>
            </div>
          </div>

        </div>

        <!-- TABLA FORMAL DE PRUEBA DE ESCRITORIO (GENERADA LÍNEA A LÍNEA) -->
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; flex-wrap: wrap; gap: 0.5rem;">
            <h4 style="color: #cbd5e1; margin: 0; font-size: 0.95rem;">
              📋 Tabla de Prueba de Escritorio Generada en Tiempo Real
            </h4>
            <div style="display: flex; gap: 0.5rem;">
              <button class="btn-print" onclick="animCopiarTabla()" style="font-size: 0.78rem; padding: 0.3rem 0.7rem;">
                📋 Copiar Tabla
              </button>
              <button class="btn-print" onclick="animLimpiarTabla()" style="font-size: 0.78rem; padding: 0.3rem 0.7rem; color: #f87171;">
                🗑️ Limpiar
              </button>
            </div>
          </div>

          <div style="overflow-x: auto; max-height: 280px; border: 1px solid var(--border-color); border-radius: 6px;">
            <table class="traza-table" id="animTrazaTable" style="margin: 0; width: 100%;">
              <thead id="animTrazaThead">
                <!-- Encabezados dinámicos según algoritmo -->
              </thead>
              <tbody id="animTrazaTbody">
                <tr><td colspan="7" style="text-align: center; color: #64748b; padding: 1.5rem;">Inicia la simulación para construir las filas de la traza de escritorio.</td></tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- SUB-MÓDULO 2: FLASHCARDS DE MEMORIZACIÓN RÁPIDA (ANKI PARA MÓVIL)       -->
    <!-- ======================================================================= -->
    <div id="toolSection-flashcards" class="tool-subpanel" style="display: none; margin-top: 1.5rem;">
      <div class="card" style="border: 1px solid rgba(56, 189, 248, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
          <h3 style="color: #38bdf8; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>🎴</span> Flashcards de Repaso Rápido para Examen (INF110)
          </h3>
          <span style="font-size: 0.8rem; background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 0.25rem 0.6rem; border-radius: 4px; border: 1px solid rgba(56, 189, 248, 0.2);">
            Optimizado para Celular / Micro-Aprendizaje
          </span>
        </div>
        <p style="font-size: 0.92rem; color: #94a3b8; margin-bottom: 1.25rem;">
          Domina los conceptos teóricos, reglas de sintaxis de Delphi, códigos ASCII indispensables y preguntas trampa que la docente incluye en los exámenes. Toca o haz clic en la tarjeta para voltearla.
        </p>

        <!-- FILTROS POR TEMA DE FLASHCARDS -->
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
          <button class="btn-print active-fc-cat" id="fcCat-todas" onclick="fcFiltrarCategoria('todas', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">Todas (25)</button>
          <button class="btn-print" id="fcCat-ascii" onclick="fcFiltrarCategoria('ascii', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">ASCII &amp; Letras</button>
          <button class="btn-print" id="fcCat-sintaxis" onclick="fcFiltrarCategoria('sintaxis', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">Sintaxis Delphi &amp; Sets</button>
          <button class="btn-print" id="fcCat-modular" onclick="fcFiltrarCategoria('modular', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">Función vs Procedimiento</button>
          <button class="btn-print" id="fcCat-trampas" onclick="fcFiltrarCategoria('trampas', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">Trampas de Examen</button>
          <button class="btn-print" id="fcCat-algoritmos" onclick="fcFiltrarCategoria('algoritmos', this)" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">Algoritmos Clave</button>
        </div>

        <!-- ÁREA CENTRAL DE LA TARJETA 3D -->
        <div style="display: flex; justify-content: center; margin-bottom: 1.5rem;">
          <div class="fc-card-scene" onclick="fcToggleFlip()" style="width: 100%; max-width: 620px; height: 320px; perspective: 1000px; cursor: pointer;">
            <div id="fcCardInner" class="fc-card-inner" style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
              
              <!-- CARA FRONTAL (PREGUNTA) -->
              <div class="fc-face fc-front" style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background: linear-gradient(145deg, #1e293b, #0f172a); border: 2px solid #38bdf8; border-radius: 12px; padding: 2rem; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span id="fcBadgeCat" style="font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #38bdf8; background: rgba(56, 189, 248, 0.15); padding: 0.25rem 0.6rem; border-radius: 4px;">
                    ASCII &amp; Caracteres
                  </span>
                  <span id="fcCounter" style="font-size: 0.8rem; color: #64748b; font-weight: 700;">
                    1 de 25
                  </span>
                </div>

                <div style="margin: auto 0;">
                  <span style="font-size: 0.9rem; color: #94a3b8; display: block; margin-bottom: 0.5rem;">Pregunta de Examen:</span>
                  <h3 id="fcPreguntaText" style="color: #f8fafc; font-size: 1.35rem; line-height: 1.4; margin: 0;">
                    ¿Cuál es el código ASCII del espacio en blanco ' '?
                  </h3>
                </div>

                <div style="font-size: 0.8rem; color: #64748b;">
                  👆 Toca o presiona [Espacio] para ver la respuesta
                </div>
              </div>

              <!-- CARA POSTERIOR (RESPUESTA Y EXPLICACIÓN) -->
              <div class="fc-face fc-back" style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; transform: rotateY(180deg); background: linear-gradient(145deg, #064e3b, #022c22); border: 2px solid #34d399; border-radius: 12px; padding: 2rem; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #34d399; background: rgba(52, 211, 153, 0.2); padding: 0.25rem 0.6rem; border-radius: 4px;">
                    ✅ Respuesta Oficial
                  </span>
                  <span id="fcBackSubcat" style="font-size: 0.8rem; color: #6ee7b7;">Concepto Clave</span>
                </div>

                <div style="margin: auto 0;">
                  <div id="fcRespuestaText" style="color: #f0fdf4; font-size: 1.35rem; font-weight: 800; line-height: 1.4; margin-bottom: 0.75rem;">
                    ASCII 32 (o en Pascal: #32)
                  </div>
                  <div id="fcDetalleText" style="color: #a7f3d0; font-size: 0.9rem; line-height: 1.5;">
                    En Pascal se evalúa con <code>cad[i] = ' '</code> o <code>Ord(cad[i]) = 32</code>. Es el delimitador universal de palabras.
                  </div>
                </div>

                <div style="font-size: 0.8rem; color: #6ee7b7;">
                  🔄 Toca para volver a la pregunta
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- CONTROLES DE NAVEGACIÓN Y CALIFICACIÓN DE REPASO -->
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; max-width: 620px; margin: 0 auto;">
          <button class="delphi-btn-vcl" onclick="fcAnterior()" style="background: #1e293b; color: #cbd5e1; font-weight: 700; padding: 0.6rem 1.2rem;">
            ◀ Anterior
          </button>

          <!-- BOTONES DE AUTOEVALUACIÓN (ANKI) -->
          <div style="display: flex; gap: 0.4rem;">
            <button onclick="fcEvaluar('dificil')" title="Repetir pronto" style="background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; border-radius: 4px; padding: 0.45rem 0.75rem; font-size: 0.8rem; font-weight: 700; cursor: pointer;">
              ❌ Difícil
            </button>
            <button onclick="fcEvaluar('duda')" title="Repasar" style="background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; border-radius: 4px; padding: 0.45rem 0.75rem; font-size: 0.8rem; font-weight: 700; cursor: pointer;">
              ⚠️ Duda
            </button>
            <button onclick="fcEvaluar('facil')" title="Dominado" style="background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; border-radius: 4px; padding: 0.45rem 0.75rem; font-size: 0.8rem; font-weight: 700; cursor: pointer;">
              ✅ Dominado
            </button>
          </div>

          <div style="display: flex; gap: 0.5rem;">
            <button class="delphi-btn-vcl" onclick="fcAleatorio()" title="Tarjeta aleatoria" style="background: #334155; color: #cbd5e1; padding: 0.6rem 0.8rem;">
              🔀
            </button>
            <button class="delphi-btn-vcl" onclick="fcSiguiente()" style="background: #0284c7; color: #fff; font-weight: 700; padding: 0.6rem 1.2rem;">
              Siguiente ▶
            </button>
          </div>
        </div>

        <!-- BARRA DE DOMINIO / PROGRESO -->
        <div style="max-width: 620px; margin: 1.5rem auto 0 auto;">
          <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: #94a3b8; margin-bottom: 0.3rem;">
            <span>Progreso de memorización:</span>
            <span id="fcProgressText">0 de 25 dominadas (0%)</span>
          </div>
          <div style="background: #1e293b; border-radius: 999px; height: 8px; overflow: hidden;">
            <div id="fcProgressBar" style="background: #10b981; height: 100%; width: 0%; transition: width 0.3s;"></div>
          </div>
        </div>

      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- SUB-MÓDULO 3: GENERADOR DE EXÁMENES ALEATORIOS IMPRIMIBLES (PARCIAL)   -->
    <!-- ======================================================================= -->
    <div id="toolSection-examen" class="tool-subpanel" style="display: none; margin-top: 1.5rem;">
      <div class="card" style="border: 1px solid rgba(245, 158, 11, 0.3);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
          <h3 style="color: #fbbf24; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>📝</span> Simulador de Examen Parcial Real UAGRM (Ponderado /100)
          </h3>
          <span style="font-size: 0.8rem; background: rgba(245, 158, 11, 0.1); color: #fbbf24; padding: 0.25rem 0.6rem; border-radius: 4px; border: 1px solid rgba(245, 158, 11, 0.2);">
            Formato Oficial para Impresión
          </span>
        </div>
        <p style="font-size: 0.92rem; color: #94a3b8; margin-bottom: 1.25rem;">
          Genera un examen aleatorio estructurado con los 3 tipos de preguntas del examen parcial de la <strong>Ing. Angélica Garzón</strong>: Números Naturales (35 pts), Cadenas con Metodología <code>(cad, n, i)</code> (40 pts) y Traza de Escritorio Formal (25 pts).
        </p>

        <!-- PANEL DE CONTROL DEL EXAMEN: BOTONES Y CRONÓMETRO -->
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.2rem; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <button class="btn-print" onclick="realExamGenerarNuevo()" style="background: #f59e0b; color: #1e293b; font-weight: 800; border-color: #d97706; padding: 0.6rem 1.25rem; font-size: 0.88rem; cursor: pointer;">
              🎲 Generar Nuevo Examen Aleatorio
            </button>
            <button class="btn-print" onclick="window.print()" style="background: #334155; color: #f8fafc; font-weight: 700; border-color: #475569; padding: 0.6rem 1.25rem; font-size: 0.88rem; cursor: pointer;">
              🖨️ Imprimir / Guardar como PDF
            </button>
            <button class="btn-print" id="btnToggleRealSolucion" onclick="realExamToggleSolucion()" style="background: rgba(16, 185, 129, 0.15); color: #34d399; font-weight: 700; border: 1px solid #10b981; padding: 0.6rem 1.25rem; font-size: 0.88rem; cursor: pointer;">
              👁️ Revelar Solución &amp; Criterios
            </button>
          </div>

          <!-- CRONÓMETRO DE EXAMEN (45 MINUTOS) -->
          <div style="display: flex; align-items: center; gap: 0.75rem; background: #070a13; border: 1px solid #334155; border-radius: 6px; padding: 0.4rem 1rem;">
            <span style="font-size: 0.8rem; color: #94a3b8; font-weight: 700;">⏱️ TIEMPO:</span>
            <span id="realExamTimerDisplay" style="font-family: 'Fira Code', monospace; font-size: 1.25rem; font-weight: 800; color: #f59e0b;">45:00</span>
            <div style="display: flex; gap: 0.3rem;">
              <button onclick="realExamStartTimer()" title="Iniciar cronómetro" style="background: #10b981; color: #022c22; border: none; border-radius: 3px; padding: 0.2rem 0.5rem; font-size: 0.75rem; font-weight: 700; cursor: pointer;">▶</button>
              <button onclick="realExamPauseTimer()" title="Pausar cronómetro" style="background: #eab308; color: #422006; border: none; border-radius: 3px; padding: 0.2rem 0.5rem; font-size: 0.75rem; font-weight: 700; cursor: pointer;">⏸</button>
              <button onclick="realExamResetTimer()" title="Reiniciar 45 min" style="background: #ef4444; color: #fff; border: none; border-radius: 3px; padding: 0.2rem 0.5rem; font-size: 0.75rem; font-weight: 700; cursor: pointer;">↺</button>
            </div>
          </div>

        </div>

        <!-- HOJA DE EXAMEN FORMAL UAGRM (DISEÑADA PARA PANTALLA E IMPRESIÓN) -->
        <div id="examSheetPrintable" class="exam-paper" style="background: #ffffff; color: #0f172a; border-radius: 8px; padding: 2.5rem; box-shadow: 0 10px 25px rgba(0,0,0,0.3); font-family: 'Segoe UI', Arial, sans-serif;">
          
          <!-- MEMBRETE UNIVERSITARIO FORMAL -->
          <div style="border-bottom: 2px solid #0f172a; padding-bottom: 1rem; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
              <h2 style="margin: 0; font-size: 1.15rem; font-weight: 900; color: #0f172a; text-transform: uppercase;">UNIVERSIDAD AUTÓNOMA GABRIEL RENÉ MORENO</h2>
              <div style="font-size: 0.95rem; font-weight: 700; color: #334155;">FACULTAD DE CIENCIAS DE LA COMPUTACIÓN Y TELECOMUNICACIONES</div>
              <div style="font-size: 0.88rem; color: #475569;">MATERIA: INTRODUCCIÓN A LA INFORMÁTICA (INF110 - GRUPO Z2)</div>
              <div style="font-size: 0.88rem; color: #475569;">DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar • Semestre 2-2025 / 2-2026</div>
            </div>
            <div style="text-align: right;">
              <span id="realExamNumBadge" style="display: inline-block; background: #0f172a; color: #fff; font-weight: 900; font-size: 0.88rem; padding: 0.35rem 0.85rem; border-radius: 4px; text-transform: uppercase;">
                PARCIAL MODELO #1
              </span>
              <div style="font-size: 0.82rem; color: #64748b; margin-top: 0.3rem;">Ponderación: 100 Puntos</div>
            </div>
          </div>

          <!-- DATOS DEL ESTUDIANTE A RELLENAR A MANO -->
          <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 1rem; border: 1px solid #cbd5e1; border-radius: 4px; padding: 0.75rem 1rem; margin-bottom: 1.5rem; font-size: 0.88rem;">
            <div><strong>Apellidos y Nombres:</strong> ___________________________________________</div>
            <div><strong>Registro U.:</strong> _______________</div>
            <div><strong>Firma:</strong> _______________</div>
          </div>

          <!-- INSTRUCCIONES FORMALES DEL EXAMEN -->
          <div style="background: #f8fafc; border-left: 4px solid #0f172a; padding: 0.6rem 1rem; margin-bottom: 1.5rem; font-size: 0.82rem; color: #334155; line-height: 1.5;">
            <strong>INSTRUCCIONES:</strong> Lea con atención cada enunciado. Debe aplicar la <strong>Programación Modular obligatoria</strong> (Funciones o Procedimientos). En Cadenas es obligatorio emplear la firma <code>(cad: string; n, i: byte)</code> con recorrido <code>while i &lt;= n</code>. Entregar el análisis, algoritmo en pseudocódigo o Pascal, y la prueba de escritorio correspondiente.
          </div>

          <!-- CUERPO DE LAS 3 PREGUNTAS DEL EXAMEN -->
          <div id="realExamQuestionsContainer">
            <!-- Contenido inyectado dinámicamente por JS -->
          </div>

        </div>

      </div>
    </div>

  </section>
  <!-- FIN SECCIÓN PRÁCTICA ACTIVA -->
''')

    return '\n'.join(out)

if __name__ == '__main__':
    print("Módulo generador de Práctica Activa compilado con éxito.")
