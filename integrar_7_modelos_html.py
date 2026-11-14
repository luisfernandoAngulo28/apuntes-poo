# -*- coding: utf-8 -*-

def update_html_with_all_7_exam_models():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    section_exam_all = '''  <!-- SECCIÓN 13: BANCO DE MODELOS DE EXAMEN PARCIAL (7 EJERCICIOS COMPLETOS) -->
  <section id="modelos-examen" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🎯 Banco Completo de Modelos de Examen Parcial (INF110-Z2)</h2>
        <span class="badge" style="background: rgba(244, 63, 94, 0.15); color: #f43f5e; border-color: rgba(244, 63, 94, 0.3);">📝 Ejercicios Típicos de Examen (30p c/u)</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución formal paso a paso y Simulador Interactivo de los <strong>7 Modelos de Examen de Números Naturales y Series</strong> de la cátedra:
      </p>

      <!-- SIMULADOR INTERACTIVO 7 MODELOS -->
      <div class="delphi-window" style="max-width: 720px; margin: 1.5rem auto; border: 2px solid #f43f5e;">
        <div class="delphi-titlebar" style="background: linear-gradient(90deg, #9f1239, #e11d48);">
          <span>FormExamenes - [Simulador de Modelos de Examen Parcial]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>
        <div class="delphi-body" style="padding: 1.5rem; background: #fff1f2;">
          <div class="delphi-header-label" style="font-size: 1.25rem; color: #881337; border-bottom: 2px solid #fecdd3; margin-bottom: 1rem;">
            Pruebas en Vivo de Modelos de Examen
          </div>

          <!-- ENTRADA N y K -->
          <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 0.75rem; margin-bottom: 0.75rem;">
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Número Natural N / Términos:</label>
              <input type="number" id="examInputN" class="delphi-form-edit" value="15378" style="width:100%; font-size:1.05rem;">
            </div>
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Posición K (si aplica):</label>
              <input type="number" id="examInputK" class="delphi-form-edit" value="2" style="width:100%; font-size:1.05rem;">
            </div>
          </div>

          <!-- BOTONES DE MODELOS -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 0.75rem;">
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo1()">1. Menor Impar & Mayor Par (85239 &rarr; 38)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo2()">2. Eliminar A PARTIR de K (78143, K=3 &rarr; 43)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo3()">3. Eliminar DÍGITO en K (78143, K=2 &rarr; 7813)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo4()">4. Promedio Pares & Impares (12345)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo5()">5. Mayor Múltiplo de 3 (8326 &rarr; 6)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo6()">6. Sumar Hasta Menor a 10 (15378 &rarr; 6)</button>
          </div>
          
          <button class="delphi-btn-vcl" style="background: #e11d48; color:#fff; border: none; padding: 0.6rem; font-weight: bold; font-size:0.85rem; width:100%; margin-bottom:0.75rem;" onclick="btnExamModelo7()">7. Promedio Serie Dual S = 4+2+8+6+12+18... (n términos)</button>

          <!-- RESULTADO -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="color: #881337;">RESULTADO (Edit2):</label>
            <input type="text" id="examOutput" class="delphi-form-edit" readonly placeholder="Resultado..." style="background: #ffffff; border: 2px solid #f43f5e; color: #9f1239; font-weight: bold; font-size: 1.1rem;">
          </div>

          <!-- CONSOLA LOG -->
          <div class="delphi-console-log" id="examConsoleLog" style="background: #1c060d; color: #fda4af; margin-top: 0.75rem;">
            [Examen]: Selecciona un ejercicio para probar con el número N ingresado.
          </div>
        </div>
      </div>

      <!-- ==================== BANCO DETALLADO ==================== -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 1rem;">📖 Solución Completa de los 7 Modelos de Examen</h3>

      <!-- MODELO 1 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-rose);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(244, 63, 94, 0.2); color: #fb7185;">EXAM 01</span> 1. Menor Impar y Mayor Par en un solo número (30p)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número natural, obtener el dígito menor impar y el dígito mayor par, mostrar en otro número formado por el menor impar y el mayor par.<br>
          • <strong>Ejemplo:</strong> <code>N = 85239</code> &rarr; MenorImpar = 3, MayorPar = 8 &rarr; <strong>Resultado:</strong> <code>38</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">FormarMenorImparMayorPar</span>(numeroNatural: <span class="type">Cardinal</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span> digitoActual: <span class="type">Cardinal</span>; menorImpar, mayorPar: <span class="type">Integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;menorImpar := <span class="number">10</span>; mayorPar := -<span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (digitoActual <span class="keyword">mod</span> <span class="number">2</span> &lt;&gt; <span class="number">0</span>) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> <span class="keyword">if</span> Integer(digitoActual) &lt; menorImpar <span class="keyword">then</span> menorImpar := digitoActual; <span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> <span class="keyword">if</span> Integer(digitoActual) &gt; mayorPar <span class="keyword">then</span> mayorPar := digitoActual; <span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">if</span> (menorImpar &lt;&gt; <span class="number">10</span>) <span class="keyword">and</span> (mayorPar &lt;&gt; -<span class="number">1</span>) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="function-name">Result</span> := (Cardinal(menorImpar) * <span class="number">10</span>) + Cardinal(mayorPar)<br>
&nbsp;&nbsp;<span class="keyword">else</span> <span class="function-name">Result</span> := <span class="number">0</span>;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 2 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-amber);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(245, 158, 11, 0.2); color: #f59e0b;">EXAM 02</span> 2. Eliminar a PARTIR de la posición K (30p)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado N natural y posición K, eliminar todos los dígitos a partir de dicha posición (desde la derecha).<br>
          • <strong>Ejemplo:</strong> <code>N = 78143</code>, <code>K = 3</code> &rarr; <strong>Resultado:</strong> <code>43</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EliminarAPartirDePosicion</span>(numeroNatural: <span class="type">Cardinal</span>; posicionK: <span class="type">Byte</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span> potencia: <span class="type">Cardinal</span>; i: <span class="type">Byte</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> posicionK &lt;= <span class="number">1</span> <span class="keyword">then</span> Exit(<span class="number">0</span>);<br>
&nbsp;&nbsp;potencia := <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> (posicionK - <span class="number">1</span>) <span class="keyword">do</span> potencia := potencia * <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := numeroNatural <span class="keyword">mod</span> potencia;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 3 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-blue);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">EXAM 03</span> 3. Eliminar el dígito de la posición K (30p)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado N natural y posición K, eliminar únicamente el dígito de dicha posición.<br>
          • <strong>Ejemplo:</strong> <code>N = 78143</code>, <code>K = 2</code> &rarr; <strong>Resultado:</strong> <code>7813</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EliminarDigitoEnPosicion</span>(numeroNatural: <span class="type">Cardinal</span>; posicionK: <span class="type">Byte</span>): <span class="type">Cardinal</span>;<br>
<span class="keyword">var</span> digitoActual, numeroResultado, potencia: <span class="type">Cardinal</span>; posicionActual: <span class="type">Byte</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;numeroResultado := <span class="number">0</span>; potencia := <span class="number">1</span>; posicionActual := <span class="number">1</span>;<br>
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
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := numeroResultado;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 4 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-emerald);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">EXAM 04</span> 4. Promedio de Pares y Promedio de Impares (Pizarra Examen)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número Natural, hacer un módulo para obtener Promedio de Pares y Promedio de Impares.<br>
          • <strong>Ejemplo:</strong> <code>N = 12345</code> &rarr; SumaPar = 2+4=6 (Cant=2) &rarr; <code>PromPar = 3.0</code> | SumaImpar = 1+3+5=9 (Cant=3) &rarr; <code>PromImpar = 3.0</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">procedure</span> <span class="function-name">PromedioParesImpares</span>(numeroNatural: <span class="type">Cardinal</span>; <span class="keyword">var</span> promPares, promImpares: <span class="type">Double</span>);<br>
<span class="keyword">var</span> digitoActual, sumaPares, cantPares, sumaImpares, cantImpares: <span class="type">Cardinal</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;sumaPares := <span class="number">0</span>; cantPares := <span class="number">0</span>; sumaImpares := <span class="number">0</span>; cantImpares := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> digitoActual <span class="keyword">mod</span> <span class="number">2</span> = <span class="number">0</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> sumaPares := sumaPares + digitoActual; Inc(cantPares); <span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> sumaImpares := sumaImpares + digitoActual; Inc(cantImpares); <span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="keyword">if</span> cantPares &gt; <span class="number">0</span> <span class="keyword">then</span> promPares := sumaPares / cantPares <span class="keyword">else</span> promPares := <span class="number">0.0</span>;<br>
&nbsp;&nbsp;<span class="keyword">if</span> cantImpares &gt; <span class="number">0</span> <span class="keyword">then</span> promImpares := sumaImpares / cantImpares <span class="keyword">else</span> promImpares := <span class="number">0.0</span>;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 5 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-purple);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(168, 85, 247, 0.2); color: #c084fc;">EXAM 05</span> 5. Dígito Mayor de los Múltiplos de 3</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número natural, mostrar el dígito mayor entre los múltiplos de 3 (3, 6, 9).<br>
          • <strong>Ejemplo:</strong> <code>N = 8326</code> &rarr; M3 = {3, 6} &rarr; <code>MayorM3 = 6</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">MayorDigitoMultiploDe3</span>(numeroNatural: <span class="type">Cardinal</span>): <span class="type">Integer</span>;<br>
<span class="keyword">var</span> digitoActual: <span class="type">Cardinal</span>; mayor: <span class="type">Integer</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;mayor := -<span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;digitoActual := numeroNatural <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (digitoActual <span class="keyword">mod</span> <span class="number">3</span> = <span class="number">0</span>) <span class="keyword">and</span> (Integer(digitoActual) &gt; mayor) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mayor := digitoActual;<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := numeroNatural <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := mayor;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 6 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-rose);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(244, 63, 94, 0.2); color: #fb7185;">EXAM 06</span> 6. Sumar Dígitos Hasta que Sea Menor a 10 (Raíz Digital - 10p)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Dado un número N natural sumar sus dígitos hasta que sea menor a 10.<br>
          • <strong>Ejemplo:</strong> <code>N = 15378</code> &rarr; <code>15378 &rarr; 24 &rarr; 6</code> (Resultado: <strong>6</strong>)</p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">SumarHastaMenorA10</span>(numeroNatural: <span class="type">Cardinal</span>): <span class="type">Byte</span>;<br>
<span class="keyword">var</span> suma, temp: <span class="type">Cardinal</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">while</span> numeroNatural &gt;= <span class="number">10</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;suma := <span class="number">0</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;temp := numeroNatural;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">while</span> temp &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma := suma + (temp <span class="keyword">mod</span> <span class="number">10</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;temp := temp <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;numeroNatural := suma;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := numeroNatural;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- MODELO 7 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-emerald);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">EXAM 07</span> 7. Promedio de la Serie Mixta Dual (4+2+8+6+12+18+16+54...)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Enunciado:</strong> Generar los N términos de la serie y mostrar el promedio de dicha serie:<br>
          <code>S = 4 + 2 + 8 + 6 + 12 + 18 + 16 + 54 + 20 + 162 + ...</code><br>
          • <strong>Ejemplo:</strong> Para <code>n = 4</code> &rarr; <code>(4 + 2 + 8 + 6) / 4 = 20 / 4 = 5.0</code></p>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">PromedioSerieDual</span>(cantidadTerminos: <span class="type">Cardinal</span>): <span class="type">Double</span>;<br>
<span class="keyword">var</span> i, terminoImpar, terminoPar, terminoActual: <span class="type">Cardinal</span>; sumaTotal: <span class="type">Double</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> cantidadTerminos = <span class="number">0</span> <span class="keyword">then</span> Exit(<span class="number">0.0</span>);<br>
&nbsp;&nbsp;terminoImpar := <span class="number">4</span>; <span class="comment">// +4</span><br>
&nbsp;&nbsp;terminoPar   := <span class="number">2</span>; <span class="comment">// *3</span><br>
&nbsp;&nbsp;sumaTotal    := <span class="number">0.0</span>;<br>
&nbsp;&nbsp;<span class="keyword">for</span> i := <span class="number">1</span> <span class="keyword">to</span> cantidadTerminos <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> (i <span class="keyword">mod</span> <span class="number">2</span> &lt;&gt; <span class="number">0</span>) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> terminoActual := terminoImpar; terminoImpar := terminoImpar + <span class="number">4</span>; <span class="keyword">end</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span> terminoActual := terminoPar; terminoPar := terminoPar * <span class="number">3</span>; <span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;sumaTotal := sumaTotal + terminoActual;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := sumaTotal / cantidadTerminos;<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
'''

    # Replace Section 13
    start_s13 = html.find('id="modelos-examen"')
    if start_s13 != -1:
        tag_start = html.rfind('<section', 0, start_s13)
        tag_end = html.find('</section>', start_s13) + len('</section>')
        html = html[:tag_start] + section_exam_all + html[tag_end:]
        print("Section 13 replaced with all 7 exam models.")

    # Update JS Simulator for 7 models
    js_exam_all = '''
  // --- SIMULADOR DE LOS 7 MODELOS DE EXAMEN ---
  function btnExamModelo1() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let menorImpar = 10, mayorPar = -1;
    while (n > 0) {
      let d = n % 10;
      if (d % 2 !== 0) { if (d < menorImpar) menorImpar = d; }
      else { if (d > mayorPar) mayorPar = d; }
      n = Math.floor(n / 10);
    }
    const res = (menorImpar !== 10 && mayorPar !== -1) ? (menorImpar * 10 + mayorPar) : 0;
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 1]: MenorImpar=${menorImpar}, MayorPar=${mayorPar} &rarr; <strong>${res}</strong>`;
  }

  function btnExamModelo2() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let k = parseInt(document.getElementById('examInputK').value) || 1;
    if (k <= 1) { document.getElementById('examOutput').value = 0; return; }
    let pot = Math.pow(10, k - 1);
    let res = n % pot;
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 2]: Eliminar a partir de pos ${k} en N=${n} &rarr; <strong>${res}</strong>`;
  }

  function btnExamModelo3() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let k = parseInt(document.getElementById('examInputK').value) || 1;
    let res = 0, pot = 1, pos = 1;
    let orig = n;
    while (n > 0) {
      let d = n % 10;
      if (pos !== k) { res += (d * pot); pot *= 10; }
      pos++;
      n = Math.floor(n / 10);
    }
    document.getElementById('examOutput').value = res;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 3]: Eliminado dígito en pos ${k} de N=${orig} &rarr; <strong>${res}</strong>`;
  }

  function btnExamModelo4() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let sumP = 0, cantP = 0, sumI = 0, cantI = 0;
    let orig = n;
    while (n > 0) {
      let d = n % 10;
      if (d % 2 === 0) { sumP += d; cantP++; }
      else { sumI += d; cantI++; }
      n = Math.floor(n / 10);
    }
    let promP = cantP > 0 ? (sumP / cantP).toFixed(2) : '0';
    let promI = cantI > 0 ? (sumI / cantI).toFixed(2) : '0';
    document.getElementById('examOutput').value = `PromPar: ${promP} | PromImpar: ${promI}`;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 4 (Pizarra)]: N=${orig} &rarr; SumaPar=${sumP}(cant=${cantP}) &rarr; PromPar=<strong>${promP}</strong> | SumaImpar=${sumI}(cant=${cantI}) &rarr; PromImpar=<strong>${promI}</strong>`;
  }

  function btnExamModelo5() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let mayor = -1;
    let orig = n;
    while (n > 0) {
      let d = n % 10;
      if (d % 3 === 0 && d > mayor) mayor = d;
      n = Math.floor(n / 10);
    }
    document.getElementById('examOutput').value = mayor;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 5]: N=${orig} &rarr; Mayor dígito múltiplo de 3: <strong>${mayor}</strong>`;
  }

  function btnExamModelo6() {
    let n = parseInt(document.getElementById('examInputN').value) || 0;
    let orig = n;
    let pasos = `${orig}`;
    while (n >= 10) {
      let suma = 0, temp = n;
      while (temp > 0) { suma += (temp % 10); temp = Math.floor(temp / 10); }
      n = suma;
      pasos += ` &rarr; ${n}`;
    }
    document.getElementById('examOutput').value = n;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 6 (Raíz Digital)]: Reducción: ${pasos} &rarr; Resultado Final: <strong>${n}</strong>`;
  }

  function btnExamModelo7() {
    let n = parseInt(document.getElementById('examInputN').value) || 4;
    if (n <= 0) return;
    let tImp = 4, tPar = 2, suma = 0;
    let terminos = [];
    for (let i = 1; i <= n; i++) {
      let t;
      if (i % 2 !== 0) { t = tImp; tImp += 4; }
      else { t = tPar; tPar *= 3; }
      terminos.push(t);
      suma += t;
    }
    let prom = (suma / n).toFixed(2);
    document.getElementById('examOutput').value = `Promedio = ${prom}`;
    document.getElementById('examConsoleLog').innerHTML = `[Examen 7 (Serie Dual)]: Términos (${n}): [${terminos.join(', ')}] &rarr; Suma = ${suma} &rarr; Promedio: <strong>${prom}</strong>`;
  }
'''
    # Replace JS simulation
    start_js = html.find('// --- SIMULADOR INTERACTIVO DE MODELOS DE EXAMEN ---')
    if start_js != -1:
        end_js = html.find('</script>', start_js)
        html = html[:start_js] + js_exam_all + '\n' + html[end_js:]
    else:
        script_end = html.rfind('</script>')
        html = html[:script_end] + js_exam_all + '\n' + html[script_end:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("teoria_programacion_modular.html updated with all 7 exam models and live simulator!")

if __name__ == '__main__':
    update_html_with_all_7_exam_models()
