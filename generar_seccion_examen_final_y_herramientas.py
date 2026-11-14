# -*- coding: utf-8 -*-
"""
Generador de las 2 nuevas secciones maestras para teoria_programacion_modular.html:
1. 'examen-final-oficial': Recreación interactiva oficial del Examen Final Real 2-2020 (40/40 Ptos)
   de la M.Sc. Ing. Angélica Garzón Cuéllar.
2. 'series-y-herramientas': Laboratorio de Series Numéricas, Generador de Pruebas de Escritorio
   en Vivo y la Plantilla Metodológica de los 5 Pasos FICCT.
"""

def build_examen_final_html():
    return r'''
  <!-- =========================================================================== -->
  <!-- SECCIÓN: EXAMEN FINAL REAL OFICIAL 2-2020 (40/40 PTOS) - ING. ANGÉLICA GARZÓN -->
  <!-- =========================================================================== -->
  <section id="examen-final-oficial" class="section-content">
    <div class="card">

      <!-- ENCABEZADO DEL EXAMEN OFICIAL -->
      <div style="background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98)); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: var(--radius-md); padding: 1.6rem 1.8rem; margin-bottom: 2rem; box-shadow: 0 4px 25px rgba(0,0,0,0.4);">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:1rem;">
          <div style="display:flex; align-items:center; gap:0.85rem;">
            <span style="font-size:2.2rem;">🏆</span>
            <div>
              <h2 style="color:#fff; margin:0; font-size:1.4rem; font-weight:800; letter-spacing:-0.02em;">
                Examen Final Oficial (40 Ptos) • Semestre 2-2020
              </h2>
              <span style="font-size:0.85rem; color:#f59e0b; font-weight:600;">
                M.Sc. Ing. Angélica Garzón Cuéllar • INF110-SI / INF110-Z2 • UAGRM
              </span>
            </div>
          </div>
          <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
            <span class="badge" style="background:rgba(16,185,129,0.2); color:#10b981; border-color:rgba(16,185,129,0.4); font-size:0.85rem; padding:0.4rem 0.8rem;">
              ⭐ CALIFICACIÓN: 40,00 / 40,00 (100%)
            </span>
            <span class="badge" style="background:rgba(56,189,248,0.15); color:#38bdf8; border-color:rgba(56,189,248,0.3); font-size:0.85rem; padding:0.4rem 0.8rem;">
              ⏱️ TIEMPO: 1h 08m
            </span>
          </div>
        </div>
        <p style="color:#cbd5e1; font-size:0.92rem; margin:0; line-height:1.6;">
          Reconstrucción interactiva fiel del examen final oficial extraído del sistema virtual de la facultad. Incluye resolución explicada, demostración matemática, análisis crítico de trampas de examen y simuladores Delphi interactivos para cada una de las <strong>7 preguntas</strong>.
        </p>
      </div>

      <!-- NAVEGACIÓN RÁPIDA DE PREGUNTAS -->
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
        <a href="#ef-p1" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P1: Precedencia (4p)</a>
        <a href="#ef-p2" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P2: Constantes (3p)</a>
        <a href="#ef-p3" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P3: Tipos de Datos (3p)</a>
        <a href="#ef-p4" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P4: Serie Triangular (5p)</a>
        <a href="#ef-p5" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P5: Dígitos Pares (10p)</a>
        <a href="#ef-p6" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P6: Valor Absoluto (5p)</a>
        <a href="#ef-p7" class="btn-print" style="text-decoration:none; font-size:0.8rem;">P7: Vacunación COVID (10p)</a>
      </div>

      <!-- =====================================================================
           PREGUNTA 1: PRECEDENCIA DE OPERADORES (4 PTOS)
           ===================================================================== -->
      <div id="ef-p1" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #38bdf8; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#38bdf8; margin:0; font-size:1.15rem;">📌 Pregunta 1: Evaluación de Expresiones Aritméticas</h3>
          <span style="background:rgba(56,189,248,0.15); color:#38bdf8; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">4,00 / 4,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:1rem;">
          <strong>Enunciado oficial:</strong> Evaluar la siguiente expresión aritmética respetando la jerarquía de operadores:
          <br>
          <code style="background:#0b1120; color:#fbbf24; font-size:1.1rem; padding:0.3rem 0.7rem; border-radius:6px; display:inline-block; margin-top:0.4rem; font-family:'Fira Code',monospace;">
            (2 + 1)^2 / 3 - (2^2 - 3)
          </code>
        </p>

        <!-- Opciones del examen -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:0.6rem; margin-bottom:1rem;">
          <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:6px; padding:0.6rem; text-align:center; color:#10b981; font-weight:700; font-family:'Fira Code',monospace;">
            a) 2 ✅ (Correcta)
          </div>
          <div style="background:rgba(15,23,42,0.6); border:1px solid #334155; border-radius:6px; padding:0.6rem; text-align:center; color:#94a3b8; font-family:'Fira Code',monospace;">
            b) 3
          </div>
          <div style="background:rgba(15,23,42,0.6); border:1px solid #334155; border-radius:6px; padding:0.6rem; text-align:center; color:#94a3b8; font-family:'Fira Code',monospace;">
            c) 1
          </div>
          <div style="background:rgba(15,23,42,0.6); border:1px solid #334155; border-radius:6px; padding:0.6rem; text-align:center; color:#94a3b8; font-family:'Fira Code',monospace;">
            d) 6
          </div>
        </div>

        <!-- Desglose paso a paso -->
        <div style="background:#070a13; border:1px dashed #334155; border-radius:6px; padding:1rem; font-family:'Fira Code',monospace; font-size:0.84rem; color:#cbd5e1; line-height:1.7;">
          <span style="color:#64748b;">// RESOLUCIÓN PASO A PASO SEGÚN JERARQUÍA OFICIAL UAGRM:</span><br>
          1. Paréntesis izquierdo: (2 + 1) = 3<br>
          2. Potencia izquierda: 3^2 = 9<br>
          3. División izquierda: 9 / 3 = 3<br>
          4. Paréntesis derecho: (2^2 - 3) = (4 - 3) = 1<br>
          5. Resta final: 3 - 1 = <strong style="color:#10b981; font-size:1.1rem;">2</strong>
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 2: CONSTANTES (3 PTOS)
           ===================================================================== -->
      <div id="ef-p2" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #10b981; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#10b981; margin:0; font-size:1.15rem;">📌 Pregunta 2: Concepto Fundamental de Constante</h3>
          <span style="background:rgba(16,185,129,0.15); color:#10b981; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">3,00 / 3,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:0.8rem;">
          <strong>Enunciado oficial:</strong> <em>"Una constante no cambia su valor durante la ejecución de un programa"</em>
        </p>
        <div style="display:flex; gap:1rem; margin-bottom:1rem;">
          <div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; border-radius:6px; padding:0.6rem 1.2rem; color:#10b981; font-weight:700;">
            VERDADERO ✅ (Respuesta Correcta)
          </div>
          <div style="background:rgba(15,23,42,0.6); border:1px solid #334155; border-radius:6px; padding:0.6rem 1.2rem; color:#64748b; text-decoration:line-through;">
            Falso
          </div>
        </div>
        <div style="background:#070a13; border-radius:6px; padding:0.9rem; font-size:0.85rem; color:#94a3b8; line-height:1.6;">
          <strong style="color:#38bdf8;">En Pascal / Delphi:</strong> Se declaran en la sección <code>const</code> (ejemplo: <code>const PI = 3.141592; MAX = 100;</code>). El compilador asigna un espacio de memoria de solo lectura. Cualquier intento de asignación como <code>PI := 3.14;</code> generará error de compilación: <em>"Left side cannot be assigned to"</em>.
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 3: CLASIFICACIÓN DE TIPOS DE DATOS (3 PTOS)
           ===================================================================== -->
      <div id="ef-p3" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #a855f7; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#a855f7; margin:0; font-size:1.15rem;">📌 Pregunta 3: Clasificación Exacta de Tipos de Datos</h3>
          <span style="background:rgba(168,85,247,0.15); color:#c084fc; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">3,00 / 3,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:1rem;">
          <strong>Enunciado oficial:</strong> Indicar a qué tipo de dato pertenece cada uno de los siguientes valores:
        </p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:0.8rem; margin-bottom:1rem;">
          <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:0.8rem;">
            <div style="font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Dato evaluado:</div>
            <code style="color:#fbbf24; font-size:1rem; font-family:'Fira Code',monospace;">'Ing. de Sistemas'</code>
            <div style="margin-top:0.5rem; color:#38bdf8; font-weight:700; font-size:0.88rem;">➜ String (Cadena)</div>
          </div>
          <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:0.8rem;">
            <div style="font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Dato evaluado:</div>
            <code style="color:#fbbf24; font-size:1rem; font-family:'Fira Code',monospace;">6,96 (Tipo de cambio)</code>
            <div style="margin-top:0.5rem; color:#10b981; font-weight:700; font-size:0.88rem;">➜ Real / Double</div>
          </div>
          <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:0.8rem;">
            <div style="font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Dato evaluado:</div>
            <code style="color:#fbbf24; font-size:1rem; font-family:'Fira Code',monospace;">70 (Nota Final)</code>
            <div style="margin-top:0.5rem; color:#f59e0b; font-weight:700; font-size:0.88rem;">➜ Integer / Word</div>
          </div>
          <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:0.8rem;">
            <div style="font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Dato evaluado:</div>
            <code style="color:#fbbf24; font-size:1rem; font-family:'Fira Code',monospace;">'M' (Sexo)</code>
            <div style="margin-top:0.5rem; color:#ec4899; font-weight:700; font-size:0.88rem;">➜ Char (Carácter)</div>
          </div>
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 4: PRUEBA DE ESCRITORIO DE LA SERIE (5 PTOS)
           ===================================================================== -->
      <div id="ef-p4" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #f59e0b; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#f59e0b; margin:0; font-size:1.15rem;">📌 Pregunta 4: Prueba de Escritorio de Serie (5 Términos)</h3>
          <span style="background:rgba(245,158,11,0.15); color:#fbbf24; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">5,00 / 5,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:1rem;">
          <strong>Enunciado oficial:</strong> Realizar la prueba de escritorio para 5 términos de la serie generada en el diagrama de flujo:
          <br>
          <span style="color:#10b981; font-weight:700; font-family:'Fira Code',monospace; font-size:1.1rem;">
            Respuesta: 1, 3, 6, 10, 15
          </span>
        </p>

        <!-- Tabla de traza oficial -->
        <div style="overflow-x:auto; margin-bottom:1rem;">
          <table style="width:100%; border-collapse:collapse; font-size:0.85rem; font-family:'Fira Code',monospace;">
            <thead>
              <tr style="background:rgba(245,158,11,0.15); color:#f59e0b;">
                <th style="padding:0.5rem; text-align:center; border:1px solid #334155;">Término (i)</th>
                <th style="padding:0.5rem; text-align:center; border:1px solid #334155;">Incremento (d)</th>
                <th style="padding:0.5rem; text-align:center; border:1px solid #334155;">Cálculo (t := t + d)</th>
                <th style="padding:0.5rem; text-align:center; border:1px solid #334155;">Salida de Pantalla</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">1</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">— (Inicial)</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">t := 1</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">1</td>
              </tr>
              <tr>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">2</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">+ 2</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">1 + 2 = 3</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">3</td>
              </tr>
              <tr>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">3</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">+ 3</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">3 + 3 = 6</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">6</td>
              </tr>
              <tr>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">4</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">+ 4</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">6 + 4 = 10</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">10</td>
              </tr>
              <tr>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">5</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">+ 5</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">10 + 5 = 15</td>
                <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">15</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div style="font-size:0.83rem; color:#94a3b8;">
          💡 <strong>Nombre matemático:</strong> Serie de Números Triangulares. Fórmula directa: <code>T(n) = n * (n + 1) div 2</code>.
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 5: DÍGITOS PARES Y LA TRAMPA DEL WHILE (10 PTOS)
           ===================================================================== -->
      <div id="ef-p5" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #f43f5e; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#f43f5e; margin:0; font-size:1.15rem;">📌 Pregunta 5: La Gran Trampa — Conteo de Dígitos Pares</h3>
          <span style="background:rgba(244,63,94,0.15); color:#fb7185; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">10,00 / 10,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:1rem;">
          <strong>Enunciado oficial:</strong> <em>"Elegir el código correcto en Pascal para contar la cantidad de dígitos pares de un número ingresado."</em>
          <br>
          <span style="color:#fb7185; font-size:0.88rem;">⚠️ Esta pregunta definió la aprobación del examen. Dos opciones tenían errores críticos que provocan bucle infinito o resultados erróneos.</span>
        </p>

        <!-- Comparador de los 3 códigos -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem; margin-bottom:1.2rem;">
          
          <!-- Opción A -->
          <div style="background:rgba(244,63,94,0.06); border:1px solid rgba(244,63,94,0.3); border-radius:6px; padding:1rem; font-size:0.8rem;">
            <div style="color:#f43f5e; font-weight:700; margin-bottom:0.4rem;">❌ Opción (a) — ERROR LÓGICO</div>
            <p style="color:#94a3b8; font-size:0.78rem; margin-bottom:0.5rem;">No tiene ningún <code>if</code>. Incrementa <code>pares</code> con cada dígito, contando pares E impares.</p>
            <div class="code-block" style="font-size:0.75rem; padding:0.5rem;">
while numero > 0 do<br>
begin<br>
&nbsp;&nbsp;dig := numero mod 10;<br>
&nbsp;&nbsp;<span style="color:#f43f5e; font-weight:700;">pares := pares + 1; // ❌ Sin condición</span><br>
&nbsp;&nbsp;numero := numero div 10;<br>
end;
            </div>
          </div>

          <!-- Opción B -->
          <div style="background:rgba(244,63,94,0.06); border:1px solid rgba(244,63,94,0.3); border-radius:6px; padding:1rem; font-size:0.8rem;">
            <div style="color:#f43f5e; font-weight:700; margin-bottom:0.4rem;">❌ Opción (b) — BUCLE INFINITO</div>
            <p style="color:#94a3b8; font-size:0.78rem; margin-bottom:0.5rem;">Coloca <code>numero := numero div 10;</code> dentro del <code>else</code>. Si el dígito es par, <strong>nunca se reduce el número</strong> y se congela el programa.</p>
            <div class="code-block" style="font-size:0.75rem; padding:0.5rem;">
if (dig mod 2) = 0 then<br>
&nbsp;&nbsp;pares := pares + 1<br>
else<br>
&nbsp;&nbsp;<span style="color:#f43f5e; font-weight:700;">numero := numero div 10; // ❌ Traba el programa</span>
            </div>
          </div>

          <!-- Opción C -->
          <div style="background:rgba(16,185,129,0.08); border:1px solid #10b981; border-radius:6px; padding:1rem; font-size:0.8rem;">
            <div style="color:#10b981; font-weight:700; margin-bottom:0.4rem;">✅ Opción (c) — CORRECTA (10/10)</div>
            <p style="color:#cbd5e1; font-size:0.78rem; margin-bottom:0.5rem;">La condición <code>if</code> filtra pares, y <code>numero := numero div 10;</code> se ejecuta <strong>SIEMPRE</strong> al final de cada iteración.</p>
            <div class="code-block" style="font-size:0.75rem; padding:0.5rem;">
while numero > 0 do<br>
begin<br>
&nbsp;&nbsp;dig := numero mod 10;<br>
&nbsp;&nbsp;<span style="color:#10b981;">if (dig mod 2) = 0 then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#10b981;">pares := pares + 1;</span><br>
&nbsp;&nbsp;<span style="color:#38bdf8; font-weight:700;">numero := numero div 10; // ✅ Siempre se reduce</span><br>
end;
            </div>
          </div>

        </div>

        <!-- Demostrador interactivo -->
        <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:1rem;">
          <div style="display:flex; gap:0.8rem; align-items:center; flex-wrap:wrap; margin-bottom:0.6rem;">
            <label style="color:#cbd5e1; font-size:0.85rem; font-weight:600;">Probar Opción Correcta (c):</label>
            <input type="number" id="efP5Input" value="2468135" style="padding:0.45rem 0.8rem; background:#0b1120; border:1px solid #334155; border-radius:6px; color:#fff; font-family:'Fira Code',monospace; width:160px;">
            <button class="btn-print" onclick="efProbarDigitosPares()" style="background:#10b981; color:#0b1120; font-weight:bold;">▶ Ejecutar Código</button>
          </div>
          <div id="efP5Result" style="color:#10b981; font-family:'Fira Code',monospace; font-size:0.9rem; font-weight:700;"></div>
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 6: FUNCIÓN VALOR ABSOLUTO (5 PTOS)
           ===================================================================== -->
      <div id="ef-p6" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #38bdf8; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#38bdf8; margin:0; font-size:1.15rem;">📌 Pregunta 6: Función Valor Absoluto en Pascal</h3>
          <span style="background:rgba(56,189,248,0.15); color:#38bdf8; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">5,00 / 5,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:0.8rem;">
          <strong>Enunciado oficial:</strong> Crear una función en Pascal que devuelva el valor absoluto de un número entero dado:
          <br>
          <code>X := ValorAbsoluto(-5); // Retorna 5</code> &nbsp;|&nbsp; <code>X := ValorAbsoluto(10); // Retorna 10</code>
        </p>

        <div class="code-block" style="font-size:0.82rem; margin-bottom:1rem;">
<span style="color:#60a5fa;">function</span> <span style="color:#f59e0b;">ValorAbsoluto</span>(Numero: <span style="color:#34d399;">Integer</span>): <span style="color:#34d399;">Integer</span>;<br>
<span style="color:#60a5fa;">begin</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> Numero &lt; <span style="color:#f59e0b;">0</span> <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;ValorAbsoluto := Numero * (<span style="color:#f59e0b;">-1</span>)<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;ValorAbsoluto := Numero;<br>
<span style="color:#60a5fa;">end</span>;
        </div>

        <div style="display:flex; gap:0.8rem; align-items:center; flex-wrap:wrap;">
          <input type="number" id="efP6Input" value="-42" style="padding:0.45rem 0.8rem; background:#0b1120; border:1px solid #334155; border-radius:6px; color:#fff; font-family:'Fira Code',monospace; width:120px;">
          <button class="btn-print" onclick="efProbarValorAbsoluto()" style="background:#38bdf8; color:#0b1120; font-weight:bold;">▶ Calcular ValorAbsoluto</button>
          <div id="efP6Result" style="color:#38bdf8; font-family:'Fira Code',monospace; font-size:0.9rem; font-weight:700;"></div>
        </div>
      </div>

      <!-- =====================================================================
           PREGUNTA 7: PROBLEMA COVID-19 MAYORES A 60 AÑOS (10 PTOS)
           ===================================================================== -->
      <div id="ef-p7" style="background:rgba(15,23,42,0.8); border:1px solid var(--border-color); border-left:4px solid #10b981; border-radius:var(--radius-sm); padding:1.4rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
          <h3 style="color:#10b981; margin:0; font-size:1.15rem;">📌 Pregunta 7: Problema de Desarrollo — Vacunación COVID-19</h3>
          <span style="background:rgba(16,185,129,0.15); color:#10b981; padding:0.25rem 0.65rem; border-radius:999px; font-size:0.78rem; font-weight:700;">10,00 / 10,00 PUNTOS</span>
        </div>
        <p style="color:#f8fafc; font-size:0.95rem; margin-bottom:1rem; line-height:1.6;">
          <strong>Enunciado oficial de examen:</strong> <em>"Diseñar y codificar un programa que permita leer el nombre y la edad de N personas y muestre aquellas personas que tienen una edad mayor a 60 años para ser vacunadas contra el COVID-19 y además el promedio de edad de este grupo de personas."</em>
        </p>

        <!-- Simulador interactivo en vivo -->
        <div style="background:#070a13; border:1px solid #334155; border-radius:6px; padding:1.2rem; margin-bottom:1.2rem;">
          <h4 style="color:#38bdf8; margin:0 0 0.8rem 0; font-size:0.95rem;">🏥 Simulador Delphi del Sistema de Vacunación:</h4>
          
          <div style="display:grid; grid-template-columns:1fr 120px auto; gap:0.6rem; margin-bottom:0.8rem; align-items:flex-end;">
            <div>
              <label style="display:block; font-size:0.78rem; color:#94a3b8; margin-bottom:0.25rem;">Nombre de la persona:</label>
              <input type="text" id="efCovidNombre" placeholder="Ej: Don Roberto Gomez" style="width:100%; padding:0.45rem 0.7rem; background:#0b1120; border:1px solid #334155; border-radius:6px; color:#fff; font-size:0.85rem;">
            </div>
            <div>
              <label style="display:block; font-size:0.78rem; color:#94a3b8; margin-bottom:0.25rem;">Edad:</label>
              <input type="number" id="efCovidEdad" placeholder="Ej: 68" min="1" max="120" style="width:100%; padding:0.45rem 0.7rem; background:#0b1120; border:1px solid #334155; border-radius:6px; color:#fff; font-size:0.85rem;">
            </div>
            <button class="btn-print" onclick="efCovidAgregarPersona()" style="background:#10b981; color:#0b1120; font-weight:bold; height:36px;">+ Registrar</button>
          </div>

          <!-- Botones de ejemplo rápido -->
          <div style="display:flex; gap:0.5rem; margin-bottom:1rem; flex-wrap:wrap;">
            <button class="btn-print" onclick="efCovidCargarEjemplo()" style="font-size:0.78rem;">📥 Cargar Datos de Prueba de la Docente</button>
            <button class="btn-print" onclick="efCovidLimpiar()" style="font-size:0.78rem;">🗑️ Limpiar Lista</button>
          </div>

          <!-- Resultados y lista -->
          <div id="efCovidSalida" style="background:#0b1120; border:1px solid #1e293b; border-radius:6px; padding:0.9rem; font-family:'Fira Code',monospace; font-size:0.82rem; min-height:80px; color:#cbd5e1;">
            <div style="color:#64748b;">// LISTA DE PERSONAS Y FILTRO DE VACUNACIÓN APARECERÁ AQUÍ...</div>
          </div>
        </div>

        <!-- Código Pascal modular completo -->
        <div style="background:#0b1120; border:1px solid #334155; border-radius:6px; padding:1.2rem;">
          <div style="color:#38bdf8; font-weight:700; font-size:0.9rem; margin-bottom:0.6rem;">💻 Solución Modular Oficial en Pascal / Delphi:</div>
          <div class="code-block" style="font-size:0.8rem; line-height:1.7;">
<span style="color:#60a5fa;">procedure</span> <span style="color:#f59e0b;">TForm1.BtnProcesarVacunacionClick</span>(Sender: TObject);<br>
<span style="color:#60a5fa;">var</span><br>
&nbsp;&nbsp;n, i, edad, cVacunados, sumaEdades: <span style="color:#34d399;">Integer</span>;<br>
&nbsp;&nbsp;nombre, reporte: <span style="color:#34d399;">String</span>;<br>
&nbsp;&nbsp;promedio: <span style="color:#34d399;">Real</span>;<br>
<span style="color:#60a5fa;">begin</span><br>
&nbsp;&nbsp;n := StrToInt(InputBox(<span style="color:#f87171;">'Registro COVID'</span>, <span style="color:#f87171;">'¿Cuántas personas desea registrar?'</span>, <span style="color:#f87171;">'3'</span>));<br>
&nbsp;&nbsp;cVacunados := <span style="color:#f59e0b;">0</span>;<br>
&nbsp;&nbsp;sumaEdades := <span style="color:#f59e0b;">0</span>;<br>
&nbsp;&nbsp;reporte := <span style="color:#f87171;">'PERSONAS APTAS PARA VACUNACIÓN (> 60 AÑOS):'</span> + #13#10;<br>
<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">for</span> i := <span style="color:#f59e0b;">1</span> <span style="color:#60a5fa;">to</span> n <span style="color:#60a5fa;">do</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;nombre := InputBox(<span style="color:#f87171;">'Datos'</span>, <span style="color:#f87171;">'Nombre persona '</span> + IntToStr(i) + <span style="color:#f87171;">':'</span>, <span style="color:#f87171;">''</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;edad := StrToInt(InputBox(<span style="color:#f87171;">'Datos'</span>, <span style="color:#f87171;">'Edad de '</span> + nombre + <span style="color:#f87171;">':'</span>, <span style="color:#f87171;">'0'</span>));<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> edad &gt; <span style="color:#f59e0b;">60</span> <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#60a5fa;">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cVacunados := cVacunados + <span style="color:#f59e0b;">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sumaEdades := sumaEdades + edad;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reporte := reporte + <span style="color:#f87171;">'• '</span> + nombre + <span style="color:#f87171;">' ('</span> + IntToStr(edad) + <span style="color:#f87171;">' años)'</span> + #13#10;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#60a5fa;">end</span>;<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">end</span>;<br>
<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> cVacunados &gt; <span style="color:#f59e0b;">0</span> <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;promedio := sumaEdades / cVacunados;<br>
&nbsp;&nbsp;&nbsp;&nbsp;reporte := reporte + #13#10 + <span style="color:#f87171;">'Total vacunados: '</span> + IntToStr(cVacunados) + #13#10 +<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f87171;">'Promedio de edad: '</span> + FloatToStrF(promedio, ffFixed, <span style="color:#f59e0b;">5</span>, <span style="color:#f59e0b;">2</span>) + <span style="color:#f87171;">' años'</span>;<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">end</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;reporte := reporte + <span style="color:#f87171;">'No hubo ninguna persona mayor a 60 años.'</span>;<br>
<br>
&nbsp;&nbsp;Memo1.Lines.Text := reporte;<br>
<span style="color:#60a5fa;">end</span>;
          </div>
        </div>

      </div>

    </div>
  </section>
  <!-- =========================================================================== -->
  <!-- FIN SECCIÓN: EXAMEN FINAL REAL OFICIAL                                     -->
  <!-- =========================================================================== -->
'''

def build_series_y_herramientas_html():
    return r'''
  <!-- =========================================================================== -->
  <!-- SECCIÓN: SERIES NUMÉRICAS, GENERADOR DE TRAZA & 5 PASOS                     -->
  <!-- =========================================================================== -->
  <section id="series-y-herramientas" class="section-content">
    <div class="card">

      <!-- ENCABEZADO -->
      <div class="header-top-actions" style="margin-bottom: 1.5rem;">
        <div>
          <h2 class="card-title" style="margin-bottom: 0.25rem;">📈 Laboratorio de Series, Generador de Traza &amp; Los 5 Pasos</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">
            Metodología oficial de resolución y trazado de la <strong>M.Sc. Ing. Angélica Garzón Cuéllar</strong> (INF110)
          </p>
        </div>
        <span class="badge" style="background:rgba(56,189,248,.15);color:#38bdf8;border-color:rgba(56,189,248,.3);">
          ⚡ HERRAMIENTAS INTERACTIVAS
        </span>
      </div>

      <!-- ÍNDICE DE HERRAMIENTAS -->
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
        <a href="#lab-5pasos" class="btn-print" style="text-decoration:none; font-size:0.82rem;">🎯 1. La Plantilla de los 5 Pasos</a>
        <a href="#lab-generador-traza" class="btn-print" style="text-decoration:none; font-size:0.82rem;">🔬 2. Generador de Traza en Vivo</a>
        <a href="#lab-catalogo-series" class="btn-print" style="text-decoration:none; font-size:0.82rem;">📊 3. Catálogo de 5 Series de Examen</a>
      </div>

      <!-- =====================================================================
           BLOQUE 1: LA PLANTILLA DE LOS 5 PASOS (TAREA #3 & EXÁMENES)
           ===================================================================== -->
      <div id="lab-5pasos" style="background:rgba(15,23,42,0.85); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:1.5rem; margin-bottom:2rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <h3 style="color:#f59e0b; margin:0; font-size:1.25rem; display:flex; align-items:center; gap:0.5rem;">
            <span>🎯</span> 1. La Metodología de los 5 Pasos para Sacar 100/100
          </h3>
          <span style="background:rgba(245,158,11,0.15); color:#fbbf24; font-size:0.75rem; padding:0.2rem 0.6rem; border-radius:999px; font-weight:700;">
            MÉTODO OFICIAL FICCT
          </span>
        </div>
        <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1.2rem; line-height:1.6;">
          Para obtener la máxima calificación en las revisiones de la docente, cada problema debe desarrollarse obligatoriamente bajo esta estructura de 5 etapas:
        </p>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem;">
          
          <div style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1rem;">
            <div style="color:#38bdf8; font-weight:800; font-size:0.95rem; margin-bottom:0.4rem;">Paso 1: Análisis Formal</div>
            <ul style="color:#cbd5e1; font-size:0.82rem; margin:0; padding-left:1.2rem; line-height:1.6;">
              <li><strong>Entrada:</strong> Variables, significado y tipo de dato exacto (<code>n: Cardinal</code>).</li>
              <li><strong>Proceso:</strong> Lógica matemática (descomposición con <code>mod 10</code> y <code>div 10</code>).</li>
              <li><strong>Salida:</strong> Resultado esperado (tipo y valor).</li>
            </ul>
          </div>

          <div style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1rem;">
            <div style="color:#10b981; font-weight:800; font-size:0.95rem; margin-bottom:0.4rem;">Paso 2: Diseño Modular</div>
            <ul style="color:#cbd5e1; font-size:0.82rem; margin:0; padding-left:1.2rem; line-height:1.6;">
              <li>Decidir si es <strong>Función</strong> (si devuelve un único valor escalar) o <strong>Procedimiento</strong> (si modifica o muestra).</li>
              <li>Definir la firma: <code>function SumarPrimos(num: Word): Word;</code></li>
            </ul>
          </div>

          <div style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1rem;">
            <div style="color:#a855f7; font-weight:800; font-size:0.95rem; margin-bottom:0.4rem;">Paso 3: Pseudocódigo FICCT</div>
            <ul style="color:#cbd5e1; font-size:0.82rem; margin:0; padding-left:1.2rem; line-height:1.6;">
              <li>Estructura formal con <code>Funcion / FinFuncion</code>.</li>
              <li>Asignación con flecha: <code>suma &lt;- 0</code>.</li>
              <li>Bucles en español: <code>Mientras n &gt; 0 Hacer ... FinMientras</code>.</li>
            </ul>
          </div>

          <div style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1rem;">
            <div style="color:#f43f5e; font-weight:800; font-size:0.95rem; margin-bottom:0.4rem;">Paso 4: Prueba de Escritorio</div>
            <ul style="color:#cbd5e1; font-size:0.82rem; margin:0; padding-left:1.2rem; line-height:1.6;">
              <li>Tabla con columnas para cada variable y condición de control.</li>
              <li>Mínimo 3 a 5 filas con datos representativos del problema.</li>
              <li>Comprobación final del valor de retorno.</li>
            </ul>
          </div>

          <div style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1rem;">
            <div style="color:#fbbf24; font-weight:800; font-size:0.95rem; margin-bottom:0.4rem;">Paso 5: Código en Delphi Form</div>
            <ul style="color:#cbd5e1; font-size:0.82rem; margin:0; padding-left:1.2rem; line-height:1.6;">
              <li>Implementación modular en archivo <code>.pas</code>.</li>
              <li>Llamada correcta desde evento <code>ButtonXClick</code>.</li>
              <li>Conversión de entrada (<code>StrToInt</code>) y salida (<code>IntToStr</code>).</li>
            </ul>
          </div>

        </div>
      </div>

      <!-- =====================================================================
           BLOQUE 2: GENERADOR INTERACTIVO DE PRUEBAS DE ESCRITORIO
           ===================================================================== -->
      <div id="lab-generador-traza" style="background:rgba(15,23,42,0.85); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:1.5rem; margin-bottom:2rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <h3 style="color:#10b981; margin:0; font-size:1.25rem; display:flex; align-items:center; gap:0.5rem;">
            <span>🔬</span> 2. Generador Automático de Pruebas de Escritorio (Live Trace Table)
          </h3>
          <span style="background:rgba(16,185,129,0.15); color:#10b981; font-size:0.75rem; padding:0.2rem 0.6rem; border-radius:999px; font-weight:700;">
            PIZARRA VIRTUAL FICCT
          </span>
        </div>
        <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1.2rem;">
          Ingresa un número natural o frase y selecciona un algoritmo. El sistema dibujará al instante la tabla completa de prueba de escritorio con todas las variables, condiciones y estados iteración por iteración:
        </p>

        <!-- Controles del generador -->
        <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1.2rem;">
          <div style="flex:1; min-width:200px;">
            <label style="display:block; font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Dato de entrada:</label>
            <input type="text" id="genTrazaInput" value="2374" style="width:100%; padding:0.55rem 0.8rem; background:#070a13; border:1px solid #334155; border-radius:6px; color:#fff; font-family:'Fira Code',monospace; font-size:1rem;">
          </div>
          <div style="flex:1.5; min-width:260px;">
            <label style="display:block; font-size:0.8rem; color:#94a3b8; margin-bottom:0.3rem;">Algoritmo de examen a trazar:</label>
            <select id="genTrazaAlgo" style="width:100%; padding:0.55rem 0.8rem; background:#070a13; border:1px solid #334155; border-radius:6px; color:#fff; font-size:0.88rem;">
              <option value="sumar_primos">Sumar Dígitos Primos (Tarea #3 Oficial: n=2374)</option>
              <option value="contar_pares">Contar Dígitos Pares (Examen Final Oficial)</option>
              <option value="invertir_numero">Invertir Número Natural (Base 10)</option>
              <option value="sumar_digitos">Sumatoria de Dígitos</option>
              <option value="contar_vocales">Cadenas: Contar Vocales</option>
              <option value="contar_palabras">Cadenas: Algoritmo Maestro de Palabras</option>
            </select>
          </div>
          <div style="display:flex; align-items:flex-end;">
            <button class="btn-print" onclick="generarTrazaEnVivo()" style="background:#10b981; color:#0b1120; font-weight:bold; height:38px;">
              ⚡ Generar Tabla de Prueba
            </button>
          </div>
        </div>

        <!-- Tabla renderizada -->
        <div id="genTrazaResultado" style="overflow-x:auto;">
          <!-- Se inyecta dinámicamente -->
        </div>
      </div>

      <!-- =====================================================================
           BLOQUE 3: CATÁLOGO DE 5 SERIES CLÁSICAS DE EXAMEN
           ===================================================================== -->
      <div id="lab-catalogo-series" style="background:rgba(15,23,42,0.85); border:1px solid var(--border-color); border-radius:var(--radius-md); padding:1.5rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <h3 style="color:#38bdf8; margin:0; font-size:1.25rem; display:flex; align-items:center; gap:0.5rem;">
            <span>📊</span> 3. Las 5 Series Numéricas Fijas de Examen
          </h3>
          <span style="background:rgba(56,189,248,0.15); color:#38bdf8; font-size:0.75rem; padding:0.2rem 0.6rem; border-radius:999px; font-weight:700;">
            CÓDIGO &amp; TRAZA
          </span>
        </div>
        <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1.2rem;">
          Explora la fórmula, la lógica de incremento y genera los términos en vivo con su código en Pascal:
        </p>

        <!-- Selector de serie -->
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap; margin-bottom:1.2rem;">
          <button class="btn-print" onclick="verSerie(1)" style="font-size:0.8rem;">1. Triangular (1, 3, 6, 10...)</button>
          <button class="btn-print" onclick="verSerie(2)" style="font-size:0.8rem;">2. Fibonacci (0, 1, 1, 2, 3...)</button>
          <button class="btn-print" onclick="verSerie(3)" style="font-size:0.8rem;">3. Alternada (1, -2, 3, -4...)</button>
          <button class="btn-print" onclick="verSerie(4)" style="font-size:0.8rem;">4. Factorial (1, 2, 6, 24...)</button>
          <button class="btn-print" onclick="verSerie(5)" style="font-size:0.8rem;">5. Primos (2, 3, 5, 7, 11...)</button>
        </div>

        <!-- Panel de la serie seleccionada -->
        <div id="panelSerieSeleccionada" style="background:#070a13; border:1px solid #334155; border-radius:8px; padding:1.2rem;">
          <!-- Dinámico -->
        </div>
      </div>

    </div>
  </section>
  <!-- =========================================================================== -->
  <!-- FIN SECCIÓN: SERIES NUMÉRICAS, GENERADOR DE TRAZA & 5 PASOS                 -->
  <!-- =========================================================================== -->
'''

def build_exam_y_herramientas_js():
    return r'''
  // ===========================================================================
  //      MOTOR JS: EXAMEN FINAL OFICIAL 2-2020 Y HERRAMIENTAS DE TRAZA
  // ===========================================================================

  // ─── PREGUNTA 5 EXAMEN FINAL: DÍGITOS PARES ───
  function efProbarDigitosPares() {
    const raw = document.getElementById('efP5Input').value;
    let n = parseInt(raw, 10);
    const resEl = document.getElementById('efP5Result');
    if (isNaN(n) || n < 0) {
      resEl.innerText = 'Ingrese un número entero positivo.';
      return;
    }
    const orig = n;
    let pares = 0, pasos = [];
    while (n > 0) {
      const dig = n % 10;
      const esPar = (dig % 2 === 0);
      if (esPar) pares++;
      pasos.push(`d=${dig} (${esPar?'PAR ✅':'Impar ❌'}) → pares=${pares}`);
      n = Math.floor(n / 10);
    }
    resEl.innerHTML = `Número: ${orig} → Total dígitos pares: <span style="color:#fbbf24; font-size:1.1rem;">${pares}</span><br><span style="font-size:0.78rem; color:#94a3b8;">Traza: ${pasos.join(' | ')}</span>`;
  }

  // ─── PREGUNTA 6 EXAMEN FINAL: VALOR ABSOLUTO ───
  function efProbarValorAbsoluto() {
    const n = parseInt(document.getElementById('efP6Input').value, 10);
    const resEl = document.getElementById('efP6Result');
    if (isNaN(n)) { resEl.innerText = ''; return; }
    const absVal = n < 0 ? n * -1 : n;
    resEl.innerHTML = `ValorAbsoluto(${n}) = <span style="color:#10b981; font-size:1.15rem;">${absVal}</span> (if ${n} &lt; 0 then ${n} * -1 else ${n})`;
  }

  // ─── PREGUNTA 7 EXAMEN FINAL: SIMULADOR COVID-19 ───
  let efCovidLista = [
    { nombre: 'Belen Aldana', edad: 65 },
    { nombre: 'Carlos Mendoza', edad: 42 },
    { nombre: 'Elena Vasquez', edad: 71 },
    { nombre: 'Jorge Cuellar', edad: 62 },
    { nombre: 'Mariana Ortiz', edad: 28 }
  ];

  function efCovidRender() {
    const sal = document.getElementById('efCovidSalida');
    if (!sal) return;
    if (efCovidLista.length === 0) {
      sal.innerHTML = '<span style="color:#64748b;">No hay personas registradas en la lista.</span>';
      return;
    }
    const aptos = efCovidLista.filter(p => p.edad > 60);
    const totalAptos = aptos.length;
    const suma = aptos.reduce((acc, p) => acc + p.edad, 0);
    const prom = totalAptos > 0 ? (suma / totalAptos).toFixed(2) : 0;

    let html = `<div style="color:#38bdf8; font-weight:700; margin-bottom:0.5rem;">📋 REGISTRO GENERAL (${efCovidLista.length} personas):</div>`;
    html += efCovidLista.map(p => {
      const apto = p.edad > 60;
      return `<div style="padding:0.2rem 0; color:${apto?'#10b981':'#94a3b8'};">
        • ${p.nombre} — ${p.edad} años ${apto?'<strong>[APTO VACUNACIÓN > 60]</strong>':''}
      </div>`;
    }).join('');

    html += `<hr style="border-color:#334155; margin:0.8rem 0;">`;
    html += `<div style="color:#10b981; font-weight:700;">💉 REPORTE DE VACUNACIÓN:</div>`;
    html += `<div>• Total de personas aptas (> 60 años): <strong style="color:#fbbf24;">${totalAptos}</strong></div>`;
    html += `<div>• Promedio de edad de este grupo: <strong style="color:#10b981;">${prom} años</strong></div>`;
    sal.innerHTML = html;
  }

  function efCovidAgregarPersona() {
    const nomEl = document.getElementById('efCovidNombre');
    const edEl = document.getElementById('efCovidEdad');
    const nom = nomEl.value.trim();
    const ed = parseInt(edEl.value, 10);
    if (!nom || isNaN(ed) || ed <= 0) {
      showMobileToast('Por favor ingresa un nombre y una edad válidos.');
      return;
    }
    efCovidLista.push({ nombre: nom, edad: ed });
    nomEl.value = '';
    edEl.value = '';
    efCovidRender();
    showMobileToast(`Registrado: ${nom} (${ed} años)`);
  }

  function efCovidCargarEjemplo() {
    efCovidLista = [
      { nombre: 'Belen Aldana', edad: 65 },
      { nombre: 'Carlos Mendoza', edad: 42 },
      { nombre: 'Elena Vasquez', edad: 71 },
      { nombre: 'Jorge Cuellar', edad: 62 },
      { nombre: 'Mariana Ortiz', edad: 28 }
    ];
    efCovidRender();
    showMobileToast('Datos de prueba de la docente cargados.');
  }

  function efCovidLimpiar() {
    efCovidLista = [];
    efCovidRender();
    showMobileToast('Lista reiniciada.');
  }

  // ─── GENERADOR DE PRUEBAS DE ESCRITORIO EN VIVO ───
  function esPrimoNum(n) {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }

  function generarTrazaEnVivo() {
    const raw = document.getElementById('genTrazaInput').value.trim();
    const algo = document.getElementById('genTrazaAlgo').value;
    const out = document.getElementById('genTrazaResultado');
    if (!raw) {
      out.innerHTML = '<div style="color:#f43f5e;">Ingresa un dato para trazar.</div>';
      return;
    }

    if (algo === 'sumar_primos') {
      let n = parseInt(raw, 10);
      if (isNaN(n) || n < 0) { out.innerHTML = 'Ingresa un número natural positivo.'; return; }
      let suma = 0, fila = 1, filas = [];
      const orig = n;
      while (n > 0) {
        const d = n % 10;
        const esP = esPrimoNum(d);
        if (esP) suma += d;
        const nSig = Math.floor(n / 10);
        filas.push({ n, d, cond: esP ? `Sí (${d} es primo)` : `No (${d} no es primo)`, suma, nSig });
        n = nSig;
        fila++;
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(16,185,129,0.15); color:#10b981;">
            <th style="padding:0.5rem; border:1px solid #334155;">n</th>
            <th style="padding:0.5rem; border:1px solid #334155;">d := n mod 10</th>
            <th style="padding:0.5rem; border:1px solid #334155;">¿EsPrimo(d)?</th>
            <th style="padding:0.5rem; border:1px solid #334155;">suma := suma + d</th>
            <th style="padding:0.5rem; border:1px solid #334155;">n := n div 10</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.n}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24; font-weight:700;">${f.d}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:${f.cond.startsWith('Sí')?'#10b981':'#f43f5e'};">${f.cond}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#38bdf8; font-weight:700;">${f.suma}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">${f.nSig}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#10b981; font-weight:700;">
        ✅ Resultado Retornado: SumarDigitosPrimos(${orig}) = ${suma}
      </div>`;
      out.innerHTML = html;
    } else if (algo === 'contar_pares') {
      let n = parseInt(raw, 10);
      if (isNaN(n) || n < 0) { out.innerHTML = 'Ingresa un número natural positivo.'; return; }
      let pares = 0;
      const orig = n;
      let filas = [];
      while (n > 0) {
        const d = n % 10;
        const esPar = (d % 2 === 0);
        if (esPar) pares++;
        const nSig = Math.floor(n / 10);
        filas.push({ n, d, cond: esPar ? `Sí (${d} mod 2 = 0)` : `No (${d} es impar)`, pares, nSig });
        n = nSig;
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(56,189,248,0.15); color:#38bdf8;">
            <th style="padding:0.5rem; border:1px solid #334155;">numero</th>
            <th style="padding:0.5rem; border:1px solid #334155;">dig := numero mod 10</th>
            <th style="padding:0.5rem; border:1px solid #334155;">(dig mod 2 = 0)</th>
            <th style="padding:0.5rem; border:1px solid #334155;">pares := pares + 1</th>
            <th style="padding:0.5rem; border:1px solid #334155;">numero := numero div 10</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.n}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24; font-weight:700;">${f.d}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:${f.cond.startsWith('Sí')?'#10b981':'#f43f5e'};">${f.cond}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#38bdf8; font-weight:700;">${f.pares}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">${f.nSig}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#38bdf8; font-weight:700;">
        ✅ Total de Dígitos Pares en ${orig} = ${pares}
      </div>`;
      out.innerHTML = html;
    } else if (algo === 'invertir_numero') {
      let n = parseInt(raw, 10);
      if (isNaN(n) || n < 0) { out.innerHTML = 'Ingresa un número natural positivo.'; return; }
      let inv = 0;
      const orig = n;
      let filas = [];
      while (n > 0) {
        const d = n % 10;
        inv = (inv * 10) + d;
        const nSig = Math.floor(n / 10);
        filas.push({ n, d, inv, nSig });
        n = nSig;
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(168,85,247,0.15); color:#a855f7;">
            <th style="padding:0.5rem; border:1px solid #334155;">n</th>
            <th style="padding:0.5rem; border:1px solid #334155;">d := n mod 10</th>
            <th style="padding:0.5rem; border:1px solid #334155;">inv := (inv * 10) + d</th>
            <th style="padding:0.5rem; border:1px solid #334155;">n := n div 10</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.n}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24; font-weight:700;">${f.d}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#a855f7; font-weight:700;">${f.inv}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">${f.nSig}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#a855f7; font-weight:700;">
        ✅ Número Invertido: ${orig} ➜ ${inv}
      </div>`;
      out.innerHTML = html;
    } else if (algo === 'sumar_digitos') {
      let n = parseInt(raw, 10);
      if (isNaN(n) || n < 0) { out.innerHTML = 'Ingresa un número natural positivo.'; return; }
      let suma = 0;
      const orig = n;
      let filas = [];
      while (n > 0) {
        const d = n % 10;
        suma += d;
        const nSig = Math.floor(n / 10);
        filas.push({ n, d, suma, nSig });
        n = nSig;
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(245,158,11,0.15); color:#f59e0b;">
            <th style="padding:0.5rem; border:1px solid #334155;">n</th>
            <th style="padding:0.5rem; border:1px solid #334155;">d := n mod 10</th>
            <th style="padding:0.5rem; border:1px solid #334155;">suma := suma + d</th>
            <th style="padding:0.5rem; border:1px solid #334155;">n := n div 10</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.n}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24; font-weight:700;">${f.d}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#f59e0b; font-weight:700;">${f.suma}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">${f.nSig}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#f59e0b; font-weight:700;">
        ✅ Suma de Dígitos de ${orig} = ${suma}
      </div>`;
      out.innerHTML = html;
    } else if (algo === 'contar_vocales') {
      const cad = raw;
      const n = cad.length;
      let voc = 0, filas = [];
      const vocales = new Set(['a','e','i','o','u','á','é','í','ó','ú']);
      for (let i = 0; i < n; i++) {
        const ch = cad[i];
        const esV = vocales.has(ch.toLowerCase());
        if (esV) voc++;
        filas.push({ i: i + 1, ch: ch === ' ' ? '␣' : ch, cond: esV ? 'SÍ (Vocal)' : 'No', voc });
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(56,189,248,0.15); color:#38bdf8;">
            <th style="padding:0.5rem; border:1px solid #334155;">i</th>
            <th style="padding:0.5rem; border:1px solid #334155;">cad[i]</th>
            <th style="padding:0.5rem; border:1px solid #334155;">cad[i] in ['A','E','I','O','U'...]</th>
            <th style="padding:0.5rem; border:1px solid #334155;">contador</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.i}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24; font-weight:700;">'${f.ch}'</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:${f.cond.startsWith('SÍ')?'#10b981':'#f43f5e'};">${f.cond}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#38bdf8; font-weight:700;">${f.voc}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#38bdf8; font-weight:700;">
        ✅ Total de Vocales en '${cad}' = ${voc}
      </div>`;
      out.innerHTML = html;
    } else if (algo === 'contar_palabras') {
      const cad = raw;
      const n = cad.length;
      let i = 0, cant = 0, filas = [];
      while (i < n) {
        while (i < n && cad[i] === ' ') {
          filas.push({ paso: 'Salto', i: i + 1, ch: '␣ (espacio)', accion: 'i := i + 1', pal: '—', cant });
          i++;
        }
        let pal = '';
        while (i < n && cad[i] !== ' ') {
          pal += cad[i];
          filas.push({ paso: 'Captura', i: i + 1, ch: cad[i], accion: `pal := pal + '${cad[i]}'`, pal: `'${pal}'`, cant });
          i++;
        }
        if (pal !== '') {
          cant++;
          filas.push({ paso: 'Fin Pal', i, ch: '—', accion: `cant := ${cant}`, pal: `'${pal}'`, cant });
        }
      }
      let html = `<table style="width:100%; border-collapse:collapse; font-size:0.84rem; font-family:'Fira Code',monospace;">
        <thead>
          <tr style="background:rgba(16,185,129,0.15); color:#10b981;">
            <th style="padding:0.5rem; border:1px solid #334155;">Fase</th>
            <th style="padding:0.5rem; border:1px solid #334155;">i</th>
            <th style="padding:0.5rem; border:1px solid #334155;">cad[i]</th>
            <th style="padding:0.5rem; border:1px solid #334155;">Acción</th>
            <th style="padding:0.5rem; border:1px solid #334155;">palabra</th>
            <th style="padding:0.5rem; border:1px solid #334155;">cantPal</th>
          </tr>
        </thead><tbody>`;
      filas.forEach(f => {
        html += `<tr>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#94a3b8;">${f.paso}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#cbd5e1;">${f.i}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#fbbf24;">${f.ch}</td>
          <td style="padding:0.45rem; text-align:left; border:1px solid #1e293b; color:#cbd5e1;">${f.accion}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#38bdf8;">${f.pal}</td>
          <td style="padding:0.45rem; text-align:center; border:1px solid #1e293b; color:#10b981; font-weight:700;">${f.cant}</td>
        </tr>`;
      });
      html += `</tbody></table>
      <div style="margin-top:0.8rem; color:#10b981; font-weight:700;">
        ✅ Total de Palabras en '${cad}' = ${cant}
      </div>`;
      out.innerHTML = html;
    }
    showMobileToast('Prueba de escritorio generada.');
  }

  // ─── CATÁLOGO DE 5 SERIES NUMÉRICAS ───
  const SERIES_DATA = {
    1: {
      nombre: '1. Serie Triangular (Examen Final 2-2020)',
      terminos: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],
      formula: 'T(n) = n * (n + 1) div 2  |  Incremento: +2, +3, +4, +5...',
      codigo: `// Generar N términos de la Serie Triangular
t := 1;
for i := 1 to n do
begin
  Write(t, ' ');
  t := t + (i + 1);
end;`
    },
    2: {
      nombre: '2. Serie de Fibonacci (Frecuente en Exámenes)',
      terminos: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
      formula: 'F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)',
      codigo: `// Generar N términos de Fibonacci
a := 0; b := 1;
for i := 1 to n do
begin
  Write(a, ' ');
  c := a + b;
  a := b;
  b := c;
end;`
    },
    3: {
      nombre: '3. Serie Alternada de Signos',
      terminos: [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],
      formula: 'T(n) = n * (-1)^(n+1)',
      codigo: `// Generar Serie Alternada
signo := 1;
for i := 1 to n do
begin
  t := i * signo;
  Write(t, ' ');
  signo := signo * (-1);
end;`
    },
    4: {
      nombre: '4. Serie de Factoriales (1!, 2!, 3!... )',
      terminos: [1, 2, 6, 24, 120, 720, 5040],
      formula: 'T(n) = n! = 1 * 2 * 3 * ... * n',
      codigo: `// Factoriales sucesivos
fact := 1;
for i := 1 to n do
begin
  fact := fact * i;
  Write(fact, ' ');
end;`
    },
    5: {
      nombre: '5. Serie de Números Primos Sucesivos',
      terminos: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
      formula: 'Primos sucesivos mayores o iguales a 2',
      codigo: `// Generar N primeros primos
cant := 0; num := 2;
while cant < n do
begin
  if EsPrimo(num) then
  begin
    Write(num, ' ');
    cant := cant + 1;
  end;
  num := num + 1;
end;`
    }
  };

  function verSerie(id) {
    const s = SERIES_DATA[id];
    const p = document.getElementById('panelSerieSeleccionada');
    if (!s || !p) return;
    p.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">
        <h4 style="color:#38bdf8; margin:0; font-size:1.05rem;">${s.nombre}</h4>
        <span style="font-size:0.8rem; color:#f59e0b; font-family:'Fira Code',monospace;">${s.formula}</span>
      </div>
      <div style="margin-bottom:0.8rem;">
        <span style="color:#94a3b8; font-size:0.8rem;">Primeros 10 términos:</span>
        <div style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-top:0.3rem;">
          ${s.terminos.map((t, idx) => `<span style="background:rgba(56,189,248,0.15); color:#38bdf8; border:1px solid rgba(56,189,248,0.3); border-radius:6px; padding:0.25rem 0.6rem; font-family:'Fira Code',monospace; font-size:0.9rem; font-weight:700;">T${idx+1}: ${t}</span>`).join('')}
        </div>
      </div>
      <div class="code-block" style="font-size:0.8rem; margin:0;">
        ${s.codigo.replace(/</g,'&lt;').replace(/>/g,'&gt;')}
      </div>
    `;
    showMobileToast(`Mostrando: ${s.nombre}`);
  }

  // Inicializar vistas al cargar
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof efCovidRender === 'function') efCovidRender();
    if (typeof verSerie === 'function') verSerie(1);
    if (typeof generarTrazaEnVivo === 'function') generarTrazaEnVivo();
  });
'''
