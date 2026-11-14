# -*- coding: utf-8 -*-
"""
Genera el bloque HTML completo de la sección Práctico #8 y las funciones JavaScript
para conectarlo con el simulador Delphi Form y los 40 ejercicios.
"""

from data_practico08 import EJERCICIOS_DATA
import generar_seccion_cadenas_docx as docx_teoria
import html
import re

def escape_code(s):
    return html.escape(s).replace(' ', '&nbsp;').replace('\n', '<br>')

def highlight_pascal(code):
    # Palabras clave de Pascal/Delphi
    keywords = [
        'unit', 'interface', 'implementation', 'uses', 'type', 'class', 'var', 'const',
        'begin', 'end', 'function', 'procedure', 'for', 'to', 'downto', 'do', 'while',
        'if', 'then', 'else', 'repeat', 'until', 'case', 'of', 'set', 'array', 'Exit',
        'Break', 'Continue', 'Result', 'and', 'or', 'not', 'mod', 'div', 'in', 'as', 'is'
    ]
    types = ['String', 'Char', 'Integer', 'Byte', 'Boolean', 'Cardinal', 'TObject', 'TForm', 'TLabel', 'TEdit', 'TButton', 'TMainMenu', 'TMenuItem']

    lines = code.strip().splitlines()
    highlighted_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('//'):
            highlighted_lines.append(f'<span class="comment">{html.escape(line)}</span>')
            continue

        # Proteger strings '...'
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
                # Tokenizar palabras
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

def build_p8_html():
    out = []

    out.append('''
  <!-- ========================================================================= -->
  <!-- SECCIÓN: SOLUCIÓN COMPLETA PRÁCTICO #8 (CADENAS & DELPHI FORM VCL)        -->
  <!-- ========================================================================= -->
  <section id="solucion-practico8" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🔤 Solución Completa: Práctico #8 Cadenas de Caracteres (40 Ejercicios)</h2>
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3);">INF110-Z2 • DELPHI 12 VCL</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución integral de los <strong>40 ejercicios del Práctico #8 (Cadena de Caracteres)</strong> exigidos por la docente <strong>M.Sc. Ing. Angélica Garzón Cuéllar</strong>, con la arquitectura completa del formulario Delphi (<code>Form1</code>), integración del <code>MainMenu</code>, variables globales (<code>cad, n, i</code>), bucles <code>while i &lt;= n do</code> y conjuntos <code>set of char</code>.
      </p>

      <!-- BADGES DE NAVEGACIÓN RÁPIDA -->
      <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.5rem;">
        <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">📖 TEORÍA OFICIAL cadenas.docx</span>
        <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">📋 40 EJERCICIOS COMPLETOS</span>
        <span class="badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc;">🖥️ CLON VISUAL DELPHI FORM1</span>
        <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">⚡ SIMULADOR EN VIVO 100% OPERATIVO</span>
        <span class="badge" style="background: rgba(244, 63, 94, 0.15); color: #fb7185;">📁 UNIDAD Cadena.pas LISTA PARA COMPILAR</span>
      </div>
''' + docx_teoria.build_cadenas_docx_html() + '''
      <!-- SIMULADOR VISUAL DELPHI FORM (CLON DEL FORMULARIO DEL ALUMNO) -->
      <div id="p8DelphiWindow" class="delphi-window" style="max-width: 840px;">
        <div class="delphi-titlebar">
          <span>Form1 - [Cadena.pas - Delphi 12 Community Edition]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>

        <!-- BARRA DE MENÚ SUPERIOR (MAINMENU DELPHI) -->
        <div style="background: #f8fafc; border-bottom: 1px solid #cbd5e1; padding: 0.35rem 1rem; display: flex; align-items: center; gap: 1rem; font-size: 0.88rem; position: relative;">
          <div style="position: relative; display: inline-block;">
            <button id="p8MenuBtn" onclick="toggleP8MenuDropdown()" style="background: none; border: 1px solid transparent; padding: 0.25rem 0.65rem; border-radius: 3px; cursor: pointer; font-weight: 700; color: #1e293b; display: flex; align-items: center; gap: 0.3rem;">
              <span>Cadenas</span>
              <span style="font-size: 0.7rem;">▼</span>
            </button>
            <!-- Dropdown del MainMenu -->
            <div id="p8MenuDropdown" style="display: none; position: absolute; top: 100%; left: 0; background: #ffffff; border: 1px solid #94a3b8; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border-radius: 4px; min-width: 280px; z-index: 100; font-size: 0.85rem; padding: 0.4rem 0;">
              <div style="padding: 0.3rem 0.8rem; font-size: 0.75rem; font-weight: 800; color: #64748b; background: #f1f5f9; text-transform: uppercase;">1. Operaciones Básicas</div>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(11)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Espacios en Blanco (Cargar1)</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(15)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Cantidad Mayúsculas (Cargar2)</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(4)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Contador Vocales (Vocales1)</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(5)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Contador Consonantes</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(6)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Cadena en Mayúsculas</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(7)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Cadena en Minúsculas (Minuscula1)</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(8)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Invertir Cadena</a>
              <div style="padding: 0.3rem 0.8rem; font-size: 0.75rem; font-weight: 800; color: #64748b; background: #f1f5f9; text-transform: uppercase; margin-top: 0.3rem;">2. Búsqueda y Letras</div>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(2)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Primera Letra</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(3)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Última Letra</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(10)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Buscar Carácter (BuscarCaracter1)</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(16)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 ¿Es Palíndroma?</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(17)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Contar Palabras</a>
              <a href="javascript:void(0)" onclick="p8EjecutarMenu(14)" style="display: block; padding: 0.4rem 1rem; color: #0f172a; text-decoration: none;">🔘 Códigos ASCII (ShowMessage)</a>
              <div style="border-top: 1px solid #e2e8f0; margin-top: 0.3rem; padding: 0.4rem 1rem; background: #fafafa; font-size: 0.78rem; color: #0284c7; font-weight: 700;">
                ℹ️ Los 40 ejercicios se pueden ejecutar en el selector inferior.
              </div>
            </div>
          </div>
          <span style="font-size: 0.78rem; color: #64748b;">(Haga clic en «Cadenas» para abrir el menú VCL)</span>
        </div>

        <div class="delphi-body" style="background: #f1f5f9; padding: 1.8rem; display: flex; flex-direction: column; gap: 1.2rem;">
          
          <!-- TÍTULO VISUAL DEL FORMULARIO -->
          <div style="text-align: center; margin-bottom: 0.5rem;">
            <h1 style="font-size: 1.75rem; font-weight: 800; color: #0f172a; letter-spacing: 0.05em; margin: 0;">Cadenas</h1>
          </div>

          <!-- FILA 1: ENTRADA (Edit1) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 110px;">Entrada:</label>
            <input type="text" id="p8SimEdit1" class="delphi-form-edit" value="Hola Mundo Delphi 2026" placeholder="Escriba aquí la cadena de texto...">
          </div>

          <!-- FILA 2: LONGITUD (Edit2) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 110px;">longitud:</label>
            <input type="text" id="p8SimEdit2" class="delphi-form-edit" readonly placeholder="Haga clic en «Longitud»...">
          </div>

          <!-- FILA 3: RESULTADO (Edit3) -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="font-weight: 700; color: #334155; width: 110px;">Resultado:</label>
            <input type="text" id="p8SimEdit3" class="delphi-form-edit" readonly placeholder="Aquí se mostrará el resultado..." style="background: #f8fafc; font-weight: 700; color: #0369a1;">
          </div>

          <!-- FILA 4: PARÁMETRO EXTRA (Para ejercicios con 2 cadenas, letras o número n) -->
          <div class="delphi-form-row" id="p8SimExtraRow">
            <label class="delphi-form-label" style="font-weight: 700; color: #64748b; width: 110px; font-size: 0.8rem;">Parámetro Extra:</label>
            <input type="text" id="p8SimExtra" class="delphi-form-edit" placeholder="Letra, palabra o número adicional (ej: 'a' o 'Delphi' o 5)" style="border-color: #cbd5e1;">
          </div>

          <!-- FILA 5: LABEL5 (cad=...) -->
          <div style="background: #e2e8f0; border-radius: 4px; padding: 0.5rem 0.85rem; font-family: 'Fira Code', monospace; font-size: 0.9rem; color: #1e293b; display: flex; justify-content: space-between; align-items: center;">
            <span id="p8SimLabel5">cad=Hola Mundo Delphi 2026</span>
            <span style="font-size: 0.75rem; color: #64748b;">(Variable Global Delphi)</span>
          </div>

          <!-- FILA DE BOTONES PRINCIPALES -->
          <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 0.5rem; flex-wrap: wrap;">
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #e2e8f0;" onclick="btnP8Registrar()">Registrar</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #e2e8f0;" onclick="btnP8Longitud()">Longitud</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem 1.6rem; font-weight: 700; background: #fee2e2; color: #991b1b; border-color: #fca5a5;" onclick="btnP8Close()">close</button>
          </div>

          <!-- SELECTOR RÁPIDO DE LOS 40 EJERCICIOS -->
          <div style="margin-top: 1rem; padding-top: 1rem; border-top: 2px dashed #cbd5e1;">
            <div style="font-size: 0.85rem; font-weight: 800; color: #1e3a8a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
              <span>⚡ EJECUTAR CUALQUIERA DE LOS 40 EJERCICIOS EN ESTE FORMULARIO:</span>
              <span id="p8SimTagTipo" class="badge" style="background:#e0f2fe; color:#0369a1; padding: 0.2rem 0.5rem; font-size: 0.75rem;">Función</span>
            </div>
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
              <select id="p8SimSelectEj" class="delphi-form-edit" style="flex: 1; min-width: 280px; font-weight: 600; color: #0369a1;" onchange="p8SeleccionarEjercicioRapido()">
''')

    # Añadir opciones al select
    for ej in EJERCICIOS_DATA:
        out.append(f'                <option value="{ej["num"]}">Ej {ej["num"]:02d}: {ej["titulo"][:60]} ({ej["tipo"]})</option>')

    out.append('''              </select>
              <button class="btn-print" style="background: #0284c7; color: #ffffff; border-color: #0369a1; font-weight: 700; padding: 0.5rem 1.25rem;" onclick="p8EjecutarDesdeSimulador()">
                ▶ Ejecutar Ejercicio
              </button>
            </div>
          </div>

          <!-- CONSOLA DE SALIDA PARA PROCEDIMIENTOS MULTILÍNEA -->
          <div id="p8ConsoleBox" style="display: none; margin-top: 0.75rem;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #475569; margin-bottom: 0.25rem;">Salida de Pantalla / Consola VCL:</div>
            <div id="p8ConsoleOutput" style="background: #070a13; color: #38bdf8; font-family: 'Fira Code', monospace; font-size: 0.82rem; padding: 0.75rem; border-radius: 4px; max-height: 160px; overflow-y: auto; white-space: pre-wrap;"></div>
          </div>

        </div>
      </div>


      <!-- GUÍA DE ARQUITECTURA DEL FORMULARIO DELPHI -->
      <div class="tag-card purple" style="margin-top: 2rem; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
          <div>
            <h3 style="color: #fff; margin-bottom: 0.25rem;">🏛️ Arquitectura del Formulario Delphi (Cadena.pas & TMainMenu)</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">Explicación de cómo conectar los 40 ejercicios a la ventana visual y a las opciones del menú.</p>
          </div>
          <button class="btn-print" onclick="toggleArquitecturaP8(this)">Mostrar Código Cadena.pas</button>
        </div>

        <div id="p8ArquitecturaBox" style="display: none; margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1rem;">
          <h4 style="color: #a855f7; margin-bottom: 0.5rem;">1. Variables Globales vs Módulos Locales</h4>
          <p style="font-size: 0.92rem; color: #e2e8f0; margin-bottom: 1rem;">
            En la materia INF110-Z2, la docente trabaja en pizarra con variables globales <code>cad: String; n, i: Byte;</code>. Al presionar <strong>Registrar</strong> (<code>BTNCargarClick</code>), el texto de <code>Edit1.Text</code> se almacena en <code>cad</code> y se actualiza <code>Label5.Caption</code>. Al hacer clic en <strong>Longitud</strong> (<code>Button2Click</code>), se ejecuta <code>n := Length(cad);</code> y se muestra en <code>Edit2.Text</code>. Luego, cada opción del menú calcula su resultado llamando al módulo correspondiente y escribiendo en <code>Edit3.Text</code>.
          </p>

          <h4 style="color: #38bdf8; margin-bottom: 0.5rem;">2. Código Fuente de la Unidad Cadena.pas</h4>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block" style="max-height: 400px; overflow-y: auto;">
<span class="keyword">unit</span> Cadena;<br>
<br>
<span class="keyword">interface</span><br>
<br>
<span class="keyword">uses</span><br>
&nbsp;&nbsp;Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,<br>
&nbsp;&nbsp;Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.Menus, Vcl.StdCtrls;<br>
<br>
<span class="keyword">type</span><br>
&nbsp;&nbsp;<span class="type">TForm1</span> = <span class="keyword">class</span>(<span class="type">TForm</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;Label1, Label2, Label3, Label4, Label5, Label6: <span class="type">TLabel</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit1, Edit2, Edit3: <span class="type">TEdit</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;BTNCargar, Button2, Button1: <span class="type">TButton</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;MainMenu1: <span class="type">TMainMenu</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Cadenas1, Cargar1, Cargar2, Minuscula1, Vocales1, BuscarCaracter1: <span class="type">TMenuItem</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">// Procedimientos de eventos OnClick</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> BTNCargarClick(Sender: <span class="type">TObject</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button2Click(Sender: <span class="type">TObject</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button1Click(Sender: <span class="type">TObject</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Cargar1Click(Sender: <span class="type">TObject</span>); <span class="comment">// Espacios</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Cargar2Click(Sender: <span class="type">TObject</span>); <span class="comment">// Mayúsculas</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Vocales1Click(Sender: <span class="type">TObject</span>); <span class="comment">// Vocales</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Minuscula1Click(Sender: <span class="type">TObject</span>); <span class="comment">// Minúsculas</span><br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;Form1: <span class="type">TForm1</span>;<br>
&nbsp;&nbsp;cad: <span class="type">String</span>; <span class="comment">// Variable global</span><br>
&nbsp;&nbsp;n, i: <span class="type">Byte</span>;<br>
<br>
<span class="keyword">implementation</span><br>
<br>
{$R *.dfm}<br>
<br>
<span class="comment">// Las 40 funciones y procedimientos están implementados abajo y en el archivo Cadena.pas</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.5rem;">
            💡 El archivo completo <code>Cadena.pas</code> se encuentra generado en tu carpeta de proyecto: <code>D:\Introz2\practico07\Cadena.pas</code> listo para abrir y compilar en Delphi 12 Community Edition.
          </p>
        </div>
      </div>


      <!-- BUSCADOR Y FILTROS DE EJERCICIOS -->
      <div style="margin-top: 2rem;">
        <h3 style="color: #fff; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>📚</span> Banco de los 40 Ejercicios Resueltos Paso a Paso
        </h3>

        <!-- INPUT DE BÚSQUEDA -->
        <div class="qa-search-box">
          <input type="text" id="searchP8Input" placeholder="🔍 Buscar por número, título, función, vocales, espacios, mayúsculas, palabras, anagramas..." onkeyup="filterP8Exercises()">
        </div>

        <!-- BOTONES DE CATEGORÍA -->
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
          <button class="btn-print active-cat" id="catBtn-all" onclick="filtrarP8Categoria('all', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Todos (40)</button>
          <button class="btn-print" id="catBtn-basicos" onclick="filtrarP8Categoria('basicos', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Básicos & Letras (1-10)</button>
          <button class="btn-print" id="catBtn-espacios" onclick="filtrarP8Categoria('espacios', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Espacios & Modificación (11-20)</button>
          <button class="btn-print" id="catBtn-palabras" onclick="filtrarP8Categoria('palabras', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Palabras & Frases (21-30)</button>
          <button class="btn-print" id="catBtn-avanzados" onclick="filtrarP8Categoria('avanzados', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Algoritmos Avanzados (31-40)</button>
          <button class="btn-print" id="catBtn-func" onclick="filtrarP8Categoria('func', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Solo Funciones</button>
          <button class="btn-print" id="catBtn-proc" onclick="filtrarP8Categoria('proc', this)" style="font-size: 0.82rem; padding: 0.4rem 0.8rem;">Solo Procedimientos</button>
        </div>

        <!-- CONTADOR DE RESULTADOS -->
        <div id="p8Counter" style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 1rem;">
          Mostrando 40 de 40 ejercicios.
        </div>
      </div>

      <!-- LISTA DE LOS 40 EJERCICIOS ACORDEÓN -->
      <div id="p8List">
''')

    # Generar las tarjetas de los 40 ejercicios
    for ej in EJERCICIOS_DATA:
        num = ej["num"]
        num_str = f"{num:02d}"
        titulo = ej["titulo"]
        tipo = ej["tipo"]
        cat = ej["categoria"]
        badge_tipo_color = "#38bdf8" if tipo == "Función" else "#a855f7"
        badge_tipo_bg = "rgba(56, 189, 248, 0.15)" if tipo == "Función" else "rgba(168, 85, 247, 0.15)"

        out.append(f'''
        <!-- EJERCICIO {num} -->
        <div class="qa-item p8-item" data-cat="{cat}" data-tipo="{tipo.lower()}">
          <div class="qa-header" onclick="toggleQA(this)">
            <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
              <span class="qa-number">EJ {num_str}</span>
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
            <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo Modular:</h5>
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

        pascal_code = highlight_pascal(ej["codigo_pascal"])
        vcl_code = highlight_pascal(ej["codigo_vcl"])
        ent_ejemplo = html.escape(ej["entrada_ejemplo"])
        sal_ejemplo = html.escape(ej["salida_ejemplo"])
        extra_default = html.escape(ej.get("extra_default", ""))

        out.append(f'''
            <!-- CÓDIGO DELPHI PASCAL MODULAR -->
            <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi Pascal (Algoritmo Modular):</h5>
            <div class="code-wrapper">
              <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
              <div class="code-block">
{pascal_code}
              </div>
            </div>

            <!-- EVENTO VCL EN EL FORMULARIO TForm1 -->
            <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Evento en Formulario Delphi (TForm1 / MainMenu Click):</h5>
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
                <div style="font-size: 0.82rem; color: #10b981;">📤 Salida esperada: <strong>{sal_ejemplo}</strong></div>
              </div>
              <button class="btn-print" style="background: #10b981; color: #0f172a; font-weight: bold; border-color: #059669; font-size: 0.82rem; cursor: pointer;" data-p8-num="{num}" data-p8-ent="{ent_ejemplo}" data-p8-extra="{extra_default}" onclick="p8ProbarBtnClick(this)">
                ▶ Probar en el Formulario
              </button>
            </div>

          </div>
        </div>
''')

    out.append('''
      </div> <!-- Fin #p8List -->

    </div> <!-- Fin .card -->
  </section>
  <!-- ========================================================================= -->
  <!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #8                                  -->
  <!-- ========================================================================= -->
''')

    return '\n'.join(out)

def build_p8_js():
    js = '''
  // ===========================================================================
  //      MOTOR JAVASCRIPT DEL SIMULADOR VCL Y PRÁCTICO #8 (40 EJERCICIOS)
  // ===========================================================================

  let p8GlobalCad = "Hola Mundo Delphi 2026";
  let p8GlobalN = 22;
  let p8GlobalI = 1;

  function btnP8Registrar() {
    const edit1 = document.getElementById('p8SimEdit1');
    p8GlobalCad = edit1.value;
    p8GlobalN = p8GlobalCad.length;
    document.getElementById('p8SimLabel5').innerText = 'cad=' + p8GlobalCad;
    showMobileToast('cadena de caracter registrado');
  }

  function btnP8Longitud() {
    p8GlobalN = p8GlobalCad.length;
    document.getElementById('p8SimEdit2').value = p8GlobalN + ' caracteres';
    showMobileToast('Longitud calculada: ' + p8GlobalN);
  }

  function btnP8Close() {
    document.getElementById('p8SimEdit1').value = '';
    document.getElementById('p8SimEdit2').value = '';
    document.getElementById('p8SimEdit3').value = '';
    document.getElementById('p8SimExtra').value = '';
    p8GlobalCad = '';
    p8GlobalN = 0;
    document.getElementById('p8SimLabel5').innerText = 'cad=';
    document.getElementById('p8ConsoleBox').style.display = 'none';
    showMobileToast('Formulario restablecido (Close)');
  }

  function toggleP8MenuDropdown() {
    const dd = document.getElementById('p8MenuDropdown');
    dd.style.display = (dd.style.display === 'block') ? 'none' : 'block';
  }

  // Cerrar dropdown si se hace clic fuera
  document.addEventListener('click', function(e) {
    const btn = document.getElementById('p8MenuBtn');
    const dd = document.getElementById('p8MenuDropdown');
    if (btn && dd && !btn.contains(e.target) && !dd.contains(e.target)) {
      dd.style.display = 'none';
    }
  });

  function p8EjecutarMenu(ejNum) {
    toggleP8MenuDropdown();
    document.getElementById('p8SimSelectEj').value = ejNum;
    p8SeleccionarEjercicioRapido();
    p8EjecutarDesdeSimulador();
  }

  function p8SeleccionarEjercicioRapido() {
    const sel = document.getElementById('p8SimSelectEj');
    const ejNum = parseInt(sel.value);
    const extraInput = document.getElementById('p8SimExtra');
    const tagTipo = document.getElementById('p8SimTagTipo');

    // Determinar si el ejercicio requiere parámetro extra
    const conParamExtra = {
      9: { label: "Segunda cadena:", def: "UAGRM" },
      10: { label: "Letra a buscar:", def: "a" },
      12: { label: "Cantidad N:", def: "5" },
      18: { label: "Palabra a buscar:", def: "Mundo" },
      19: { label: "Letra vieja,nueva (ej: a,o):", def: "a,o" },
      20: { label: "Letra a eliminar:", def: "e" },
      21: { label: "Palabra a contar:", def: "Mundo" },
      30: { label: "Segunda cadena a intercalar:", def: "12345" },
      39: { label: "Segunda palabra para anagrama:", def: "amor" }
    };

    if (conParamExtra[ejNum]) {
      extraInput.placeholder = conParamExtra[ejNum].label;
      if (!extraInput.value) extraInput.value = conParamExtra[ejNum].def;
      document.getElementById('p8SimExtraRow').style.opacity = '1';
    } else {
      document.getElementById('p8SimExtraRow').style.opacity = '0.6';
    }

    const procs = [2, 14, 22, 28, 29];
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

  function p8ProbarBtnClick(btn) {
    const num = parseInt(btn.getAttribute('data-p8-num'), 10);
    const ent = btn.getAttribute('data-p8-ent') || '';
    const extra = btn.getAttribute('data-p8-extra') || '';
    p8ProbarEnSimulador(num, ent, extra);
  }

  function p8ProbarEnSimulador(ejNum, ent, extraVal) {
    // Si la entrada viene como formato cad='...', extraer
    let texto = ent;
    if (texto.includes("cad='")) {
      const m = texto.match(/cad='([^']+)'/);
      if (m) texto = m[1];
    } else if (texto.includes("pal='")) {
      const m = texto.match(/pal='([^']+)'/);
      if (m) texto = m[1];
    } else if (texto.includes("frase='")) {
      const m = texto.match(/frase='([^']+)'/);
      if (m) texto = m[1];
    }

    document.getElementById('p8SimEdit1').value = texto;
    btnP8Registrar();
    btnP8Longitud();

    if (extraVal) {
      document.getElementById('p8SimExtra').value = extraVal;
    }

    document.getElementById('p8SimSelectEj').value = ejNum;
    p8SeleccionarEjercicioRapido();
    p8EjecutarDesdeSimulador();

    // Scroll suave hacia el simulador Delphi
    const targetWin = document.getElementById('p8DelphiWindow') || document.querySelector('.delphi-window');
    if (targetWin) {
      targetWin.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  function p8EjecutarDesdeSimulador() {
    const ejNum = parseInt(document.getElementById('p8SimSelectEj').value);
    const cadActual = document.getElementById('p8SimEdit1').value;
    p8GlobalCad = cadActual;
    p8GlobalN = cadActual.length;
    document.getElementById('p8SimLabel5').innerText = 'cad=' + p8GlobalCad;

    const extraVal = document.getElementById('p8SimExtra').value.trim();
    const edit3 = document.getElementById('p8SimEdit3');
    const consoleBox = document.getElementById('p8ConsoleBox');
    const consoleOut = document.getElementById('p8ConsoleOutput');

    consoleBox.style.display = 'none';
    consoleOut.innerText = '';

    const esVocal = (c) => ['A','E','I','O','U','Á','É','Í','Ó','Ú'].includes(c.toUpperCase());
    const esLetra = (c) => /^[A-Za-zÁÉÍÓÚáéíóúñÑ]$/.test(c);
    const esConsonante = (c) => esLetra(c) && !esVocal(c);
    const normalizar = (s) => s.trim().replace(/\\s+/g, ' ');

    let res = "";

    switch(ejNum) {
      case 1: // Contar caracteres
        res = p8GlobalN + ' caracteres';
        break;

      case 2: // Primera letra
        {
          let letra = '';
          for (let ch of p8GlobalCad) {
            if (esLetra(ch)) { letra = ch; break; }
          }
          res = letra ? 'Primera letra: ' + letra : 'No contiene letras';
        }
        break;

      case 3: // Última letra
        {
          let letra = '';
          for (let i = p8GlobalCad.length - 1; i >= 0; i--) {
            if (esLetra(p8GlobalCad[i])) { letra = p8GlobalCad[i]; break; }
          }
          res = letra ? 'Ultima letra: ' + letra : 'No contiene letras';
        }
        break;

      case 4: // Contar vocales
        {
          let c = 0;
          for (let ch of p8GlobalCad) if (esVocal(ch)) c++;
          res = c + ' vocales';
        }
        break;

      case 5: // Contar consonantes
        {
          let c = 0;
          for (let ch of p8GlobalCad) if (esConsonante(ch)) c++;
          res = c + ' consonantes';
        }
        break;

      case 6: // Mayúsculas
        res = p8GlobalCad.toUpperCase();
        break;

      case 7: // Minúsculas
        res = p8GlobalCad.toLowerCase();
        break;

      case 8: // Invertir cadena
        res = p8GlobalCad.split('').reverse().join('');
        break;

      case 9: // Concatenar
        res = p8GlobalCad + ' ' + (extraVal || 'UAGRM');
        break;

      case 10: // Ocurrencias letra
        {
          const l = (extraVal || 'a').toLowerCase();
          let c = 0;
          for (let ch of p8GlobalCad) if (ch.toLowerCase() === l) c++;
          res = 'La letra "' + l + '" aparece ' + c + ' veces';
        }
        break;

      case 11: // Eliminar espacios
        res = p8GlobalCad.replace(/\\s+/g, '');
        break;

      case 12: // Primeros N caracteres
        {
          const nCant = parseInt(extraVal) || 5;
          res = p8GlobalCad.substring(0, nCant);
        }
        break;

      case 13: // Determinar si está vacía
        res = (p8GlobalCad.trim().length === 0) ? 'La cadena esta VACIA' : 'La cadena CONTIENE TEXTO';
        break;

      case 14: // Códigos ASCII
        {
          let lineas = "";
          for (let i = 0; i < p8GlobalCad.length; i++) {
            lineas += "'" + p8GlobalCad[i] + "' -> ASCII: " + p8GlobalCad.charCodeAt(i) + "\\n";
          }
          res = 'Ver códigos en consola VCL';
          consoleBox.style.display = 'block';
          consoleOut.innerText = lineas;
        }
        break;

      case 15: // Contar mayúsculas
        {
          let c = 0;
          for (let ch of p8GlobalCad) if (ch >= 'A' && ch <= 'Z') c++;
          res = c + ' Mayusculas';
        }
        break;

      case 16: // Es palíndroma
        {
          const limpia = p8GlobalCad.toLowerCase().replace(/[^a-z0-9]/g, '');
          const rev = limpia.split('').reverse().join('');
          res = (limpia.length > 0 && limpia === rev) ? 'SI es Palindroma (Capicúa)' : 'NO es Palindroma';
        }
        break;

      case 17: // Contar palabras
        {
          const palabras = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0);
          res = palabras.length + ' palabras';
        }
        break;

      case 18: // Verificar si existe palabra
        {
          const buscada = extraVal || 'Delphi';
          const existe = p8GlobalCad.toLowerCase().includes(buscada.toLowerCase());
          res = existe ? 'SI existe la palabra "' + buscada + '"' : 'NO existe la palabra "' + buscada + '"';
        }
        break;

      case 19: // Reemplazar letra
        {
          const partes = (extraVal || 'a,o').split(',');
          const v = partes[0] || 'a';
          const n = partes[1] || 'o';
          res = p8GlobalCad.split(v).join(n);
        }
        break;

      case 20: // Eliminar letra
        {
          const l = extraVal || 'e';
          res = p8GlobalCad.split('').filter(c => c.toLowerCase() !== l.toLowerCase()).join('');
        }
        break;

      case 21: // Contar ocurrencias palabra
        {
          const pal = (extraVal || 'Mundo').toLowerCase();
          const tokens = p8GlobalCad.toLowerCase().split(/[^a-záéíóú0-9]/).filter(t => t === pal);
          res = 'La palabra "' + pal + '" aparece ' + tokens.length + ' veces';
        }
        break;

      case 22: // Mostrar cada carácter en una línea
        {
          let outText = "";
          for (let i = 0; i < p8GlobalCad.length; i++) {
            outText += "[" + (i + 1) + "]: " + p8GlobalCad[i] + "\\n";
          }
          res = 'Caracteres listados en consola VCL';
          consoleBox.style.display = 'block';
          consoleOut.innerText = outText;
        }
        break;

      case 23: // Números o solo letras
        {
          let tieneLetras = false, tieneDigitos = false, otros = false;
          for (let ch of p8GlobalCad) {
            if (esLetra(ch)) tieneLetras = true;
            else if (ch >= '0' && ch <= '9') tieneDigitos = true;
            else if (ch !== ' ') otros = true;
          }
          if (tieneDigitos && !tieneLetras && !otros) res = 'Solo digitos numericos';
          else if (tieneLetras && !tieneDigitos && !otros) res = 'Solo letras';
          else if (tieneLetras && tieneDigitos) res = 'Alfanumerica (Letras y Numeros)';
          else res = 'Contiene caracteres especiales';
        }
        break;

      case 24: // Contar dígitos
        {
          let c = 0;
          for (let ch of p8GlobalCad) if (ch >= '0' && ch <= '9') c++;
          res = c + ' digitos numericos';
        }
        break;

      case 25: // Extraer primera palabra
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0);
          res = pals.length > 0 ? 'Primera: "' + pals[0] + '"' : '';
        }
        break;

      case 26: // Extraer última palabra
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0);
          res = pals.length > 0 ? 'Ultima: "' + pals[pals.length - 1] + '"' : '';
        }
        break;

      case 27: // Normalizar espacios
        res = normalizar(p8GlobalCad);
        break;

      case 28: // Palabras que empiezan con vocal
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0 && esVocal(w[0]));
          res = 'Empiezan con vocal: ' + (pals.join(', ') || 'Ninguna');
        }
        break;

      case 29: // Palabras que terminan en consonante
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0 && esConsonante(w[w.length - 1]));
          res = 'Terminan en consonante: ' + (pals.join(', ') || 'Ninguna');
        }
        break;

      case 30: // Intercalar dos cadenas
        {
          const cad2 = extraVal || '12345';
          let intercalada = '';
          const maxL = Math.max(p8GlobalCad.length, cad2.length);
          for (let i = 0; i < maxL; i++) {
            if (i < p8GlobalCad.length) intercalada += p8GlobalCad[i];
            if (i < cad2.length) intercalada += cad2[i];
          }
          res = intercalada;
        }
        break;

      case 31: // Palabras con más de 5 letras
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 5);
          res = pals.length + ' palabras con > 5 letras (' + pals.join(', ') + ')';
        }
        break;

      case 32: // Reemplazar vocales por *
        res = p8GlobalCad.replace(/[aeiouáéíóúAEIOUÁÉÍÓÚ]/g, '*');
        break;

      case 33: // Eliminar acentos
        res = p8GlobalCad.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "");
        break;

      case 34: // Palabra más larga
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0);
          let mayor = "";
          for (let p of pals) if (p.length > mayor.length) mayor = p;
          res = 'Mas larga: "' + mayor + '" (' + mayor.length + ' letras)';
        }
        break;

      case 35: // Palabra más corta
        {
          const pals = normalizar(p8GlobalCad).split(' ').filter(w => w.length > 0);
          let menor = pals[0] || "";
          for (let p of pals) if (p.length < menor.length) menor = p;
          res = 'Mas corta: "' + menor + '" (' + menor.length + ' letras)';
        }
        break;

      case 36: // Contar palabras repetidas
        {
          const pals = normalizar(p8GlobalCad).toLowerCase().split(' ').filter(w => w.length > 0);
          const frec = {};
          for (let p of pals) frec[p] = (frec[p] || 0) + 1;
          const rep = Object.keys(frec).filter(k => frec[k] > 1);
          res = rep.length + ' palabras repetidas (' + rep.join(', ') + ')';
        }
        break;

      case 37: // Solo contiene letras
        {
          const soloL = p8GlobalCad.length > 0 && /^[A-Za-zÁÉÍÓÚáéíóúñÑ]+$/.test(p8GlobalCad);
          res = soloL ? 'SI: Solo contiene letras' : 'NO: Contiene espacios, numeros o simbolos';
        }
        break;

      case 38: // Caracteres únicos
        {
          let unicos = '';
          for (let ch of p8GlobalCad) {
            if (!unicos.includes(ch)) unicos += ch;
          }
          res = unicos;
        }
        break;

      case 39: // Son anagramas
        {
          const cad2 = (extraVal || 'amor').toLowerCase().replace(/[^a-z]/g, '').split('').sort().join('');
          const c1 = p8GlobalCad.toLowerCase().replace(/[^a-z]/g, '').split('').sort().join('');
          const sonAnag = (c1.length > 0 && c1 === cad2);
          res = sonAnag ? 'SI: Son anagramas' : 'NO: No son anagramas';
        }
        break;

      case 40: // Caracteres índice impar (posiciones 1, 3, 5...)
        {
          let impares = '';
          for (let i = 0; i < p8GlobalCad.length; i += 2) {
            impares += p8GlobalCad[i];
          }
          res = impares;
        }
        break;

      default:
        res = 'Ejercicio no implementado';
    }

    edit3.value = res;
    showMobileToast('Ejecutado Ej ' + ejNum + ' exitosamente');
  }

  function toggleArquitecturaP8(btn) {
    const box = document.getElementById('p8ArquitecturaBox');
    if (box.style.display === 'none' || !box.style.display) {
      box.style.display = 'block';
      btn.innerText = 'Ocultar Código Cadena.pas';
    } else {
      box.style.display = 'none';
      btn.innerText = 'Mostrar Código Cadena.pas';
    }
  }

  function filterP8Exercises() {
    const query = document.getElementById('searchP8Input').value.toLowerCase();
    const items = document.querySelectorAll('#p8List .p8-item');
    let visible = 0;

    items.forEach(item => {
      const text = item.innerText.toLowerCase();
      if (text.includes(query)) {
        item.style.display = '';
        visible++;
      } else {
        item.style.display = 'none';
      }
    });

    document.getElementById('p8Counter').innerText = 'Mostrando ' + visible + ' de ' + items.length + ' ejercicios.';
  }

  function filtrarP8Categoria(cat, btn) {
    document.querySelectorAll('.btn-print').forEach(b => b.classList.remove('active-cat'));
    btn.classList.add('active-cat');

    const items = document.querySelectorAll('#p8List .p8-item');
    let visible = 0;

    items.forEach(item => {
      const itemCat = item.getAttribute('data-cat');
      const itemTipo = item.getAttribute('data-tipo');

      let match = false;
      if (cat === 'all') match = true;
      else if (cat === 'func') match = (itemTipo === 'función' || itemTipo === 'funcion');
      else if (cat === 'proc') match = (itemTipo === 'procedimiento');
      else match = (itemCat === cat);

      if (match) {
        item.style.display = '';
        visible++;
      } else {
        item.style.display = 'none';
      }
    });

    document.getElementById('p8Counter').innerText = 'Mostrando ' + visible + ' de ' + items.length + ' ejercicios.';
  }
'''
    return js + '\n\n' + docx_teoria.build_cadenas_docx_js()

if __name__ == '__main__':
    print("Módulo de generación de HTML y JS para Práctico 8 listo.")
