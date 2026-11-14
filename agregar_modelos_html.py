# -*- coding: utf-8 -*-

def add_exam_models_to_html():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add nav button
    nav_btn_html = '<button class="nav-btn" onclick="switchTab(\'modelos-examen\')">🎯 13. Modelos de Examen (30p)</button>'
    if 'modelos-examen' not in html:
        pos_nav_end = html.find('</nav>')
        html = html[:pos_nav_end] + '    ' + nav_btn_html + '\n  ' + html[pos_nav_end:]
        print("Nav button for Modelos de Examen added.")

    # 2. Section 13 HTML
    section_exam_html = '''
  <!-- SECCIÓN 13: MODELOS DE EXAMEN PARCIAL RESUELTOS (30 PUNTOS C/U) -->
  <section id="modelos-examen" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🎯 Modelos de Examen Parcial Resueltos (INF110-Z2)</h2>
        <span class="badge" style="background: rgba(244, 63, 94, 0.15); color: #f43f5e; border-color: rgba(244, 63, 94, 0.3);">📝 Ponderación: 30 Puntos c/u</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución formal completa (<strong>Análisis &rarr; Pseudocódigo &rarr; Prueba de Escritorio &rarr; Delphi Clean Code &rarr; Eventos con InputBox</strong>) y Simulador Interactivo de los 3 modelos de examen:
      </p>

      <!-- SIMULADOR INTERACTIVO MODELOS DE EXAMEN -->
      <div class="delphi-window" style="max-width: 680px; margin: 1.5rem auto; border: 2px solid #f43f5e;">
        <div class="delphi-titlebar" style="background: linear-gradient(90deg, #9f1239, #e11d48);">
          <span>FormExamen - [Simulador Interactivo de Modelos de Examen]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>
        <div class="delphi-body" style="padding: 1.5rem; background: #fff1f2;">
          <div class="delphi-header-label" style="font-size: 1.25rem; color: #881337; border-bottom: 2px solid #fecdd3; margin-bottom: 1rem;">
            Ejercicios de Examen Parcial
          </div>

          <!-- ENTRADA N y K -->
          <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 0.75rem; margin-bottom: 0.75rem;">
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Número N:</label>
              <input type="number" id="examInputN" class="delphi-form-edit" value="85239" style="width:100%; font-size:1.05rem;">
            </div>
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Posición K:</label>
              <input type="number" id="examInputK" class="delphi-form-edit" value="2" style="width:100%; font-size:1.05rem;">
            </div>
          </div>

          <!-- BOTONES DE EXAMEN -->
          <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 0.75rem;">
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.6rem; text-align: left; padding-left: 1rem; font-weight: bold; color: #881337;" onclick="btnExamModelo1()">1. Menor Impar y Mayor Par (ej. 85239 &rarr; 38)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.6rem; text-align: left; padding-left: 1rem; font-weight: bold; color: #881337;" onclick="btnExamModelo2()">2. Eliminar A PARTIR de Posición K (ej. 78143, K=3 &rarr; 43)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.6rem; text-align: left; padding-left: 1rem; font-weight: bold; color: #881337;" onclick="btnExamModelo3()">3. Eliminar DÍGITO en Posición K (ej. 78143, K=2 &rarr; 7813)</button>
          </div>

          <!-- RESULTADO -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="color: #881337;">RESULTADO (Edit2):</label>
            <input type="text" id="examOutput" class="delphi-form-edit" readonly placeholder="Resultado del examen..." style="background: #ffffff; border: 2px solid #f43f5e; color: #9f1239; font-weight: bold; font-size: 1.1rem;">
          </div>

          <!-- CONSOLA LOG -->
          <div class="delphi-console-log" id="examConsoleLog" style="background: #1c060d; color: #fda4af; margin-top: 0.75rem;">
            [Examen]: Selecciona una opción para ejecutar la prueba en tiempo real.
          </div>
        </div>
      </div>

      <!-- ==================== BANCO DETALLADO DE MODELOS ==================== -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 1rem;">📖 Desarrollo Paso a Paso de los Modelos de Examen</h3>

      <!-- MODELO 1 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-rose);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(244, 63, 94, 0.2); color: #fb7185;">EXAM 01</span> 2) Menor Impar y Mayor Par en un solo número (30 Puntos)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Hacer una función para que dado un número natural, obtener el dígito menor impar y el dígito mayor par, mostrar en otro número formado por el menor impar y el mayor par.<br>
          • <strong>Ejemplo:</strong> <code>N = 85239</code> &rarr; MenorImpar = 3, MayorPar = 8 &rarr; <strong>MOSTRAR:</strong> <code>MenorImpar_MayorPar = 38</code></p>
          
          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Análisis:</h5>
          <p>
            • <strong>Entrada:</strong> <code>numeroNatural : Cardinal</code> (ej. 85239)<br>
            • <strong>Proceso:</strong> Inicializar <code>menorImpar := 10</code>, <code>mayorPar := -1</code>. Descomponer con <code>mod 10</code>. Si es impar y <code>d &lt; menorImpar</code> actualizar. Si es par y <code>d &gt; mayorPar</code> actualizar. Reconstruir con <code>(menorImpar * 10) + mayorPar</code>.<br>
            • <strong>Salida:</strong> <code>Cardinal</code> (ej. 38)
          </p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion FormarMenorImparMayorPar(numeroNatural: Entero): Entero<br>
&nbsp;&nbsp;menorImpar <- 10<br>
&nbsp;&nbsp;mayorPar   <- -1<br>
&nbsp;&nbsp;Mientras numeroNatural > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual <- numeroNatural MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si (digitoActual MOD 2 <> 0) Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si digitoActual < menorImpar Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;menorImpar <- digitoActual<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;Sino<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Si digitoActual > mayorPar Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mayorPar <- digitoActual<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural <- numeroNatural DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar (menorImpar * 10) + mayorPar<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>numeroNatural</th><th>digitoActual</th><th>¿Impar?</th><th>menorImpar</th><th>¿Par?</th><th>mayorPar</th><th>n div 10</th></tr></thead>
              <tbody>
                <tr><td>85239</td><td>9</td><td>Sí</td><td>9</td><td>No</td><td>-1</td><td>8523</td></tr>
                <tr><td>8523</td><td>3</td><td>Sí</td><td>3</td><td>No</td><td>-1</td><td>852</td></tr>
                <tr><td>852</td><td>2</td><td>No</td><td>3</td><td>Sí</td><td>2</td><td>85</td></tr>
                <tr><td>85</td><td>5</td><td>Sí</td><td>3</td><td>No</td><td>2</td><td>8</td></tr>
                <tr><td>8</td><td>8</td><td>No</td><td>3</td><td>Sí</td><td>8</td><td>0</td></tr>
              </tbody>
            </table>
          </div>
          <p style="color:#38bdf8; font-weight:bold;">Resultado: (3 * 10) + 8 = 38</p>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Clean Code):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">FormarMenorImparMayorPar</span>(numeroNatural: <span class="type">Cardinal</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;digitoActual: <span class="type">Cardinal</span>;<br>
&nbsp;&nbsp;menorImpar, mayorPar: <span class="type">Integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;menorImpar := <span class="number">10</span>;<br>
&nbsp;&nbsp;mayorPar   := -<span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (digitoActual <span class="keyword">mod</span> <span class="number">2</span> &lt;&gt; <span class="number">0</span>) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Integer(digitoActual) &lt; menorImpar <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;menorImpar := digitoActual;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> Integer(digitoActual) &gt; mayorPar <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mayorPar := digitoActual;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">if</span> (menorImpar &lt;&gt; <span class="number">10</span>) <span class="keyword">and</span> (mayorPar &lt;&gt; -<span class="number">1</span>) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function-name">Result</span> := (Cardinal(menorImpar) * <span class="number">10</span>) + Cardinal(mayorPar)<br>
&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function-name">Result</span> := <span class="number">0</span>;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 2 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-amber);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(245, 158, 11, 0.2); color: #f59e0b;">EXAM 02</span> 2) Eliminar a partir de la posición K (30 Puntos)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número N natural y una posición K registrado por teclado, eliminar todos los dígitos a partir de dicha posición (contando desde la derecha).<br>
          • <strong>Ejemplo:</strong> <code>N = 78143</code>, <code>Posición K = 3</code> &rarr; <strong>Resultado:</strong> <code>43</code></p>
          
          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Análisis:</h5>
          <p>
            • <strong>Entrada:</strong> <code>numeroNatural : Cardinal</code> (78143), <code>posicionK : Byte</code> (3)<br>
            • <strong>Proceso:</strong> Pos 1 = '3', Pos 2 = '4', Pos 3 = '1', Pos 4 = '8', Pos 5 = '7'. Al eliminar a partir de pos 3 hacia la izquierda, quedan las posiciones 1 y 2 ('43'). Se calcula <code>pot := 10^(K-1)</code> y se retorna <code>numeroNatural mod pot</code>.<br>
            • <strong>Salida:</strong> <code>Cardinal</code> (43)
          </p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion EliminarAPartirDePosicion(numeroNatural: Entero; posicionK: Entero): Entero<br>
&nbsp;&nbsp;Si posicionK <= 1 Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;Retornar 0<br>
&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;potencia <- 1<br>
&nbsp;&nbsp;Para i <- 1 Hasta (posicionK - 1) Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;potencia <- potencia * 10<br>
&nbsp;&nbsp;FinPara<br>
&nbsp;&nbsp;Retornar numeroNatural MOD potencia<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Clean Code):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EliminarAPartirDePosicion</span>(numeroNatural: <span class="type">Cardinal</span>; posicionK: <span class="type">Byte</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;potencia: <span class="type">Cardinal</span>;<br>
&nbsp;&nbsp;i: <span class="type">Byte</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> posicionK &lt;= <span class="number">1</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Exit(<span class="number">0</span>);<br><br>
&nbsp;&nbsp;potencia := <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> (posicionK - <span class="number">1</span>) <span class="keyword">do</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;potencia := potencia * <span class="number">10</span>;<br><br>
&nbsp;&nbsp;<span class="function-name">Result</span> := numeroNatural <span class="keyword">mod</span> potencia;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 3 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-blue);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">EXAM 03</span> 2) Eliminar el dígito de la posición K (30 Puntos)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número N natural y una posición K, hacer una función para que elimine el dígito de dicha posición.<br>
          • <strong>Ejemplo:</strong> <code>N = 78143</code>, <code>K = 2</code> &rarr; <strong>Resultado:</strong> <code>7813</code></p>
          
          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Análisis:</h5>
          <p>
            • <strong>Entrada:</strong> <code>numeroNatural : Cardinal</code> (78143), <code>posicionK : Byte</code> (2)<br>
            • <strong>Proceso:</strong> Recorrer con <code>mod 10</code> llevando <code>posicionActual := 1</code> y <code>potencia := 1</code>. Si <code>posicionActual &lt;&gt; posicionK</code>, acumular <code>numeroResultado := numeroResultado + (digitoActual * potencia)</code> y multiplicar <code>potencia := potencia * 10</code>. Si <code>posicionActual = K</code>, el dígito se ignora.<br>
            • <strong>Salida:</strong> <code>Cardinal</code> (7813)
          </p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion EliminarDigitoEnPosicion(numeroNatural: Entero; posicionK: Entero): Entero<br>
&nbsp;&nbsp;numeroResultado <- 0<br>
&nbsp;&nbsp;potencia <- 1<br>
&nbsp;&nbsp;posicionActual <- 1<br>
&nbsp;&nbsp;Mientras numeroNatural > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual <- numeroNatural MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si posicionActual <> posicionK Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numeroResultado <- numeroResultado + (digitoActual * potencia)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;potencia <- potencia * 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;posicionActual <- posicionActual + 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural <- numeroNatural DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar numeroResultado<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Clean Code):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EliminarDigitoEnPosicion</span>(numeroNatural: <span class="type">Cardinal</span>; posicionK: <span class="type">Byte</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;digitoActual: <span class="type">Cardinal</span>;<br>
&nbsp;&nbsp;numeroResultado, potencia: <span class="type">Cardinal</span>;<br>
&nbsp;&nbsp;posicionActual: <span class="type">Byte</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;numeroResultado := <span class="number">0</span>;<br>
&nbsp;&nbsp;potencia := <span class="number">1</span>;<br>
&nbsp;&nbsp;posicionActual := <span class="number">1</span>;<br><br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> posicionActual &lt;&gt; posicionK <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numeroResultado := numeroResultado + (digitoActual * potencia);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;potencia := potencia * <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Inc(posicionActual);<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br><br>
&nbsp;&nbsp;<span class="function-name">Result</span> := numeroResultado;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
'''

    # Insert Section 13 before closing container
    if 'id="modelos-examen"' not in html:
        container_close = html.rfind('</div>\n  <!-- Botón flotante')
        if container_close == -1:
            container_close = html.rfind('</div>\n\n<script>')
        html = html[:container_close] + section_exam_html + '\n' + html[container_close:]
        print("Section modelos-examen added.")

    # 3. Add JS interactive simulator functions
    js_exam = '''
  // --- SIMULADOR INTERACTIVO DE MODELOS DE EXAMEN ---
  function btnExamModelo1() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let menorImpar = 10, mayorPar = -1;
    while (n > 0) {
      let d = n % 10;
      if (d % 2 !== 0) {
        if (d < menorImpar) menorImpar = d;
      } else {
        if (d > mayorPar) mayorPar = d;
      }
      n = Math.floor(n / 10);
    }
    const res = (menorImpar !== 10 && mayorPar !== -1) ? (menorImpar * 10 + mayorPar) : 0;
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = 
      `[Examen 1]: MenorImpar = <strong>${menorImpar}</strong>, MayorPar = <strong>${mayorPar}</strong> &rarr; Resultado: <strong>${res}</strong>`;
  }

  function btnExamModelo2() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let k = parseInt(document.getElementById('examInputK').value) || 1;
    if (k <= 1) {
      document.getElementById('examOutput').value = 0;
      document.getElementById('examConsoleLog').innerHTML = `[Examen 2]: K <= 1 &rarr; Resultado: 0`;
      return;
    }
    let pot = Math.pow(10, k - 1);
    let res = n % pot;
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = 
      `[Examen 2]: Eliminar a partir de pos ${k} en N=${n} &rarr; Resultado: <strong>${res}</strong>`;
  }

  function btnExamModelo3() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let k = parseInt(document.getElementById('examInputK').value) || 1;
    let res = 0, pot = 1, pos = 1;
    let origN = n;
    while (n > 0) {
      let d = n % 10;
      if (pos !== k) {
        res += (d * pot);
        pot *= 10;
      }
      pos++;
      n = Math.floor(n / 10);
    }
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = 
      `[Examen 3]: Eliminado dígito en pos ${k} de N=${origN} &rarr; Resultado: <strong>${res}</strong>`;
  }
'''

    if 'btnExamModelo1' not in html:
        script_end = html.rfind('</script>')
        html = html[:script_end] + js_exam + '\n' + html[script_end:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("teoria_programacion_modular.html updated with Exam Models tab!")

if __name__ == '__main__':
    add_exam_models_to_html()
