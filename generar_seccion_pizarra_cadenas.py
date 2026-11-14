# -*- coding: utf-8 -*-
"""
Generador e integrador de la sección Pizarra Cadenas 21-Octubre en teoria_programacion_modular.html
"""

import sys
import shutil

# Leer el HTML actual
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Crear backup de seguridad
shutil.copyfile('teoria_programacion_modular.html', 'teoria_programacion_modular.html.bak_pizarra_cadenas')

# Contenido de la nueva sección
section_html = '''
  <!-- =========================================================================
       SECCIÓN: EJERCICIOS DE LA PIZARRA DE HOY - CADENAS (21 DE OCTUBRE)
       DOCENTE: M.Sc. Ing. Angélica Garzón Cuéllar - INF110-Z2
       ========================================================================= -->
  <section id="pizarra-cadenas-hoy" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">✨ Pizarra Cadenas de Hoy: 5 Ejercicios Resueltos (INF110-Z2)</h2>
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">📅 Miércoles 21 de Octubre - Clase Presencial</span>
      </div>

      <!-- BANNER DE AVISOS OFICIALES DE LA PIZARRA -->
      <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(239, 68, 68, 0.12)); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 10px; padding: 1.1rem 1.3rem; margin: 1.25rem 0; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.85rem;">
          <span style="font-size: 2.2rem;">📢</span>
          <div>
            <div style="font-weight: 800; color: #fbbf24; font-size: 1.05rem;">Avisos Oficiales Anotados en la Pizarra de Hoy</div>
            <div style="color: #cbd5e1; font-size: 0.88rem;">Horarios y habilitaciones para la plataforma UAGRM informados por la docente:</div>
          </div>
        </div>
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(245, 158, 11, 0.5); padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem;">
            <strong style="color: #f59e0b;">⏰ Tarea Plataforma:</strong> <span style="color: #fff; font-weight: 600;">Hoy Miércoles 21-10 a Hs: 20:00</span>
          </div>
          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.5); padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem;">
            <strong style="color: #38bdf8;">📂 Práctico Cadena #11:</strong> <span style="color: #fff; font-weight: 600;">Habilitar 23:59</span>
          </div>
        </div>
      </div>

      <p style="margin: 1rem 0; font-size: 1.05rem; line-height: 1.6;">
        En esta clase presencial, la docente avanzó los fundamentos de <strong>manipulación vectorial de cadenas de caracteres</strong>, el cálculo de posiciones simétricas inversas con la fórmula <code style="color: #38bdf8; font-weight: bold;">N - I + 1</code>, recorrido por palabras, reconocimiento de vocales consecutivas y filtrado estricto de consonantes. A continuación dispones del <strong>Simulador VCL Interactivo</strong>, la explicación metodológica detallada, pruebas de escritorio y la <strong>Unidad Delphi (UnitPizarraCadenas.pas)</strong> lista para compilar:
      </p>

      <!-- =====================================================================
           SIMULADOR INTERACTIVO DELPHI VCL FORM (PIZARRA CADENAS)
           ===================================================================== -->
      <div class="delphi-window" style="max-width: 780px; margin: 1.75rem auto; border: 2px solid #38bdf8; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div class="delphi-titlebar" style="background: linear-gradient(90deg, #0369a1, #0284c7); display: flex; justify-content: space-between; align-items: center;">
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span>💻</span>
            <span style="font-weight: bold; letter-spacing: 0.03em;">FormPizarraCadenas - [Clase Presencial 21-Oct Delphi VCL]</span>
          </div>
          <span style="font-size: 0.8rem; font-family: monospace;">_ □ ✕</span>
        </div>
        <div class="delphi-body" style="padding: 1.5rem; background: #0f172a; color: #f8fafc;">
          
          <div style="margin-bottom: 0.85rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
            <label style="font-size: 0.88rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.05em;">
              Cadena de Entrada (Edit1.Text):
            </label>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
              <span style="font-size: 0.75rem; color: #94a3b8; align-self: center;">Ejemplos pizarra:</span>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('mundo')">"mundo"</button>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('Estudio Superior de Bolivia')">"Estudio Superior..."</button>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('ana')">"ana"</button>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('voc')">"voc"</button>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('Hola a todos los alumnos')">"Hola a todos..."</button>
              <button type="button" class="delphi-btn-vcl" style="padding: 0.2rem 0.5rem; font-size: 0.75rem; background: #1e293b; color: #38bdf8; border: 1px solid #334155; border-radius: 4px; cursor: pointer;" onclick="cargarEjemploPizarra('Hola mundo')">"Hola mundo"</button>
            </div>
          </div>

          <!-- INPUT EDIT1 -->
          <div style="margin-bottom: 1rem;">
            <input type="text" id="pizarraEdit1" class="delphi-form-edit" style="width: 100%; font-size: 1.15rem; padding: 0.65rem 0.9rem; background: #1e293b; border: 2px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; font-family: 'Fira Code', monospace;" value="mundo" placeholder="Escriba aquí la cadena de prueba...">
          </div>

          <!-- OUTPUT EDIT2 -->
          <div style="margin-bottom: 1.25rem;">
            <label style="font-size: 0.85rem; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.35rem;">
              Resultado Obtenido (Edit2.Text):
            </label>
            <input type="text" id="pizarraEdit2" class="delphi-form-edit" style="width: 100%; font-size: 1.2rem; padding: 0.65rem 0.9rem; background: #064e3b; border: 2px solid #10b981; font-weight: 800; color: #6ee7b7; border-radius: 6px; box-sizing: border-box; font-family: 'Fira Code', monospace;" readonly value="odnum" placeholder="El resultado se mostrará aquí...">
          </div>

          <!-- GRID DE BOTONES VCL -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.65rem; margin-bottom: 1.25rem;">
            <button type="button" class="delphi-btn-vcl" style="padding: 0.65rem 0.8rem; font-size: 0.88rem; font-weight: bold; background: #1e293b; color: #e2e8f0; border: 1px solid #475569; border-radius: 6px; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem;" onclick="btnPizarraEj1()">
              <span style="background: #0284c7; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;">1</span>
              <span>Invertir Cadena</span>
            </button>
            <button type="button" class="delphi-btn-vcl" style="padding: 0.65rem 0.8rem; font-size: 0.88rem; font-weight: bold; background: #1e293b; color: #e2e8f0; border: 1px solid #475569; border-radius: 6px; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem;" onclick="btnPizarraEj2()">
              <span style="background: #7c3aed; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;">2</span>
              <span>2 Vocales Juntas</span>
            </button>
            <button type="button" class="delphi-btn-vcl" style="padding: 0.65rem 0.8rem; font-size: 0.88rem; font-weight: bold; background: #1e293b; color: #e2e8f0; border: 1px solid #475569; border-radius: 6px; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem;" onclick="btnPizarraEj3()">
              <span style="background: #d97706; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;">3</span>
              <span>Verificar si es Capicúa</span>
            </button>
            <button type="button" class="delphi-btn-vcl" style="padding: 0.65rem 0.8rem; font-size: 0.88rem; font-weight: bold; background: #1e293b; color: #e2e8f0; border: 1px solid #475569; border-radius: 6px; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem;" onclick="btnPizarraEj4()">
              <span style="background: #059669; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;">4</span>
              <span>Contar Palabras</span>
            </button>
            <button type="button" class="delphi-btn-vcl" style="padding: 0.65rem 0.8rem; font-size: 0.88rem; font-weight: bold; background: #1e293b; color: #e2e8f0; border: 1px solid #475569; border-radius: 6px; cursor: pointer; text-align: left; display: flex; align-items: center; gap: 0.5rem;" onclick="btnPizarraEj5()">
              <span style="background: #e11d48; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;">5</span>
              <span>Contar Consonantes</span>
            </button>
          </div>

          <!-- PANEL DE TRAZA Y VISUALIZADOR EN VIVO -->
          <div id="pizarraLiveBox" style="background: rgba(15, 23, 42, 0.95); border: 1px solid #334155; border-radius: 8px; padding: 1rem 1.2rem;">
            <div style="font-weight: 700; color: #38bdf8; font-size: 0.9rem; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
              <span>🔍</span>
              <span>Visualizador del Algoritmo de la Pizarra:</span>
            </div>
            <div id="pizarraLiveContent" style="font-family: 'Fira Code', monospace; font-size: 0.88rem; color: #e2e8f0; line-height: 1.6;">
              Haz clic en cualquiera de los botones de arriba para ver la simulación gráfica y la traza exacta de la pizarra.
            </div>
          </div>

        </div>
      </div>

      <!-- =====================================================================
           DETALLE METODOLÓGICO Y CÓDIGO DE CADA UNO DE LOS 5 EJERCICIOS
           ===================================================================== -->
      <h3 style="color: #fff; margin: 2rem 0 1rem 0; font-size: 1.3rem; border-bottom: 2px solid #334155; padding-bottom: 0.5rem;">
        📘 Explicación Paso a Paso de los 5 Ejercicios de la Pizarra
      </h3>

      <!-- EJERCICIO 1 -->
      <div class="tag-card blue" style="margin-bottom: 2rem; border-left: 4px solid #38bdf8;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
          <h3 style="color: #38bdf8; margin: 0; font-size: 1.15rem;">① Invertir Cadena (Algoritmo Vectorial Simétrico)</h3>
          <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; border-color: rgba(56, 189, 248, 0.3);">Intercambio In-Place (Swap)</span>
        </div>
        <p style="color: #cbd5e1; margin-bottom: 0.75rem;">
          <strong>Ejemplo de la pizarra:</strong> <code>Cad = 'mundo'</code> (Longitud N = 5) &nbsp;|&nbsp; <strong>Resultado:</strong> <code>Cad = 'odnum'</code>
        </p>

        <!-- DIAGRAMA VISUAL DEL VECTOR EXPLICADO EN PIZARRA -->
        <div style="background: rgba(0,0,0,0.35); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid rgba(56,189,248,0.2);">
          <div style="font-weight: 700; color: #38bdf8; margin-bottom: 0.5rem; font-size: 0.9rem;">
            📊 Diagrama Vectorial de la Pizarra:
          </div>
          <div style="display: flex; gap: 6px; margin: 0.75rem 0; overflow-x: auto; padding-bottom: 0.5rem;">
            <div style="background: #1e293b; border: 2px solid #38bdf8; border-radius: 6px; padding: 0.5rem 0.8rem; text-align: center; min-width: 48px;">
              <div style="font-size: 0.75rem; color: #94a3b8;">I = 1</div>
              <div style="font-size: 1.25rem; font-weight: bold; color: #f8fafc;">'m'</div>
              <div style="font-size: 0.7rem; color: #38bdf8;">Aux='m'</div>
            </div>
            <div style="background: #1e293b; border: 2px solid #a855f7; border-radius: 6px; padding: 0.5rem 0.8rem; text-align: center; min-width: 48px;">
              <div style="font-size: 0.75rem; color: #94a3b8;">I = 2</div>
              <div style="font-size: 1.25rem; font-weight: bold; color: #f8fafc;">'u'</div>
              <div style="font-size: 0.7rem; color: #a855f7;">Aux='u'</div>
            </div>
            <div style="background: #0f172a; border: 2px dashed #64748b; border-radius: 6px; padding: 0.5rem 0.8rem; text-align: center; min-width: 48px;">
              <div style="font-size: 0.75rem; color: #94a3b8;">I = 3 (Centro)</div>
              <div style="font-size: 1.25rem; font-weight: bold; color: #94a3b8;">'n'</div>
              <div style="font-size: 0.7rem; color: #64748b;">(Fijo)</div>
            </div>
            <div style="background: #1e293b; border: 2px solid #a855f7; border-radius: 6px; padding: 0.5rem 0.8rem; text-align: center; min-width: 48px;">
              <div style="font-size: 0.75rem; color: #94a3b8;">Pos = 4</div>
              <div style="font-size: 1.25rem; font-weight: bold; color: #f8fafc;">'d'</div>
              <div style="font-size: 0.7rem; color: #a855f7;">5-2+1=4</div>
            </div>
            <div style="background: #1e293b; border: 2px solid #38bdf8; border-radius: 6px; padding: 0.5rem 0.8rem; text-align: center; min-width: 48px;">
              <div style="font-size: 0.75rem; color: #94a3b8;">Pos = 5 (N)</div>
              <div style="font-size: 1.25rem; font-weight: bold; color: #f8fafc;">'o'</div>
              <div style="font-size: 0.7rem; color: #38bdf8;">5-1+1=5</div>
            </div>
          </div>
          <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
            📌 <strong>Deducción de la Pizarra:</strong><br>
            • Límite del bucle: <code style="color: #38bdf8;">n1 := n div 2;</code> (5 div 2 = 2 iteraciones). Si el bucle llegara hasta N, los caracteres volverían a intercambiarse y la cadena quedaría igual.<br>
            • Fórmula del opuesto simétrico: <code style="color: #38bdf8;">N - I + 1</code>. Para I=1 &rarr; 5-1+1=5; Para I=2 &rarr; 5-2+1=4.<br>
            • <strong>Técnica de Intercambio (3 pasos):</strong><br>
            &nbsp;&nbsp;1) Guardar elemento en variable auxiliar: <code>Aux := Cad[I];</code><br>
            &nbsp;&nbsp;2) Asignar el último elemento al primer elemento: <code>Cad[I] := Cad[N - I + 1];</code><br>
            &nbsp;&nbsp;3) Recuperar de auxiliar elemento para asignar al último: <code>Cad[N - I + 1] := Aux;</code>
          </div>
        </div>

        <!-- PRUEBA DE ESCRITORIO -->
        <div style="margin-bottom: 1rem; overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; font-family: 'Fira Code', monospace; background: rgba(15,23,42,0.6); border: 1px solid #334155;">
            <thead>
              <tr style="background: rgba(56,189,248,0.15); color: #38bdf8;">
                <th style="padding: 0.5rem; border: 1px solid #334155;">Iteración (I)</th>
                <th style="padding: 0.5rem; border: 1px solid #334155;">N - I + 1</th>
                <th style="padding: 0.5rem; border: 1px solid #334155;">Aux</th>
                <th style="padding: 0.5rem; border: 1px solid #334155;">Cad[I] &larr; Cad[N-I+1]</th>
                <th style="padding: 0.5rem; border: 1px solid #334155;">Cad[N-I+1] &larr; Aux</th>
                <th style="padding: 0.5rem; border: 1px solid #334155;">Cadena Actual</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">Inicio</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">-</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">-</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">-</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">-</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; color: #94a3b8;">'mundo'</td>
              </tr>
              <tr>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center; color: #38bdf8;">I = 1</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">5 - 1 + 1 = 5</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center; color: #fbbf24;">'m'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155;">Cad[1] := 'o'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155;">Cad[5] := 'm'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; color: #38bdf8;">'oundm'</td>
              </tr>
              <tr>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center; color: #a855f7;">I = 2</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center;">5 - 2 + 1 = 4</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; text-align: center; color: #fbbf24;">'u'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155;">Cad[2] := 'd'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155;">Cad[4] := 'u'</td>
                <td style="padding: 0.5rem; border: 1px solid #334155; color: #10b981; font-weight: bold;">'odnum' (Fin)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
          <div class="code-block">
<span class="comment">// Procedimiento In-Place exacto como en la pizarra</span><br>
<span class="keyword">procedure</span> <span class="function-name">InvertirCadena</span>(<span class="keyword">var</span> Cad: <span class="type">string</span>);<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, n, n1, opp: <span class="type">integer</span>;<br>
&nbsp;&nbsp;aux: <span class="type">char</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;n := <span class="function-name">Length</span>(Cad);<br>
&nbsp;&nbsp;n1 := n <span class="keyword">div</span> <span class="number">2</span>; <span class="comment">// Solo hasta la mitad</span><br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> n1 <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;opp := n - i + <span class="number">1</span>; <span class="comment">// Formula pizarra: N - I + 1</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;aux := Cad[i];&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">// 1) Guardar elemento en variable auxiliar</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Cad[i] := Cad[opp];<span class="comment">// 2) Asignar ultimo al primer elemento</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Cad[opp] := aux;&nbsp;&nbsp;&nbsp;<span class="comment">// 3) Recuperar de auxiliar elemento</span><br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// Evento del botón en Delphi VCL</span><br>
<span class="keyword">procedure</span> TForm1.Button1Click(Sender: TObject);<br>
<span class="keyword">var</span> s: <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;s := Edit1.Text;<br>
&nbsp;&nbsp;<span class="function-name">InvertirCadena</span>(s);<br>
&nbsp;&nbsp;Edit2.Text := s;<br>
<span class="keyword">end</span>;
          </div>
        </div>
      </div>

      <!-- EJERCICIO 2 -->
      <div class="tag-card purple" style="margin-bottom: 2rem; border-left: 4px solid #a855f7;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
          <h3 style="color: #a855f7; margin: 0; font-size: 1.15rem;">② Contar las palabras donde existan 2 vocales juntas</h3>
          <span class="badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border-color: rgba(168, 85, 247, 0.3);">Descomposición Modular</span>
        </div>
        <p style="color: #cbd5e1; margin-bottom: 0.75rem;">
          <strong>Ejemplo de la pizarra:</strong> <code>Cad = 'Estudio Superior de Bolivia'</code> &nbsp;|&nbsp; <strong>Resultado:</strong> <code>CantPal = 3 palabras</code>
        </p>

        <div style="background: rgba(0,0,0,0.35); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid rgba(168, 85, 247, 0.2);">
          <div style="font-weight: 700; color: #c084fc; margin-bottom: 0.5rem; font-size: 0.9rem;">
            🔍 Análisis Palabra por Palabra de la Pizarra:
          </div>
          <div style="display: flex; gap: 0.6rem; flex-wrap: wrap; margin-bottom: 0.75rem;">
            <div style="background: #1e293b; border: 1px solid #10b981; border-radius: 6px; padding: 0.5rem 0.8rem;">
              <span style="font-weight: bold; color: #fff;">"Estud<span style="color:#10b981; text-decoration: underline;">io</span>"</span>
              <div style="font-size: 0.75rem; color: #10b981;">✅ Cumple ('io' juntas)</div>
            </div>
            <div style="background: #1e293b; border: 1px solid #10b981; border-radius: 6px; padding: 0.5rem 0.8rem;">
              <span style="font-weight: bold; color: #fff;">"Super<span style="color:#10b981; text-decoration: underline;">io</span>r"</span>
              <div style="font-size: 0.75rem; color: #10b981;">✅ Cumple ('io' juntas)</div>
            </div>
            <div style="background: #1e293b; border: 1px solid #64748b; border-radius: 6px; padding: 0.5rem 0.8rem;">
              <span style="font-weight: bold; color: #94a3b8;">"de"</span>
              <div style="font-size: 0.75rem; color: #ef4444;">❌ No cumple (solo 'e')</div>
            </div>
            <div style="background: #1e293b; border: 1px solid #10b981; border-radius: 6px; padding: 0.5rem 0.8rem;">
              <span style="font-weight: bold; color: #fff;">"Boliv<span style="color:#10b981; text-decoration: underline;">ia</span>"</span>
              <div style="font-size: 0.75rem; color: #10b981;">✅ Cumple ('ia' juntas)</div>
            </div>
          </div>
          <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
            📌 <strong>Estrategia Modular Recomendada:</strong><br>
            • Sub-módulo <code>EsVocal(c: char): boolean</code> &rarr; Verifica si un caracter pertenece a <code>['A','E','I','O','U']</code>.<br>
            • Sub-módulo <code>TieneDosVocalesJuntas(pal: string): boolean</code> &rarr; Recorre desde <code>1 to Length(pal)-1</code> evaluando si <code>EsVocal(pal[i]) and EsVocal(pal[i+1])</code>.<br>
            • Módulo Principal &rarr; Tokeniza las palabras y cuenta únicamente las que retornen <code>True</code>.
          </div>
        </div>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
          <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EsVocal</span>(c: <span class="type">char</span>): <span class="type">boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;c := <span class="function-name">UpCase</span>(c);<br>
&nbsp;&nbsp;Result := (c = <span class="string">'A'</span>) <span class="keyword">or</span> (c = <span class="string">'E'</span>) <span class="keyword">or</span> (c = <span class="string">'I'</span>) <span class="keyword">or</span> (c = <span class="string">'O'</span>) <span class="keyword">or</span> (c = <span class="string">'U'</span>);<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">TieneDosVocalesJuntas</span>(pal: <span class="type">string</span>): <span class="type">boolean</span>;<br>
<span class="keyword">var</span> i: <span class="type">integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Result := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(pal) - <span class="number">1</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsVocal</span>(pal[i]) <span class="keyword">and</span> <span class="function-name">EsVocal</span>(pal[i + <span class="number">1</span>]) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result := <span class="keyword">True</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">Exit</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">ContarPalabrasDosVocalesJuntas</span>(Cad: <span class="type">string</span>): <span class="type">integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">integer</span>;<br>
&nbsp;&nbsp;pal: <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Cad := <span class="function-name">Trim</span>(Cad) + <span class="string">' '</span>; <span class="comment">// Centinela para procesar la última palabra</span><br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;pal := <span class="string">''</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Cad[i] &lt;&gt; <span class="string">' '</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pal := pal + Cad[i]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (pal &lt;&gt; <span class="string">''</span>) <span class="keyword">and</span> <span class="function-name">TieneDosVocalesJuntas</span>(pal) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pal := <span class="string">''</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;
          </div>
        </div>
      </div>

      <!-- EJERCICIO 3 -->
      <div class="tag-card amber" style="margin-bottom: 2rem; border-left: 4px solid #f59e0b;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
          <h3 style="color: #f59e0b; margin: 0; font-size: 1.15rem;">③ Leer una cadena y Verificar si es Capicúa al invertir</h3>
          <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; border-color: rgba(245, 158, 11, 0.3);">Palíndromos / Simetría</span>
        </div>
        <p style="color: #cbd5e1; margin-bottom: 0.75rem;">
          <strong>Ejemplos de la pizarra:</strong><br>
          • <code>Cad = 'ana'</code> &nbsp;&rarr;&nbsp; inv: <code>'ana'</code> &nbsp;&rarr;&nbsp; <strong style="color: #10b981;">✓ (Sí es Capicúa)</strong><br>
          • <code>Cad = 'voc'</code> &nbsp;&rarr;&nbsp; inv: <code>'cov'</code> &nbsp;&rarr;&nbsp; <strong style="color: #ef4444;">✕ (voc = cov No)</strong>
        </p>

        <div style="background: rgba(0,0,0,0.35); padding: 0.85rem 1.15rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid rgba(245, 158, 11, 0.2); font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
          📌 <strong>Principio de Solución:</strong><br>
          En palabras suele llamarse <em>palíndromo</em>, pero la docente lo enunció como <strong>"Capicúa al invertir"</strong> para conectar con la lógica aprendida en números naturales. Podemos reutilizar el procedimiento <code style="color: #38bdf8;">InvertirCadena</code> del Ejercicio 1 y comparar <code>Cad = inv</code> (insensible a mayúsculas/minúsculas con <code>AnsiLowerCase</code>).
        </div>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
          <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EsCapicua</span>(Cad: <span class="type">string</span>): <span class="type">boolean</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;inv: <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;inv := Cad;<br>
&nbsp;&nbsp;<span class="function-name">InvertirCadena</span>(inv); <span class="comment">// Reutiliza el Ejercicio 1 de la pizarra</span><br>
&nbsp;&nbsp;Result := (<span class="function-name">AnsiLowerCase</span>(Cad) = <span class="function-name">AnsiLowerCase</span>(inv));<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// Evento del botón en Delphi VCL</span><br>
<span class="keyword">procedure</span> TForm1.Button3Click(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsCapicua</span>(Edit1.Text) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit2.Text := <span class="string">'SI es Capicua'</span><br>
&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit2.Text := <span class="string">'NO es Capicua'</span>;<br>
<span class="keyword">end</span>;
          </div>
        </div>
      </div>

      <!-- EJERCICIO 4 -->
      <div class="tag-card emerald" style="margin-bottom: 2rem; border-left: 4px solid #10b981;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
          <h3 style="color: #10b981; margin: 0; font-size: 1.15rem;">④ Contar palabras de una cadena</h3>
          <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399; border-color: rgba(16, 185, 129, 0.3);">Máquina de Estados / Delimitadores</span>
        </div>
        <p style="color: #cbd5e1; margin-bottom: 0.75rem;">
          <strong>Ejemplo de la pizarra:</strong> <code>Cad = 'Hola a todos los alumnos'</code> &nbsp;|&nbsp; <strong>Resultado:</strong> <code>CantPal = 5 palabras</code>
        </p>

        <div style="background: rgba(0,0,0,0.35); padding: 0.85rem 1.15rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid rgba(16, 185, 129, 0.2); font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
          📌 <strong>Trampa Clásica de Examen Resuelta:</strong><br>
          Si el usuario introduce espacios dobles, triples o espacios al principio/final (ej: <code>'  Hola   mundo  '</code>), contar simplemente espacios daría un resultado incorrecto. La técnica estándar de la docente utiliza una bandera booleana <code>enPalabra</code>: cada vez que pasamos de espacio a una letra válida, incrementamos el contador.
        </div>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
          <div class="code-block">
<span class="keyword">function</span> <span class="function-name">ContarPalabras</span>(Cad: <span class="type">string</span>): <span class="type">integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">integer</span>;<br>
&nbsp;&nbsp;enPalabra: <span class="type">boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;enPalabra := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Cad[i] &lt;&gt; <span class="string">' '</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="keyword">not</span> enPalabra <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enPalabra := <span class="keyword">True</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enPalabra := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;
          </div>
        </div>
      </div>

      <!-- EJERCICIO 5 -->
      <div class="tag-card rose" style="margin-bottom: 2rem; border-left: 4px solid #f43f5e;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.5rem;">
          <h3 style="color: #f43f5e; margin: 0; font-size: 1.15rem;">⑤ Contar Consonantes (no son vocales)</h3>
          <span class="badge" style="background: rgba(244, 63, 94, 0.15); color: #fb7185; border-color: rgba(244, 63, 94, 0.3);">Filtro Alfabético Estricto</span>
        </div>
        <p style="color: #cbd5e1; margin-bottom: 0.75rem;">
          <strong>Ejemplo de la pizarra:</strong> <code>Cad = 'Hola mundo'</code> &nbsp;|&nbsp; <strong>Resultado:</strong> <code>CantCons = 5</code> (letras: H, l, m, n, d)
        </p>

        <!-- DIAGRAMA CON FLECHAS DE LA PIZARRA -->
        <div style="background: rgba(0,0,0,0.35); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid rgba(244, 63, 94, 0.2);">
          <div style="font-weight: 700; color: #fb7185; margin-bottom: 0.5rem; font-size: 0.9rem;">
            🎯 Flechas Analíticas Dibujadas en la Pizarra:
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin: 0.75rem 0;">
            <div style="text-align: center; background: #1e293b; border: 1px solid #10b981; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #fff; font-size: 1.1rem;">H</span>
              <div style="font-size: 0.7rem; color: #10b981;">↑ Cons (1)</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #64748b; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #94a3b8; font-size: 1.1rem;">o</span>
              <div style="font-size: 0.7rem; color: #38bdf8;">Vocal</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #10b981; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #fff; font-size: 1.1rem;">l</span>
              <div style="font-size: 0.7rem; color: #10b981;">↑ Cons (2)</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #64748b; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #94a3b8; font-size: 1.1rem;">a</span>
              <div style="font-size: 0.7rem; color: #38bdf8;">Vocal</div>
            </div>
            <div style="text-align: center; background: #0f172a; border: 1px dashed #475569; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #64748b; font-size: 1.1rem;">_</span>
              <div style="font-size: 0.7rem; color: #64748b;">Espacio</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #10b981; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #fff; font-size: 1.1rem;">m</span>
              <div style="font-size: 0.7rem; color: #10b981;">↑ Cons (3)</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #64748b; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #94a3b8; font-size: 1.1rem;">u</span>
              <div style="font-size: 0.7rem; color: #38bdf8;">Vocal</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #10b981; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #fff; font-size: 1.1rem;">n</span>
              <div style="font-size: 0.7rem; color: #10b981;">↑ Cons (4)</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #10b981; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #fff; font-size: 1.1rem;">d</span>
              <div style="font-size: 0.7rem; color: #10b981;">↑ Cons (5)</div>
            </div>
            <div style="text-align: center; background: #1e293b; border: 1px solid #64748b; padding: 0.35rem 0.6rem; border-radius: 6px;">
              <span style="font-weight: bold; color: #94a3b8; font-size: 1.1rem;">o</span>
              <div style="font-size: 0.7rem; color: #38bdf8;">Vocal</div>
            </div>
          </div>
          <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5;">
            ⚠️ <strong>Punto Crítico Evaluado por la Docente:</strong><br>
            La nota <em>"(no son vocales)"</em> escrita en la pizarra implica que <strong>debe ser una letra del alfabeto</strong> (A..Z) y a la vez no estar en el conjunto de vocales. Si solo preguntáramos <code>not EsVocal(c)</code>, los espacios <code>' '</code>, signos <code>','</code> y números <code>'9'</code> serían contados por error como consonantes. Por eso la condición formal es: <code>(c in ['A'..'Z']) and not (c in ['A', 'E', 'I', 'O', 'U'])</code>.
          </div>
        </div>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
          <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EsConsonante</span>(c: <span class="type">char</span>): <span class="type">boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;c := <span class="function-name">UpCase</span>(c);<br>
&nbsp;&nbsp;<span class="comment">// Letra del abecedario y NO vocal</span><br>
&nbsp;&nbsp;Result := (c <span class="keyword">in</span> [<span class="string">'A'</span>..<span class="string">'Z'</span>]) <span class="keyword">and</span> <span class="keyword">not</span> (c <span class="keyword">in</span> [<span class="string">'A'</span>, <span class="string">'E'</span>, <span class="string">'I'</span>, <span class="string">'O'</span>, <span class="string">'U'</span>]);<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">ContarConsonantes</span>(Cad: <span class="type">string</span>): <span class="type">integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsConsonante</span>(Cad[i]) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;
          </div>
        </div>
      </div>

      <!-- =====================================================================
           UNIDAD COMPLETA EN DELPHI: UnitPizarraCadenas.pas
           ===================================================================== -->
      <div class="card" style="margin-top: 2rem; background: rgba(15,23,42,0.85); border: 1px solid #334155;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
          <div>
            <h3 style="color: #38bdf8; margin: 0; font-size: 1.15rem;">📁 Código Fuente Completo: UnitPizarraCadenas.pas</h3>
            <span style="font-size: 0.8rem; color: #94a3b8;">Unidad compilable probada con Free Pascal / Delphi 10/11/12</span>
          </div>
          <span class="badge" style="background: rgba(16,185,129,0.15); color: #10b981; border-color: rgba(16,185,129,0.3);">100% Validado con fpc</span>
        </div>
        <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 1rem;">
          Esta unidad ha sido creada en la raíz de tu proyecto como <code>UnitPizarraCadenas.pas</code>. Puedes usarla directamente en Delphi agregándola al <code>uses</code> de tu Formulario principal.
        </p>

        <div class="code-wrapper">
          <button class="copy-btn" onclick="copyCode(this)">Copiar Unidad Completa</button>
          <div class="code-block">
<span class="keyword">unit</span> UnitPizarraCadenas;<br><br>
<span class="keyword">interface</span><br><br>
<span class="keyword">uses</span> SysUtils;<br><br>
<span class="comment">// Funciones Auxiliares</span><br>
<span class="keyword">function</span> <span class="function-name">EsVocal</span>(c: <span class="type">Char</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">function</span> <span class="function-name">EsConsonante</span>(c: <span class="type">Char</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">function</span> <span class="function-name">TieneDosVocalesJuntas</span>(pal: <span class="type">string</span>): <span class="type">Boolean</span>;<br><br>
<span class="comment">// 5 Ejercicios de la Pizarra INF110-Z2</span><br>
<span class="keyword">procedure</span> <span class="function-name">InvertirCadena</span>(<span class="keyword">var</span> Cad: <span class="type">string</span>);<br>
<span class="keyword">function</span> <span class="function-name">InvertirCadenaFn</span>(Cad: <span class="type">string</span>): <span class="type">string</span>;<br>
<span class="keyword">function</span> <span class="function-name">ContarPalabrasDosVocalesJuntas</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br>
<span class="keyword">function</span> <span class="function-name">EsCapicua</span>(Cad: <span class="type">string</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">function</span> <span class="function-name">ContarPalabras</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br>
<span class="keyword">function</span> <span class="function-name">ContarConsonantes</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br><br>
<span class="keyword">implementation</span><br><br>
<span class="keyword">function</span> <span class="function-name">EsVocal</span>(c: <span class="type">Char</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;c := <span class="function-name">UpCase</span>(c);<br>
&nbsp;&nbsp;Result := (c = <span class="string">'A'</span>) <span class="keyword">or</span> (c = <span class="string">'E'</span>) <span class="keyword">or</span> (c = <span class="string">'I'</span>) <span class="keyword">or</span> (c = <span class="string">'O'</span>) <span class="keyword">or</span> (c = <span class="string">'U'</span>);<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">EsConsonante</span>(c: <span class="type">Char</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;c := <span class="function-name">UpCase</span>(c);<br>
&nbsp;&nbsp;Result := (c <span class="keyword">in</span> [<span class="string">'A'</span>..<span class="string">'Z'</span>]) <span class="keyword">and</span> <span class="keyword">not</span> (c <span class="keyword">in</span> [<span class="string">'A'</span>, <span class="string">'E'</span>, <span class="string">'I'</span>, <span class="string">'O'</span>, <span class="string">'U'</span>]);<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">TieneDosVocalesJuntas</span>(pal: <span class="type">string</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">var</span> i: <span class="type">Integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Result := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(pal) - <span class="number">1</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsVocal</span>(pal[i]) <span class="keyword">and</span> <span class="function-name">EsVocal</span>(pal[i + <span class="number">1</span>]) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result := <span class="keyword">True</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">Exit</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">procedure</span> <span class="function-name">InvertirCadena</span>(<span class="keyword">var</span> Cad: <span class="type">string</span>);<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, n, n1, opp: <span class="type">Integer</span>;<br>
&nbsp;&nbsp;aux: <span class="type">Char</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;n := <span class="function-name">Length</span>(Cad);<br>
&nbsp;&nbsp;n1 := n <span class="keyword">div</span> <span class="number">2</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> n1 <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;opp := n - i + <span class="number">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;aux := Cad[i];<br>
&nbsp;&nbsp;&nbsp;&nbsp;Cad[i] := Cad[opp];<br>
&nbsp;&nbsp;&nbsp;&nbsp;Cad[opp] := aux;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">InvertirCadenaFn</span>(Cad: <span class="type">string</span>): <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="function-name">InvertirCadena</span>(Cad);<br>
&nbsp;&nbsp;Result := Cad;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">ContarPalabrasDosVocalesJuntas</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">Integer</span>;<br>
&nbsp;&nbsp;pal: <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Cad := <span class="function-name">Trim</span>(Cad) + <span class="string">' '</span>;<br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;pal := <span class="string">''</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Cad[i] &lt;&gt; <span class="string">' '</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pal := pal + Cad[i]<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (pal &lt;&gt; <span class="string">''</span>) <span class="keyword">and</span> <span class="function-name">TieneDosVocalesJuntas</span>(pal) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pal := <span class="string">''</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">EsCapicua</span>(Cad: <span class="type">string</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">var</span> inv: <span class="type">string</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;inv := <span class="function-name">InvertirCadenaFn</span>(Cad);<br>
&nbsp;&nbsp;Result := (<span class="function-name">AnsiLowerCase</span>(Cad) = <span class="function-name">AnsiLowerCase</span>(inv));<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">ContarPalabras</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">Integer</span>;<br>
&nbsp;&nbsp;enPalabra: <span class="type">Boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;enPalabra := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Cad[i] &lt;&gt; <span class="string">' '</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="keyword">not</span> enPalabra <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enPalabra := <span class="keyword">True</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enPalabra := <span class="keyword">False</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">function</span> <span class="function-name">ContarConsonantes</span>(Cad: <span class="type">string</span>): <span class="type">Integer</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;i, cant: <span class="type">Integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;cant := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> <span class="function-name">Length</span>(Cad) <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsConsonante</span>(Cad[i]) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cant := cant + <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;Result := cant;<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">end</span>.
          </div>
        </div>
      </div>

    </div>
  </section>
'''

# 2. Código JavaScript para los interactivos
js_pizarra = '''
  // =========================================================================
  // SIMULADOR INTERACTIVO PIZARRA DE CADENAS (21 DE OCTUBRE)
  // =========================================================================
  function cargarEjemploPizarra(txt) {
    const edit1 = document.getElementById('pizarraEdit1');
    if (edit1) edit1.value = txt;
  }

  function btnPizarraEj1() {
    const edit1 = document.getElementById('pizarraEdit1');
    const edit2 = document.getElementById('pizarraEdit2');
    const box = document.getElementById('pizarraLiveContent');
    const cad = edit1.value;
    const n = cad.length;
    const n1 = Math.floor(n / 2);
    let arr = cad.split('');
    let traceRows = [];

    for (let i = 1; i <= n1; i++) {
      const opp = n - i + 1; // 1-indexed formula
      const aux = arr[i - 1];
      traceRows.push(`<tr>
        <td style="padding: 4px 8px; border: 1px solid #334155; text-align: center; color: #38bdf8;">I = ${i}</td>
        <td style="padding: 4px 8px; border: 1px solid #334155; text-align: center;">${n} - ${i} + 1 = <strong>${opp}</strong></td>
        <td style="padding: 4px 8px; border: 1px solid #334155; text-align: center; color: #fbbf24;">'${aux}'</td>
        <td style="padding: 4px 8px; border: 1px solid #334155;">Cad[${i}] &larr; Cad[${opp}] ('${arr[opp - 1]}')</td>
        <td style="padding: 4px 8px; border: 1px solid #334155;">Cad[${opp}] &larr; Aux ('${aux}')</td>
      </tr>`);
      arr[i - 1] = arr[opp - 1];
      arr[opp - 1] = aux;
    }

    const resultado = arr.join('');
    edit2.value = resultado;

    box.innerHTML = `
      <div style="margin-bottom: 0.6rem; color: #38bdf8; font-weight: bold;">
        🔄 Ejercicio 1: Invertir Cadena in-place (N = ${n}, Bucle hasta n div 2 = ${n1})
      </div>
      <div style="margin-bottom: 0.6rem; color: #cbd5e1;">
        Cadena Original: <span style="color: #f8fafc; font-weight: bold;">"${cad}"</span> &rarr; Invertida: <span style="color: #10b981; font-weight: bold;">"${resultado}"</span>
      </div>
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.8rem; background: #0b1120;">
          <thead>
            <tr style="background: rgba(56,189,248,0.2); color: #38bdf8;">
              <th style="padding: 4px 8px; border: 1px solid #334155;">Iteración</th>
              <th style="padding: 4px 8px; border: 1px solid #334155;">Fórmula N - I + 1</th>
              <th style="padding: 4px 8px; border: 1px solid #334155;">Aux</th>
              <th style="padding: 4px 8px; border: 1px solid #334155;">Paso 2: Cad[I] := Cad[opp]</th>
              <th style="padding: 4px 8px; border: 1px solid #334155;">Paso 3: Cad[opp] := Aux</th>
            </tr>
          </thead>
          <tbody>
            ${traceRows.length > 0 ? traceRows.join('') : '<tr><td colspan="5" style="text-align: center; padding: 6px;">Cadena de 0 o 1 caracter (no requiere swaps).</td></tr>'}
          </tbody>
        </table>
      </div>
    `;
  }

  function btnPizarraEj2() {
    const edit1 = document.getElementById('pizarraEdit1');
    const edit2 = document.getElementById('pizarraEdit2');
    const box = document.getElementById('pizarraLiveContent');
    const cad = edit1.value.trim();
    if (!cad) {
      edit2.value = '0 palabras';
      box.innerHTML = 'Cadena vacía.';
      return;
    }

    const words = cad.split(/\\s+/);
    const esVocal = c => /[aeiouáéíóú]/i.test(c);
    let count = 0;
    let cardsHtml = [];

    words.forEach(w => {
      let tiene = false;
      let pares = [];
      for (let i = 0; i < w.length - 1; i++) {
        if (esVocal(w[i]) && esVocal(w[i+1])) {
          tiene = true;
          pares.push(w[i] + w[i+1]);
        }
      }
      if (tiene) {
        count++;
        cardsHtml.push(`<span style="background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #6ee7b7; padding: 3px 8px; border-radius: 6px; margin: 2px;">
          "${w}" (✅ ${pares.join(', ')})
        </span>`);
      } else {
        cardsHtml.push(`<span style="background: rgba(239,68,68,0.1); border: 1px solid #64748b; color: #94a3b8; padding: 3px 8px; border-radius: 6px; margin: 2px;">
          "${w}" (❌)
        </span>`);
      }
    });

    edit2.value = `${count} palabra${count === 1 ? '' : 's'}`;

    box.innerHTML = `
      <div style="margin-bottom: 0.6rem; color: #a855f7; font-weight: bold;">
        🔍 Ejercicio 2: Palabras donde existen 2 vocales juntas (Total = ${count} palabras)
      </div>
      <div style="margin-bottom: 0.6rem; display: flex; flex-wrap: wrap; gap: 4px;">
        ${cardsHtml.join('')}
      </div>
      <div style="font-size: 0.8rem; color: #94a3b8;">
        Condición evaluada: <code>EsVocal(pal[i]) and EsVocal(pal[i+1])</code> palabra por palabra.
      </div>
    `;
  }

  function btnPizarraEj3() {
    const edit1 = document.getElementById('pizarraEdit1');
    const edit2 = document.getElementById('pizarraEdit2');
    const box = document.getElementById('pizarraLiveContent');
    const cad = edit1.value;
    const inv = cad.split('').reverse().join('');
    const esCap = (cad.toLowerCase() === inv.toLowerCase());

    edit2.value = esCap ? 'SI es Capicua' : 'NO es Capicua';

    box.innerHTML = `
      <div style="margin-bottom: 0.6rem; color: #f59e0b; font-weight: bold;">
        🔁 Ejercicio 3: Verificar Capicúa al Invertir
      </div>
      <div style="font-size: 0.95rem; margin-bottom: 0.5rem;">
        • Cadena Original: <strong style="color: #38bdf8;">"${cad}"</strong><br>
        • Cadena Invertida: <strong style="color: #fbbf24;">"${inv}"</strong>
      </div>
      <div style="padding: 0.5rem 0.8rem; border-radius: 6px; background: ${esCap ? 'rgba(16,185,129,0.2)' : 'rgba(239,68,68,0.2)'}; border: 1px solid ${esCap ? '#10b981' : '#ef4444'}; color: ${esCap ? '#34d399' : '#f87171'}; font-weight: bold;">
        ${esCap ? '✓ VERIFICACIÓN EXITOSA: "'+cad+'" = "'+inv+'" &rarr; La cadena SI es capicúa / palíndromo.' : '✕ NO COINCIDEN: "'+cad+'" &ne; "'+inv+'" &rarr; voc = cov No.'}
      </div>
    `;
  }

  function btnPizarraEj4() {
    const edit1 = document.getElementById('pizarraEdit1');
    const edit2 = document.getElementById('pizarraEdit2');
    const box = document.getElementById('pizarraLiveContent');
    const cad = edit1.value;
    const trimmed = cad.trim();
    const words = trimmed ? trimmed.split(/\\s+/) : [];
    const count = words.length;

    edit2.value = `${count} palabra${count === 1 ? '' : 's'}`;

    const chips = words.map((w, idx) => `<span style="background: rgba(56,189,248,0.15); border: 1px solid #38bdf8; color: #fff; padding: 3px 8px; border-radius: 6px; margin: 2px;">
      <strong style="color: #38bdf8;">${idx + 1}.</strong> ${w}
    </span>`).join('');

    box.innerHTML = `
      <div style="margin-bottom: 0.6rem; color: #10b981; font-weight: bold;">
        📝 Ejercicio 4: Contar palabras de una cadena (Total = ${count})
      </div>
      <div style="margin-bottom: 0.6rem; display: flex; flex-wrap: wrap; gap: 4px;">
        ${chips || '<span style="color: #94a3b8;">Cadena vacía o solo espacios.</span>'}
      </div>
      <div style="font-size: 0.8rem; color: #94a3b8;">
        La máquina de estados con la bandera <code>enPalabra</code> ignora dobles espacios y espacios en los extremos.
      </div>
    `;
  }

  function btnPizarraEj5() {
    const edit1 = document.getElementById('pizarraEdit1');
    const edit2 = document.getElementById('pizarraEdit2');
    const box = document.getElementById('pizarraLiveContent');
    const cad = edit1.value;

    const esLetra = c => /[a-záéíóúñ]/i.test(c);
    const esVocal = c => /[aeiouáéíóú]/i.test(c);

    let consonantes = [];
    let breakdown = [];
    let count = 0;

    for (let i = 0; i < cad.length; i++) {
      const c = cad[i];
      if (esLetra(c) && !esVocal(c)) {
        count++;
        consonantes.push(c);
        breakdown.push(`<span style="background: rgba(16,185,129,0.25); border: 1px solid #10b981; color: #6ee7b7; padding: 2px 6px; border-radius: 4px; font-weight: bold;" title="Consonante">${c}</span>`);
      } else if (esVocal(c)) {
        breakdown.push(`<span style="background: rgba(56,189,248,0.1); border: 1px solid #38bdf8; color: #38bdf8; padding: 2px 6px; border-radius: 4px;" title="Vocal">${c}</span>`);
      } else if (c === ' ') {
        breakdown.push(`<span style="background: #1e293b; color: #64748b; padding: 2px 6px; border-radius: 4px;" title="Espacio">&middot;</span>`);
      } else {
        breakdown.push(`<span style="background: #1e293b; color: #94a3b8; padding: 2px 6px; border-radius: 4px;" title="Símbolo">${c}</span>`);
      }
    }

    edit2.value = `${count} consonante${count === 1 ? '' : 's'}`;

    box.innerHTML = `
      <div style="margin-bottom: 0.6rem; color: #f43f5e; font-weight: bold;">
        🔡 Ejercicio 5: Contar Consonantes (Total = ${count})
      </div>
      <div style="margin-bottom: 0.6rem; display: flex; flex-wrap: wrap; gap: 4px; font-size: 1.05rem;">
        ${breakdown.join('')}
      </div>
      <div style="font-size: 0.8rem; color: #cbd5e1;">
        <span style="color: #6ee7b7; font-weight: bold;">■ Consonantes encontradas (${count}):</span> [ ${consonantes.join(', ')} ]<br>
        <span style="color: #94a3b8;">Filtro: Letra del alfabeto y NO vocal (espacios y puntuación descartados).</span>
      </div>
    `;
  }
'''

# 3. Insertar la nueva sección justo después de ejercicios-pizarra
pos_pizarra = html.find('id="ejercicios-pizarra"')
pos_sec_end = html.find('</section>', pos_pizarra) + 10

if pos_pizarra == -1 or pos_sec_end == -1:
    print("Error: No se encontró la sección ejercicios-pizarra")
    sys.exit(1)

html_new = html[:pos_sec_end] + "\n" + section_html + "\n" + html[pos_sec_end:]

# 4. Insertar el botón en nav-tabs bajo TAREAS & PIZARRA
nav_target = '<button class="nav-btn" data-cat="tareas" onclick="switchTab(\'ejercicios-pizarra\')">'
new_nav_btn = '''<button class="nav-btn" data-cat="tareas" onclick="switchTab('pizarra-cadenas-hoy')">✨ Pizarra Cadenas Hoy (21-Oct) [5 Ejercicios]</button>
    '''
html_new = html_new.replace(nav_target, new_nav_btn + nav_target)

# 5. Insertar el item en el mobileDrawer
drawer_target = '<div class="drawer-item" onclick="selectDrawerTab(\'ejercicios-pizarra\')">'
new_drawer_item = '''<div class="drawer-item" onclick="selectDrawerTab('pizarra-cadenas-hoy')">
            <span>✨ Pizarra Cadenas Hoy (21-Oct) [5 Ejercicios]</span>
            <span style="color: var(--accent-emerald);">➜</span>
          </div>
          '''
html_new = html_new.replace(drawer_target, new_drawer_item + drawer_target)

# Actualizar el badge de conteo en el grupo TAREA S2-2026 del drawer de 2 a 3
html_new = html_new.replace(
    '<span>📋 TAREA S2-2026 &amp; PIZARRA</span>\n          <span style="background: rgba(16,185,129,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">2</span>',
    '<span>📋 TAREA S2-2026 &amp; PIZARRA</span>\n          <span style="background: rgba(16,185,129,0.15); padding: 0.1rem 0.45rem; border-radius: 999px;">3</span>'
)

# 6. Actualizar el chip de categorías de 2 a 3 y de 21 a 22
html_new = html_new.replace('Todos (21)', 'Todos (22)')
html_new = html_new.replace('Tareas &amp; Pizarra (2)', 'Tareas &amp; Pizarra (3)')

# 7. Insertar el script de simulación antes de </script>
pos_script_end = html_new.rfind('</script>')
if pos_script_end != -1:
    html_new = html_new[:pos_script_end] + "\n" + js_pizarra + "\n" + html_new[pos_script_end:]
else:
    print("Warning: </script> no encontrado, agregando al final del body")
    html_new = html_new.replace('</body>', '<script>' + js_pizarra + '</script>\n</body>')

# 8. Guardar el archivo modificado
with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
    f.write(html_new)

print("¡Sección de la Pizarra de Cadenas integrada exitosamente!")
print("Nuevo tamaño del archivo HTML:", len(html_new), "bytes")
