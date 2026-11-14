# -*- coding: utf-8 -*-

def update_html_with_11_exam_models():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Reemplazamos la sección de modelos de examen con los 11 modelos completos
    # Localizamos <section id="modelos-examen"
    start_tag = '<section id="modelos-examen"'
    end_tag = '</section>'
    
    start_pos = html.find(start_tag)
    if start_pos == -1:
        print("No se encontro la seccion modelos-examen")
        return

    # Buscar el cierre de esta seccion
    end_pos = html.find(end_tag, start_pos)
    if end_pos == -1:
        print("No se encontro el cierre de la seccion")
        return

    end_pos += len(end_tag)

    nueva_seccion = '''  <!-- SECCIÓN 13: BANCO DE MODELOS DE EXAMEN PARCIAL (11 EJERCICIOS COMPLETOS) -->
  <section id="modelos-examen" class="section-content">
    <div class="card">
      <div class="header-top-actions">
        <h2 class="card-title" style="margin-bottom: 0;">🎯 Banco Completo de Modelos de Examen Parcial (INF110-Z2)</h2>
        <span class="badge" style="background: rgba(244, 63, 94, 0.15); color: #f43f5e; border-color: rgba(244, 63, 94, 0.3);">📝 11 Modelos de Examen Reales (10p - 30p c/u)</span>
      </div>
      <p style="margin: 1rem 0; font-size: 1.05rem;">
        Resolución formal paso a paso y Simulador Interactivo de los <strong>11 Modelos de Examen de Números Naturales, Lotes y Series</strong> de la cátedra:
      </p>

      <!-- SIMULADOR INTERACTIVO 11 MODELOS -->
      <div class="delphi-window" style="max-width: 780px; margin: 1.5rem auto; border: 2px solid #f43f5e;">
        <div class="delphi-titlebar" style="background: linear-gradient(90deg, #9f1239, #e11d48);">
          <span>FormExamenes - [Simulador de Modelos de Examen Parcial]</span>
          <span style="font-size: 0.75rem;">— ◻ ✕</span>
        </div>
        <div class="delphi-body" style="padding: 1.5rem; background: #fff1f2;">
          <div class="delphi-header-label" style="font-size: 1.25rem; color: #881337; border-bottom: 2px solid #fecdd3; margin-bottom: 1rem;">
            Pruebas en Vivo de Modelos de Examen
          </div>

          <!-- ENTRADA N, K y Lote -->
          <div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 0.75rem; margin-bottom: 0.75rem;">
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Número Natural N / Cantidad Términos:</label>
              <input type="number" id="examInputN" class="delphi-form-edit" value="16327" style="width:100%; font-size:1.05rem;">
            </div>
            <div>
              <label class="delphi-form-label" style="color: #9f1239;">Posición K (si aplica):</label>
              <input type="number" id="examInputK" class="delphi-form-edit" value="2" style="width:100%; font-size:1.05rem;">
            </div>
          </div>

          <div style="margin-bottom: 0.75rem;">
            <label class="delphi-form-label" style="color: #9f1239;">Lote de Números (separados por coma para Modelos 8, 10, 11):</label>
            <input type="text" id="examInputLote" class="delphi-form-edit" value="123, 25, 281, 94, 46" style="width:100%; font-size:1rem;">
          </div>

          <!-- BOTONES DE MODELOS -->
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 0.75rem;">
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo1()">1. Menor Impar & Mayor Par (85239 &rarr; 38)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo2()">2. Eliminar A PARTIR de K (78143, K=3 &rarr; 43)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo3()">3. Eliminar DÍGITO en K (78143, K=2 &rarr; 7813)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo4()">4. Promedio Pares & Impares (12345)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo5()">5. Mayor Múltiplo de 3 (8326 &rarr; 6)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo6()">6. Sumar Hasta Menor a 10 (15378 &rarr; 6)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo7()">7. Promedio Serie Dual (4+2+8+6...)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo8()">8. Sumas de Dígitos Impares Lote (10p)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo9()">9. Separar &lt;6 y &gt;=6 (16327 &rarr; 231, 76)</button>
            <button class="delphi-btn-vcl" style="background: #ffffff; border: 1px solid #fda4af; padding: 0.5rem; font-weight: bold; font-size:0.8rem; color: #881337;" onclick="btnExamModelo10()">10. Promedio Ascendentes [100-200]</button>
          </div>
          
          <button class="delphi-btn-vcl" style="background: #e11d48; color:#fff; border: none; padding: 0.6rem; font-weight: bold; font-size:0.85rem; width:100%; margin-bottom:0.75rem;" onclick="btnExamModelo11()">11. Sumatoria Global de Dígitos Primos en Lote (Pizarra)</button>

          <!-- RESULTADO -->
          <div class="delphi-form-row">
            <label class="delphi-form-label" style="color: #881337;">RESULTADO (Edit2):</label>
            <input type="text" id="examOutput" class="delphi-form-edit" readonly placeholder="Resultado..." style="background: #ffffff; border: 2px solid #f43f5e; color: #9f1239; font-weight: bold; font-size: 1.1rem;">
          </div>

          <!-- CONSOLA LOG -->
          <div class="delphi-console-log" id="examConsoleLog" style="background: #1c060d; color: #fda4af; margin-top: 0.75rem;">
            [Ready] Simulador de Examen cargado. Ingrese valores y presione cualquier botón de modelo.
          </div>
        </div>
      </div>

      <!-- ACORDEÓN DE LOS 11 MODELOS DE EXAMEN -->
      <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 2rem;">

        <!-- MODELO 1 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #2563eb;">
          <h3 style="color: #1e3a8a; margin-top:0;">📝 MODELO 1: Formar Número con Menor Dígito Impar y Mayor Dígito Par (30 Puntos)</h3>
          <p><strong>Enunciado:</strong> Dado un número natural $N$, extraer todos sus dígitos y formar un nuevo número uniendo su menor dígito impar y su mayor dígito par.</p>
          <div class="box-info" style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $N = 85239$ &rarr; Menor Impar = 3, Mayor Par = 8 &rarr; <strong>Resultado = 38</strong>.
          </div>
          <pre><code class="language-pascal">function FormarMenorImparMayorPar(numeroNatural: Cardinal): Cardinal;
var
  digitoActual: Cardinal;
  menorImpar, mayorPar: Integer;
begin
  menorImpar := 10;
  mayorPar   := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 2 <> 0) then
    begin
      if Integer(digitoActual) < menorImpar then menorImpar := digitoActual;
    end
    else
    begin
      if Integer(digitoActual) > mayorPar then mayorPar := digitoActual;
    end;
    numeroNatural := numeroNatural div 10;
  end;
  if (menorImpar <> 10) and (mayorPar <> -1) then
    Result := (Cardinal(menorImpar) * 10) + Cardinal(mayorPar)
  else
    Result := 0;
end;</code></pre>
        </div>

        <!-- MODELO 2 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #2563eb;">
          <h3 style="color: #1e3a8a; margin-top:0;">📝 MODELO 2: Eliminar Dígitos a PARTIR de la Posición K (30 Puntos)</h3>
          <p><strong>Enunciado:</strong> Dado un número natural $N$ y una posición $K$ (contando desde la derecha, 1 = unidades), eliminar todos los dígitos a partir de dicha posición.</p>
          <div class="box-info" style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $N = 78143, K = 3$ &rarr; Corta en pos 3 hacia la izquierda &rarr; <strong>Resultado = 43</strong> ($78143 \pmod{10^2} = 43$).
          </div>
          <pre><code class="language-pascal">function EliminarAPartirDePosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  potencia: Cardinal;
  i: Byte;
begin
  if posicionK <= 1 then Exit(0);
  potencia := 1;
  for i := 1 to (posicionK - 1) do potencia := potencia * 10;
  Result := numeroNatural mod potencia;
end;</code></pre>
        </div>

        <!-- MODELO 3 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #2563eb;">
          <h3 style="color: #1e3a8a; margin-top:0;">📝 MODELO 3: Eliminar Únicamente el Dígito de la Posición K (30 Puntos)</h3>
          <p><strong>Enunciado:</strong> Eliminar el dígito ubicado exactamente en la posición $K$, preservando todos los demás dígitos en su posición y orden original.</p>
          <div class="box-info" style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $N = 78143, K = 2$ &rarr; Elimina el dígito '4' &rarr; <strong>Resultado = 7813</strong>.
          </div>
          <pre><code class="language-pascal">function EliminarDigitoEnPosicion(numeroNatural: Cardinal; posicionK: Byte): Cardinal;
var
  digitoActual, numeroResultado, potencia: Cardinal;
  posicionActual: Byte;
begin
  numeroResultado := 0; potencia := 1; posicionActual := 1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if posicionActual <> posicionK then
    begin
      numeroResultado := numeroResultado + (digitoActual * potencia);
      potencia := potencia * 10;
    end;
    Inc(posicionActual);
    numeroNatural := numeroNatural div 10;
  end;
  Result := numeroResultado;
end;</code></pre>
        </div>

        <!-- MODELO 4 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #f59e0b;">
          <h3 style="color: #b45309; margin-top:0;">📝 MODELO 4: Promedio de Dígitos Pares y Promedio de Impares (Pizarra)</h3>
          <p><strong>Enunciado:</strong> En un único procedimiento modular con parámetros por referencia (<code>var</code>), calcular simultáneamente el promedio de los dígitos pares y el promedio de los dígitos impares.</p>
          <pre><code class="language-pascal">procedure PromedioParesImpares(numeroNatural: Cardinal; var promPares, promImpares: Double);
var
  digitoActual: Cardinal;
  sumaPares, cantPares, sumaImpares, cantImpares: Cardinal;
begin
  sumaPares := 0; cantPares := 0; sumaImpares := 0; cantImpares := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual mod 2 = 0 then
    begin
      sumaPares := sumaPares + digitoActual;
      Inc(cantPares);
    end
    else
    begin
      sumaImpares := sumaImpares + digitoActual;
      Inc(cantImpares);
    end;
    numeroNatural := numeroNatural div 10;
  end;
  if cantPares > 0 then promPares := sumaPares / cantPares else promPares := 0.0;
  if cantImpares > 0 then promImpares := sumaImpares / cantImpares else promImpares := 0.0;
end;</code></pre>
        </div>

        <!-- MODELO 5 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #2563eb;">
          <h3 style="color: #1e3a8a; margin-top:0;">📝 MODELO 5: Mayor Dígito de los Múltiplos de 3 (10p)</h3>
          <p><strong>Enunciado:</strong> Encontrar el dígito de mayor valor numérico entre aquellos que son múltiplos de 3 (0, 3, 6, 9).</p>
          <pre><code class="language-pascal">function MayorDigitoMultiploDe3(numeroNatural: Cardinal): Integer;
var
  digitoActual: Cardinal;
  mayor: Integer;
begin
  mayor := -1;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if (digitoActual mod 3 = 0) and (Integer(digitoActual) > mayor) then
      mayor := digitoActual;
    numeroNatural := numeroNatural div 10;
  end;
  Result := mayor;
end;</code></pre>
        </div>

        <!-- MODELO 6 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #9333ea;">
          <h3 style="color: #6b21a8; margin-top:0;">📝 MODELO 6: Sumar Dígitos Hasta que Sea Menor a 10 / Raíz Digital (10p)</h3>
          <p><strong>Enunciado:</strong> Dado un número natural $N$, sumar sucesivamente sus dígitos hasta que el resultado final sea un valor menor a 10 (un solo dígito).</p>
          <div class="box-info" style="background: #faf5ff; border-left: 4px solid #a855f7; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $N = 15378 \longrightarrow (1+5+3+7+8 = 24) \longrightarrow (2+4 = 6) \longrightarrow$ <strong>Resultado = 6</strong>.
          </div>
          <pre><code class="language-pascal">function SumarHastaMenorA10(numeroNatural: Cardinal): Byte;
var
  suma, temp: Cardinal;
begin
  while numeroNatural >= 10 do
  begin
    suma := 0;
    temp := numeroNatural;
    while temp > 0 do
    begin
      suma := suma + (temp mod 10);
      temp := temp div 10;
    end;
    numeroNatural := suma;
  end;
  Result := numeroNatural;
end;</code></pre>
        </div>

        <!-- MODELO 7 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #10b981;">
          <h3 style="color: #047857; margin-top:0;">📝 MODELO 7: Promedio de la Serie Dual (S = 4 + 2 + 8 + 6 + 12 + 18...)</h3>
          <p><strong>Enunciado:</strong> Generar los primeros $N$ términos de la serie mixta intercalada: Posiciones impares $(4, 8, 12, 16\dots \text{ razón } +4)$ y posiciones pares $(2, 6, 18, 54\dots \text{ razón } \times 3)$, y retornar su promedio.</p>
          <pre><code class="language-pascal">function PromedioSerieDual(cantidadTerminos: Cardinal): Double;
var
  i, terminoImpar, terminoPar, terminoActual: Cardinal;
  sumaTotal: Double;
begin
  if cantidadTerminos = 0 then Exit(0.0);
  terminoImpar := 4; // Razón +4
  terminoPar   := 2; // Razón *3
  sumaTotal    := 0.0;
  for i := 1 to cantidadTerminos do
  begin
    if (i mod 2 <> 0) then
    begin
      terminoActual := terminoImpar;
      terminoImpar := terminoImpar + 4;
    end
    else
    begin
      terminoActual := terminoPar;
      terminoPar := terminoPar * 3;
    end;
    sumaTotal := sumaTotal + terminoActual;
  end;
  Result := sumaTotal / cantidadTerminos;
end;</code></pre>
        </div>

        <!-- MODELO 8 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #f59e0b;">
          <h3 style="color: #b45309; margin-top:0;">📝 MODELO 8: Sumar Dígitos de Cada Número y Acumular los Impares (10p)</h3>
          <p><strong>Enunciado:</strong> Hacer una función para sumar los dígitos de cada número de un lote y mostrar la sumatoria acumulada de aquellas sumas que resulten impares.</p>
          <div class="box-info" style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $n = 5, \{123, 25, 281, 94, 46\}$ &rarr; Sumas de dígitos: $6, \mathbf{7}, \mathbf{11}, \mathbf{13}, 10$ &rarr; $\text{SumaNumeroImpar} = 7 + 11 + 13 =$ <strong>Resultado = 31</strong>.
          </div>
          <pre><code class="language-pascal">function SumaDigitosImparesDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, temp, sumaDigitos, sumaTotalImpares: Cardinal;
begin
  sumaTotalImpares := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    sumaDigitos := 0;
    temp := numActual;
    while temp > 0 do
    begin
      sumaDigitos := sumaDigitos + (temp mod 10);
      temp := temp div 10;
    end;
    if (sumaDigitos mod 2 <> 0) then
      sumaTotalImpares := sumaTotalImpares + sumaDigitos;
  end;
  Result := sumaTotalImpares;
end;</code></pre>
        </div>

        <!-- MODELO 9 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #9333ea;">
          <h3 style="color: #6b21a8; margin-top:0;">📝 MODELO 9: Separar Dígitos Menores a 6 y Mayores o Iguales a 6 (10p)</h3>
          <p><strong>Enunciado:</strong> Dado un número natural, separar los dígitos menores a 6 en un número y los mayores o iguales a 6 en otro número.</p>
          <div class="box-info" style="background: #faf5ff; border-left: 4px solid #a855f7; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> Entrada = $16327$ &rarr; $&lt; 6 \text{ Resultado} = \mathbf{231}$ | $\ge 6 \text{ Resultado} = \mathbf{76}$.
          </div>
          <pre><code class="language-pascal">procedure SepararMenoresYMayores6(numeroNatural: Cardinal; var numMenores6, numMayores6: Cardinal);
var
  digitoActual: Cardinal;
begin
  numMenores6 := 0;
  numMayores6 := 0;
  while numeroNatural > 0 do
  begin
    digitoActual := numeroNatural mod 10;
    if digitoActual < 6 then
      numMenores6 := (numMenores6 * 10) + digitoActual // Formato inverso de pizarra: 231
    else
      numMayores6 := (numMayores6 * 10) + digitoActual; // Formato inverso de pizarra: 76
    numeroNatural := numeroNatural div 10;
  end;
end;</code></pre>
        </div>

        <!-- MODELO 10 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #10b981;">
          <h3 style="color: #047857; margin-top:0;">📝 MODELO 10: Promedio de Números Ascendentes en Rango [100-200] (10p)</h3>
          <p><strong>Enunciado:</strong> Introducir $n$ números por teclado y mostrar el promedio de aquellos números que llegan de forma ascendente dentro del rango $[100, 200]$.</p>
          <div class="box-info" style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> Si $n = 5$, números = $211, 120, 50, 180, 200$ &rarr; Válidos ascendentes: $120, 180, 200$ &rarr; $\text{Promedio} = (120 + 180 + 200) / 3 =$ <strong>166.66</strong>.
          </div>
          <pre><code class="language-pascal">function PromedioAscendentesRango100_200(const listaNumeros: array of Cardinal): Double;
var
  i: Integer;
  numActual, ultimoValido, sumaValidos, cantValidos: Cardinal;
begin
  sumaValidos := 0;
  cantValidos := 0;
  ultimoValido := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    if (numActual >= 100) and (numActual <= 200) and (numActual > ultimoValido) then
    begin
      sumaValidos := sumaValidos + numActual;
      Inc(cantValidos);
      ultimoValido := numActual;
    end;
  end;
  if cantValidos > 0 then
    Result := sumaValidos / cantValidos
  else
    Result := 0.0;
end;</code></pre>
        </div>

        <!-- MODELO 11 -->
        <div class="card" style="background: #ffffff; border-left: 5px solid #38bdf8;">
          <h3 style="color: #0369a1; margin-top:0;">📝 MODELO 11: Sumatoria Global de Dígitos Primos en Lote (Pizarra)</h3>
          <p><strong>Enunciado:</strong> Dado $N$ números naturales, verificar si existen dígitos primos ($2, 3, 5, 7$) en cada uno y realizar la sumatoria acumulada total.</p>
          <div class="box-info" style="background: #f0f9ff; border-left: 4px solid #38bdf8; padding: 0.75rem; margin: 0.5rem 0;">
            <strong>Ejemplo:</strong> $N = 4$, Números: $123 \ (2+3=5), 249 \ (2), 729 \ (7+2=9), 562 \ (5+2=7)$ &rarr; $SN = 5 + 2 + 9 + 7 =$ <strong>Resultado = 23</strong>.
          </div>
          <pre><code class="language-pascal">function SumatoriaPrimosDeLote(const listaNumeros: array of Cardinal): Cardinal;
var
  i: Integer;
  numActual, digito, temp, sumaTotalPrimos: Cardinal;
begin
  sumaTotalPrimos := 0;
  for i := Low(listaNumeros) to High(listaNumeros) do
  begin
    numActual := listaNumeros[i];
    temp := numActual;
    while temp > 0 do
    begin
      digito := temp mod 10;
      if (digito = 2) or (digito = 3) or (digito = 5) or (digito = 7) then
        sumaTotalPrimos := sumaTotalPrimos + digito;
      temp := temp div 10;
    end;
  end;
  Result := sumaTotalPrimos;
end;</code></pre>
        </div>

      </div>
    </div>
  </section>'''

    nuevo_html = html[:start_pos] + nueva_seccion + html[end_pos:]

    # Actualizamos las funciones JavaScript del simulador de examen
    js_exam_start = '// --- SIMULADOR MODELOS DE EXAMEN ---'
    js_exam_end = '// --- FIN SIMULADOR MODELOS ---'
    
    start_js_pos = nuevo_html.find(js_exam_start)
    end_js_pos = nuevo_html.find(js_exam_end)
    
    js_exam_code = '''// --- SIMULADOR MODELOS DE EXAMEN ---
    function parseLote() {
      const txt = document.getElementById('examInputLote').value;
      return txt.split(',').map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
    }

    function btnExamModelo1() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      let temp = n, menorImpar = 10, mayorPar = -1;
      while (temp > 0) {
        let d = temp % 10;
        if (d % 2 !== 0) { if (d < menorImpar) menorImpar = d; }
        else { if (d > mayorPar) mayorPar = d; }
        temp = Math.floor(temp / 10);
      }
      let res = (menorImpar !== 10 && mayorPar !== -1) ? (menorImpar * 10 + mayorPar) : 0;
      document.getElementById('examOutput').value = res;
      document.getElementById('examConsoleLog').innerText = `[Modelo 1] N = ${n} => MenorImpar: ${menorImpar === 10 ? 'None' : menorImpar}, MayorPar: ${mayorPar === -1 ? 'None' : mayorPar} => Resultado: ${res}`;
    }

    function btnExamModelo2() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      const k = parseInt(document.getElementById('examInputK').value, 10);
      if (k <= 1) {
        document.getElementById('examOutput').value = 0;
        document.getElementById('examConsoleLog').innerText = `[Modelo 2] N = ${n}, K = ${k} => Corta todo => Resultado: 0`;
        return;
      }
      let pot = Math.pow(10, k - 1);
      let res = n % pot;
      document.getElementById('examOutput').value = res;
      document.getElementById('examConsoleLog').innerText = `[Modelo 2] N = ${n}, K = ${k} => Formula N mod 10^(${k-1}) = ${n} mod ${pot} => Resultado: ${res}`;
    }

    function btnExamModelo3() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      const k = parseInt(document.getElementById('examInputK').value, 10);
      let temp = n, pos = 1, pot = 1, res = 0;
      while (temp > 0) {
        let d = temp % 10;
        if (pos !== k) {
          res += d * pot;
          pot *= 10;
        }
        pos++;
        temp = Math.floor(temp / 10);
      }
      document.getElementById('examOutput').value = res;
      document.getElementById('examConsoleLog').innerText = `[Modelo 3] N = ${n}, K = ${k} => Eliminando dígito en pos ${k} => Resultado: ${res}`;
    }

    function btnExamModelo4() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      let temp = n, sPar = 0, cPar = 0, sImp = 0, cImp = 0;
      while (temp > 0) {
        let d = temp % 10;
        if (d % 2 === 0) { sPar += d; cPar++; }
        else { sImp += d; cImp++; }
        temp = Math.floor(temp / 10);
      }
      let promP = cPar > 0 ? (sPar / cPar).toFixed(2) : '0.00';
      let promI = cImp > 0 ? (sImp / cImp).toFixed(2) : '0.00';
      document.getElementById('examOutput').value = `PromPar: ${promP} | PromImpar: ${promI}`;
      document.getElementById('examConsoleLog').innerText = `[Modelo 4] N = ${n} => Pares: suma=${sPar}, cant=${cPar} (prom=${promP}) | Impares: suma=${sImp}, cant=${cImp} (prom=${promI})`;
    }

    function btnExamModelo5() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      let temp = n, mayor = -1;
      while (temp > 0) {
        let d = temp % 10;
        if (d % 3 === 0 && d > mayor) mayor = d;
        temp = Math.floor(temp / 10);
      }
      document.getElementById('examOutput').value = mayor !== -1 ? mayor : 'Sin múltiplos de 3';
      document.getElementById('examConsoleLog').innerText = `[Modelo 5] N = ${n} => Mayor dígito múltiplo de 3 => Resultado: ${mayor}`;
    }

    function btnExamModelo6() {
      let n = parseInt(document.getElementById('examInputN').value, 10);
      let steps = [n];
      while (n >= 10) {
        let sum = 0, temp = n;
        while (temp > 0) {
          sum += temp % 10;
          temp = Math.floor(temp / 10);
        }
        n = sum;
        steps.push(n);
      }
      document.getElementById('examOutput').value = n;
      document.getElementById('examConsoleLog').innerText = `[Modelo 6] Raíz digital: ${steps.join(' -> ')} => Resultado final: ${n}`;
    }

    function btnExamModelo7() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      if (n <= 0) {
        document.getElementById('examOutput').value = '0.00';
        return;
      }
      let tImp = 4, tPar = 2, sum = 0, terminos = [];
      for (let i = 1; i <= n; i++) {
        let t;
        if (i % 2 !== 0) {
          t = tImp; tImp += 4;
        } else {
          t = tPar; tPar *= 3;
        }
        terminos.push(t);
        sum += t;
      }
      let prom = (sum / n).toFixed(2);
      document.getElementById('examOutput').value = `Promedio: ${prom} (Suma: ${sum})`;
      document.getElementById('examConsoleLog').innerText = `[Modelo 7] Serie (${n} términos): [${terminos.join(', ')}] => Suma=${sum} => Promedio = ${prom}`;
    }

    function btnExamModelo8() {
      const lote = parseLote();
      let sumaTotalImpares = 0;
      let logs = [];
      lote.forEach(num => {
        let sumDig = 0, temp = num;
        while (temp > 0) { sumDig += temp % 10; temp = Math.floor(temp / 10); }
        let esImp = sumDig % 2 !== 0;
        if (esImp) sumaTotalImpares += sumDig;
        logs.push(`${num}(suma=${sumDig}${esImp ? ' -> impar ✅' : ' -> par ❌'})`);
      });
      document.getElementById('examOutput').value = sumaTotalImpares;
      document.getElementById('examConsoleLog').innerText = `[Modelo 8] Lote: ${logs.join(' + ')} => SumaNumeroImpar = ${sumaTotalImpares}`;
    }

    function btnExamModelo9() {
      const n = parseInt(document.getElementById('examInputN').value, 10);
      let temp = n, numMenores6 = 0, numMayores6 = 0;
      while (temp > 0) {
        let d = temp % 10;
        if (d < 6) numMenores6 = (numMenores6 * 10) + d;
        else numMayores6 = (numMayores6 * 10) + d;
        temp = Math.floor(temp / 10);
      }
      document.getElementById('examOutput').value = `<6: ${numMenores6} | >=6: ${numMayores6}`;
      document.getElementById('examConsoleLog').innerText = `[Modelo 9] N = ${n} => Dígitos < 6: ${numMenores6} | Dígitos >= 6: ${numMayores6}`;
    }

    function btnExamModelo10() {
      const lote = parseLote();
      let sum = 0, cant = 0, ultimoValido = 0, validos = [];
      lote.forEach(num => {
        if (num >= 100 && num <= 200 && num > ultimoValido) {
          sum += num;
          cant++;
          ultimoValido = num;
          validos.push(num);
        }
      });
      let prom = cant > 0 ? (sum / cant).toFixed(2) : '0.00';
      document.getElementById('examOutput').value = `Promedio: ${prom} (Válidos: ${validos.join(', ')})`;
      document.getElementById('examConsoleLog').innerText = `[Modelo 10] Lote: [${lote.join(', ')}] => Ascendentes en [100-200]: [${validos.join(', ')}] => Promedio = (${sum})/${cant} = ${prom}`;
    }

    function btnExamModelo11() {
      const lote = parseLote();
      let sumaTotalPrimos = 0, logs = [];
      lote.forEach(num => {
        let temp = num, primosEnNum = [], sumNum = 0;
        while (temp > 0) {
          let d = temp % 10;
          if (d === 2 || d === 3 || d === 5 || d === 7) {
            primosEnNum.push(d);
            sumNum += d;
            sumaTotalPrimos += d;
          }
          temp = Math.floor(temp / 10);
        }
        logs.push(`${num}: [${primosEnNum.reverse().join('+') || 'ninguno'}]`);
      });
      document.getElementById('examOutput').value = sumaTotalPrimos;
      document.getElementById('examConsoleLog').innerText = `[Modelo 11] Lote Primos: ${logs.join(' | ')} => SN = ${sumaTotalPrimos}`;
    }
'''

    if start_js_pos != -1 and end_js_pos != -1:
        nuevo_html = nuevo_html[:start_js_pos] + js_exam_code + '\n    ' + nuevo_html[end_js_pos:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(nuevo_html)
    print("HTML actualizado con exito con los 11 modelos de examen interactivos.")

if __name__ == '__main__':
    update_html_with_11_exam_models()
