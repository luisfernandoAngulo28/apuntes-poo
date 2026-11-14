# -*- coding: utf-8 -*-
"""
Kit Completo de Preparación para el Examen de Cadenas en Delphi Pascal.
Incluye:
  1. Guía de 4 Patrones Clave de Examen
  2. Laboratorio ASCII & Conjuntos set of char
  3. Trampas Clásicas de Examen
  4. Visualizador de Traza Paso a Paso
  5. Simulacro de Examen con Temporizador
"""

def build_exam_kit_html():
    return r'''
  <!-- =========================================================================== -->
  <!-- KIT COMPLETO DE PREPARACIÓN PARA EL EXAMEN DE CADENAS — INF110-Z2           -->
  <!-- =========================================================================== -->
  <section id="cadenas-exam-kit" class="section-content">
    <div class="card">

      <!-- Encabezado del Kit -->
      <div class="header-top-actions" style="margin-bottom: 1.5rem;">
        <div>
          <h2 class="card-title" style="margin-bottom: 0.25rem;">🎯 Kit Completo de Preparación: Examen de Cadenas</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">
            Material 100% orientado al estilo de examen de la <strong>M.Sc. Ing. Angélica Garzón C.</strong> (INF110-Z2 • UAGRM)
          </p>
        </div>
        <span class="badge" style="background:rgba(16,185,129,.15);color:#10b981;border-color:rgba(16,185,129,.3);">
          ⚡ 5 MÓDULOS INTERACTIVOS
        </span>
      </div>

      <!-- Índice navegable rápido -->
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:2rem;">
        <a href="#kit-patrones" class="btn-print" style="text-decoration:none;font-size:.82rem;">🏆 1. Patrones Clave</a>
        <a href="#kit-ascii" class="btn-print" style="text-decoration:none;font-size:.82rem;">🔢 2. ASCII &amp; Conjuntos</a>
        <a href="#kit-trampas" class="btn-print" style="text-decoration:none;font-size:.82rem;">⚠️ 3. Trampas de Examen</a>
        <a href="#kit-traza" class="btn-print" style="text-decoration:none;font-size:.82rem;">🔬 4. Traza Animada</a>
        <a href="#kit-simulacro" class="btn-print" style="text-decoration:none;font-size:.82rem;">⏱️ 5. Simulacro de Examen</a>
      </div>

      <!-- =====================================================================
           MÓDULO 1: PATRONES CLAVE DE EXAMEN
           ===================================================================== -->
      <div id="kit-patrones" style="margin-bottom:2.5rem;">
        <h3 style="color:#f59e0b;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;font-size:1.3rem;">
          <span>🏆</span> Módulo 1: Los 4 Patrones Clave de Examen
        </h3>
        <p style="color:var(--text-muted);font-size:.88rem;margin-bottom:1.25rem;">
          El 90% de los exámenes de la facultad se resuelven aplicando uno de estos cuatro patrones estructurales. Reconócelos y tendrás ventaja.
        </p>

        <!-- Patrón 1 -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-left:4px solid #38bdf8;border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem;margin-bottom:.75rem;">
            <h4 style="color:#38bdf8;margin:0;font-size:1.05rem;">Patrón 1 — Recorrido Carácter a Carácter</h4>
            <span style="background:rgba(56,189,248,.15);color:#38bdf8;padding:.2rem .6rem;border-radius:999px;font-size:.75rem;font-weight:700;">CONTAR • BUSCAR • FILTRAR</span>
          </div>
          <p style="font-size:.85rem;color:#cbd5e1;margin-bottom:.75rem;">
            Estructura base: <code>i := 1; while i &lt;= n do begin ... i := i + 1; end;</code><br>
            Se usa para <strong>contar vocales, consonantes, espacios, mayúsculas</strong> o cualquier condición sobre cada carácter.
          </p>
          <div class="code-block" style="font-size:.82rem;">
<span style="color:#64748b;">// PLANTILLA PATRÓN 1 — Contar con condición</span><br>
<span style="color:#60a5fa;">var</span> cad: <span style="color:#34d399;">String</span>; i, n, contador: <span style="color:#34d399;">Byte</span>;<br>
<span style="color:#64748b;">// cad := Edit1.Text;  n := Length(cad);</span><br>
contador := <span style="color:#f59e0b;">0</span>;<br>
i := <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">while</span> i &lt;= n <span style="color:#60a5fa;">do begin</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> cad[i] <span style="color:#60a5fa;">in</span> [<span style="color:#f87171;">'A','E','I','O','U','a','e','i','o','u'</span>] <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;contador := contador + <span style="color:#f59e0b;">1</span>;<br>
&nbsp;&nbsp;i := i + <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">end</span>;<br>
Edit2.Text := IntToStr(contador);
          </div>
          <button class="btn-print" onclick="kitProbarPatron(1)" style="margin-top:.75rem;font-size:.8rem;background:#38bdf8;color:#0b1120;font-weight:bold;">▶ Probar Patrón 1 en Vivo</button>
        </div>

        <!-- Patrón 2 -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-left:4px solid #10b981;border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem;margin-bottom:.75rem;">
            <h4 style="color:#10b981;margin:0;font-size:1.05rem;">Patrón 2 — Extracción de Palabras (Algoritmo Maestro)</h4>
            <span style="background:rgba(16,185,129,.15);color:#10b981;padding:.2rem .6rem;border-radius:999px;font-size:.75rem;font-weight:700;">PALABRAS • FRASES</span>
          </div>
          <p style="font-size:.85rem;color:#cbd5e1;margin-bottom:.75rem;">
            El algoritmo más pedido en examen para <strong>contar palabras, extraer la primera, última o k-ésima palabra</strong>. Usa doble bucle: uno que salta espacios y otro que captura la palabra.
          </p>
          <div class="code-block" style="font-size:.82rem;">
<span style="color:#64748b;">// PATRÓN 2 — Extraer palabras con doble bucle</span><br>
i := <span style="color:#f59e0b;">1</span>; cantPal := <span style="color:#f59e0b;">0</span>;<br>
<span style="color:#60a5fa;">while</span> i &lt;= n <span style="color:#60a5fa;">do begin</span><br>
&nbsp;&nbsp;<span style="color:#64748b;">// Saltar espacios (puede haber múltiples)</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">while</span> (i &lt;= n) <span style="color:#60a5fa;">and</span> (cad[i] = <span style="color:#f87171;">' '</span>) <span style="color:#60a5fa;">do</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;i := i + <span style="color:#f59e0b;">1</span>;<br>
&nbsp;&nbsp;<span style="color:#64748b;">// Capturar palabra</span><br>
&nbsp;&nbsp;pal := <span style="color:#f87171;">''</span>;<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">while</span> (i &lt;= n) <span style="color:#60a5fa;">and</span> (cad[i] &lt;&gt; <span style="color:#f87171;">' '</span>) <span style="color:#60a5fa;">do begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;pal := pal + cad[i];<br>
&nbsp;&nbsp;&nbsp;&nbsp;i := i + <span style="color:#f59e0b;">1</span>;<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">end</span>;<br>
&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> pal &lt;&gt; <span style="color:#f87171;">''</span> <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;cantPal := cantPal + <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">end</span>;<br>
Edit2.Text := IntToStr(cantPal) + <span style="color:#f87171;">' palabras'</span>;
          </div>
          <button class="btn-print" onclick="kitProbarPatron(2)" style="margin-top:.75rem;font-size:.8rem;background:#10b981;color:#0b1120;font-weight:bold;">▶ Probar Patrón 2 en Vivo</button>
        </div>

        <!-- Patrón 3 -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-left:4px solid #a855f7;border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem;margin-bottom:.75rem;">
            <h4 style="color:#a855f7;margin:0;font-size:1.05rem;">Patrón 3 — Simetría e Inversión (Palíndromas &amp; Anagramas)</h4>
            <span style="background:rgba(168,85,247,.15);color:#c084fc;padding:.2rem .6rem;border-radius:999px;font-size:.75rem;font-weight:700;">PALÍNDROMAS • INVERSIÓN</span>
          </div>
          <p style="font-size:.85rem;color:#cbd5e1;margin-bottom:.75rem;">
            Usado para invertir cadenas o detectar palíndromas. Se acumula carácter a carácter en orden inverso.
          </p>
          <div class="code-block" style="font-size:.82rem;">
<span style="color:#64748b;">// PATRÓN 3a — Invertir cadena</span><br>
inv := <span style="color:#f87171;">''</span>; i := n;<br>
<span style="color:#60a5fa;">while</span> i &gt;= <span style="color:#f59e0b;">1</span> <span style="color:#60a5fa;">do begin</span><br>
&nbsp;&nbsp;inv := inv + cad[i];<br>
&nbsp;&nbsp;i := i - <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">end</span>;<br>
<br>
<span style="color:#64748b;">// PATRÓN 3b — Detectar palíndroma</span><br>
esPalin := <span style="color:#60a5fa;">True</span>; izq := <span style="color:#f59e0b;">1</span>; der := n;<br>
<span style="color:#60a5fa;">while</span> (izq &lt; der) <span style="color:#60a5fa;">and</span> esPalin <span style="color:#60a5fa;">do begin</span><br>
&nbsp;&nbsp;<span style="color:#60a5fa;">if</span> UpCase(cad[izq]) &lt;&gt; UpCase(cad[der]) <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;esPalin := <span style="color:#60a5fa;">False</span>;<br>
&nbsp;&nbsp;izq := izq + <span style="color:#f59e0b;">1</span>; der := der - <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">end</span>;
          </div>
          <button class="btn-print" onclick="kitProbarPatron(3)" style="margin-top:.75rem;font-size:.8rem;background:#a855f7;color:#fff;font-weight:bold;">▶ Probar Patrón 3 en Vivo</button>
        </div>

        <!-- Patrón 4 -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-left:4px solid #f59e0b;border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem;margin-bottom:.75rem;">
            <h4 style="color:#f59e0b;margin:0;font-size:1.05rem;">Patrón 4 — Transformaciones Manuales con ASCII (Sin funciones del sistema)</h4>
            <span style="background:rgba(245,158,11,.15);color:#fbbf24;padding:.2rem .6rem;border-radius:999px;font-size:.75rem;font-weight:700;">ASCII • Ord • Chr</span>
          </div>
          <p style="font-size:.85rem;color:#cbd5e1;margin-bottom:.75rem;">
            Conversión manual de mayúsculas a minúsculas y viceversa usando <code>Ord(c)</code> y <code>Chr()</code>. Fundamental cuando el examen pide <em>"sin usar UpperCase ni LowerCase"</em>.
          </p>
          <div class="code-block" style="font-size:.82rem;">
<span style="color:#64748b;">// PATRÓN 4 — Conversión manual Minúscula → Mayúscula</span><br>
<span style="color:#60a5fa;">if</span> (Ord(c) &gt;= <span style="color:#f59e0b;">97</span>) <span style="color:#60a5fa;">and</span> (Ord(c) &lt;= <span style="color:#f59e0b;">122</span>) <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;cMay := Chr(Ord(c) - <span style="color:#f59e0b;">32</span>);<br>
<br>
<span style="color:#64748b;">// PATRÓN 4b — Conversión Mayúscula → Minúscula</span><br>
<span style="color:#60a5fa;">if</span> (Ord(c) &gt;= <span style="color:#f59e0b;">65</span>) <span style="color:#60a5fa;">and</span> (Ord(c) &lt;= <span style="color:#f59e0b;">90</span>) <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;cMin := Chr(Ord(c) + <span style="color:#f59e0b;">32</span>);<br>
<br>
<span style="color:#64748b;">// PATRÓN 4c — Detectar dígito numérico</span><br>
<span style="color:#60a5fa;">if</span> (Ord(c) &gt;= <span style="color:#f59e0b;">48</span>) <span style="color:#60a5fa;">and</span> (Ord(c) &lt;= <span style="color:#f59e0b;">57</span>) <span style="color:#60a5fa;">then</span><br>
&nbsp;&nbsp;<span style="color:#64748b;">// c es '0'..'9', valor numérico = Ord(c) - 48</span>
          </div>
          <button class="btn-print" onclick="kitProbarPatron(4)" style="margin-top:.75rem;font-size:.8rem;background:#f59e0b;color:#0b1120;font-weight:bold;">▶ Probar Patrón 4 en Vivo</button>
        </div>

        <!-- Playground de patrones -->
        <div id="kitPatronPlayground" style="display:none;background:rgba(7,10,19,.85);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:1.2rem;margin-top:.75rem;">
          <div style="display:flex;gap:.75rem;margin-bottom:.75rem;flex-wrap:wrap;">
            <div style="flex:1;min-width:220px;">
              <label style="display:block;font-size:.8rem;color:#cbd5e1;margin-bottom:.3rem;font-weight:600;">Cadena de prueba:</label>
              <input type="text" id="kitPatronInput" value="Anita lava la tina" style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:.9rem;">
            </div>
            <div style="display:flex;align-items:flex-end;">
              <button class="btn-print" onclick="kitEjecutarPatron()" style="background:#38bdf8;color:#0b1120;font-weight:bold;">Ejecutar</button>
            </div>
          </div>
          <div style="font-family:'Fira Code',monospace;font-size:.85rem;">
            <div style="color:#64748b;font-size:.78rem;margin-bottom:.3rem;">// RESULTADO:</div>
            <div id="kitPatronResult" style="color:#10b981;font-weight:700;font-size:1rem;">&mdash;</div>
            <div id="kitPatronExplain" style="color:#94a3b8;font-size:.82rem;margin-top:.4rem;border-top:1px dashed #1e293b;padding-top:.4rem;"></div>
          </div>
        </div>
      </div>

      <!-- =====================================================================
           MÓDULO 2: ASCII & CONJUNTOS set of char
           ===================================================================== -->
      <div id="kit-ascii" style="margin-bottom:2.5rem;">
        <h3 style="color:#38bdf8;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;font-size:1.3rem;">
          <span>🔢</span> Módulo 2: Laboratorio ASCII &amp; Conjuntos <code>set of char</code>
        </h3>

        <!-- Tabla resumen ASCII de examen -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <h4 style="color:#38bdf8;margin:0 0 .75rem 0;font-size:1rem;">📋 Rangos ASCII Críticos para el Examen</h4>
          <div style="overflow-x:auto;">
            <table style="width:100%;font-size:.85rem;border-collapse:collapse;">
              <thead>
                <tr style="background:rgba(56,189,248,.1);">
                  <th style="padding:.5rem .75rem;text-align:left;color:#38bdf8;border-bottom:1px solid var(--border-color);">Grupo</th>
                  <th style="padding:.5rem .75rem;text-align:left;color:#38bdf8;border-bottom:1px solid var(--border-color);">Rango Ord()</th>
                  <th style="padding:.5rem .75rem;text-align:left;color:#38bdf8;border-bottom:1px solid var(--border-color);">Ejemplo en Pascal</th>
                  <th style="padding:.5rem .75rem;text-align:left;color:#38bdf8;border-bottom:1px solid var(--border-color);">Truco Clave</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,.06);">
                  <td style="padding:.45rem .75rem;color:#fbbf24;font-weight:700;">Dígitos '0'..'9'</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">48 — 57</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">Ord('0')=48, Ord('9')=57</td>
                  <td style="padding:.45rem .75rem;color:#10b981;font-size:.8rem;">Valor numérico = Ord(c) - 48</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,.06);">
                  <td style="padding:.45rem .75rem;color:#38bdf8;font-weight:700;">Mayúsculas 'A'..'Z'</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">65 — 90</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">Ord('A')=65, Ord('Z')=90</td>
                  <td style="padding:.45rem .75rem;color:#10b981;font-size:.8rem;">A Min → + 32</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,.06);">
                  <td style="padding:.45rem .75rem;color:#a855f7;font-weight:700;">Minúsculas 'a'..'z'</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">97 — 122</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">Ord('a')=97, Ord('z')=122</td>
                  <td style="padding:.45rem .75rem;color:#10b981;font-size:.8rem;">A May → - 32</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,.06);">
                  <td style="padding:.45rem .75rem;color:#fb7185;font-weight:700;">Espacio ' '</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">32</td>
                  <td style="padding:.45rem .75rem;color:#94a3b8;font-family:'Fira Code',monospace;">Ord(' ')=32</td>
                  <td style="padding:.45rem .75rem;color:#10b981;font-size:.8rem;">Detectar con cad[i]=' '</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Conversor ASCII interactivo -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <h4 style="color:#f59e0b;margin:0 0 .75rem 0;font-size:1rem;">⚡ Conversor Interactivo Ord / Chr</h4>
          <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:.75rem;">
            <div style="flex:1;min-width:180px;">
              <label style="display:block;font-size:.8rem;color:#cbd5e1;margin-bottom:.3rem;font-weight:600;">Carácter → Ord():</label>
              <input type="text" id="asciiCharInput" maxlength="1" placeholder="Ej: A" oninput="kitOrdConvert()" style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:1rem;text-align:center;">
              <div id="asciiOrdResult" style="margin-top:.4rem;font-family:'Fira Code',monospace;color:#38bdf8;font-size:.9rem;font-weight:700;min-height:1.2rem;"></div>
            </div>
            <div style="flex:1;min-width:180px;">
              <label style="display:block;font-size:.8rem;color:#cbd5e1;margin-bottom:.3rem;font-weight:600;">Código → Chr():</label>
              <input type="number" id="asciiCodeInput" min="0" max="255" placeholder="Ej: 65" oninput="kitChrConvert()" style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:1rem;">
              <div id="asciiChrResult" style="margin-top:.4rem;font-family:'Fira Code',monospace;color:#a855f7;font-size:.9rem;font-weight:700;min-height:1.2rem;"></div>
            </div>
          </div>
        </div>

        <!-- Conjuntos set of char -->
        <div style="background:rgba(15,23,42,.75);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:1.25rem;margin-bottom:1rem;">
          <h4 style="color:#10b981;margin:0 0 .75rem 0;font-size:1rem;">🎯 Conjuntos <code>set of char</code> — La Herramienta Clave del Examen</h4>
          <p style="font-size:.84rem;color:#94a3b8;margin-bottom:.75rem;">Los conjuntos eliminan cadenas largas de <code>if (c='A') or (c='E') or...</code> y hacen el código más limpio y legible — <strong>exactamente lo que la docente espera en pizarra</strong>.</p>
          <div class="code-block" style="font-size:.82rem;margin-bottom:.75rem;">
<span style="color:#60a5fa;">const</span><br>
&nbsp;&nbsp;voc: <span style="color:#34d399;">set of Char</span> = [<span style="color:#f87171;">'A','E','I','O','U','a','e','i','o','u'</span>];<br>
&nbsp;&nbsp;mayus: <span style="color:#34d399;">set of Char</span> = [<span style="color:#f87171;">'A'..'Z'</span>];<br>
&nbsp;&nbsp;minus: <span style="color:#34d399;">set of Char</span> = [<span style="color:#f87171;">'a'..'z'</span>];<br>
&nbsp;&nbsp;digitos: <span style="color:#34d399;">set of Char</span> = [<span style="color:#f87171;">'0'..'9'</span>];<br>
&nbsp;&nbsp;letras: <span style="color:#34d399;">set of Char</span> = [<span style="color:#f87171;">'A'..'Z','a'..'z'</span>];<br>
<br>
<span style="color:#64748b;">// USO con el operador in:</span><br>
<span style="color:#60a5fa;">if</span> cad[i] <span style="color:#60a5fa;">in</span> voc <span style="color:#60a5fa;">then</span> cantVoc := cantVoc + <span style="color:#f59e0b;">1</span>;<br>
<span style="color:#60a5fa;">if</span> cad[i] <span style="color:#60a5fa;">in</span> digitos <span style="color:#60a5fa;">then</span> cantNum := cantNum + <span style="color:#f59e0b;">1</span>;
          </div>

          <!-- Verificador de conjunto interactivo -->
          <div style="background:rgba(7,10,19,.7);border:1px dashed #334155;border-radius:6px;padding:.9rem;margin-top:.5rem;">
            <div style="font-size:.82rem;color:#94a3b8;margin-bottom:.5rem;font-weight:600;">🔬 Verificador de Conjuntos en Vivo:</div>
            <div style="display:flex;gap:.75rem;flex-wrap:wrap;align-items:center;">
              <input type="text" id="kitSetChar" maxlength="1" placeholder="Carácter" oninput="kitVerificarConjunto()" style="width:90px;padding:.4rem .7rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:1.1rem;text-align:center;">
              <div id="kitSetResults" style="display:flex;gap:.5rem;flex-wrap:wrap;"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- =====================================================================
           MÓDULO 3: TRAMPAS CLÁSICAS DE EXAMEN
           ===================================================================== -->
      <div id="kit-trampas" style="margin-bottom:2.5rem;">
        <h3 style="color:#f43f5e;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;font-size:1.3rem;">
          <span>⚠️</span> Módulo 3: Las 6 Trampas Clásicas del Examen de Cadenas
        </h3>
        <p style="color:var(--text-muted);font-size:.88rem;margin-bottom:1.25rem;">
          Estas son las causas más frecuentes de pérdida de puntos. Identifícalas en tu código <strong>antes de entregar</strong>.
        </p>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1rem;">

          <!-- Trampa 1 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">1</span>
              <strong style="color:#fb7185;font-size:.92rem;">El bucle infinito — Olvidar <code>i := i + 1</code></strong>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;font-size:.78rem;">
              <div>
                <div style="color:#f43f5e;font-weight:700;margin-bottom:.3rem;">❌ INCORRECTO:</div>
                <div style="background:#0b1120;padding:.45rem .6rem;border-radius:4px;font-family:'Fira Code',monospace;color:#f87171;line-height:1.5;">
                  i := 1;<br>while i &lt;= n do<br>begin<br>&nbsp;&nbsp;if cad[i]='A'<br>&nbsp;&nbsp;then c:=c+1;<br>&nbsp;&nbsp;<span style="text-decoration:line-through;opacity:.5;">i:=i+1;</span><br>end;
                </div>
              </div>
              <div>
                <div style="color:#10b981;font-weight:700;margin-bottom:.3rem;">✅ CORRECTO:</div>
                <div style="background:#0b1120;padding:.45rem .6rem;border-radius:4px;font-family:'Fira Code',monospace;color:#6ee7b7;line-height:1.5;">
                  i := 1;<br>while i &lt;= n do<br>begin<br>&nbsp;&nbsp;if cad[i]='A'<br>&nbsp;&nbsp;then c:=c+1;<br>&nbsp;&nbsp;<span style="color:#4ade80;font-weight:800;">i:=i+1;</span><br>end;
                </div>
              </div>
            </div>
          </div>

          <!-- Trampa 2 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">2</span>
              <strong style="color:#fb7185;font-size:.92rem;">Confundir <code>UpCase(Char)</code> con <code>UpperCase(String)</code></strong>
            </div>
            <div style="background:#0b1120;padding:.6rem .75rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.8rem;line-height:1.8;">
              <span style="color:#f43f5e;">// ❌ Error de compilación:</span><br>
              res := UpperCase(cad[i]); <span style="color:#f43f5e;">// cad[i] es Char, no String</span><br>
              <br>
              <span style="color:#10b981;">// ✅ Correcto para un carácter:</span><br>
              c := UpCase(cad[i]); <span style="color:#10b981;">// UpCase recibe Char</span><br>
              <span style="color:#10b981;">// ✅ Para la cadena completa:</span><br>
              res := UpperCase(cad); <span style="color:#10b981;">// UpperCase recibe String</span>
            </div>
          </div>

          <!-- Trampa 3 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">3</span>
              <strong style="color:#fb7185;font-size:.92rem;">Desbordamiento: Acceder a <code>cad[0]</code> o <code>cad[n+1]</code></strong>
            </div>
            <div style="background:#0b1120;padding:.6rem .75rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.8rem;line-height:1.8;">
              <span style="color:#f43f5e;">// ❌ PELIGROSO — Puede lanzar Range Check Error:</span><br>
              c := cad[<span style="color:#f43f5e;">0</span>]; <span style="color:#f43f5e;">// En Delphi, cad[0] es la longitud interna (ShortString)</span><br>
              c := cad[n+<span style="color:#f43f5e;">1</span>]; <span style="color:#f43f5e;">// Acceso fuera de rango</span><br>
              <br>
              <span style="color:#10b981;">// ✅ Rango válido siempre: cad[1] .. cad[Length(cad)]</span><br>
              n := Length(cad);<br>
              <span style="color:#60a5fa;">if</span> n &gt; <span style="color:#f59e0b;">0</span> <span style="color:#60a5fa;">then</span> c := cad[n]; <span style="color:#10b981;">// última letra</span>
            </div>
          </div>

          <!-- Trampa 4 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">4</span>
              <strong style="color:#fb7185;font-size:.92rem;">Parámetros <code>var</code> vs por Valor — Cuándo la cadena NO se modifica</strong>
            </div>
            <div style="background:#0b1120;padding:.6rem .75rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.8rem;line-height:1.8;">
              <span style="color:#f43f5e;">// ❌ Por valor — el procedimiento NO modifica cad original:</span><br>
              <span style="color:#60a5fa;">procedure</span> AgregarPunto(cad: <span style="color:#34d399;">String</span>);<br>
              <span style="color:#60a5fa;">begin</span> cad := cad + <span style="color:#f87171;">'.'</span>; <span style="color:#60a5fa;">end</span>; <span style="color:#f43f5e;">// Inútil</span><br>
              <br>
              <span style="color:#10b981;">// ✅ Con VAR — sí modifica el original:</span><br>
              <span style="color:#60a5fa;">procedure</span> AgregarPunto(<span style="color:#60a5fa;">var</span> cad: <span style="color:#34d399;">String</span>);<br>
              <span style="color:#60a5fa;">begin</span> cad := cad + <span style="color:#f87171;">'.'</span>; <span style="color:#60a5fa;">end</span>; <span style="color:#10b981;">// Modifica el original</span>
            </div>
          </div>

          <!-- Trampa 5 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">5</span>
              <strong style="color:#fb7185;font-size:.92rem;">No validar cadena vacía (<code>cad = ''</code> / <code>n = 0</code>)</strong>
            </div>
            <div style="background:#0b1120;padding:.6rem .75rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.8rem;line-height:1.8;">
              <span style="color:#f43f5e;">// ❌ Sin validación: si cad='' n=0, accede a cad[1] = ERROR</span><br>
              primeraLetra := cad[<span style="color:#f59e0b;">1</span>]; <span style="color:#f43f5e;">// Crash si cad está vacía</span><br>
              <br>
              <span style="color:#10b981;">// ✅ Siempre validar primero:</span><br>
              n := Length(cad);<br>
              <span style="color:#60a5fa;">if</span> n = <span style="color:#f59e0b;">0</span> <span style="color:#60a5fa;">then</span><br>
              &nbsp;&nbsp;ShowMessage(<span style="color:#f87171;">'Cadena vacía'</span>)<br>
              <span style="color:#60a5fa;">else</span><br>
              &nbsp;&nbsp;primeraLetra := cad[<span style="color:#f59e0b;">1</span>];
            </div>
          </div>

          <!-- Trampa 6 -->
          <div style="background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.35);border-radius:var(--radius-sm);padding:1rem;">
            <div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem;">
              <span style="background:rgba(244,63,94,.2);color:#fb7185;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;">6</span>
              <strong style="color:#fb7185;font-size:.92rem;">Espacios extras — Count simple falla con frases como <code>'  Hola  Mundo  '</code></strong>
            </div>
            <div style="background:#0b1120;padding:.6rem .75rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.8rem;line-height:1.8;">
              <span style="color:#f43f5e;">// ❌ Contar espacios = contar palabras SOLO funciona sin espacios extras</span><br>
              <span style="color:#60a5fa;">if</span> cad[i] = <span style="color:#f87171;">' '</span> <span style="color:#60a5fa;">then</span> cant:=cant+<span style="color:#f59e0b;">1</span>; <span style="color:#f43f5e;">// Incorrecto para '  A  B  '</span><br>
              <br>
              <span style="color:#10b981;">// ✅ Usar el Patrón 2 (doble bucle que detecta transición)</span><br>
              <span style="color:#64748b;">// Detectar transición: el carácter actual NO es espacio</span><br>
              <span style="color:#64748b;">// y el anterior SÍ era espacio (o es el primero)</span>
            </div>
          </div>

        </div>
      </div>

      <!-- =====================================================================
           MÓDULO 4: VISUALIZADOR DE TRAZA PASO A PASO
           ===================================================================== -->
      <div id="kit-traza" style="margin-bottom:2.5rem;">
        <h3 style="color:#10b981;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;font-size:1.3rem;">
          <span>🔬</span> Módulo 4: Visualizador de Traza Paso a Paso
        </h3>
        <p style="color:var(--text-muted);font-size:.88rem;margin-bottom:1.25rem;">
          Visualiza cómo el índice <code>i</code> recorre la cadena y cómo se actualizan las variables en cada paso — igual que la docente lo muestra en la pizarra.
        </p>

        <div style="background:rgba(15,23,42,.85);border:1px solid var(--border-color);border-radius:var(--radius-md);padding:1.5rem;">
          <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1rem;">
            <div style="flex:1;min-width:220px;">
              <label style="display:block;font-size:.8rem;color:#cbd5e1;margin-bottom:.35rem;font-weight:600;">Cadena a trazar:</label>
              <input type="text" id="trazaCad" value="Hola Mundo" style="width:100%;padding:.55rem .8rem;background:#070a13;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:.95rem;">
            </div>
            <div>
              <label style="display:block;font-size:.8rem;color:#cbd5e1;margin-bottom:.35rem;font-weight:600;">Algoritmo a trazar:</label>
              <select id="trazaAlgo" style="padding:.55rem .8rem;background:#070a13;border:1px solid #334155;border-radius:6px;color:#fff;font-size:.85rem;min-width:200px;">
                <option value="contar_vocales">Contar Vocales</option>
                <option value="contar_mayus">Contar Mayúsculas</option>
                <option value="contar_espacios">Contar Espacios</option>
                <option value="contar_palabras">Contar Palabras</option>
                <option value="invertir">Invertir Cadena</option>
                <option value="palindroma">Detectar Palíndroma</option>
              </select>
            </div>
            <div style="display:flex;align-items:flex-end;gap:.5rem;">
              <button class="btn-print" onclick="kitIniciarTraza()" style="background:#10b981;color:#0b1120;font-weight:bold;">▶ Iniciar Traza</button>
              <button class="btn-print" onclick="kitPasoTraza()" id="kitBtnPaso" style="display:none;background:#38bdf8;color:#0b1120;font-weight:bold;">⏭ Siguiente Paso</button>
              <button class="btn-print" onclick="kitAutoTraza()" id="kitBtnAuto" style="display:none;font-size:.8rem;">▶▶ Auto (500ms)</button>
            </div>
          </div>

          <!-- Visualizador de cadena con puntero -->
          <div style="overflow-x:auto;margin-bottom:1rem;padding:0.25rem 0;">
            <div id="trazaMemGrid" style="display:flex;gap:5px;min-width:max-content;align-items:flex-start;padding-bottom:.5rem;"></div>
          </div>

          <!-- Tabla de traza -->
          <div style="overflow-x:auto;margin-bottom:1rem;">
            <table id="trazaTable" style="width:100%;font-size:.82rem;border-collapse:collapse;">
              <thead>
                <tr id="trazaTableHead" style="background:rgba(16,185,129,.1);">
                  <th style="padding:.4rem .6rem;text-align:left;color:#10b981;border-bottom:1px solid var(--border-color);">Paso</th>
                </tr>
              </thead>
              <tbody id="trazaTableBody"></tbody>
            </table>
          </div>

          <!-- Resultado final -->
          <div id="trazaResultBox" style="display:none;background:rgba(16,185,129,.1);border:1px solid #10b981;border-radius:6px;padding:.9rem 1.1rem;font-family:'Fira Code',monospace;">
            <div style="color:#64748b;font-size:.78rem;margin-bottom:.3rem;">// RESULTADO FINAL:</div>
            <div id="trazaResultText" style="color:#10b981;font-weight:700;font-size:1.1rem;"></div>
          </div>
        </div>
      </div>

      <!-- =====================================================================
           MÓDULO 5: SIMULACRO DE EXAMEN CON TEMPORIZADOR
           ===================================================================== -->
      <div id="kit-simulacro" style="margin-bottom:1.5rem;">
        <h3 style="color:#a855f7;display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;font-size:1.3rem;">
          <span>⏱️</span> Módulo 5: Simulacro de Examen con Temporizador
        </h3>
        <p style="color:var(--text-muted);font-size:.88rem;margin-bottom:1.25rem;">
          3 ejercicios aleatorios estilo examen de la docente. Resuelve en papel o en la aplicación Delphi, luego verifica aquí. Tienes <strong>45 minutos</strong>.
        </p>

        <!-- Panel principal del simulacro -->
        <div style="background:rgba(15,23,42,.9);border:1px solid rgba(168,85,247,.3);border-radius:var(--radius-md);padding:1.5rem;">

          <!-- Controles -->
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
            <div>
              <div id="simuTimer" style="font-family:'Fira Code',monospace;font-size:2rem;font-weight:800;color:#a855f7;letter-spacing:.05em;">45:00</div>
              <div style="font-size:.78rem;color:#94a3b8;margin-top:.2rem;">Tiempo restante</div>
            </div>
            <div style="display:flex;gap:.75rem;flex-wrap:wrap;">
              <button class="btn-print" onclick="simuIniciar()" id="simuBtnIniciar" style="background:#a855f7;color:#fff;font-weight:bold;border-color:#9333ea;">
                🎲 Generar Examen &amp; Iniciar
              </button>
              <button class="btn-print" onclick="simuPausar()" id="simuBtnPausar" style="display:none;">⏸ Pausar</button>
              <button class="btn-print" onclick="simuReset()" style="font-size:.82rem;">🔄 Reiniciar</button>
            </div>
            <div id="simuScoreDisplay" style="display:none;">
              <div id="simuScoreText" style="font-size:1.5rem;font-weight:800;color:#10b981;font-family:'Fira Code',monospace;"></div>
              <div style="font-size:.78rem;color:#94a3b8;">Puntaje obtenido</div>
            </div>
          </div>

          <!-- Ejercicios del simulacro -->
          <div id="simuExercises" style="display:none;">

            <!-- Ejercicio 1 -->
            <div style="background:rgba(7,10,19,.7);border:1px solid var(--border-color);border-radius:8px;padding:1.2rem;margin-bottom:1.25rem;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.75rem;flex-wrap:wrap;gap:.5rem;">
                <h4 style="color:#38bdf8;margin:0;font-size:1rem;">📝 Ejercicio 1 <span style="font-size:.8rem;color:#94a3b8;">(10 puntos)</span></h4>
                <span id="simuQ1Badge" class="badge" style="margin:0;font-size:.75rem;"></span>
              </div>
              <p id="simuQ1Text" style="color:#f8fafc;font-size:.9rem;margin-bottom:.9rem;"></p>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">🧪 Dato de prueba de la docente:</label>
                <code id="simuQ1Input" style="background:#0b1120;padding:.35rem .65rem;border-radius:4px;color:#fbbf24;font-size:.88rem;display:block;"></code>
              </div>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">📝 Tu respuesta — Resultado esperado:</label>
                <input type="text" id="simuA1" placeholder="Escribe el resultado que calculaste..." style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:.9rem;">
              </div>
              <div id="simuFB1" style="display:none;font-size:.83rem;padding:.6rem .85rem;border-radius:6px;margin-top:.5rem;"></div>
            </div>

            <!-- Ejercicio 2 -->
            <div style="background:rgba(7,10,19,.7);border:1px solid var(--border-color);border-radius:8px;padding:1.2rem;margin-bottom:1.25rem;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.75rem;flex-wrap:wrap;gap:.5rem;">
                <h4 style="color:#10b981;margin:0;font-size:1rem;">📝 Ejercicio 2 <span style="font-size:.8rem;color:#94a3b8;">(10 puntos)</span></h4>
                <span id="simuQ2Badge" class="badge" style="margin:0;font-size:.75rem;"></span>
              </div>
              <p id="simuQ2Text" style="color:#f8fafc;font-size:.9rem;margin-bottom:.9rem;"></p>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">🧪 Dato de prueba de la docente:</label>
                <code id="simuQ2Input" style="background:#0b1120;padding:.35rem .65rem;border-radius:4px;color:#fbbf24;font-size:.88rem;display:block;"></code>
              </div>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">📝 Tu respuesta — Resultado esperado:</label>
                <input type="text" id="simuA2" placeholder="Escribe el resultado que calculaste..." style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:.9rem;">
              </div>
              <div id="simuFB2" style="display:none;font-size:.83rem;padding:.6rem .85rem;border-radius:6px;margin-top:.5rem;"></div>
            </div>

            <!-- Ejercicio 3 -->
            <div style="background:rgba(7,10,19,.7);border:1px solid var(--border-color);border-radius:8px;padding:1.2rem;margin-bottom:1.25rem;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.75rem;flex-wrap:wrap;gap:.5rem;">
                <h4 style="color:#f59e0b;margin:0;font-size:1rem;">📝 Ejercicio 3 <span style="font-size:.8rem;color:#94a3b8;">(10 puntos)</span></h4>
                <span id="simuQ3Badge" class="badge" style="margin:0;font-size:.75rem;"></span>
              </div>
              <p id="simuQ3Text" style="color:#f8fafc;font-size:.9rem;margin-bottom:.9rem;"></p>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">🧪 Dato de prueba de la docente:</label>
                <code id="simuQ3Input" style="background:#0b1120;padding:.35rem .65rem;border-radius:4px;color:#fbbf24;font-size:.88rem;display:block;"></code>
              </div>
              <div style="margin-bottom:.75rem;">
                <label style="display:block;font-size:.8rem;color:#94a3b8;margin-bottom:.35rem;">📝 Tu respuesta — Resultado esperado:</label>
                <input type="text" id="simuA3" placeholder="Escribe el resultado que calculaste..." style="width:100%;padding:.5rem .8rem;background:#0b1120;border:1px solid #334155;border-radius:6px;color:#fff;font-family:'Fira Code',monospace;font-size:.9rem;">
              </div>
              <div id="simuFB3" style="display:none;font-size:.83rem;padding:.6rem .85rem;border-radius:6px;margin-top:.5rem;"></div>
            </div>

            <!-- Botón de corrección -->
            <div style="display:flex;gap:.75rem;flex-wrap:wrap;">
              <button class="btn-print" onclick="simuCorregir()" style="background:#a855f7;color:#fff;font-weight:bold;border-color:#9333ea;padding:.6rem 1.4rem;">
                🎯 Corregir Examen
              </button>
              <button class="btn-print" onclick="simuVerSoluciones()" style="font-size:.82rem;">
                📖 Ver Soluciones Completas
              </button>
            </div>
          </div>

          <!-- Mensaje de bienvenida -->
          <div id="simuWelcome" style="text-align:center;padding:2rem 1rem;">
            <div style="font-size:3rem;margin-bottom:1rem;">🎓</div>
            <div style="color:#c084fc;font-size:1.15rem;font-weight:700;margin-bottom:.5rem;">¿Listo para el Simulacro?</div>
            <div style="color:#94a3b8;font-size:.88rem;max-width:480px;margin:0 auto;">
              Se generarán <strong>3 ejercicios aleatorios</strong> estilo examen de la docente. Resuelve cada uno en papel, luego ingresa el resultado calculado y presiona <strong>"Corregir Examen"</strong>.
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
  <!-- =========================================================================== -->
  <!-- FIN KIT COMPLETO DE PREPARACIÓN PARA EL EXAMEN DE CADENAS                  -->
  <!-- =========================================================================== -->
'''


def build_exam_kit_js():
    return r'''
  // ===========================================================================
  //      KIT COMPLETO DE PREPARACIÓN PARA EL EXAMEN — CADENAS DELPHI
  // ===========================================================================

  // ─── DATOS COMUNES ───
  const KIT_VOCALES = new Set(['A','E','I','O','U','a','e','i','o','u','Á','É','Í','Ó','Ú','á','é','í','ó','ú']);

  function kitEsVocal(c) { return KIT_VOCALES.has(c); }
  function kitEsLetra(c) { const o=c.charCodeAt(0); return (o>=65&&o<=90)||(o>=97&&o<=122); }
  function kitEsMayus(c) { const o=c.charCodeAt(0); return (o>=65&&o<=90); }
  function kitEsMinus(c) { const o=c.charCodeAt(0); return (o>=97&&o<=122); }
  function kitEsDigito(c){ const o=c.charCodeAt(0); return (o>=48&&o<=57); }

  // ─── MÓDULO 1: PATRONES ───
  let kitPatronActivo = 0;

  function kitProbarPatron(num) {
    kitPatronActivo = num;
    const pg = document.getElementById('kitPatronPlayground');
    pg.style.display = 'block';
    pg.scrollIntoView({ behavior:'smooth', block:'center' });
    const inp = document.getElementById('kitPatronInput');
    if (num === 1) inp.value = 'Universidad Gabriel Rene Moreno';
    if (num === 2) inp.value = '  El sol brilla  hoy en Santa Cruz  ';
    if (num === 3) inp.value = 'Anita lava la tina';
    if (num === 4) inp.value = 'Hola Mundo 2025';
    kitEjecutarPatron();
  }

  function kitEjecutarPatron() {
    const cad = document.getElementById('kitPatronInput').value;
    const n = cad.length;
    const res = document.getElementById('kitPatronResult');
    const exp = document.getElementById('kitPatronExplain');

    if (kitPatronActivo === 1) {
      let c = 0;
      for (let i = 0; i < n; i++) if (kitEsVocal(cad[i])) c++;
      res.innerHTML = `Vocales: <span style="color:#f59e0b;">${c}</span> &nbsp;|&nbsp; Longitud: ${n}`;
      exp.innerHTML = `Patrón 1 aplicado: recorrió ${n} posiciones, encontró ${c} vocal${c!==1?'es':''}.`;
    } else if (kitPatronActivo === 2) {
      let cant = 0, pal = '', palActual = '', palabras = [];
      let i = 0;
      while (i < n) {
        while (i < n && cad[i] === ' ') i++;
        palActual = '';
        while (i < n && cad[i] !== ' ') { palActual += cad[i]; i++; }
        if (palActual !== '') { palabras.push(palActual); cant++; }
      }
      res.innerHTML = `Palabras: <span style="color:#f59e0b;">${cant}</span> → [${palabras.map(p=>`'${p}'`).join(', ')}]`;
      exp.innerHTML = `Patrón 2 (doble bucle): detectó transiciones espacio↔carácter. Espacios extras ignorados automáticamente.`;
    } else if (kitPatronActivo === 3) {
      const cadL = cad.toLowerCase().replace(/\s/g,'');
      const inv = cadL.split('').reverse().join('');
      const esPalin = (cadL === inv);
      const invOrig = cad.split('').reverse().join('');
      res.innerHTML = `Invertida: '<span style="color:#a855f7;">${invOrig}</span>' | ¿Palíndroma?: <span style="color:${esPalin?'#10b981':'#f43f5e'};">${esPalin?'SÍ':'NO'}</span>`;
      exp.innerHTML = `Patrón 3: se acumuló carácter a carácter desde el final. La comparación ignoró espacios y mayúsculas.`;
    } else if (kitPatronActivo === 4) {
      let res2 = '';
      for (let i = 0; i < n; i++) {
        const o = cad.charCodeAt(i);
        if (o >= 97 && o <= 122) res2 += String.fromCharCode(o - 32);
        else if (o >= 65 && o <= 90) res2 += String.fromCharCode(o + 32);
        else res2 += cad[i];
      }
      res.innerHTML = `Inversión de mayús/minús: '<span style="color:#f59e0b;">${res2}</span>'`;
      exp.innerHTML = `Patrón 4 (ASCII manual): Para mayúscula (65-90): Ord(c)+32 → minúscula. Para minúscula (97-122): Ord(c)-32 → mayúscula. Dígitos y símbolos sin cambio.`;
    }
  }

  // ─── MÓDULO 2: ASCII ───
  function kitOrdConvert() {
    const c = document.getElementById('asciiCharInput').value;
    const el = document.getElementById('asciiOrdResult');
    if (!c) { el.innerHTML = ''; return; }
    const o = c.charCodeAt(0);
    let grupo = '';
    if(o>=48&&o<=57) grupo='<span style="color:#fbbf24;">(Dígito)</span>';
    else if(o>=65&&o<=90) grupo='<span style="color:#38bdf8;">(Mayúscula)</span>';
    else if(o>=97&&o<=122) grupo='<span style="color:#a855f7;">(Minúscula)</span>';
    else if(o===32) grupo='<span style="color:#fb7185;">(Espacio)</span>';
    el.innerHTML = `Ord('${c}') = <strong>${o}</strong> ${grupo} | Chr(${o}) = '${c}'`;
  }

  function kitChrConvert() {
    const code = parseInt(document.getElementById('asciiCodeInput').value,10);
    const el = document.getElementById('asciiChrResult');
    if (isNaN(code)||code<0||code>255) { el.innerHTML = ''; return; }
    const ch = String.fromCharCode(code);
    let grupo='';
    if(code>=48&&code<=57) grupo='<span style="color:#fbbf24;">(Dígito)</span>';
    else if(code>=65&&code<=90) grupo='<span style="color:#38bdf8;">(Mayúscula)</span>';
    else if(code>=97&&code<=122) grupo='<span style="color:#a855f7;">(Minúscula)</span>';
    else if(code===32) grupo='<span style="color:#fb7185;">(Espacio)</span>';
    el.innerHTML = `Chr(${code}) = '<strong>${ch}</strong>' ${grupo} | Ord('${ch}') = ${code}`;
  }

  function kitVerificarConjunto() {
    const c = document.getElementById('kitSetChar').value;
    const el = document.getElementById('kitSetResults');
    if (!c) { el.innerHTML=''; return; }
    const conjuntos = [
      { name:'voc (Vocal)', test: kitEsVocal(c) },
      { name:'mayus A..Z', test: kitEsMayus(c) },
      { name:'minus a..z', test: kitEsMinus(c) },
      { name:'digito 0..9', test: kitEsDigito(c) },
      { name:'letra A..Z a..z', test: kitEsLetra(c) },
    ];
    el.innerHTML = conjuntos.map(cv => {
      const bg = cv.test ? 'rgba(16,185,129,.2)' : 'rgba(71,85,105,.2)';
      const col = cv.test ? '#10b981' : '#64748b';
      const icon = cv.test ? '✅' : '❌';
      return `<span style="background:${bg};color:${col};padding:.2rem .55rem;border-radius:999px;font-size:.78rem;font-weight:700;border:1px solid ${col}30;">${icon} '${c}' in ${cv.name}</span>`;
    }).join('');
  }

  // ─── MÓDULO 4: TRAZA ───
  let trazaPasos = [], trazaIdx = 0, trazaAutoInterval = null;

  function kitIniciarTraza() {
    clearInterval(trazaAutoInterval);
    trazaAutoInterval = null;
    const cad = document.getElementById('trazaCad').value;
    const algo = document.getElementById('trazaAlgo').value;
    const n = cad.length;
    trazaPasos = [];

    if (algo === 'contar_vocales') {
      let c = 0;
      for (let i = 0; i < n; i++) {
        const esVoc = kitEsVocal(cad[i]);
        if (esVoc) c++;
        trazaPasos.push({ i: i+1, ch: cad[i] === ' ' ? '␣' : cad[i], esEspacio: cad[i]===' ', cond: esVoc ? 'SÍ (Vocal)' : 'No', accion: esVoc ? `contador=${c}` : '—', vars: { i: i+1, contador: c } });
      }
      trazaPasos.push({ tipo:'result', texto: `Resultado final: ${c} vocal${c!==1?'es':''}` });
    } else if (algo === 'contar_mayus') {
      let c = 0;
      for (let i = 0; i < n; i++) {
        const esM = kitEsMayus(cad[i]);
        if (esM) c++;
        trazaPasos.push({ i: i+1, ch: cad[i]===' '?'␣':cad[i], esEspacio: cad[i]===' ', cond: esM?'SÍ (Mayús)':'No', accion: esM?`contador=${c}`:'—', vars: {i:i+1, contador:c} });
      }
      trazaPasos.push({ tipo:'result', texto:`Resultado final: ${c} mayúscula${c!==1?'s':''}` });
    } else if (algo === 'contar_espacios') {
      let c = 0;
      for (let i = 0; i < n; i++) {
        const esEsp = cad[i]===' ';
        if (esEsp) c++;
        trazaPasos.push({ i:i+1, ch:esEsp?'␣':cad[i], esEspacio:esEsp, cond:esEsp?'SÍ (Espacio)':'No', accion:esEsp?`contador=${c}`:'—', vars:{i:i+1,contador:c} });
      }
      trazaPasos.push({ tipo:'result', texto:`Resultado final: ${c} espacio${c!==1?'s':''}` });
    } else if (algo === 'contar_palabras') {
      let cant=0, i=0, pal='';
      while (i<n) {
        while(i<n && cad[i]===' ') { trazaPasos.push({i:i+1, ch:'␣', esEspacio:true, cond:'Espacio → saltar', accion:'i++'  , vars:{i:i+1, palabras:cant, pal: `'${pal}'`}}); i++; }
        pal='';
        while(i<n && cad[i]!==' ') { pal+=cad[i]; trazaPasos.push({i:i+1, ch:cad[i], esEspacio:false, cond:'Capturando palabra', accion:`pal='${pal}'`, vars:{i:i+1, palabras:cant, pal:`'${pal}'`}}); i++; }
        if(pal!=='') { cant++; trazaPasos.push({i:i, ch:'—', esEspacio:false, cond:'Fin de palabra', accion:`palabras=${cant}`, vars:{i:i, palabras:cant, pal:`'${pal}'`}}); }
      }
      trazaPasos.push({ tipo:'result', texto:`Resultado final: ${cant} palabra${cant!==1?'s':''}` });
    } else if (algo === 'invertir') {
      let inv='';
      for(let i=n-1;i>=0;i--) {
        inv+=cad[i];
        trazaPasos.push({i:i+1, ch:cad[i]===' '?'␣':cad[i], esEspacio:cad[i]===' ', cond:`cad[${i+1}]`, accion:`inv='${inv}'`, vars:{i:i+1, inv:`'${inv}'`}});
      }
      trazaPasos.push({ tipo:'result', texto:`Cadena invertida: '${inv}'` });
    } else if (algo === 'palindroma') {
      const cadL=cad.toLowerCase().replace(/\s/g,'');
      let izq=0, der=cadL.length-1, esPalin=true;
      while(izq<=der) {
        const ok = cadL[izq]===cadL[der];
        if(!ok) esPalin=false;
        trazaPasos.push({i:izq+1, ch:cadL[izq], esEspacio:false, cond:`'${cadL[izq]}'=='${cadL[der]}'? ${ok?'SÍ':'NO'}`, accion:ok?'izq++, der--':'esPalin=False', vars:{izq:izq+1, der:der+1, esPalin}});
        izq++; der--;
      }
      trazaPasos.push({ tipo:'result', texto:`¿Es palíndroma?: ${esPalin?'SÍ ✅':'NO ❌'}` });
    }

    trazaIdx = 0;
    kitRenderTrazaGrid(cad, -1);
    document.getElementById('trazaResultBox').style.display='none';
    document.getElementById('kitBtnPaso').style.display='inline-flex';
    document.getElementById('kitBtnAuto').style.display='inline-flex';
    kitBuildTrazaHeaders(algo);
    document.getElementById('trazaTableBody').innerHTML='';
    showMobileToast('Traza iniciada. Presiona "Siguiente Paso" para avanzar.');
  }

  function kitBuildTrazaHeaders(algo) {
    const head = document.getElementById('trazaTableHead');
    let cols = ['Paso','i','cad[i]','Condición','Acción'];
    if(algo==='invertir') cols=['Paso','i (desde fin)','cad[i]','Variable acum.'];
    if(algo==='palindroma') cols=['Paso','izq','der','cad[izq]==cad[der]','Resultado'];
    head.innerHTML='<tr style="background:rgba(16,185,129,.1);">'+cols.map(c=>`<th style="padding:.4rem .6rem;text-align:left;color:#10b981;border-bottom:1px solid var(--border-color);font-size:.8rem;">${c}</th>`).join('')+'</tr>';
  }

  function kitRenderTrazaGrid(cad, activeIdx) {
    const grid = document.getElementById('trazaMemGrid');
    grid.innerHTML = '';
    const n = cad.length;
    for (let i=0; i<n; i++) {
      const ch = cad[i];
      const isActive = (i === activeIdx);
      const isEsp = ch===' ';
      const cell = document.createElement('div');
      cell.style.cssText=`display:flex;flex-direction:column;align-items:center;background:${isActive?'rgba(16,185,129,.3)':isEsp?'rgba(244,63,94,.1)':'rgba(30,41,59,.8)'};border:${isActive?'2px solid #10b981':'1px solid'}${isEsp?' rgba(244,63,94,.4)':isActive?'':' #334155'};border-radius:6px;min-width:40px;padding:.4rem .25rem;transition:all .2s;`;
      const cs = document.createElement('span');
      cs.style.cssText=`font-family:'Fira Code',monospace;font-size:1.1rem;font-weight:700;color:${isActive?'#10b981':isEsp?'#fb7185':'#f8fafc'};height:26px;display:flex;align-items:center;`;
      cs.innerText = isEsp?'␣':ch;
      const idx = document.createElement('span');
      idx.style.cssText=`font-family:'Fira Code',monospace;font-size:.68rem;color:${isActive?'#4ade80':'#64748b'};margin-top:.2rem;border-top:1px solid rgba(255,255,255,.08);width:100%;text-align:center;padding-top:.15rem;font-weight:${isActive?'800':'400'};`;
      idx.innerText = i+1;
      if (isActive) {
        const arrow = document.createElement('span');
        arrow.style.cssText='font-size:.6rem;color:#10b981;margin-top:-.1rem;';
        arrow.innerText='▲ i';
        cell.appendChild(arrow);
      }
      cell.appendChild(cs);
      cell.appendChild(idx);
      grid.appendChild(cell);
    }
  }

  function kitPasoTraza() {
    if (trazaIdx >= trazaPasos.length) {
      showMobileToast('Traza completada.');
      return;
    }
    const paso = trazaPasos[trazaIdx];
    const cad = document.getElementById('trazaCad').value;

    if (paso.tipo === 'result') {
      const rb = document.getElementById('trazaResultBox');
      rb.style.display='block';
      document.getElementById('trazaResultText').innerText = paso.texto;
      kitRenderTrazaGrid(cad, -1);
      trazaIdx++;
      return;
    }

    kitRenderTrazaGrid(cad, paso.i - 1);

    const tbody = document.getElementById('trazaTableBody');
    const tr = document.createElement('tr');
    tr.style.cssText=`background:rgba(16,185,129,.06);border-bottom:1px solid rgba(255,255,255,.04);`;
    const vars = paso.vars || {};
    const cells = [trazaIdx+1, paso.i, paso.ch==='␣'?`'␣' (espacio)`:`'${paso.ch}'`, paso.cond || '—', paso.accion || '—'];
    tr.innerHTML = cells.map((v,ci) => `<td style="padding:.35rem .6rem;font-family:'Fira Code',monospace;font-size:.8rem;color:${ci===2&&paso.esEspacio?'#fb7185':ci===3&&paso.cond&&paso.cond.includes('SÍ')?'#10b981':'#cbd5e1'};">${v}</td>`).join('');
    tbody.appendChild(tr);
    tbody.scrollTop = tbody.scrollHeight;

    trazaIdx++;
    if (trazaIdx >= trazaPasos.length) {
      document.getElementById('kitBtnAuto').style.display='none';
    }
  }

  function kitAutoTraza() {
    if (trazaAutoInterval) {
      clearInterval(trazaAutoInterval);
      trazaAutoInterval = null;
      document.getElementById('kitBtnAuto').innerText='▶▶ Auto (500ms)';
      return;
    }
    document.getElementById('kitBtnAuto').innerText='⏸ Detener Auto';
    trazaAutoInterval = setInterval(() => {
      if (trazaIdx >= trazaPasos.length) {
        clearInterval(trazaAutoInterval);
        trazaAutoInterval = null;
        document.getElementById('kitBtnAuto').innerText='▶▶ Auto (500ms)';
        return;
      }
      kitPasoTraza();
    }, 500);
  }

  // ─── MÓDULO 5: SIMULACRO ───
  const SIMU_BANCO = [
    { txt:'Dada la cadena cad, crea una función que cuente cuántas <strong>vocales</strong> tiene.', input:"cad = 'Universidad Gabriel Rene Moreno'", fn: c => c.split('').filter(kitEsVocal).length + ' vocal' + (c.split('').filter(kitEsVocal).length!==1?'es':''), respRef: "'Universidad Gabriel Rene Moreno' → 14 vocales" },
    { txt:'Diseña una función que cuente la cantidad de <strong>espacios en blanco</strong> en la cadena.', input:"cad = '  El sol brilla  hoy  '", fn: c => c.split('').filter(x=>x===' ').length + ' espacio' + (c.split('').filter(x=>x===' ').length!==1?'s':''), respRef:"'  El sol brilla  hoy  ' → 7 espacios" },
    { txt:'Escribe una función que <strong>cuente las palabras</strong> de la frase (puede haber espacios múltiples).', input:"cad = '  Hola   Mundo  Delphi  '", fn: c => { let i=0,cnt=0; while(i<c.length){ while(i<c.length&&c[i]===' ')i++; let p=''; while(i<c.length&&c[i]!==' '){p+=c[i];i++;} if(p!=='')cnt++; } return cnt+' palabra'+(cnt!==1?'s':''); }, respRef:"'  Hola   Mundo  Delphi  ' → 3 palabras" },
    { txt:'Crea una función que retorne la cadena con todos los caracteres <strong>en orden inverso</strong>.', input:"cad = 'Bolivar Campeon'", fn: c => "'"+c.split('').reverse().join('')+"'", respRef:"'Bolivar Campeon' → 'oepmaC raviloB'" },
    { txt:'Diseña una función que indique si la cadena es <strong>palíndroma</strong> (ignorando mayúsculas y espacios).', input:"cad = 'Anita lava la tina'", fn: c => { const l=c.toLowerCase().replace(/\s/g,''); return l===l.split('').reverse().join('')?'SÍ es palíndroma':'NO es palíndroma'; }, respRef:"'Anita lava la tina' → SÍ es palíndroma" },
    { txt:'Escribe una función que cuente cuántos <strong>dígitos numéricos</strong> hay en la cadena.', input:"cad = 'INF110-Z2 Sem 2-2025'", fn: c => c.split('').filter(kitEsDigito).length + ' dígito' + (c.split('').filter(kitEsDigito).length!==1?'s':''), respRef:"'INF110-Z2 Sem 2-2025' → 7 dígitos" },
    { txt:'Crea una función que cuente cuántas <strong>letras mayúsculas</strong> tiene la cadena.', input:"cad = 'UAGRM FICCT INF110'", fn: c => c.split('').filter(kitEsMayus).length + ' mayúscula' + (c.split('').filter(kitEsMayus).length!==1?'s':''), respRef:"'UAGRM FICCT INF110' → 12 mayúsculas" },
    { txt:'Diseña una función que cuente cuántas <strong>consonantes</strong> tiene la cadena (sin contar vocales, dígitos ni espacios).', input:"cad = 'Programacion Modular'", fn: c => { let cnt=0; for(let ch of c){ if(kitEsLetra(ch)&&!kitEsVocal(ch)) cnt++; } return cnt+' consonante'+(cnt!==1?'s':''); }, respRef:"'Programacion Modular' → 10 consonantes" },
    { txt:'Crea una función que retorne la cadena con la primera letra de <strong>cada palabra en Mayúscula</strong> (TitleCase).', input:"cad = 'hola como estas'", fn: c => c.split(' ').map(w=>w?w[0].toUpperCase()+w.slice(1):w).join(' '), respRef:"'hola como estas' → 'Hola Como Estas'" },
    { txt:'Diseña una función que elimine todos los <strong>espacios dobles o extras</strong> dejando solo un espacio entre palabras.', input:"cad = '  El   sol    brilla  '", fn: c => "'"+c.trim().replace(/\s+/g,' ')+"'", respRef:"'  El   sol    brilla  ' → 'El sol brilla'" },
  ];

  let simuActivo = false, simuInterval = null, simuSecs = 45*60;
  let simuEjIds = [], simuCads = [], simuRespCorr = [];

  function simuReset() {
    clearInterval(simuInterval);
    simuInterval = null;
    simuActivo = false;
    simuSecs = 45*60;
    document.getElementById('simuTimer').innerText = '45:00';
    document.getElementById('simuTimer').style.color = '#a855f7';
    document.getElementById('simuBtnPausar').style.display = 'none';
    document.getElementById('simuBtnIniciar').style.display = 'inline-flex';
    document.getElementById('simuExercises').style.display = 'none';
    document.getElementById('simuWelcome').style.display = 'block';
    document.getElementById('simuScoreDisplay').style.display = 'none';
    ['simuFB1','simuFB2','simuFB3'].forEach(id=>{ const el=document.getElementById(id); if(el)el.style.display='none'; });
    ['simuA1','simuA2','simuA3'].forEach(id=>{ const el=document.getElementById(id); if(el)el.value=''; });
    ['simuQ1Badge','simuQ2Badge','simuQ3Badge'].forEach(id=>{ const el=document.getElementById(id); if(el)el.innerText=''; });
  }

  function simuIniciar() {
    simuReset();
    // Elegir 3 ejercicios aleatorios sin repetir
    const shuffled = [...SIMU_BANCO].sort(()=>Math.random()-.5);
    simuEjIds = [0,1,2];
    const cads = [
      'Universidad Gabriel Rene Moreno',
      '  El sol brilla  hoy  ',
      '  Hola   Mundo  Delphi  ',
      'Bolivar Campeon',
      'Anita lava la tina',
      'INF110-Z2 Sem 2-2025',
      'UAGRM FICCT INF110',
      'Programacion Modular',
      'hola como estas',
      '  El   sol    brilla  ',
    ];

    simuRespCorr = [];
    simuCads = [];

    for (let q = 0; q < 3; q++) {
      const ej = shuffled[q];
      // Extraer la cadena del input
      const m = ej.input.match(/cad = '(.+)'/);
      const cadUsada = m ? m[1] : cads[q % cads.length];
      simuCads.push(cadUsada);

      const corrResp = ej.fn(cadUsada);
      simuRespCorr.push({ corr: corrResp, ref: ej.respRef, txt: ej.txt, input: ej.input });

      document.getElementById(`simuQ${q+1}Text`).innerHTML = ej.txt;
      document.getElementById(`simuQ${q+1}Input`).innerText = ej.input;
      document.getElementById(`simuQ${q+1}Badge`).innerText = '⏳ Pendiente';
      document.getElementById(`simuQ${q+1}Badge`).style.background = 'rgba(100,116,139,.2)';
      document.getElementById(`simuQ${q+1}Badge`).style.color = '#94a3b8';
    }

    document.getElementById('simuWelcome').style.display = 'none';
    document.getElementById('simuExercises').style.display = 'block';
    document.getElementById('simuBtnIniciar').style.display = 'none';
    document.getElementById('simuBtnPausar').style.display = 'inline-flex';
    simuActivo = true;

    simuInterval = setInterval(() => {
      if (!simuActivo) return;
      simuSecs--;
      const m = Math.floor(simuSecs / 60);
      const s = simuSecs % 60;
      const el = document.getElementById('simuTimer');
      el.innerText = String(m).padStart(2,'0') + ':' + String(s).padStart(2,'0');
      if (simuSecs <= 300) el.style.color = '#f59e0b';
      if (simuSecs <= 60) el.style.color = '#f43f5e';
      if (simuSecs <= 0) {
        clearInterval(simuInterval);
        el.innerText = '00:00';
        showMobileToast('⏰ Tiempo agotado. Revisa tus respuestas.');
        simuCorregir();
      }
    }, 1000);

    showMobileToast('Examen iniciado. Tienes 45 minutos.');
  }

  function simuPausar() {
    simuActivo = !simuActivo;
    document.getElementById('simuBtnPausar').innerText = simuActivo ? '⏸ Pausar' : '▶ Continuar';
  }

  function simuCorregir() {
    let total = 0;
    const answers = [
      document.getElementById('simuA1').value.trim(),
      document.getElementById('simuA2').value.trim(),
      document.getElementById('simuA3').value.trim(),
    ];

    for (let q = 0; q < 3; q++) {
      const userAns = answers[q].toLowerCase();
      const corrAns = simuRespCorr[q].corr.toLowerCase();
      // Extraer solo el número de la respuesta correcta para comparación flexible
      const corrNum = corrAns.match(/\d+/)?.[0];
      const userNum = userAns.match(/\d+/)?.[0];
      const ok = (corrNum && userNum && corrNum === userNum) || userAns.includes(corrAns) || corrAns.includes(userAns);

      const fb = document.getElementById(`simuFB${q+1}`);
      const badge = document.getElementById(`simuQ${q+1}Badge`);
      fb.style.display = 'block';

      if (ok) {
        total += 10;
        fb.style.background = 'rgba(16,185,129,.15)';
        fb.style.border = '1px solid #10b981';
        fb.style.color = '#10b981';
        fb.innerHTML = `✅ <strong>¡Correcto! +10 puntos.</strong><br>Resultado esperado: <code>${simuRespCorr[q].corr}</code>`;
        badge.innerText = '✅ Correcto (+10)';
        badge.style.background = 'rgba(16,185,129,.2)'; badge.style.color = '#10b981';
      } else {
        fb.style.background = 'rgba(244,63,94,.15)';
        fb.style.border = '1px solid #f43f5e';
        fb.style.color = '#fb7185';
        fb.innerHTML = `❌ <strong>Incorrecto. +0 puntos.</strong><br>Tu respuesta: <code>${answers[q]||'(en blanco)'}</code><br>Resultado correcto: <code>${simuRespCorr[q].corr}</code><br><em>Referencia: ${simuRespCorr[q].ref}</em>`;
        badge.innerText = '❌ Incorrecto';
        badge.style.background = 'rgba(244,63,94,.2)'; badge.style.color = '#fb7185';
      }
    }

    const scoreDisplay = document.getElementById('simuScoreDisplay');
    scoreDisplay.style.display = 'block';
    const scoreText = document.getElementById('simuScoreText');
    scoreText.innerText = `${total}/30 ptos.`;
    scoreText.style.color = total === 30 ? '#10b981' : total >= 18 ? '#f59e0b' : '#f43f5e';

    if (simuInterval) { clearInterval(simuInterval); simuInterval = null; }
    showMobileToast(`Examen corregido: ${total}/30 puntos.`);
  }

  function simuVerSoluciones() {
    for (let q = 0; q < 3; q++) {
      if (simuRespCorr[q]) {
        const fb = document.getElementById(`simuFB${q+1}`);
        fb.style.display = 'block';
        if (!fb.innerHTML.includes('Resultado')) {
          fb.style.background = 'rgba(56,189,248,.1)';
          fb.style.border = '1px solid #38bdf8';
          fb.style.color = '#38bdf8';
          fb.innerHTML = `📖 <strong>Solución:</strong> Resultado = <code>${simuRespCorr[q].corr}</code><br>Referencia: ${simuRespCorr[q].ref}`;
        }
      }
    }
    showMobileToast('Soluciones mostradas.');
  }
'''
