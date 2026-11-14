# -*- coding: utf-8 -*-

def update_html_with_debugging_and_clean_code():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Section 12 enhanced content (Hoja de Atajos + Debugging + Clean Code + InputBox)
    section_12_new = '''  <!-- SECCIÓN 12: HOJA DE ATAJOS Y GUÍA RÁPIDA (CHEAT SHEET) -->
  <section id="hoja-atajos" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">⚡ Hoja de Atajos, Debugging y Clean Code (Guía de Bolsillo)</h2>
        <span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8;">INF110-Z2 • GUÍA DE BOLSILLO</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resumen ultrarrápido con <strong>atajos de depuración (Debugger) en Delphi</strong>, <strong>estándares de código limpio (Clean Code) con nombres auto-descriptivos</strong>, <strong>uso de InputBox</strong>, <strong>fórmulas matemáticas de descomposición</strong> y <strong>plantillas de funciones y procedimientos</strong>.
      </p>

      <!-- BUSCADOR DE ATAJOS -->
      <div class="qa-search-box">
        <input type="text" id="searchAtajosInput" placeholder="🔍 Buscar atajo, breakpoint, F8, F7, InputBox, digitoActual, mod 10, primo, var..." onkeyup="filterAtajos()">
      </div>

      <!-- 1. GUÍA DE DEPURACIÓN (DEBUGGER) EN DELPHI -->
      <h3 style="color: #fff; margin-top: 1.5rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>🐞</span> 1. Atajos de Depuración (Debugger) Paso a Paso en Delphi RAD Studio
      </h3>
      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 20%;">Atajo</th>
              <th style="width: 30%;">Herramienta de Depuración</th>
              <th style="width: 50%;">Para Qué Sirve y Cómo Usarlo</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F5</kbd></td>
              <td><strong>Poner / Quitar Breakpoint</strong></td>
              <td>Marca la línea con un punto rojo (o clic en el margen izquierdo). La ejecución se pausará automáticamente al llegar a esa línea para inspeccionar la memoria.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F9</kbd></td>
              <td><strong>Ejecutar con Debugger (Run)</strong></td>
              <td>Inicia el programa en modo depuración hasta detenerse en el primer Breakpoint activo.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F8</kbd></td>
              <td><strong>Step Over (Paso a Paso)</strong></td>
              <td>Avanza a la siguiente línea de código sin entrar dentro de los subprogramas o funciones llamadas.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F7</kbd></td>
              <td><strong>Trace Into (Entrar a la Función)</strong></td>
              <td>Entra dentro del código de la función invocada (ej: <code>EsPrimo</code> o <code>InvertirNumero</code>) para ver su ejecución interna línea por línea.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd>+<kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F5</kbd></td>
              <td><strong>Watch List (Inspeccionar Variable)</strong></td>
              <td>Abre la ventana de Watch List para ver cómo cambian en vivo los valores de <code>digitoActual</code>, <code>sumaAcumulada</code>, <code>potencia</code>, etc.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd>+<kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F7</kbd></td>
              <td><strong>Evaluate / Modify</strong></td>
              <td>Permite evaluar fórmulas al vuelo o modificar temporalmente el valor de una variable en memoria durante la pausa.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd>+<kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F2</kbd></td>
              <td><strong>Program Reset (Detener)</strong></td>
              <td>Finaliza la sesión de depuración y vuelve al editor de código normal.</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">F12</kbd></td>
              <td><strong>Alternar Código / Formulario</strong></td>
              <td>Cambia instantáneamente entre la vista de código Pascal (<code>.pas</code>) y el diseñador visual (<code>.dfm</code>).</td>
            </tr>
            <tr>
              <td><kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Ctrl</kbd>+<kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">Shift</kbd>+<kbd style="background:#1e293b; color:#38bdf8; padding:0.2rem 0.5rem; border-radius:4px; border:1px solid #475569; font-weight:bold;">C</kbd></td>
              <td><strong>Class Completion</strong></td>
              <td>Autocompleta en <code>implementation</code> las cabeceras de todos los eventos declarados en la clase <code>TForm1</code>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 2. BUENAS PRÁCTICAS: CLEAN CODE Y VARIABLES AUTO-DESCRIPTIVAS -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>✨</span> 2. Buenas Prácticas (Clean Code): Nombres Auto-Descriptivos
      </h3>
      <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0.75rem;">
        Un buen programador escribe código que cualquier persona puede leer y entender sin esfuerzo. En lugar de usar variables crípticas de 1 letra (<code>d</code>, <code>n</code>, <code>s</code>, <code>p</code>), utiliza nombres que expliquen exactamente su rol en el algoritmo:
      </p>

      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 25%;">Variable Corta (Poco Clara)</th>
              <th style="width: 35%;">Nombre Auto-Descriptivo (Recomendado)</th>
              <th style="width: 40%;">Significado en el Algoritmo</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>n</code></td>
              <td><strong style="color:#38bdf8;">numeroNatural / numeroRestante</strong></td>
              <td>El número que se reduce sucesivamente con <code>div 10</code>.</td>
            </tr>
            <tr>
              <td><code>d</code></td>
              <td><strong style="color:#38bdf8;">digitoActual</strong></td>
              <td>El dígito extraído en cada ciclo con <code>mod 10</code>.</td>
            </tr>
            <tr>
              <td><code>suma / s</code></td>
              <td><strong style="color:#38bdf8;">sumaDigitosAcumulada</strong></td>
              <td>Acumulador donde se suman los dígitos que cumplen la condición.</td>
            </tr>
            <tr>
              <td><code>inv</code></td>
              <td><strong style="color:#38bdf8;">numeroInvertido</strong></td>
              <td>Acumulador multiplicativo para armar el número al revés.</td>
            </tr>
            <tr>
              <td><code>npar</code></td>
              <td><strong style="color:#38bdf8;">numeroSoloPares</strong></td>
              <td>Número que almacena exclusivamente los dígitos pares.</td>
            </tr>
            <tr>
              <td><code>pot</code></td>
              <td><strong style="color:#38bdf8;">potenciaPosicional</strong></td>
              <td>Multiplicador (1, 10, 100...) para armar dígitos en su orden original.</td>
            </tr>
            <tr>
              <td><code>c / cont</code></td>
              <td><strong style="color:#38bdf8;">cantidadDigitosValidos</strong></td>
              <td>Contador para promedios o frecuencias.</td>
            </tr>
            <tr>
              <td><code>p / u</code></td>
              <td><strong style="color:#38bdf8;">primerDigito / ultimoDigito</strong></td>
              <td>Extremos más y menos significativos del número.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="code-wrapper">
        <button class="copy-btn" onclick="copyCode(this)">Copiar Código Limpio</button>
        <div class="code-block">
<span class="comment">// EJEMPLO DE CÓDIGO PROFESIONAL, LIMPIO Y FÁCIL DE LEER:</span><br>
<span class="keyword">function</span> <span class="function-name">SumarDigitosPrimos</span>(numeroNatural: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;digitoActual, sumaDigitosPrimos: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;sumaDigitosPrimos := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsPrimo</span>(digitoActual) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sumaDigitosPrimos := sumaDigitosPrimos + digitoActual;<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := sumaDigitosPrimos;<br>
<span class="keyword">end</span>;
        </div>
      </div>

      <!-- 3. USO DE INPUTBOX EN DELPHI -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>📥</span> 3. Captura Rápida de Datos con InputBox (Ventana Emergente Modal)
      </h3>
      <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0.75rem;">
        La función <code>InputBox</code> permite solicitar números o cadenas al usuario a través de una ventana emergente sin necesidad de un control TEdit en la pantalla:
      </p>

      <div class="tag-card amber" style="margin-bottom: 1rem;">
        <h4 style="color:#f59e0b;">Sintaxis de InputBox:</h4>
        <p style="font-family:'Fira Code', monospace; color:#fef08a; font-size:0.95rem; margin:0.35rem 0;">
          textoIngresado := InputBox(TituloVentana, MensajeInstruccion, ValorSugeridoPorDefecto);
        </p>
        <button class="delphi-btn-vcl" style="margin-top:0.5rem; background:#f59e0b; color:#000; font-weight:bold; padding:0.4rem 1rem;" onclick="probarInputBoxWeb()">🎯 Probar InputBox Interactivo Aquí</button>
      </div>

      <div class="code-wrapper">
        <button class="copy-btn" onclick="copyCode(this)">Copiar InputBox Delphi</button>
        <div class="code-block">
<span class="keyword">procedure</span> TForm1.<span class="function-name">ButtonCargarConInputBoxClick</span>(Sender: TObject);<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;textoIngresado: <span class="type">String</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="comment">// Abre ventana modal pidiendo el número al usuario:</span><br>
&nbsp;&nbsp;textoIngresado := <span class="function-name">InputBox</span>(<span class="string">'Cargar Número Natural'</span>, <span class="string">'Por favor ingrese un número natural:'</span>, <span class="string">'1234'</span>);<br><br>
&nbsp;&nbsp;<span class="comment">// Validamos que no esté vacío:</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> textoIngresado &lt;&gt; <span class="string">''</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;n := StrToInt(textoIngresado);<br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit1.Text := IntToStr(n);<br>
&nbsp;&nbsp;&nbsp;&nbsp;ShowMessage(<span class="string">'Número registrado exitosamente: '</span> + IntToStr(n));<br>
&nbsp;&nbsp;<span class="keyword">end</span><br>
&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;ShowMessage(<span class="string">'Operación cancelada.'</span>);<br>
<span class="keyword">end</span>;
        </div>
      </div>

      <!-- 4. FÓRMULAS DE NÚMEROS NATURALES -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>🔢</span> 4. Fórmulas y Patrones Esenciales para Números Naturales
      </h3>
      <div class="table-container atajos-group">
        <table class="atajos-table">
          <thead>
            <tr>
              <th style="width: 25%;">Operación / Patrón</th>
              <th style="width: 35%;">Sintaxis Limpia en Pascal / Delphi</th>
              <th style="width: 40%;">Explicación y Ejemplo</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Extraer último dígito</strong></td>
              <td><code>digitoActual := numero mod 10;</code></td>
              <td>Obtiene las unidades. Ej: <code>1234 mod 10 = 4</code>.</td>
            </tr>
            <tr>
              <td><strong>Eliminar último dígito</strong></td>
              <td><code>numero := numero div 10;</code></td>
              <td>Trunca el último dígito. Ej: <code>1234 div 10 = 123</code>.</td>
            </tr>
            <tr>
              <td><strong>Bucle de recorrido</strong></td>
              <td><code>while numero > 0 do begin ... end;</code></td>
              <td>Recorre de derecha a izquierda hasta consumir el número.</td>
            </tr>
            <tr>
              <td><strong>Dígito Par</strong></td>
              <td><code>if (digitoActual mod 2 = 0) then</code></td>
              <td>Verifica divisibilidad entre 2 (dígitos 0, 2, 4, 6, 8).</td>
            </tr>
            <tr>
              <td><strong>Dígito Impar</strong></td>
              <td><code>if (digitoActual mod 2 <> 0) then</code></td>
              <td>Verifica no divisibilidad entre 2 (dígitos 1, 3, 5, 7, 9).</td>
            </tr>
            <tr>
              <td><strong>Dígito Primo</strong></td>
              <td><code>(d = 2) or (d = 3) or (d = 5) or (d = 7)</code></td>
              <td>Únicos primos entre 0 y 9 en base 10.</td>
            </tr>
            <tr>
              <td><strong>Múltiplo de K</strong></td>
              <td><code>if (digitoActual mod K = 0) then</code></td>
              <td>Múltiplo de 3 (<code>mod 3 = 0</code>), múltiplo de 4 (<code>mod 4 = 0</code>).</td>
            </tr>
            <tr>
              <td><strong>Invertir número</strong></td>
              <td><code>inv := (inv * 10) + digitoActual;</code></td>
              <td>Desplaza a la izquierda multiplicando por 10 y añade <code>d</code>.</td>
            </tr>
            <tr>
              <td><strong>Construir en orden original</strong></td>
              <td><code>res := res + (digito * pot);<br>pot := pot * 10;</code></td>
              <td>Mantiene la posición relativa (inicializar <code>pot := 1</code>).</td>
            </tr>
            <tr>
              <td><strong>Capicúa (Palíndromo)</strong></td>
              <td><code>EsCapicua := (numero = InvertirNumero(numero));</code></td>
              <td>Comprueba si el número original coincide con su invertido.</td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  </section>
'''

    # Replace Section 12 in HTML
    start_s12 = html.find('id="hoja-atajos"')
    if start_s12 != -1:
        tag_start = html.rfind('<section', 0, start_s12)
        tag_end = html.find('</section>', start_s12) + len('</section>')
        html = html[:tag_start] + section_12_new + html[tag_end:]
        print("Section 12 updated with Debugging, Clean Code and InputBox.")

    # Add interactive JS function for probarInputBoxWeb
    js_inputbox = '''
  // --- DEMOSTRACIÓN INTERACTIVA DE INPUTBOX ---
  function probarInputBoxWeb() {
    const val = prompt('Cargar Número Natural (InputBox Demo):\\nPor favor ingrese un número natural:', '1234');
    if (val !== null && val.trim() !== '') {
      const num = parseInt(val) || 0;
      alert(`[ShowMessage]: Número registrado exitosamente en variable global: ${num}`);
      // Actualizar en el form de la clase si está abierto
      const edit1 = document.getElementById('claseEdit1');
      if (edit1) {
        edit1.value = num;
        if (typeof btnClaseCargar === 'function') btnClaseCargar();
      }
    } else {
      alert('[ShowMessage]: Operación cancelada o vacía.');
    }
  }
'''
    if 'probarInputBoxWeb' not in html:
        script_end = html.rfind('</script>')
        html = html[:script_end] + js_inputbox + '\n' + html[script_end:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("teoria_programacion_modular.html fully enhanced!")

if __name__ == '__main__':
    update_html_with_debugging_and_clean_code()
