# -*- coding: utf-8 -*-
import re

pizarra_new_html = '''<section id="ejercicios-pizarra" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">📋 Tarea de Clase de Hoy: Formulario VCL y Descomposición de Números</h2>
        <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b; border-color: rgba(245, 158, 11, 0.3);">📅 Ejercicios Asignados en Clase</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución formal paso a paso (<strong>Análisis &rarr; Pseudocódigo &rarr; Prueba de Escritorio &rarr; Codificación Delphi &rarr; Eventos de Botón</strong>) y Simulador Interactivo del formulario desarrollado en el aula:
      </p>

      <!-- SIMULADOR INTERACTIVO FORMULARIO TAREA DE CLASE -->
      <div class="delphi-window" style="max-width: 650px; margin: 1.5rem auto; border: 2px solid #3b82f6;">
        <div class="delphi-titlebar" style="background: linear-gradient(90deg, #1e3a8a, #2563eb);">
          <span>Form1 - [Tarea de clase - VCL Form]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>
        <div class="delphi-body" style="padding: 1.5rem; background: #f8fafc;">
          <div class="delphi-header-label" style="font-size: 1.3rem; color: #0f172a; border-bottom: 2px solid #cbd5e1; margin-bottom: 1rem;">
            Tarea de clase
          </div>

          <!-- FILA 1: CARGAR + EDIT1 -->
          <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1rem;">
            <button class="delphi-btn-vcl" style="flex: 1; padding: 0.6rem; font-size: 1rem; background: #e2e8f0; border: 2px solid #94a3b8; font-weight: bold;" onclick="btnClaseCargar()">Cargar</button>
            <input type="number" id="claseEdit1" class="delphi-form-edit" style="flex: 1.5; font-size: 1.1rem; padding: 0.5rem;" value="1234" placeholder="Ingrese número natural...">
          </div>

          <!-- FILA 2: EDIT2 (RESULTADO) -->
          <div style="margin-bottom: 1.25rem;">
            <input type="text" id="claseEdit2" class="delphi-form-edit" style="width: 100%; font-size: 1.1rem; padding: 0.6rem; background: #ffffff; border: 2px solid #38bdf8; font-weight: bold; color: #0369a1;" readonly placeholder="Resultado (Edit2)...">
          </div>

          <!-- BOTONES DE FUNCIONES -->
          <div style="display: flex; flex-direction: column; gap: 0.6rem;">
            <button class="delphi-btn-vcl" style="padding: 0.65rem; font-size: 0.95rem; font-weight: bold; text-align: left; padding-left: 1.2rem; background: #f1f5f9;" onclick="btnClaseSumarPrimos()">SumarDigitosPrimos</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem; font-size: 0.95rem; font-weight: bold; text-align: left; padding-left: 1.2rem; background: #f1f5f9;" onclick="btnClaseSoloPares()">SoloPares</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem; font-size: 0.95rem; font-weight: bold; text-align: left; padding-left: 1.2rem; background: #f1f5f9;" onclick="btnClaseSumarMult3()">SumarMultiplosDe3</button>
            <button class="delphi-btn-vcl" style="padding: 0.65rem; font-size: 0.95rem; font-weight: bold; text-align: left; padding-left: 1.2rem; background: #f1f5f9;" onclick="btnClaseInvertir()">InvertirNumero</button>
          </div>

          <!-- CONSOLA DE EVENTOS -->
          <div class="delphi-console-log" id="claseConsoleLog" style="margin-top: 1rem; font-size: 0.82rem;">
            [Delphi VCL]: Variable Global <strong>n = 1234</strong> cargada en memoria. Haz clic en cualquier botón para ejecutar.
          </div>
        </div>
      </div>

      <!-- BANCO DE EJERCICIOS DE CLASE -->
      <h3 style="color: #fff; margin-top: 2.5rem; margin-bottom: 1rem;">📖 Detalle Metodológico de los Ejercicios de Clase</h3>

      <!-- FUNCIÓN AUXILIAR: ESPRIMO -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-emerald);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number" style="background: rgba(16, 185, 129, 0.2); color: #34d399;">AUX</span> Función Auxiliar: EsPrimo (Dígito primo 0..9)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Análisis:</strong><br>
          • <strong>Entrada:</strong> <code>d</code> (Byte / Dígito de 0 a 9)<br>
          • <strong>Proceso:</strong> Comprobar si <code>(d = 2) or (d = 3) or (d = 5) or (d = 7)</code>. Los dígitos 0, 1, 4, 6, 8 y 9 no son primos.<br>
          • <strong>Salida:</strong> <code>Boolean</code> (True / False)</p>
          
          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion EsPrimo(d: Byte): Booleano<br>
&nbsp;&nbsp;Retornar (d = 2) O (d = 3) O (d = 5) O (d = 7)<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>d (Dígito)</th><th>¿d = 2?</th><th>¿d = 3?</th><th>¿d = 5?</th><th>¿d = 7?</th><th>Resultado</th></tr></thead>
              <tbody>
                <tr><td>2</td><td>Sí</td><td>No</td><td>No</td><td>No</td><td><strong style="color:#10b981;">TRUE</strong></td></tr>
                <tr><td>3</td><td>No</td><td>Sí</td><td>No</td><td>No</td><td><strong style="color:#10b981;">TRUE</strong></td></tr>
                <tr><td>4</td><td>No</td><td>No</td><td>No</td><td>No</td><td><strong style="color:#f43f5e;">FALSE</strong></td></tr>
                <tr><td>5</td><td>No</td><td>No</td><td>Sí</td><td>No</td><td><strong style="color:#10b981;">TRUE</strong></td></tr>
                <tr><td>7</td><td>No</td><td>No</td><td>No</td><td>Sí</td><td><strong style="color:#10b981;">TRUE</strong></td></tr>
                <tr><td>9</td><td>No</td><td>No</td><td>No</td><td>No</td><td><strong style="color:#f43f5e;">FALSE</strong></td></tr>
              </tbody>
            </table>
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Unit1.pas):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">EsPrimo</span>(d: <span class="type">Byte</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="function-name">Result</span> := (d = <span class="number">2</span>) <span class="keyword">or</span> (d = <span class="number">3</span>) <span class="keyword">or</span> (d = <span class="number">5</span>) <span class="keyword">or</span> (d = <span class="number">7</span>);<br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- EJERCICIO 1: SUMARDIGITOSPRIMOS -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-blue);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number">EJ 01</span> 1. Sumar los dígitos primos (SumarDigitosPrimos)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Análisis:</strong><br>
          • <strong>Entrada:</strong> <code>n</code> (Número natural, tipo Word/Cardinal)<br>
          • <strong>Proceso:</strong> Extraer dígitos con <code>n mod 10</code>. Si <code>EsPrimo(d)</code> entonces acumular <code>suma := suma + d</code>. Reducir <code>n := n div 10</code>.<br>
          • <strong>Salida:</strong> <code>suma</code> (Suma total de los dígitos primos)</p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion SumarDigitosPrimos(n: Entero): Entero<br>
&nbsp;&nbsp;suma <- 0<br>
&nbsp;&nbsp;Mientras n > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;d <- n MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si EsPrimo(d) Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma <- suma + d<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;n <- n DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar suma<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>n</th><th>d := n mod 10</th><th>¿EsPrimo(d)?</th><th>suma := suma + d</th><th>n := n div 10</th></tr></thead>
              <tbody>
                <tr><td>2374</td><td>4</td><td>No (4 no es primo)</td><td>0</td><td>237</td></tr>
                <tr><td>237</td><td>7</td><td>Sí (7 es primo)</td><td>7</td><td>23</td></tr>
                <tr><td>23</td><td>3</td><td>Sí (3 es primo)</td><td>10</td><td>2</td></tr>
                <tr><td>2</td><td>2</td><td>Sí (2 es primo)</td><td><strong style="color:#38bdf8;">12</strong></td><td>0</td></tr>
              </tbody>
            </table>
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Unit1.pas):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">SumarDigitosPrimos</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, suma: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;suma := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsPrimo</span>(d) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma := suma + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := suma;<br>
<span class="keyword">end</span>;
            </div>
          </div>

          <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Llamada en Botón Delphi (Button2 / Edit2 / ShowMessage):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button2Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="comment">// 1. En un Edit (Asignación directa):</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">SumarDigitosPrimos</span>(n));<br><br>
&nbsp;&nbsp;<span class="comment">// 2. En un ShowMessage (Ventana emergente):</span><br>
&nbsp;&nbsp;<span class="comment">// ShowMessage('Suma de dígitos primos: ' + IntToStr(SumarDigitosPrimos(n)));</span><br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- EJERCICIO 2: FORMARSOLOPARES -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-purple);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number">EJ 02</span> 2. Mostrar en otro número solo pares (SoloPares / FormarSoloPares)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Análisis:</strong><br>
          • <strong>Entrada:</strong> <code>n</code> (Número natural, ej: pizarra <code>N = 1234</code>)<br>
          • <strong>Proceso:</strong> Inicializar <code>npar := 0</code> y <code>pot := 1</code>. Mientras <code>n &gt; 0</code>: <code>d := n mod 10</code>; si <code>d mod 2 = 0</code> entonces <code>npar := npar + (d * pot); pot := pot * 10;</code>; <code>n := n div 10;</code>.<br>
          • <strong>Salida:</strong> <code>npar</code> (Número natural con los dígitos pares en orden original: <code>24</code>)</p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion FormarSoloPares(n: Entero): Entero<br>
&nbsp;&nbsp;npar <- 0<br>
&nbsp;&nbsp;pot <- 1<br>
&nbsp;&nbsp;Mientras n > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;d <- n MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si (d MOD 2 = 0) Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;npar <- npar + (d * pot)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pot <- pot * 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;n <- n DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar npar<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>n</th><th>d := n mod 10</th><th>¿d mod 2 = 0?</th><th>npar := npar + (d*pot)</th><th>pot := pot * 10</th><th>n := n div 10</th></tr></thead>
              <tbody>
                <tr><td>1234</td><td>4</td><td>Sí (Par)</td><td>0 + 4*1 = 4</td><td>10</td><td>123</td></tr>
                <tr><td>123</td><td>3</td><td>No (Impar)</td><td>4 (sin cambio)</td><td>10 (sin cambio)</td><td>12</td></tr>
                <tr><td>12</td><td>2</td><td>Sí (Par)</td><td>4 + 2*10 = 24</td><td>100</td><td>1</td></tr>
                <tr><td>1</td><td>1</td><td>No (Impar)</td><td><strong style="color:#38bdf8;">24</strong></td><td>100 (sin cambio)</td><td>0</td></tr>
              </tbody>
            </table>
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Unit1.pas):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">FormarSoloPares</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, npar, pot: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;npar := <span class="number">0</span>;<br>
&nbsp;&nbsp;pot := <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> d <span class="keyword">mod</span> <span class="number">2</span> = <span class="number">0</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;npar := npar + (d * pot);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pot := pot * <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := npar;<br>
<span class="keyword">end</span>;
            </div>
          </div>

          <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Llamada en Botón Delphi (Button3 / Edit2 / ShowMessage):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button3Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="comment">// 1. En un Edit (Asignación):</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">FormarSoloPares</span>(n));<br><br>
&nbsp;&nbsp;<span class="comment">// 2. En un ShowMessage:</span><br>
&nbsp;&nbsp;<span class="comment">// ShowMessage('Número solo con pares: ' + IntToStr(FormarSoloPares(n)));</span><br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- EJERCICIO 3: SUMARMULTIPLOSDE3 -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-amber);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number">EJ 03</span> 3. Sumar múltiplos de 3 (SumarMultiplosDe3)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Análisis:</strong><br>
          • <strong>Entrada:</strong> <code>n</code> (Número natural)<br>
          • <strong>Proceso:</strong> Extraer dígitos con <code>n mod 10</code>. Si <code>d mod 3 = 0</code> acumular <code>suma := suma + d</code>. Reducir <code>n := n div 10</code>.<br>
          • <strong>Salida:</strong> <code>suma</code> (Suma total de los múltiplos de 3)</p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion SumarMultiplosDe3(n: Entero): Entero<br>
&nbsp;&nbsp;suma <- 0<br>
&nbsp;&nbsp;Mientras n > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;d <- n MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;Si (d MOD 3 = 0) Entonces<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma <- suma + d<br>
&nbsp;&nbsp;&nbsp;&nbsp;FinSi<br>
&nbsp;&nbsp;&nbsp;&nbsp;n <- n DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar suma<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>n</th><th>d := n mod 10</th><th>¿d mod 3 = 0?</th><th>suma := suma + d</th><th>n := n div 10</th></tr></thead>
              <tbody>
                <tr><td>3681</td><td>1</td><td>No (1 mod 3 <> 0)</td><td>0</td><td>368</td></tr>
                <tr><td>368</td><td>8</td><td>No (8 mod 3 <> 0)</td><td>0</td><td>36</td></tr>
                <tr><td>36</td><td>6</td><td>Sí (6 mod 3 = 0)</td><td>6</td><td>3</td></tr>
                <tr><td>3</td><td>3</td><td>Sí (3 mod 3 = 0)</td><td><strong style="color:#38bdf8;">9</strong></td><td>0</td></tr>
              </tbody>
            </table>
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Unit1.pas):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">SumarMultiplosDe3</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, suma: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;suma := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> d <span class="keyword">mod</span> <span class="number">3</span> = <span class="number">0</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma := suma + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := suma;<br>
<span class="keyword">end</span>;
            </div>
          </div>

          <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Llamada en Botón Delphi (Button4 / Edit2 / ShowMessage):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button4Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="comment">// 1. En un Edit (Asignación):</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">SumarMultiplosDe3</span>(n));<br><br>
&nbsp;&nbsp;<span class="comment">// 2. En un ShowMessage:</span><br>
&nbsp;&nbsp;<span class="comment">// ShowMessage('Suma múltiplos de 3: ' + IntToStr(SumarMultiplosDe3(n)));</span><br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- EJERCICIO 4: INVERTIRNUMERO -->
      <div class="qa-item open" style="border-left: 4px solid var(--accent-rose);">
        <div class="qa-header" onclick="toggleQA(this)">
          <div><span class="qa-number">EJ 04</span> 4. Invertir número (InvertirNumero)</div>
          <span class="qa-icon">▼</span>
        </div>
        <div class="qa-body" style="display: block;">
          <p><strong>Análisis:</strong><br>
          • <strong>Entrada:</strong> <code>n</code> (Número natural original, ej: <code>4782</code>)<br>
          • <strong>Proceso:</strong> Inicializar <code>inv := 0</code>. Mientras <code>n &gt; 0</code>: <code>d := n mod 10</code>; desplazar <code>inv := (inv * 10) + d</code>; <code>n := n div 10</code>.<br>
          • <strong>Salida:</strong> <code>inv</code> (Número invertido: <code>2874</code>)</p>

          <h5 style="color: var(--accent-purple); margin-top: 0.75rem;">Pseudocódigo:</h5>
          <div class="code-block">
Funcion InvertirNumero(n: Entero): Entero<br>
&nbsp;&nbsp;inv <- 0<br>
&nbsp;&nbsp;Mientras n > 0 Hacer<br>
&nbsp;&nbsp;&nbsp;&nbsp;d <- n MOD 10<br>
&nbsp;&nbsp;&nbsp;&nbsp;inv <- (inv * 10) + d<br>
&nbsp;&nbsp;&nbsp;&nbsp;n <- n DIV 10<br>
&nbsp;&nbsp;FinMientras<br>
&nbsp;&nbsp;Retornar inv<br>
FinFuncion
          </div>

          <h5 style="color: var(--accent-blue); margin-top: 0.75rem;">Prueba de Escritorio:</h5>
          <div class="table-container">
            <table>
              <thead><tr><th>n</th><th>d := n mod 10</th><th>inv := (inv * 10) + d</th><th>n := n div 10</th></tr></thead>
              <tbody>
                <tr><td>4782</td><td>2</td><td>(0 * 10) + 2 = 2</td><td>478</td></tr>
                <tr><td>478</td><td>8</td><td>(2 * 10) + 8 = 28</td><td>47</td></tr>
                <tr><td>47</td><td>7</td><td>(28 * 10) + 7 = 287</td><td>4</td></tr>
                <tr><td>4</td><td>4</td><td>(287 * 10) + 4 = <strong style="color:#38bdf8;">2874</strong></td><td>0</td></tr>
              </tbody>
            </table>
          </div>

          <h5 style="color: var(--accent-emerald); margin-top: 0.75rem;">Codificación Delphi (Unit1.pas):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">function</span> <span class="function-name">InvertirNumero</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, inv: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;inv := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;inv := (inv * <span class="number">10</span>) + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := inv;<br>
<span class="keyword">end</span>;
            </div>
          </div>

          <h5 style="color: var(--accent-amber); margin-top: 0.75rem;">Llamada en Botón Delphi (Button5 / Edit2 / ShowMessage):</h5>
          <div class="code-wrapper">
            <button class="copy-btn" onclick="copyCode(this)">Copiar</button>
            <div class="code-block">
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button5Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="comment">// 1. En un Edit (Asignación):</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">InvertirNumero</span>(n));<br><br>
&nbsp;&nbsp;<span class="comment">// 2. En un ShowMessage:</span><br>
&nbsp;&nbsp;<span class="comment">// ShowMessage('Número invertido: ' + IntToStr(InvertirNumero(n)));</span><br>
<span class="keyword">end</span>;
            </div>
          </div>
        </div>
      </div>

      <!-- CÓDIGO FUENTE COMPLETO DE UNIT1.PAS -->
      <h3 style="color: #fff; margin-top: 2rem; margin-bottom: 0.75rem;">📦 Código Fuente Completo de Unit1.pas (VCL Formulario)</h3>
      <div class="code-wrapper">
        <button class="copy-btn" onclick="copyCode(this)">Copiar Unit1.pas Completo</button>
        <div class="code-block">
<span class="keyword">unit</span> Unit1;<br><br>
<span class="keyword">interface</span><br><br>
<span class="keyword">uses</span><br>
&nbsp;&nbsp;Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,<br>
&nbsp;&nbsp;Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;<br><br>
<span class="keyword">type</span><br>
&nbsp;&nbsp;<span class="type">TForm1</span> = <span class="keyword">class</span>(TForm)<br>
&nbsp;&nbsp;&nbsp;&nbsp;Label1: TLabel;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Button1: TButton;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Button2: TButton;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Button3: TButton;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Button4: TButton;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Button5: TButton;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit1: TEdit;<br>
&nbsp;&nbsp;&nbsp;&nbsp;Edit2: TEdit;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button1Click(Sender: TObject);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button2Click(Sender: TObject);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button3Click(Sender: TObject);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button4Click(Sender: TObject);<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">procedure</span> Button5Click(Sender: TObject);<br>
&nbsp;&nbsp;<span class="keyword">private</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">{ Private declarations }</span><br>
&nbsp;&nbsp;<span class="keyword">public</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment">{ Public declarations }</span><br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br><br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;Form1: TForm1;<br>
&nbsp;&nbsp;n: <span class="type">Word</span>; <span class="comment">// Variable global para almacenar el número ingresado</span><br><br>
<span class="keyword">implementation</span><br><br>
<span class="comment">{$R *.dfm}</span><br><br>
<span class="comment">// Función auxiliar: Determina si un dígito (0..9) es primo</span><br>
<span class="keyword">function</span> <span class="function-name">EsPrimo</span>(d: <span class="type">Byte</span>): <span class="type">Boolean</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="function-name">Result</span> := (d = <span class="number">2</span>) <span class="keyword">or</span> (d = <span class="number">3</span>) <span class="keyword">or</span> (d = <span class="number">5</span>) <span class="keyword">or</span> (d = <span class="number">7</span>);<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// 1. Sumar dígitos primos</span><br>
<span class="keyword">function</span> <span class="function-name">SumarDigitosPrimos</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, suma: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;suma := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> <span class="function-name">EsPrimo</span>(d) <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma := suma + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := suma;<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// 2. Mostrar en otro número solo pares (Ejemplo pizarra: N = 1234 -&gt; NPar = 24)</span><br>
<span class="keyword">function</span> <span class="function-name">FormarSoloPares</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, npar, pot: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;npar := <span class="number">0</span>;<br>
&nbsp;&nbsp;pot := <span class="number">1</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> d <span class="keyword">mod</span> <span class="number">2</span> = <span class="number">0</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;npar := npar + (d * pot);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pot := pot * <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := npar;<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// 3. Sumar múltiplos de 3</span><br>
<span class="keyword">function</span> <span class="function-name">SumarMultiplosDe3</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, suma: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;suma := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">if</span> d <span class="keyword">mod</span> <span class="number">3</span> = <span class="number">0</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suma := suma + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := suma;<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// 4. Invertir número</span><br>
<span class="keyword">function</span> <span class="function-name">InvertirNumero</span>(n: <span class="type">Word</span>): <span class="type">Word</span>;<br>
<span class="keyword">var</span><br>
&nbsp;&nbsp;d, inv: <span class="type">Word</span>;<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;inv := <span class="number">0</span>;<br>
&nbsp;&nbsp;<span class="keyword">while</span> n &gt; <span class="number">0</span> <span class="keyword">do</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;d := n <span class="keyword">mod</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;&nbsp;&nbsp;inv := (inv * <span class="number">10</span>) + d;<br>
&nbsp;&nbsp;&nbsp;&nbsp;n := n <span class="keyword">div</span> <span class="number">10</span>;<br>
&nbsp;&nbsp;<span class="keyword">end</span>;<br>
&nbsp;&nbsp;<span class="function-name">Result</span> := inv;<br>
<span class="keyword">end</span>;<br><br>
<span class="comment">// ==========================================</span><br>
<span class="comment">// EVENTOS ONCLICK DE LOS BOTONES</span><br>
<span class="comment">// ==========================================</span><br><br>
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button1Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;<span class="keyword">if</span> Edit1.Text &lt;&gt; <span class="string">''</span> <span class="keyword">then</span><br>
&nbsp;&nbsp;<span class="keyword">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;n := StrToInt(Edit1.Text);<br>
&nbsp;&nbsp;&nbsp;&nbsp;ShowMessage(<span class="string">'Número natural registrado: '</span> + IntToStr(n));<br>
&nbsp;&nbsp;<span class="keyword">end</span><br>
&nbsp;&nbsp;<span class="keyword">else</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;ShowMessage(<span class="string">'Por favor ingresa un número en Edit1'</span>);<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button2Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">SumarDigitosPrimos</span>(n));<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button3Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">FormarSoloPares</span>(n));<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button4Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">SumarMultiplosDe3</span>(n));<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">procedure</span> TForm1.<span class="function-name">Button5Click</span>(Sender: TObject);<br>
<span class="keyword">begin</span><br>
&nbsp;&nbsp;Edit2.Text := IntToStr(<span class="function-name">InvertirNumero</span>(n));<br>
<span class="keyword">end</span>;<br><br>
<span class="keyword">end</span>.
        </div>
      </div>

    </div>
  </section>'''

# Javascript logic to add to the HTML
js_clase_script = '''
  // --- MÉTODOS DEL FORMULARIO TAREA DE CLASE ---
  let variableGlobalClaseN = 1234;

  function btnClaseCargar() {
    const val = parseInt(document.getElementById('claseEdit1').value) || 0;
    variableGlobalClaseN = val;
    document.getElementById('claseEdit2').value = '';
    document.getElementById('claseConsoleLog').innerHTML = 
      `Button1Click: n := StrToInt(Edit1.Text); -> ShowMessage('Número natural registrado: ${variableGlobalClaseN}') | <strong>n = ${variableGlobalClaseN}</strong>`;
  }

  function btnClaseSumarPrimos() {
    let temp = variableGlobalClaseN;
    let suma = 0;
    while (temp > 0) {
      let d = temp % 10;
      if (d === 2 || d === 3 || d === 5 || d === 7) suma += d;
      temp = Math.floor(temp / 10);
    }
    document.getElementById('claseEdit2').value = suma;
    document.getElementById('claseConsoleLog').innerHTML = 
      `Button2Click: Edit2.Text := IntToStr(SumarDigitosPrimos(${variableGlobalClaseN})); -> Resultado asignado: <strong>${suma}</strong>`;
  }

  function btnClaseSoloPares() {
    let temp = variableGlobalClaseN;
    let npar = 0;
    let pot = 1;
    while (temp > 0) {
      let d = temp % 10;
      if (d % 2 === 0) {
        npar = npar + (d * pot);
        pot = pot * 10;
      }
      temp = Math.floor(temp / 10);
    }
    document.getElementById('claseEdit2').value = npar;
    document.getElementById('claseConsoleLog').innerHTML = 
      `Button3Click: Edit2.Text := IntToStr(FormarSoloPares(${variableGlobalClaseN})); -> Resultado asignado: <strong>${npar}</strong>`;
  }

  function btnClaseSumarMult3() {
    let temp = variableGlobalClaseN;
    let suma = 0;
    while (temp > 0) {
      let d = temp % 10;
      if (d % 3 === 0) suma += d;
      temp = Math.floor(temp / 10);
    }
    document.getElementById('claseEdit2').value = suma;
    document.getElementById('claseConsoleLog').innerHTML = 
      `Button4Click: Edit2.Text := IntToStr(SumarMultiplosDe3(${variableGlobalClaseN})); -> Resultado asignado: <strong>${suma}</strong>`;
  }

  function btnClaseInvertir() {
    let temp = variableGlobalClaseN;
    let inv = 0;
    while (temp > 0) {
      let d = temp % 10;
      inv = (inv * 10) + d;
      temp = Math.floor(temp / 10);
    }
    document.getElementById('claseEdit2').value = inv;
    document.getElementById('claseConsoleLog').innerHTML = 
      `Button5Click: Edit2.Text := IntToStr(InvertirNumero(${variableGlobalClaseN})); -> Resultado asignado: <strong>${inv}</strong>`;
  }
'''

def update_html():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace section id="ejercicios-pizarra"
    start_sec = content.find('id="ejercicios-pizarra"')
    if start_sec != -1:
        # find the <section opening
        tag_start = content.rfind('<section', 0, start_sec)
        tag_end = content.find('</section>', start_sec) + len('</section>')
        content = content[:tag_start] + pizarra_new_html + content[tag_end:]
        print("Section ejercicios-pizarra replaced successfully.")

    # Add the javascript functions before </script>
    if 'btnClaseCargar' not in content:
        script_end = content.rfind('</script>')
        content = content[:script_end] + js_clase_script + "\n" + content[script_end:]
        print("JavaScript handlers for Tarea de Clase inserted successfully.")

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("teoria_programacion_modular.html updated successfully!")

if __name__ == "__main__":
    update_html()
