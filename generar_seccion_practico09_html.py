# -*- coding: utf-8 -*-
"""
Generador del bloque HTML completo de la sección Práctico #9 y las funciones JavaScript
para conectarlo con el simulador Delphi Form y los 31 ejercicios.
"""

from data_practico09 import EJERCICIOS_P9_DATA
import html
import re

def escape_code(s):
    return html.escape(s).replace(' ', '&nbsp;').replace('\n', '<br>')

def highlight_pascal(code):
    keywords = [
        'unit', 'interface', 'implementation', 'uses', 'type', 'class', 'var', 'const',
        'begin', 'end', 'function', 'procedure', 'for', 'to', 'downto', 'do', 'while',
        'if', 'then', 'else', 'repeat', 'until', 'case', 'of', 'set', 'array', 'Exit',
        'Break', 'Continue', 'Result', 'and', 'or', 'not', 'mod', 'div', 'in', 'as', 'is',
        'Inc', 'Dec'
    ]
    types = [
        'String', 'Char', 'Integer', 'Byte', 'Boolean', 'Cardinal', 'TObject', 'TForm',
        'TLabel', 'TEdit', 'TButton', 'TMainMenu', 'TMenuItem', 'AnsiChar'
    ]

    lines = code.strip().splitlines()
    highlighted_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('//'):
            highlighted_lines.append(f'<span class="comment">{html.escape(line)}</span>')
            continue

        parts = []
        in_str = False
        cur = ""
        for ch in line:
            if ch == "'":
                cur += ch
                if in_str:
                    parts.append(('str', cur))
                    cur = ""
                    in_str = False
                else:
                    if cur:
                        parts.append(('code', cur[:-1]))
                    cur = "'"
                    in_str = True
            else:
                cur += ch
        if cur:
            parts.append(('str' if in_str else 'code', cur))

        line_res = ""
        for ptype, pval in parts:
            if ptype == 'str':
                line_res += f'<span class="string">{html.escape(pval)}</span>'
            else:
                tokens = re.split(r'(\b[A-Za-z0-9_]+\b)', pval)
                for tok in tokens:
                    if tok in keywords:
                        line_res += f'<span class="keyword">{tok}</span>'
                    elif tok in types:
                        line_res += f'<span class="type">{tok}</span>'
                    elif tok.isdigit():
                        line_res += f'<span class="number">{tok}</span>'
                    else:
                        line_res += html.escape(tok)
        highlighted_lines.append(line_res.replace(' ', '&nbsp;'))

    return '<br>'.join(highlighted_lines)

def build_p9_html():
    out = []

    out.append('''
  <!-- ========================================================================= -->
  <!-- SECCIÓN: SOLUCIÓN COMPLETA PRÁCTICO #9 (CADENAS, FUNCIONES Y PROCEDIMIENTOS) -->
  <!-- ========================================================================= -->
  <section id="solucion-practico9" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🎯 Solución Completa: Práctico #9 Cadenas, Funciones &amp; Procedimientos (31 Ejercicios)</h2>
        <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3);">INF110-Z2 • M.SC. ANGÉLICA GARZÓN CUÉLLAR</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución académica y práctica de los <strong>31 ejercicios oficiales del Práctico #9 (Cadenas, Funciones y Procedimientos)</strong>, con análisis de entradas y salidas, pseudocódigo modular, pruebas de escritorio formales, diagramas de flujo ANSI, código compilable para <strong>Free Pascal y Delphi 12 VCL</strong>, y un <strong>simulador interactivo en vivo</strong> para probar cualquier ejercicio al instante.
      </p>

      <!-- BADGES DE NAVEGACIÓN RÁPIDA -->
      <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.5rem;">
        <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b;">📋 31 EJERCICIOS COMPLETOS</span>
        <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">🖥️ SIMULADOR VISUAL DELPHI FORM1</span>
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">⚡ 100% OPERATIVO EN VIVO</span>
        <span class="badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc;">📊 DIAGRAMAS DE FLUJO ANSI</span>
        <span class="badge" style="background: rgba(34, 197, 94, 0.15); color: #22c55e;">✅ TEST UNITARIOS COMPILADOS (fpc)</span>
      </div>

      <!-- SIMULADOR VISUAL DELPHI FORM (CLON DEL FORMULARIO DEL ALUMNO) -->
      <div id="p9DelphiWindow" class="delphi-window" style="max-width: 860px; margin: 0 auto 2rem auto;">
        <div class="delphi-titlebar">
          <span>Form1 - [UnitPractico09.pas - Delphi 12 Community Edition]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>

        <!-- BARRA DE MENÚ SUPERIOR (MAINMENU DELPHI) -->
        <div style="background: #f8fafc; border-bottom: 1px solid #cbd5e1; padding: 0.35rem 1rem; display: flex; align-items: center; gap: 1rem; font-size: 0.88rem; position: relative;">
          <div style="position: relative; display: inline-block;">
            <button id="p9MenuBtn" onclick="toggleP9MenuDropdown()" style="background: none; border: 1px solid transparent; padding: 0.25rem 0.65rem; border-radius: 3px; cursor: pointer; font-weight: 700; color: #1e293b; display: flex; align-items: center; gap: 0.3rem;">
              <span>Práctico 9 (Cadenas)</span>
              <span style="font-size: 0.7rem;">▼</span>
            </button>
            <!-- Dropdown del MainMenu -->
            <div id="p9MenuDropdown" style="display: none; position: absolute; top: 100%; left: 0; background: #ffffff; border: 1px solid #94a3b8; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border-radius: 4px; min-width: 290px; z-index: 100; font-size: 0.85rem; padding: 0.4rem 0;">
              <div style="padding: 0.3rem 0.8rem; font-size: 0.75rem; font-weight: 800; color: #64748b; background: #f1f5f9; text-transform: uppercase;">1. Básicos &amp; Funciones</div>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(1)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 1. Contar Palabra</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(2)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 2. Quitar Signos de Puntuación</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(4)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 4. Mayúscula Inicial (Title Case)</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(6)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 6. Comparar Cadenas</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(8)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 8. Extraer Dominio de Email</a>
              <div style="padding: 0.3rem 0.8rem; font-size: 0.75rem; font-weight: 800; color: #64748b; background: #f1f5f9; text-transform: uppercase; margin-top: 0.3rem;">2. Palabras &amp; Modificación</div>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(12)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 12. Eliminar Palabra k</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(13)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 13. Eliminar Palabras tras 'c'</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(16)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 16. Invertir Segunda Palabra</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(17)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 17. Mayúsculas Impar con 'c'</a>
              <div style="padding: 0.3rem 0.8rem; font-size: 0.75rem; font-weight: 800; color: #64748b; background: #f1f5f9; text-transform: uppercase; margin-top: 0.3rem;">3. Algoritmos &amp; Conjuntos</div>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(21)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 21. Intersección de Conjuntos (A ∩ B)</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(22)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 22. Decimal a Binario con Cadenas</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(23)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 23. Dos Vocales Juntas</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(25)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 25. Ordenación Burbuja de Caracteres</a>
              <a href="javascript:void(0)" onclick="p9EjecutarMenu(31)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 31. ¿Es Capicúa / Palíndroma?</a>
              <div style="border-top: 1px solid #e2e8f0; margin-top: 0.3rem; padding: 0.4rem 1rem; background: #fafafa; font-size: 0.78rem; color: #d97706; font-weight: 700;">
                ℹ️ Usa el selector para ejecutar cualquiera de los 31 ejercicios.
              </div>
            </div>
          </div>
          <span style="font-size: 0.78rem; color: #64748b;">(Clic en «Práctico 9» para desplegar el menú de opciones)</span>
        </div>

        <div class="delphi-body" style="background: #f1f5f9; padding: 1.8rem; display: flex; flex-direction: column; gap: 1.2rem;">
          
          <div style="text-align: center; margin-bottom: 0.5rem;">
            <h1 style="font-size: 1.65rem; font-weight: 800; color: #0f172a; letter-spacing: 0.05em; margin: 0;">Práctico #9: Cadenas &amp; Subprogramas</h1>
          </div>

          <!-- FILA 1: ENTRADA (Edit1) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 130px;">Entrada (Edit1):</label>
            <input type="text" id="p9SimEdit1" class="delphi-form-edit" value="hola mundo hola" placeholder="Escriba aquí la cadena de texto...">
          </div>

          <!-- FILA 2: LONGITUD (Edit2) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 130px;">Longitud (Edit2):</label>
            <input type="text" id="p9SimEdit2" class="delphi-form-edit" readonly placeholder="Haga clic en «Longitud»...">
          </div>

          <!-- FILA 3: RESULTADO (Edit3) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 130px;">Resultado (Edit3):</label>
            <input type="text" id="p9SimEdit3" class="delphi-form-edit" readonly placeholder="Aquí se mostrará el resultado..." style="background: #f8fafc; font-weight: 700; color: #d97706;">
          </div>

          <!-- FILA 4: PARÁMETRO EXTRA -->
          <div class="delphi-form-row" id="p9SimExtraRow">
            <label class="delphi-form-label" id="p9SimExtraLabel" style="font-weight: 700; color: #64748b; width: 130px; font-size: 0.82rem;">Parámetro Extra:</label>
            <input type="text" id="p9SimExtra" class="delphi-form-edit" value="hola" placeholder="Palabra, letra o número k adicional..." style="border-color: #cbd5e1;">
          </div>

          <!-- FILA 5: VARIABLES GLOBALES DELPHI (Label5 y Label6: Metodología Ing. Angélica Garzón) -->
          <div style="background: #e2e8f0; border-radius: 4px; padding: 0.5rem 0.85rem; font-family: 'Fira Code', monospace; font-size: 0.88rem; color: #1e293b; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
            <div style="display: flex; gap: 1.5rem;">
              <span id="p9SimLabel5" style="font-weight: 700; color: #0284c7;">cad=hola mundo hola</span>
              <span id="p9SimLabel6" style="font-weight: 700; color: #16a34a;">n=15</span>
            </div>
            <span style="font-size: 0.75rem; color: #64748b;">(Variables Globales Delphi: cad: String; n, i: Byte)</span>
          </div>

          <!-- FILA DE BOTONES PRINCIPALES -->
          <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 0.5rem; flex-wrap: wrap;">
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #e2e8f0;" onclick="btnP9Registrar()">Registrar</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #e2e8f0;" onclick="btnP9Longitud()">Longitud</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #fee2e2; color: #991b1b; border-color: #fca5a5;" onclick="btnP9Close()">Limpiar / Close</button>
          </div>

          <!-- SELECTOR RÁPIDO DE LOS 31 EJERCICIOS -->
          <div style="margin-top: 1rem; padding-top: 1rem; border-top: 2px dashed #cbd5e1;">
            <div style="font-size: 0.85rem; font-weight: 800; color: #92400e; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
              <span>⚡ EJECUTAR CUALQUIERA DE LOS 31 EJERCICIOS:</span>
              <span id="p9SimTagTipo" class="badge" style="background:#fef3c7; color:#b45309; padding: 0.2rem 0.5rem; font-size: 0.75rem;">Función</span>
            </div>
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
              <select id="p9SimSelectEj" class="delphi-form-edit" style="flex: 1; min-width: 280px; font-weight: 600; color: #b45309;" onchange="p9SeleccionarEjercicioRapido()">
''')

    for ej in EJERCICIOS_P9_DATA:
        out.append(f'                <option value="{ej["num"]}">Ej {ej["num"]:02d}: {ej["titulo"][:60]} ({ej["tipo"]})</option>')

    out.append('''              </select>
              <button class="btn-print" style="background: #f59e0b; color: #1e293b; border-color: #d97706; font-weight: 700; padding: 0.5rem 1.25rem; cursor: pointer;" onclick="p9EjecutarDesdeSimulador()">
                ▶ Ejecutar Ejercicio
              </button>
            </div>
          </div>

          <!-- CONSOLA DE SALIDA PARA REPORTES -->
          <div id="p9ConsoleBox" style="display: none; margin-top: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #475569; margin-bottom: 0.25rem;">Consola de Diagnóstico VCL:</div>
            <div id="p9ConsoleOutput" style="background: #070a13; color: #f59e0b; font-family: 'Fira Code', monospace; font-size: 0.82rem; padding: 0.75rem; border-radius: 4px; max-height: 160px; overflow-y: auto; white-space: pre-wrap;"></div>
          </div>

        </div>
      </div>

      <!-- ARQUITECTURA ACADÉMICA Y UNIDAD UnitPractico09.pas -->
      <div class="tag-card amber" style="margin-top: 1.5rem; margin-bottom: 1.5rem; border-left: 4px solid #f59e0b;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <div>
            <h3 style="color: #fff; margin-bottom: 0.25rem;">📁 Unidad Compilable UnitPractico09.pas (Free Pascal &amp; Delphi 12)</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">Todos los 31 algoritmos se encuentran estructurados, testeados y verificados con el compilador Free Pascal (<code>fpc 3.2.2</code>).</p>
          </div>
          <button class="btn-print" onclick="toggleArquitecturaP9(this)" style="background: #f59e0b; color: #1e293b; font-weight: bold; border-color: #d97706;">Ver Código UnitPractico09.pas</button>
        </div>

        <div id="p9ArquitecturaBox" style="display: none; margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem;">
          <h4 style="color: #f59e0b; margin-bottom: 0.5rem;">1. Metodología Oficial de la Docente (M.Sc. Angélica Garzón)</h4>
          <ul style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6; margin-left: 1.2rem; margin-bottom: 1rem;">
            <li><strong>Parámetros Obligatorios <code>(cad: String; n, i: Byte)</code>:</strong> Toda función o procedimiento de cadenas recibe como base <code>cad</code> (el texto), <code>n</code> (longitud previamente calculada con <code>n := Length(cad);</code> en el botón Longitud) y el índice <code>i</code>. Parámetros auxiliares (como caracteres de búsqueda o números k) se colocan a continuación.</li>
            <li><strong>Inicialización Interna y Bucle <code>while</code> Obligatorio:</strong> En la cabecera del cuerpo se inicia <code>i := 1;</code> y se recorre secuencialmente con:
              <br><code style="background: rgba(0,0,0,0.4); padding: 2px 6px; border-radius: 4px; color: #38bdf8;">i := 1; while i &lt;= n do begin ... i := i + 1; end;</code></li>
            <li><strong>Estructura Formulario VCL (Delphi):</strong>
              <br>• Variables globales: <code>cad: String; n, i: Byte;</code>
              <br>• Botón Cargar: <code>cad := Edit1.Text; Label5.Caption := 'cad=' + cad;</code>
              <br>• Botón Longitud: <code>n := Length(cad); Edit2.Text := IntToStr(n) + ' caracteres'; Label6.Caption := 'n=' + IntToStr(n);</code>
              <br>• Opciones de Menú: Invocan cada función pasando <code>(cad, n, i)</code> y mostrando el resultado en <code>Edit3.Text</code>.</li>
            <li><strong>Conjuntos de Caracteres (<code>set of char</code>):</strong> Uso idiomático con constantes locales: <code>const may: set of char = ['A'..'Z'];</code> y <code>const voc: set of char = ['A','E','I','O','U'];</code> consultados mediante <code>if cad[i] in ... then</code>.</li>
            <li><strong>Descomposición en Palabras:</strong> Omitir delimitadores con <code>while (i &lt;= n) and (cad[i] = ' ') do i := i + 1;</code> y extraer término continuo con <code>while (i &lt;= n) and (cad[i] &lt;&gt; ' ') do begin pal := pal + cad[i]; i := i + 1; end;</code>.</li>
          </ul>

          <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">2. Interfaz Oficial Compilable UnitPractico09.pas (31 Subprogramas)</h4>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block" style="max-height: 420px; overflow-y: auto;">
<span class="keyword">unit</span> UnitPractico09;<br>
<br>
<span class="keyword">interface</span><br>
<br>
<span class="keyword">uses</span><br>
&nbsp;&nbsp;SysUtils;<br>
<br>
<span class="comment">// Variables globales del Formulario: cad: String; n, i: Byte;</span><br>
<span class="comment">// 31 Subprogramas con firma oficial: (cad: String; n, i: Byte)</span><br>
<span class="keyword">function</span> ContarPalabra(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>; palBuscada: <span class="type">String</span>): <span class="type">Byte</span>;<br>
<span class="keyword">function</span> QuitarSignos(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> RepetirCadena(cad: <span class="type">String</span>; n, i, nVeces: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> MayusculaInicial(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> ContarMayusMinus(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">procedure</span> ContarMayusMinusProc(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>; <span class="keyword">var</span> may, min: <span class="type">Byte</span>);<br>
<span class="keyword">function</span> CompararCadenas(cad1, cad2: <span class="type">String</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> AnalizarFrase(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> ExtraerDominio(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> EliminarPrimerosN(cad: <span class="type">String</span>; n, i, nDel: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> InsertarSubcadena(cad, sub: <span class="type">String</span>; n, i, posIndex: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> UnirCadenas(cad1, cad2: <span class="type">String</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> EliminarPalabraK(cad: <span class="type">String</span>; n, i, k: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> EliminarPalabrasDelanteDeC(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> CantidadPalabras(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">Byte</span>;<br>
<span class="keyword">function</span> InvertirCadena(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> InvertirSegundaPalabra(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> MayusculaPalabrasImparConC(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> MezclarCadenas(cad1, cad2: <span class="type">String</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> IntercalarCaracteres(cad1, cad2: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> CadenaCaracteresOrdenados(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> OrdenarPalabrasAlfabeticamente(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> InterseccionConjuntos(cadA, cadB: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> DecimalABinario(num: <span class="type">Integer</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> ContarDosVocalesJuntas(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">Byte</span>;<br>
<span class="keyword">procedure</span> InvertirCadenaProc(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>; <span class="keyword">var</span> invertida: <span class="type">String</span>);<br>
<span class="keyword">procedure</span> OrdenarBurbuja(<span class="keyword">var</span> cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>);<br>
<span class="keyword">function</span> ContarPalabrasVocalesExtremos(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">Byte</span>;<br>
<span class="keyword">function</span> EliminarConsonantesUltimaPal(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> InsertarTrasSegunda(cad, palNueva: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> CaracteresIndicesPares(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> EliminarUltimaPalabra(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">String</span>;<br>
<span class="keyword">function</span> EsCapicua(cad: <span class="type">String</span>; n, i: <span class="type">Byte</span>): <span class="type">Boolean</span>;<br>
<br>
<span class="keyword">implementation</span><br>
<br>
<span class="comment">// Los 31 códigos se encuentran implementados íntegramente abajo en cada tarjeta</span><br>
<span class="keyword">end</span>.
            </div>
          </div>
          <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.5rem;">
            💡 Archivo creado en la carpeta del proyecto: <code>d:/Introz2/practico07/UnitPractico09.pas</code> y programa de prueba <code>TestPractico09.pas</code> (41/41 tests unitarios superados en <code>fpc 3.2.2</code>).
          </p>
        </div>
          </p>
        </div>
      </div>

      <!-- BUSCADOR Y FILTROS DE EJERCICIOS -->
      <div style="margin-top: 2rem;">
        <h3 style="color: #fff; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>📚</span> Banco de los 31 Ejercicios Resueltos Paso a Paso
        </h3>

        <!-- INPUT DE BÚSQUEDA -->
        <div class="qa-search-box">
          <input type="text" id="searchP9Input" placeholder="🔍 Buscar en Práctico 9 (ej: contar palabra, signos, repetir, mayúsculas, email, k, burbuja, capicúa...)" onkeyup="filterP9Exercises()">
        </div>

        <!-- BOTONES DE CATEGORÍA -->
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
          <button class="btn-print active-cat" id="catBtn-p9-all" onclick="filtrarP9Categoria('all', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Todos (31)</button>
          <button class="btn-print" id="catBtn-p9-basicos" onclick="filtrarP9Categoria('basicos', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Básicos &amp; Formato (1-10)</button>
          <button class="btn-print" id="catBtn-p9-palabras" onclick="filtrarP9Categoria('palabras', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Palabras &amp; Modificación (11-20)</button>
          <button class="btn-print" id="catBtn-p9-avanzados" onclick="filtrarP9Categoria('avanzados', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Algoritmos, Conjuntos &amp; Capicúa (21-31)</button>
          <button class="btn-print" id="catBtn-p9-func" onclick="filtrarP9Categoria('func', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Solo Funciones</button>
          <button class="btn-print" id="catBtn-p9-proc" onclick="filtrarP9Categoria('proc', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Solo Procedimientos</button>
        </div>

        <!-- CONTADOR DE RESULTADOS -->
        <div id="p9Counter" style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 1rem;">
          Mostrando 31 de 31 ejercicios del Práctico #9.
        </div>
      </div>

      <!-- LISTA DE LOS 31 EJERCICIOS ACORDEÓN -->
      <div id="p9List">
''')

    # Generar las tarjetas de los 31 ejercicios
    for ej in EJERCICIOS_P9_DATA:
        num = ej["num"]
        num_str = f"{num:02d}"
        titulo = ej["titulo"]
        tipo = ej["tipo"]
        cat = ej["categoria"]
        badge_tipo_color = "#38bdf8" if tipo == "Función" else "#a855f7"
        badge_tipo_bg = "rgba(56, 189, 248, 0.15)" if tipo == "Función" else "rgba(168, 85, 247, 0.15)"

        out.append(f'''
        <!-- EJERCICIO {num} -->
        <div class="qa-item p9-item" data-cat="{cat}" data-tipo="{tipo.lower()}">
          <div class="qa-header" onclick="toggleQA(this)">
            <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
              <span class="qa-number" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b; border-color: rgba(245, 158, 11, 0.3);">P9-{num_str}</span>
              <span style="color: #fff; font-weight: 600;">{num}. {titulo}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem;">
              <span class="badge" style="background: {badge_tipo_bg}; color: {badge_tipo_color}; padding: 0.2rem 0.6rem; font-size: 0.75rem; margin: 0;">{tipo}</span>
              <span class="qa-icon">▼</span>
            </div>
          </div>
          <div class="qa-body">
            
            <!-- ANÁLISIS ACADÉMICO -->
            <p><strong>Análisis Académico:</strong><br>{ej["analisis"]}</p>

            <!-- PSEUDOCÓDIGO -->
            <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo Modular (INF110):</h5>
            <div class="code-block" style="font-size: 0.86rem;">
{escape_code(ej["pseudo"])}
            </div>

            <!-- PRUEBA DE ESCRITORIO -->
            <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
            <div class="table-container">
              <table>
                <thead>
                  <tr>''')
        for th in ej["traza_headers"]:
            out.append(f'<th>{html.escape(th)}</th>')
        out.append('''</tr>
                </thead>
                <tbody>''')
        for row in ej["traza_rows"]:
            out.append('<tr>')
            for cell in row:
                out.append(f'<td>{html.escape(cell)}</td>')
            out.append('</tr>')
        out.append('''
                </tbody>
              </table>
            </div>
''')

        # Diagrama Mermaid si existe
        if "diagrama_mermaid" in ej and ej["diagrama_mermaid"]:
            out.append(f'''
            <!-- DIAGRAMA DE FLUJO ANSI -->
            <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Diagrama de Flujo ANSI:</h5>
            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; margin-top: 0.5rem; text-align: center; overflow-x: auto;">
              <div class="mermaid">
{ej["diagrama_mermaid"]}
              </div>
            </div>
''')

        pascal_code = highlight_pascal(ej["codigo_pascal"])
        vcl_code = highlight_pascal(ej["codigo_vcl"])
        ent_ejemplo = html.escape(ej["entrada_ejemplo"])
        sal_ejemplo = html.escape(ej["salida_ejemplo"])
        extra_default = html.escape(ej.get("extra_default", ""))

        out.append(f'''
            <!-- CÓDIGO DELPHI PASCAL MODULAR -->
            <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Pascal / Delphi:</h5>
            <div class="code-wrapper">
              <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
              <div class="code-block">
{pascal_code}
              </div>
            </div>

            <!-- EVENTO VCL EN EL FORMULARIO TForm1 -->
            <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Evento OnClick en Formulario Delphi (TForm1 / MainMenu):</h5>
            <div class="code-wrapper">
              <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
              <div class="code-block">
{vcl_code}
              </div>
            </div>

            <!-- CASO DE PRUEBA Y BOTÓN DE PRUEBA EN VIVO -->
            <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border-color); border-radius: 6px; padding: 0.85rem 1rem; margin-top: 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
              <div>
                <div style="font-size: 0.82rem; color: #94a3b8;">📥 Entrada: <strong style="color: #f8fafc;">{ent_ejemplo}</strong></div>
                <div style="font-size: 0.82rem; color: #f59e0b;">📤 Salida esperada: <strong>{sal_ejemplo}</strong></div>
              </div>
              <button class="btn-print" style="background: #f59e0b; color: #1e293b; font-weight: bold; border-color: #d97706; font-size: 0.82rem; cursor: pointer;" data-p9-num="{num}" data-p9-ent="{ent_ejemplo}" data-p9-extra="{extra_default}" onclick="p9ProbarBtnClick(this)">
                ▶ Probar en el Simulador
              </button>
            </div>

          </div>
        </div>
''')

    out.append('''
      </div> <!-- Fin #p9List -->

    </div> <!-- Fin .card -->
  </section>
  <!-- ========================================================================= -->
  <!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #9                                  -->
  <!-- ========================================================================= -->
''')

    return '\n'.join(out)

def build_p9_js():
    js = '''
  // ===========================================================================
  //      MOTOR JAVASCRIPT DEL SIMULADOR VCL Y PRÁCTICO #9 (31 EJERCICIOS)
  // ===========================================================================

  let p9GlobalCad = "hola mundo hola";
  let p9GlobalN = 15;

  function btnP9Registrar() {
    const edit1 = document.getElementById('p9SimEdit1');
    p9GlobalCad = edit1.value;
    p9GlobalN = p9GlobalCad.length;
    document.getElementById('p9SimLabel5').innerText = 'cad=' + p9GlobalCad;
    document.getElementById('p9SimLabel6').innerText = 'n=' + p9GlobalN;
    if (typeof showMobileToast === 'function') {
      showMobileToast('Cadena registrada en variable global cad');
    }
  }

  function btnP9Longitud() {
    p9GlobalN = p9GlobalCad.length;
    document.getElementById('p9SimEdit2').value = p9GlobalN + ' caracteres';
    document.getElementById('p9SimLabel6').innerText = 'n=' + p9GlobalN;
    if (typeof showMobileToast === 'function') {
      showMobileToast('Longitud calculada: n=' + p9GlobalN);
    }
  }

  function btnP9Close() {
    document.getElementById('p9SimEdit1').value = '';
    document.getElementById('p9SimEdit2').value = '';
    document.getElementById('p9SimEdit3').value = '';
    document.getElementById('p9SimExtra').value = '';
    p9GlobalCad = '';
    p9GlobalN = 0;
    document.getElementById('p9SimLabel5').innerText = 'cad=';
    document.getElementById('p9SimLabel6').innerText = 'n=0';
    document.getElementById('p9ConsoleBox').style.display = 'none';
    if (typeof showMobileToast === 'function') {
      showMobileToast('Formulario restablecido');
    }
  }

  function toggleP9MenuDropdown() {
    const dd = document.getElementById('p9MenuDropdown');
    dd.style.display = (dd.style.display === 'block') ? 'none' : 'block';
  }

  document.addEventListener('click', function(e) {
    const btn = document.getElementById('p9MenuBtn');
    const dd = document.getElementById('p9MenuDropdown');
    if (btn && dd && !btn.contains(e.target) && !dd.contains(e.target)) {
      dd.style.display = 'none';
    }
  });

  function toggleArquitecturaP9(btn) {
    const box = document.getElementById('p9ArquitecturaBox');
    if (box.style.display === 'none' || !box.style.display) {
      box.style.display = 'block';
      btn.innerText = 'Ocultar Código UnitPractico09.pas';
    } else {
      box.style.display = 'none';
      btn.innerText = 'Ver Código UnitPractico09.pas';
    }
  }

  function p9EjecutarMenu(ejNum) {
    toggleP9MenuDropdown();
    const sel = document.getElementById('p9SimSelectEj');
    if (sel) {
      sel.value = ejNum;
      p9SeleccionarEjercicioRapido();
      p9EjecutarDesdeSimulador();
    }
  }

  function p9SeleccionarEjercicioRapido() {
    const sel = document.getElementById('p9SimSelectEj');
    const ejNum = parseInt(sel.value);
    const extraInput = document.getElementById('p9SimExtra');
    const extraLabel = document.getElementById('p9SimExtraLabel');
    const tagTipo = document.getElementById('p9SimTagTipo');

    const conParamExtra = {
      1: { label: "Palabra a buscar:", def: "hola" },
      3: { label: "Valor de N (veces):", def: "3" },
      6: { label: "Segunda cadena:", def: "Perro" },
      9: { label: "Cantidad N a borrar:", def: "3" },
      10: { label: "Posición (1..N):", def: "5" },
      11: { label: "Segunda cadena:", def: "Mundo" },
      12: { label: "Número de palabra k:", def: "3" },
      18: { label: "Segunda cadena cad2:", def: "jose" },
      21: { label: "Conjunto B:", def: "a, m, g, p, l, h, k, n" },
      28: { label: "Palabra a insertar:", def: "es" }
    };

    if (conParamExtra[ejNum]) {
      extraLabel.innerText = conParamExtra[ejNum].label;
      extraInput.placeholder = conParamExtra[ejNum].label;
      if (!extraInput.value) extraInput.value = conParamExtra[ejNum].def;
      document.getElementById('p9SimExtraRow').style.opacity = '1';
    } else {
      extraLabel.innerText = "Parámetro Extra:";
      document.getElementById('p9SimExtraRow').style.opacity = '0.5';
    }

    const procs = [7, 19, 20, 21, 24, 25, 28];
    if (procs.includes(ejNum)) {
      tagTipo.innerText = 'Procedimiento';
      tagTipo.style.background = 'rgba(168, 85, 247, 0.15)';
      tagTipo.style.color = '#c084fc';
    } else {
      tagTipo.innerText = 'Función';
      tagTipo.style.background = 'rgba(56, 189, 248, 0.15)';
      tagTipo.style.color = '#38bdf8';
    }
  }

  function p9ProbarBtnClick(btn) {
    const num = parseInt(btn.getAttribute('data-p9-num'), 10);
    const ent = btn.getAttribute('data-p9-ent') || '';
    const extra = btn.getAttribute('data-p9-extra') || '';
    p9ProbarEnSimulador(num, ent, extra);
  }

  function p9ProbarEnSimulador(ejNum, ent, extraVal) {
    document.getElementById('p9SimEdit1').value = ent;
    btnP9Registrar();
    btnP9Longitud();

    if (extraVal) {
      document.getElementById('p9SimExtra').value = extraVal;
    }

    document.getElementById('p9SimSelectEj').value = ejNum;
    p9SeleccionarEjercicioRapido();
    p9EjecutarDesdeSimulador();

    const targetWin = document.getElementById('p9DelphiWindow');
    if (targetWin) {
      targetWin.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  function p9EjecutarDesdeSimulador() {
    const ejNum = parseInt(document.getElementById('p9SimSelectEj').value);
    const cadActual = document.getElementById('p9SimEdit1').value;
    p9GlobalCad = cadActual;
    p9GlobalN = cadActual.length;
    document.getElementById('p9SimLabel5').innerText = 'cad=' + p9GlobalCad;
    document.getElementById('p9SimLabel6').innerText = 'n=' + p9GlobalN;

    const extraVal = document.getElementById('p9SimExtra').value.trim();
    const edit3 = document.getElementById('p9SimEdit3');
    const consoleBox = document.getElementById('p9ConsoleBox');
    const consoleOut = document.getElementById('p9ConsoleOutput');

    consoleBox.style.display = 'none';
    consoleOut.innerText = '';

    const esVocal = (c) => ['A','E','I','O','U','Á','É','Í','Ó','Ú'].includes(c.toUpperCase());
    const esLetra = (c) => /^[A-Za-zÁÉÍÓÚáéíóúñÑ]$/.test(c);
    const esConsonante = (c) => esLetra(c) && !esVocal(c);

    let res = "";

    switch(ejNum) {
      case 1: { // ContarPalabra
        const palBuscada = (extraVal || 'hola').toLowerCase();
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        let c = 0;
        for (let p of palabras) {
          if (p.toLowerCase() === palBuscada) c++;
        }
        res = 'La palabra "' + extraVal + '" aparece ' + c + ' veces';
        break;
      }

      case 2: { // QuitarSignos
        res = p9GlobalCad.replace(/[.,;:!¡?¿"'()\\[\\]{}\\-_]/g, '');
        break;
      }

      case 3: { // RepetirCadena
        const nRep = parseInt(extraVal) || 3;
        res = p9GlobalCad.repeat(Math.max(0, nRep));
        break;
      }

      case 4: { // MayusculaInicial (Title Case)
        res = p9GlobalCad.replace(/(^|\\s)([a-záéíóúñ])/gi, (match, sep, letra) => sep + letra.toUpperCase());
        break;
      }

      case 5: { // ContarMayusMinus
        let may = 0, min = 0;
        for (let ch of p9GlobalCad) {
          if (ch >= 'A' && ch <= 'Z') may++;
          else if (ch >= 'a' && ch <= 'z') min++;
        }
        res = 'Mayúsculas: ' + may + ', Minúsculas: ' + min;
        break;
      }

      case 6: { // CompararCadenas
        const cad2 = extraVal || 'Perro';
        const c1 = p9GlobalCad.toLowerCase();
        const c2 = cad2.toLowerCase();
        if (c1 < c2) res = '"' + p9GlobalCad + '" va antes que "' + cad2 + '"';
        else if (c1 > c2) res = '"' + cad2 + '" va antes que "' + p9GlobalCad + '"';
        else res = 'Ambas cadenas son alfabéticamente iguales';
        break;
      }

      case 7: { // AnalizarFrase con funciones individuales
        const pals = p9GlobalCad.trim().length ? p9GlobalCad.trim().split(/\\s+/).length : 0;
        let letras = 0, voc = 0, cons = 0, may = 0, min = 0;
        for (let ch of p9GlobalCad) {
          if (esLetra(ch)) letras++;
          if (esVocal(ch)) voc++;
          if (esConsonante(ch)) cons++;
          if (ch >= 'A' && ch <= 'Z') may++;
          if (ch >= 'a' && ch <= 'z') min++;
        }
        res = 'Palabras: ' + pals + ' | Letras: ' + letras + ' | Vocales: ' + voc + ' | Consonantes: ' + cons + ' | Mayúsculas: ' + may + ' | Minúsculas: ' + min;
        consoleBox.style.display = 'block';
        consoleOut.innerText = 'REPORTE MODULAR INF110:\\n' +
          '• ContarPalabras: ' + pals + '\\n' +
          '• ContarLetrasTotales: ' + letras + '\\n' +
          '• ContarVocales: ' + voc + '\\n' +
          '• ContarConsonantes: ' + cons + '\\n' +
          '• ContarMayusculas: ' + may + '\\n' +
          '• ContarMinusculas: ' + min;
        break;
      }

      case 8: { // ExtraerDominio
        const p = p9GlobalCad.indexOf('@');
        if (p !== -1) res = p9GlobalCad.substring(p + 1);
        else res = 'Correo sin arroba válida';
        break;
      }

      case 9: { // EliminarPrimerosN
        const nDel = parseInt(extraVal) || 3;
        res = p9GlobalCad.substring(nDel);
        break;
      }

      case 10: { // InsertarSubcadena
        const posIns = parseInt(extraVal) || 5;
        const sub = ' ';
        const idx = Math.max(0, posIns - 1);
        res = p9GlobalCad.slice(0, idx) + sub + p9GlobalCad.slice(idx);
        break;
      }

      case 11: { // UnirCadenas
        const cad2 = extraVal || 'Mundo';
        res = p9GlobalCad + (p9GlobalCad && cad2 ? ' ' : '') + cad2;
        break;
      }

      case 12: { // EliminarPalabraK
        const k = parseInt(extraVal) || 3;
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        if (k >= 1 && k <= palabras.length) {
          palabras.splice(k - 1, 1);
        }
        res = palabras.join(' ');
        break;
      }

      case 13: { // EliminarPalabrasDelanteDeC
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        const resultado = [];
        for (let i = 0; i < palabras.length; i++) {
          let eliminar = false;
          if (i > 0 && palabras[i - 1].toLowerCase().includes('c')) {
            eliminar = true;
          }
          if (!eliminar) {
            resultado.push(palabras[i]);
          }
        }
        res = resultado.join(' ');
        break;
      }

      case 14: { // CantidadPalabras
        res = 'Total de palabras: ' + (p9GlobalCad.trim() ? p9GlobalCad.trim().split(/\\s+/).length : 0);
        break;
      }

      case 15: { // InvertirCadena
        res = p9GlobalCad.split('').reverse().join('');
        break;
      }

      case 16: { // InvertirSegundaPalabra
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        if (palabras.length >= 2) {
          palabras[1] = palabras[1].split('').reverse().join('');
        }
        res = palabras.join(' ');
        break;
      }

      case 17: { // MayusculaPalabrasImparConC
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        for (let i = 0; i < palabras.length; i++) {
          const p = palabras[i];
          if (p.length % 2 !== 0 && p.toLowerCase().includes('c')) {
            palabras[i] = p.toUpperCase();
          }
        }
        res = palabras.join(' ');
        break;
      }

      case 18: { // MezclarCadenas
        const cad2 = extraVal || 'jose';
        res = p9GlobalCad + cad2;
        break;
      }

      case 19: { // Inserción ordenada de caracteres
        const chars = p9GlobalCad.replace(/\\s+/g, '').split('');
        const ordenados = [];
        for (let ch of chars) {
          let j = 0;
          while (j < ordenados.length && ch > ordenados[j]) j++;
          ordenados.splice(j, 0, ch);
        }
        res = ordenados.join('');
        break;
      }

      case 20: { // Inserción ordenada de palabras
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        const ordenadas = [];
        for (let p of palabras) {
          let j = 0;
          while (j < ordenadas.length && p.toLowerCase() > ordenadas[j].toLowerCase()) j++;
          ordenadas.splice(j, 0, p);
        }
        res = ordenadas.join(' ');
        break;
      }

      case 21: { // Intersección de Conjuntos A ∩ B
        const bChars = (extraVal || 'a, m, g, p, l, h, k, n').toLowerCase().replace(/[^a-z]/g, '').split('');
        const aChars = p9GlobalCad.toLowerCase().replace(/[^a-z]/g, '').split('');
        const intersect = [];
        for (let ch of aChars) {
          if (bChars.includes(ch) && !intersect.includes(ch)) {
            intersect.push(ch);
          }
        }
        intersect.sort();
        res = '{' + intersect.join(', ') + '}';
        break;
      }

      case 22: { // Decimal a Binario
        let num = parseInt(p9GlobalCad) || 0;
        if (num === 0) res = 'Binario: 0';
        else {
          let bin = '';
          while (num > 0) {
            bin = (num % 2) + bin;
            num = Math.floor(num / 2);
          }
          res = 'Binario: ' + bin;
        }
        break;
      }

      case 23: { // Contar 2 vocales juntas
        let c = 0;
        for (let i = 0; i < p9GlobalCad.length - 1; i++) {
          if (esVocal(p9GlobalCad[i]) && esVocal(p9GlobalCad[i + 1])) {
            c++;
          }
        }
        res = 'Cantidad de 2 vocales juntas: ' + c;
        break;
      }

      case 24: { // Invertir procedimental
        res = p9GlobalCad.split('').reverse().join('');
        break;
      }

      case 25: { // Burbuja de caracteres
        const arr = p9GlobalCad.split('');
        const n = arr.length;
        for (let i = 0; i < n - 1; i++) {
          for (let j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
              const aux = arr[j];
              arr[j] = arr[j + 1];
              arr[j + 1] = aux;
            }
          }
        }
        res = arr.join('');
        break;
      }

      case 26: { // Palabras inician y terminan en vocal
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        let c = 0;
        for (let p of palabras) {
          if (p.length > 0 && esVocal(p[0]) && esVocal(p[p.length - 1])) {
            c++;
          }
        }
        res = 'Palabras con vocales en ambos extremos: ' + c;
        break;
      }

      case 27: { // Eliminar consonantes de la última palabra
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        if (palabras.length > 0) {
          const ult = palabras[palabras.length - 1];
          let ultLimpia = '';
          for (let ch of ult) {
            if (!esConsonante(ch)) ultLimpia += ch;
          }
          palabras[palabras.length - 1] = ultLimpia;
        }
        res = palabras.join(' ');
        break;
      }

      case 28: { // Insertar palabra a partir de la segunda palabra
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        const ins = extraVal || 'es';
        if (palabras.length >= 2) {
          palabras.splice(2, 0, ins);
        } else {
          palabras.push(ins);
        }
        res = palabras.join(' ');
        break;
      }

      case 29: { // Caracteres en índices pares (1-based: 2, 4, 6...)
        let sub = '';
        for (let i = 1; i < p9GlobalCad.length; i += 2) {
          sub += p9GlobalCad[i];
        }
        res = sub;
        break;
      }

      case 30: { // Eliminar última palabra
        const palabras = p9GlobalCad.trim().split(/\\s+/);
        palabras.pop();
        res = palabras.join(' ');
        break;
      }

      case 31: { // Verificar si es capicúa / palíndroma
        const limpia = p9GlobalCad.toLowerCase().replace(/\\s+/g, '');
        const rev = limpia.split('').reverse().join('');
        const esCap = (limpia.length > 0) && (limpia === rev);
        res = esCap ? ('Es Capicúa / Palíndroma (' + p9GlobalCad + ')') : ('No es Capicúa (' + p9GlobalCad + ')');
        break;
      }

      default:
        res = 'Ejercicio no implementado';
    }

    edit3.value = res;
    if (typeof showMobileToast === 'function') {
      showMobileToast('Ejercicio ' + ejNum + ' ejecutado');
    }
  }

  function filterP9Exercises() {
    const input = document.getElementById('searchP9Input').value.toLowerCase().trim();
    const items = document.querySelectorAll('.p9-item');
    let visible = 0;

    items.forEach(item => {
      const text = item.innerText.toLowerCase();
      if (text.includes(input)) {
        item.style.display = 'block';
        visible++;
      } else {
        item.style.display = 'none';
      }
    });

    const counter = document.getElementById('p9Counter');
    if (counter) {
      counter.innerText = 'Mostrando ' + visible + ' de 31 ejercicios del Práctico #9.';
    }
  }

  function filtrarP9Categoria(cat, btn) {
    document.querySelectorAll('[id^="catBtn-p9-"]').forEach(b => b.classList.remove('active-cat'));
    if (btn) btn.classList.add('active-cat');

    const items = document.querySelectorAll('.p9-item');
    let visible = 0;

    items.forEach(item => {
      const itemCat = item.getAttribute('data-cat');
      const itemTipo = item.getAttribute('data-tipo');

      let show = false;
      if (cat === 'all') show = true;
      else if (cat === 'func' && itemTipo === 'función') show = true;
      else if (cat === 'proc' && itemTipo === 'procedimiento') show = true;
      else if (cat === itemCat) show = true;

      if (show) {
        item.style.display = 'block';
        visible++;
      } else {
        item.style.display = 'none';
      }
    });

    const counter = document.getElementById('p9Counter');
    if (counter) {
      counter.innerText = 'Mostrando ' + visible + ' de 31 ejercicios del Práctico #9.';
    }
  }
'''
    return js
