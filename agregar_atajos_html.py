# -*- coding: utf-8 -*-

def add_cheatsheet_tab():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add nav button
    nav_btn_html = '<button class="nav-btn" onclick="switchTab(\'hoja-atajos\')">⚡ 12. Hoja de Atajos (Cheat Sheet)</button>'
    if 'hoja-atajos' not in html:
        pos_nav_end = html.find('</nav>')
        html = html[:pos_nav_end] + '    ' + nav_btn_html + '\n  ' + html[pos_nav_end:]
        print("Nav button added.")

    # 2. Add section
    section_cheatsheet = '''
  <!-- SECCIÓN 12: HOJA DE ATAJOS Y GUÍA RÁPIDA (CHEAT SHEET) -->
  <section id="hoja-atajos" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">⚡ Hoja de Atajos y Fórmulas Rápidas (Cheat Sheet)</h2>
        <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">INF110-Z2 • GUÍA DE BOLSILLO</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resumen ultrarrápido con los <strong>atajos de teclado de Delphi</strong>, las <strong>fórmulas matemáticas para descomposición de dígitos</strong>, <strong>conversiones de tipo</strong> y <strong>plantillas de funciones y procedimientos</strong>.
      </p>

      <!-- BUSCADOR DE ATAJOS -->
      <div class="qa-search-box">
        <input type="text" id="searchAtajosInput" placeholder="🔍 Buscar atajo o fórmula (ej: F9, F12, mod 10, primo, invertir, StrToInt, var)..." onkeyup="filterAtajos()">
      </div>

      <!-- 1. ATAJOS DE TECLADO DELPHI -->
      <h3 style="color: #fff; margin-top: 1.5rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>⌨️</span> 1. Atajos de Teclado Indispensables en Delphi RAD Studio
      </h3>
      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 25%;">Atajo de Teclado</th>
              <th style="width: 75%;">Función y Utilidad en Laboratorio</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F9</kbd></td>
              <td><strong>Compilar y Ejecutar</strong> el proyecto (Run).</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F12</kbd></td>
              <td><strong>Alternar</strong> entre la vista de Código Pascal (<code>.pas</code>) y el Diseñador Visual del Formulario (<code>.dfm</code>).</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Shift</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">C</kbd></td>
              <td><strong>Class Completion:</strong> Genera automáticamente el cuerpo de los métodos declarados en la clase <code>TForm1</code> dentro de <code>implementation</code>.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Espacio</kbd></td>
              <td><strong>Code Completion (IntelliSense):</strong> Muestra sugerencias de funciones, variables y propiedades.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Shift</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">↑ / ↓</kbd></td>
              <td><strong>Navegación Rápida:</strong> Salta entre la cabecera en <code>interface</code> y el código en <code>implementation</code>.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F11</kbd></td>
              <td><strong>Object Inspector:</strong> Abre la barra lateral para editar Properties y Events (<code>OnClick</code>).</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F9</kbd></td>
              <td><strong>Compilar sintaxis:</strong> Verifica que no haya errores de compilación sin abrir la aplicación.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F8</kbd> / <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F7</kbd></td>
              <td><strong>Depurador Paso a Paso:</strong> <code>F8</code> avanza línea por línea (Step Over); <code>F7</code> entra al subprograma (Trace Into).</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd> + <kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">/</kbd></td>
              <td><strong>Comentar / Descomentar</strong> bloques de código con <code>//</code>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 2. FÓRMULAS DE NÚMEROS NATURALES -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>🔢</span> 2. Fórmulas y Patrones Esenciales para Números Naturales
      </h3>
      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 25%;">Operación / Patrón</th>
              <th style="width: 35%;">Sintaxis en Pascal / Delphi</th>
              <th style="width: 40%;">Explicación y Ejemplo</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Extraer último dígito</strong></td>
              <td><code>d := n mod 10;</code></td>
              <td>Obtiene las unidades. Ej: <code>1234 mod 10 = 4</code>.</td>
            </tr>
            <tr>
              <td><strong>Eliminar último dígito</strong></td>
              <td><code>n := n div 10;</code></td>
              <td>Trunca el último dígito. Ej: <code>1234 div 10 = 123</code>.</td>
            </tr>
            <tr>
              <td><strong>Bucle de recorrido</strong></td>
              <td><code>while n > 0 do begin ... end;</code></td>
              <td>Recorre de derecha a izquierda hasta consumir el número.</td>
            </tr>
            <tr>
              <td><strong>Dígito Par</strong></td>
              <td><code>if (d mod 2 = 0) then</code></td>
              <td>Verifica divisibilidad entre 2 (dígitos 0, 2, 4, 6, 8).</td>
            </tr>
            <tr>
              <td><strong>Dígito Impar</strong></td>
              <td><code>if (d mod 2 &lt;&gt; 0) then</code></td>
              <td>Verifica no divisibilidad entre 2 (dígitos 1, 3, 5, 7, 9).</td>
            </tr>
            <tr>
              <td><strong>Dígito Primo</strong></td>
              <td><code>(d = 2) or (d = 3) or (d = 5) or (d = 7)</code></td>
              <td>Únicos primos entre 0 y 9 en base 10.</td>
            </tr>
            <tr>
              <td><strong>Múltiplo de K</strong></td>
              <td><code>if (d mod K = 0) then</code></td>
              <td>Múltiplo de 3 (<code>d mod 3 = 0</code>), múltiplo de 4 (<code>d mod 4 = 0</code>).</td>
            </tr>
            <tr>
              <td><strong>Invertir número</strong></td>
              <td><code>inv := (inv * 10) + d;</code></td>
              <td>Desplaza a la izquierda multiplicando por 10 y añade <code>d</code>.</td>
            </tr>
            <tr>
              <td><strong>Construir en orden original</strong></td>
              <td><code>res := res + (d * pot);<br>pot := pot * 10;</code></td>
              <td>Mantiene la posición relativa (inicializar <code>pot := 1</code>).</td>
            </tr>
            <tr>
              <td><strong>Capicúa (Palíndromo)</strong></td>
              <td><code>EsCapicua := (n = InvertirNumero(n));</code></td>
              <td>Comprueba si el número original coincide con su invertido.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 3. CONVERSIONES DE TIPOS Y VCL -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>🔄</span> 3. Conversiones de Tipo y Manipulación VCL
      </h3>
      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 25%;">Conversión / Acción</th>
              <th style="width: 35%;">Código Delphi</th>
              <th style="width: 40%;">Uso Común en el Formulario</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Texto &rarr; Entero</strong></td>
              <td><code>n := StrToInt(Edit1.Text);</code></td>
              <td>Leer número ingresado por el usuario en <code>Edit1</code>.</td>
            </tr>
            <tr>
              <td><strong>Entero &rarr; Texto</strong></td>
              <td><code>Edit2.Text := IntToStr(resultado);</code></td>
              <td>Mostrar el resultado entero en la caja <code>Edit2</code>.</td>
            </tr>
            <tr>
              <td><strong>Real &rarr; Texto (2 dec)</strong></td>
              <td><code>Edit2.Text := FloatToStrF(prom, ffFixed, 8, 2);</code></td>
              <td>Mostrar promedios formateados (ej: <code>4.67</code>).</td>
            </tr>
            <tr>
              <td><strong>Ventana Emergente</strong></td>
              <td><code>ShowMessage('Mensaje: ' + IntToStr(n));</code></td>
              <td>Mostrar diálogo modal informativo en pantalla.</td>
            </tr>
            <tr>
              <td><strong>Carácter dígito &rarr; Entero</strong></td>
              <td><code>d := Ord(s[i]) - Ord('0');</code></td>
              <td>Convierte el carácter <code>'7'</code> a su valor entero <code>7</code>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 4. PLANTILLA MODULAR: FUNCIÓN VS PROCEDIMIENTO -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>📐</span> 4. Plantilla Base: Función vs. Procedimiento
      </h3>
      <div class="tag-grid">
        <div class="tag-card emerald">
          <h4 style="color:#10b981;">Función (function)</h4>
          <p><strong>Devuelve UN SOLO valor</strong> escalar por su nombre o <code>Result</code>.</p>
          <div class="code-wrapper" style="margin-top:0.75rem;">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block" style="font-size:0.78rem; padding:0.75rem;">
<span class="keyword">function</span> <span class="function-name">CalcularAlgo</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, res: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;res := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">// proceso con d...</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := res;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>

        <div class="tag-card purple">
          <h4 style="color:#a855f7;">Procedimiento (procedure)</h4>
          <p><strong>Devuelve MÚLTIPLES valores</strong> mediante parámetros por referencia (<code>var</code>).</p>
          <div class="code-wrapper" style="margin-top:0.75rem;">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block" style="font-size:0.78rem; padding:0.75rem;">
<span class="keyword">procedure</span> <span class="function-name">ObtenerDosValores</span>(n: <span class="type">Word</span>; <span class="keyword">var</span> s1, s2: <span class="type">Byte</span>);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;s1 := n <span class="keyword">mod</span> <span class="number">10</span>; <span class="comment">// último</span><br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt;= <span class="number">10</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;s2 := n;        <span class="comment">// primero</span><br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
'''

    if 'id="hoja-atajos"' not in html:
        sec_end = html.find('</div>\n\n<script>')
        if sec_end == -1:
            sec_end = html.rfind('</div>\n  <!-- Botón flotante')
        if sec_end == -1:
            sec_end = html.rfind('</div>\n\n')
        
        # insert section before the closing container div
        container_close = html.rfind('</div>\n  <!-- Botón')
        if container_close == -1:
            container_close = html.rfind('</div>\n\n<script>')
        if container_close == -1:
            container_close = html.rfind('</section>') + len('</section>')
            
        html = html[:container_close] + section_cheatsheet + '\n' + html[container_close:]
        print("Section hoja-atajos added.")

    # JS Search Filter for Atajos
    js_atajos_filter = '''
  // --- BUSCADOR DE LA HOJA DE ATAJOS ---
  function filterAtajos() {
    const input = document.getElementById('searchAtajosInput').value.toLowerCase();
    const rows = document.querySelectorAll('.atajos-table tbody tr');
    rows.forEach(row => {
      const text = row.innerText.toLowerCase();
      if (text.includes(input)) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    });
  }
'''
    if 'filterAtajos' not in html:
        script_end = html.rfind('</script>')
        html = html[:script_end] + js_atajos_filter + '\n' + html[script_end:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("teoria_programacion_modular.html updated with complete interactive Cheat Sheet!")

if __name__ == '__main__':
    add_cheatsheet_tab()
