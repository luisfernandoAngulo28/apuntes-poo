// =============================================================================
// MOTOR DE LAS 4 NUEVAS HERRAMIENTAS ACTIVAS (EXAMEN UAGRM - INF110-Z2)
// 1. Carrera Visual de los 5 Métodos de Ordenamiento
// 2. Laboratorio «Detecta y Corrige el Bug de Examen»
// 3. Entrenador de Prueba de Escritorio («Modo Llenar Tabla»)
// 4. Banco Maestro de 25 Preguntas Trampa Teóricas (Quiz Rápido)
// =============================================================================

// =============================================================================
// HERRAMIENTA 1: CARRERA VISUAL DE ORDENAMIENTOS
// =============================================================================
let raceDataOriginal = [4, 5, 1, 2, 3];

function raceCargarVector(str) {
  document.getElementById('raceInputVector').value = str;
  raceRenderInitial();
}

function raceGenerarAleatorio(cant) {
  const arr = [];
  for (let i = 0; i < cant; i++) {
    arr.push(Math.floor(Math.random() * 90) + 10);
  }
  document.getElementById('raceInputVector').value = arr.join(', ');
  raceRenderInitial();
}

function raceParseInput() {
  const raw = document.getElementById('raceInputVector').value || '';
  const parts = raw.split(',').map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
  return parts.length > 0 ? parts : [4, 5, 1, 2, 3];
}

function raceRenderInitial() {
  const arr = raceParseInput();
  const algs = ['burbuja', 'seleccion', 'insercion', 'shell', 'quicksort'];
  algs.forEach(alg => {
    raceDrawBars(alg, arr);
    document.getElementById('raceComp-' + alg).innerText = '0';
    document.getElementById('raceSwap-' + alg).innerText = '0';
    document.getElementById('raceStatus-' + alg).innerText = 'Listo';
    document.getElementById('raceStatus-' + alg).style.color = '#94a3b8';
  });
  document.getElementById('raceVerdictBox').innerHTML = 'Presiona <strong>«Iniciar Carrera»</strong> para ver competir los 5 algoritmos simultáneamente.';
}

function raceDrawBars(alg, arr, activeIdx = -1) {
  const container = document.getElementById('raceBars-' + alg);
  if (!container) return;
  container.innerHTML = '';
  const max = Math.max(...arr, 1);

  arr.forEach((val, idx) => {
    const bar = document.createElement('div');
    const heightPct = Math.max(15, Math.round((val / max) * 100));
    bar.style.flex = '1';
    bar.style.minWidth = '8px';
    bar.style.height = heightPct + '%';
    bar.style.borderRadius = '3px 3px 0 0';
    bar.style.transition = 'height 0.1s ease, background 0.1s ease';
    bar.style.position = 'relative';

    if (idx === activeIdx) {
      bar.style.background = '#fbbf24';
    } else {
      bar.style.background = (alg === 'burbuja' ? '#10b981' : alg === 'seleccion' ? '#38bdf8' : alg === 'insercion' ? '#c084fc' : alg === 'shell' ? '#f59e0b' : '#ec4899');
    }
    container.appendChild(bar);
  });
}

function raceIniciarCarrera() {
  const original = raceParseInput();
  const btn = document.getElementById('btnRaceStart');
  btn.disabled = true;
  btn.innerText = '⏳ Compitiendo...';

  // Ejecución y conteo de cada algoritmo
  const stats = {};

  // 1. Burbuja
  {
    const a = [...original];
    let comp = 0, swap = 0;
    for (let i = 0; i < a.length - 1; i++) {
      for (let j = i + 1; j < a.length; j++) {
        comp++;
        if (a[i] > a[j]) {
          swap++;
          let t = a[i]; a[i] = a[j]; a[j] = t;
        }
      }
    }
    stats.burbuja = { comp, swap, res: a };
  }

  // 2. Selección
  {
    const a = [...original];
    let comp = 0, swap = 0;
    for (let i = 0; i < a.length - 1; i++) {
      let min = i;
      for (let j = i + 1; j < a.length; j++) {
        comp++;
        if (a[j] < a[min]) min = j;
      }
      if (min !== i) {
        swap++;
        let t = a[i]; a[i] = a[min]; a[min] = t;
      }
    }
    stats.seleccion = { comp, swap, res: a };
  }

  // 3. Inserción
  {
    const a = [...original];
    let comp = 0, swap = 0;
    for (let i = 1; i < a.length; i++) {
      let key = a[i];
      let j = i - 1;
      while (j >= 0) {
        comp++;
        if (a[j] > key) {
          a[j + 1] = a[j];
          swap++;
          j--;
        } else {
          break;
        }
      }
      a[j + 1] = key;
    }
    stats.insercion = { comp, swap, res: a };
  }

  // 4. Shell Sort
  {
    const a = [...original];
    let comp = 0, swap = 0;
    let n = a.length;
    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
      for (let i = gap; i < n; i++) {
        let temp = a[i];
        let j = i;
        while (j >= gap) {
          comp++;
          if (a[j - gap] > temp) {
            a[j] = a[j - gap];
            swap++;
            j -= gap;
          } else {
            break;
          }
        }
        a[j] = temp;
      }
    }
    stats.shell = { comp, swap, res: a };
  }

  // 5. QuickSort
  {
    const a = [...original];
    let comp = 0, swap = 0;
    function qs(low, high) {
      if (low < high) {
        let pIndex = partition(low, high);
        qs(low, pIndex - 1);
        qs(pIndex + 1, high);
      }
    }
    function partition(low, high) {
      let pivot = a[high];
      let i = low - 1;
      for (let j = low; j < high; j++) {
        comp++;
        if (a[j] < pivot) {
          i++;
          swap++;
          let t = a[i]; a[i] = a[j]; a[j] = t;
        }
      }
      swap++;
      let t = a[i + 1]; a[i + 1] = a[high]; a[high] = t;
      return i + 1;
    }
    qs(0, a.length - 1);
    stats.quicksort = { comp, swap, res: a };
  }

  // Animar las barras progresivamente
  const algs = ['burbuja', 'seleccion', 'insercion', 'shell', 'quicksort'];
  let step = 0;
  const interval = setInterval(() => {
    step++;
    algs.forEach(alg => {
      const s = stats[alg];
      const compVal = Math.min(s.comp, Math.round(s.comp * (step / 8)));
      const swapVal = Math.min(s.swap, Math.round(s.swap * (step / 8)));
      document.getElementById('raceComp-' + alg).innerText = compVal;
      document.getElementById('raceSwap-' + alg).innerText = swapVal;
    });

    if (step >= 8) {
      clearInterval(interval);
      algs.forEach(alg => {
        raceDrawBars(alg, stats[alg].res);
        document.getElementById('raceStatus-' + alg).innerText = '✓ Terminado';
        document.getElementById('raceStatus-' + alg).style.color = '#34d399';
      });

      btn.disabled = false;
      btn.innerText = '🚀 Iniciar Carrera';

      // Veredicto
      const totalBurbuja = stats.burbuja.comp + stats.burbuja.swap;
      const totalQuick = stats.quicksort.comp + stats.quicksort.swap;
      const totalShell = stats.shell.comp + stats.shell.swap;

      document.getElementById('raceVerdictBox').innerHTML = 
        '🏆 <strong>Conclusión Técnica de Examen:</strong> Para este vector de ' + original.length + ' elementos, ' +
        '<strong>Burbuja</strong> realizó <span style="color:#f87171; font-weight:800;">' + stats.burbuja.comp + ' comparaciones</span> y ' + stats.burbuja.swap + ' intercambios (total ' + totalBurbuja + ' ops), ' +
        'mientras que <strong>QuickSort</strong> resolvió con solo <span style="color:#34d399; font-weight:800;">' + stats.quicksort.comp + ' comparaciones</span> y ' + stats.quicksort.swap + ' swaps. ' +
        '¡QuickSort fue <strong>' + (totalBurbuja > 0 ? (totalBurbuja / Math.max(1, totalQuick)).toFixed(1) : 1) + 'x veces más eficiente</strong>!';
    }
  }, 90);
}

// =============================================================================
// HERRAMIENTA 2: LABORATORIO «DETECTA Y CORRIGE EL BUG DE EXAMEN»
// =============================================================================
const bugCasosData = [
  {
    titulo: 'Caso 1: ¿Por qué este algoritmo cuelga la computadora (Freeze / Hang)?',
    badge: 'BUCLE INFINITO',
    badgeColor: '#f87171',
    prompt: 'Analiza el siguiente código que debería contar los espacios en blanco de una cadena:',
    code: `function EspaciosEnBlanco(cad: String; n: Byte): Byte;
var c, i: Byte;
begin
  c := 0; i := 1;
  while i <= n do begin
    if cad[i] = ' ' then
      c := c + 1;
    // ¿Qué línea crítica falta aquí antes de cerrar el bucle?
  end;
  Result := c;
end;`,
    lineHighlight: 7,
    options: [
      { text: "A) La variable 'c' debe inicializarse en 1 y no en 0.", correct: false },
      { text: "B) Falta el incremento obligatorio del puntero: 'i := i + 1;' provocando un bucle infinito que nunca sale.", correct: true },
      { text: "C) Se debe usar 'cad[i] = #0' en lugar del espacio.", correct: false },
      { text: "D) 'Result' no es una palabra válida en funciones Delphi.", correct: false }
    ],
    feedback: "¡Exacto! Al olvidar <code>i := i + 1;</code> dentro del bloque <code>while</code>, la variable <code>i</code> permanece eternamente en 1. La condición <code>1 <= n</code> jamás se vuelve falsa, congelando el programa.",
    correctCode: `function EspaciosEnBlanco(cad: String; n: Byte): Byte;
var c, i: Byte;
begin
  c := 0; i := 1;
  while i <= n do begin
    if cad[i] = ' ' then
      c := c + 1;
    i := i + 1; // <-- ¡INCREMENTO OBLIGATORIO!
  end;
  Result := c;
end;`
  },
  {
    titulo: 'Caso 2: ¿Por qué este código genera "Access Violation" o lee basura?',
    badge: 'OFF-BY-ONE INDEXING',
    badgeColor: '#fbbf24',
    prompt: 'El estudiante vino de C++/Java e intentó recorrer la cadena en Delphi de esta manera:',
    code: `function PrimeraLetra(cad: String; n: Byte): Char;
var i: Byte;
begin
  i := 0; // <-- Inicia en cero como en Java/Python
  Result := cad[i];
end;`,
    lineHighlight: 4,
    options: [
      { text: "A) En Delphi los String nativos se indexan a partir de 1. 'cad[0]' no es la primera letra (contiene la longitud en ShortString o es inválido).", correct: true },
      { text: "B) 'Char' no es compatible con cadenas en Delphi.", correct: false },
      { text: "C) Se debe usar siempre un procedimiento y no una función.", correct: false },
      { text: "D) La variable 'i' debe ser de tipo Real.", correct: false }
    ],
    feedback: "¡Brillante! En Pascal/Delphi, los caracteres válidos de un String van desde <code>cad[1]</code> hasta <code>cad[n]</code>. Acceder a <code>cad[0]</code> es un error de examen clásico.",
    correctCode: `function PrimeraLetra(cad: String; n: Byte): Char;
begin
  if n > 0 then
    Result := cad[1] // <-- ¡ÍNDICE 1 ES EL PRIMER CARÁCTER!
  else
    Result := ' ';
end;`
  },
  {
    titulo: 'Caso 3: ¿Por qué el compilador lanza "Statement expected, but ELSE found"?',
    badge: 'ERROR DE SINTAXIS',
    badgeColor: '#ec4899',
    prompt: 'El alumno jura que su estructura if-else está perfecta:',
    code: `if cad[i] in ['a'..'z'] then begin
  contador := contador + 1;
end; // <-- ¡Cuidado con este punto y coma!
else begin
  consonantes := consonantes + 1;
end;`,
    lineHighlight: 3,
    options: [
      { text: "A) En Delphi el 'else' debe escribirse en mayúsculas obligatoriamente.", correct: false },
      { text: "B) En Pascal NUNCA se coloca punto y coma (;) inmediatamente antes de la palabra reservada 'else'.", correct: true },
      { text: "C) El conjunto ['a'..'z'] no admite rangos de letras.", correct: false },
      { text: "D) No se permite usar 'begin..end' dentro de una rama if.", correct: false }
    ],
    feedback: "¡Correcto! En la gramática formal de Pascal, la instrucción completa termina en el <code>else</code>. Un punto y coma antes de <code>else</code> cierra la sentencia prematuramente, haciendo que el compilador considere el <code>else</code> huérfano.",
    correctCode: `if cad[i] in ['a'..'z'] then begin
  contador := contador + 1;
end // <-- ¡SIN PUNTO Y COMA ANTES DE ELSE!
else begin
  consonantes := consonantes + 1;
end;`
  },
  {
    titulo: 'Caso 4: ¿Por qué la función siempre retorna 0 o valores erráticos?',
    badge: 'FALTA DE ASIGNACIÓN A RESULT',
    badgeColor: '#a855f7',
    prompt: 'El algoritmo cuenta correctamente todas las mayúsculas, pero el Edit3.Text siempre muestra 0:',
    code: `function CantidadMayusculas(cad: String; n, i: Byte): Byte;
var cont: Byte;
begin
  cont := 0; i := 1;
  while i <= n do begin
    if cad[i] in ['A'..'Z'] then
      cont := cont + 1;
    i := i + 1;
  end;
  // Fin de la función... ¿Dónde se entrega la respuesta?
end;`,
    lineHighlight: 9,
    options: [
      { text: "A) Falta asignar el resultado final a la pseudo-variable 'Result := cont;' o al nombre de la función.", correct: true },
      { text: "B) Se debe declarar 'cad' como 'var' obligatoriamente.", correct: false },
      { text: "C) 'cont' no puede superar el valor 10.", correct: false },
      { text: "D) La función debe llamarse 'procedure'.", correct: false }
    ],
    feedback: "¡Así es! Toda función en Delphi debe depositar su valor de retorno en <code>Result := cont;</code> o <code>CantidadMayusculas := cont;</code>. Si no se hace, Delphi retorna lo que haya quedado en el registro EAX de la CPU (basura).",
    correctCode: `  // ...
  while i <= n do begin
    // ...
  end;
  Result := cont; // <-- ¡ASIGNACIÓN DEL RETORNO!
end;`
  },
  {
    titulo: 'Caso 5: ¿Por qué la suma da números gigantes como 32742 en vez de 15?',
    badge: 'BASURA EN LA PILA (RAM)',
    badgeColor: '#38bdf8',
    prompt: 'Observa la función de sumar dígitos de un número natural:',
    code: `function SumarDigitos(n: Cardinal): Cardinal;
var suma, dig: Cardinal;
begin
  // Falta inicializar suma := 0;
  while n > 0 do begin
    dig := n mod 10;
    suma := suma + dig;
    n := n div 10;
  end;
  Result := suma;
end;`,
    lineHighlight: 4,
    options: [
      { text: "A) 'n mod 10' no funciona con tipo Cardinal.", correct: false },
      { text: "B) Las variables locales en Delphi NO se inicializan automáticamente en 0; contienen basura de la memoria RAM hasta que las inicializas con 'suma := 0;'.", correct: true },
      { text: "C) El bucle debe ser 'while n >= 0'.", correct: false },
      { text: "D) Se debe usar multiplicación en lugar de suma.", correct: false }
    ],
    feedback: "¡Totalmente correcto! A diferencia de las variables globales que residen en el segmento BSS/Data y se rellenan con ceros al cargar el ejecutable, las variables locales se alojan en el Stack (pila) y conservan el valor residual previo.",
    correctCode: `function SumarDigitos(n: Cardinal): Cardinal;
var suma, dig: Cardinal;
begin
  suma := 0; // <-- ¡INICIALIZACIÓN OBLIGATORIA!
  while n > 0 do begin
    dig := n mod 10;
    suma := suma + dig;
    n := n div 10;
  end;
  Result := suma;
end;`
  },
  {
    titulo: 'Caso 6: ¿Por qué este ordenamiento duplica un número y pierde el otro?',
    badge: 'SWAP DESTRUCTIVO',
    badgeColor: '#f59e0b',
    prompt: 'El estudiante intentó intercambiar Cad[I] y Cad[J] sin usar variable Auxiliar:',
    code: `if cad[i] > cad[j] then begin
  cad[i] := cad[j]; // Sobrescribe cad[i] perdiendo su valor original
  cad[j] := cad[i]; // ¡Aquí copia el mismo cad[j] recién asignado!
end;`,
    lineHighlight: 2,
    options: [
      { text: "A) El intercambio requiere obligatoriamente una variable auxiliar temporal: 'aux := cad[i]; cad[i] := cad[j]; cad[j] := aux;'.", correct: true },
      { text: "B) Se debe usar una función matemática de división.", correct: false },
      { text: "C) En Delphi no se pueden modificar dos posiciones de un string.", correct: false },
      { text: "D) La condición debe ser con operador '<>'.", correct: false }
    ],
    feedback: "¡Excelente! Si asignas <code>cad[i] := cad[j];</code> sin guardar antes el valor de <code>cad[i]</code> en <code>aux</code>, el dato original se destruye para siempre.",
    correctCode: `if cad[i] > cad[j] then begin
  aux := cad[i];    // 1. Guarda 1er elemento
  cad[i] := cad[j]; // 2. Actualiza con el segundo
  cad[j] := aux;    // 3. Recupera desde Aux
end;`
  }
];

let bugCasoActual = 0;

function bugCargarCaso(idx, btn) {
  bugCasoActual = idx;
  const c = bugCasosData[idx];

  // Actualizar botones activos
  document.querySelectorAll('#bugNavButtons button').forEach(b => {
    b.style.background = '#1e293b';
    b.style.color = '#94a3b8';
  });
  if (btn) {
    btn.style.background = '#0284c7';
    btn.style.color = '#ffffff';
  }

  document.getElementById('bugTitle').innerText = c.titulo;
  document.getElementById('bugBadge').innerText = c.badge;
  document.getElementById('bugBadge').style.color = c.badgeColor;
  document.getElementById('bugBadge').style.borderColor = c.badgeColor;
  document.getElementById('bugPrompt').innerText = c.prompt;

  // Renderizar código con números de línea
  const lines = c.code.split('\n');
  let codeHtml = '';
  lines.forEach((l, i) => {
    const lineNum = i + 1;
    const isHighlight = (lineNum === c.lineHighlight);
    codeHtml += '<div style="padding: 2px 6px; ' + (isHighlight ? 'background: rgba(239, 68, 68, 0.2); border-left: 3px solid #ef4444;' : '') + '">' +
                '<span style="color: #64748b; margin-right: 12px; user-select: none;">' + (lineNum < 10 ? ' ' : '') + lineNum + '</span>' +
                '<span style="color: ' + (isHighlight ? '#fca5a5' : '#f8fafc') + ';">' + htmlEscape(l) + '</span>' +
                '</div>';
  });
  document.getElementById('bugCodeContainer').innerHTML = codeHtml;

  // Renderizar opciones
  let optHtml = '';
  c.options.forEach((opt, oIdx) => {
    optHtml += '<button class="delphi-btn-vcl" id="bugOptBtn-' + oIdx + '" onclick="bugSeleccionarOpcion(' + oIdx + ')" style="text-align: left; background: #0f172a; border: 1.5px solid #334155; color: #cbd5e1; padding: 0.75rem 1rem; border-radius: 6px; font-size: 0.88rem; transition: all 0.2s;">' +
               htmlEscape(opt.text) +
               '</button>';
  });
  document.getElementById('bugOptionsGrid').innerHTML = optHtml;

  // Ocultar caja de explicación
  document.getElementById('bugExplanationBox').style.display = 'none';
}

function bugSeleccionarOpcion(oIdx) {
  const c = bugCasosData[bugCasoActual];
  const isCorrect = c.options[oIdx].correct;

  c.options.forEach((opt, idx) => {
    const btn = document.getElementById('bugOptBtn-' + idx);
    if (!btn) return;
    btn.disabled = true;
    if (opt.correct) {
      btn.style.background = 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10b981';
      btn.style.color = '#34d399';
    } else if (idx === oIdx && !isCorrect) {
      btn.style.background = 'rgba(239, 68, 68, 0.25)';
      btn.style.borderColor = '#ef4444';
      btn.style.color = '#f87171';
    }
  });

  const expBox = document.getElementById('bugExplanationBox');
  expBox.style.display = 'block';

  if (isCorrect) {
    document.getElementById('bugFeedbackTitle').innerHTML = '✅ ¡CORRECTO! Detectaste el error';
    document.getElementById('bugFeedbackTitle').style.color = '#34d399';
  } else {
    document.getElementById('bugFeedbackTitle').innerHTML = '❌ Incorrecto. Revisa el análisis técnico:';
    document.getElementById('bugFeedbackTitle').style.color = '#f87171';
  }

  document.getElementById('bugFeedbackText').innerHTML = c.feedback;
  document.getElementById('bugCorrectCode').innerText = c.correctCode;
}

// =============================================================================
// HERRAMIENTA 3: ENTRENADOR DE PRUEBA DE ESCRITORIO (MODO LLENAR TABLA)
// =============================================================================
const trainExercisesData = {
  vocales: {
    titulo: "Contar Vocales en 'casa' (n = 4)",
    code: `contador := 0; i := 1;
while i <= n do begin
  if cad[i] in ['a','e','i','o','u'] then
    contador := contador + 1;
  i := i + 1;
end;`,
    headers: ["Paso", "i", "i <= n", "cad[i]", "¿Vocal?", "contador", "i := i+1"],
    rows: [
      { step: 1, i: "1", cond: "SÍ", char: "c", vocal: "NO", contador: "0", nextI: "2" },
      { step: 2, i: "2", cond: "SÍ", char: "a", vocal: "SÍ", contador: "1", nextI: "3" },
      { step: 3, i: "3", cond: "SÍ", char: "s", vocal: "NO", contador: "1", nextI: "4" },
      { step: 4, i: "4", cond: "SÍ", char: "a", vocal: "SÍ", contador: "2", nextI: "5" },
      { step: 5, i: "5", cond: "NO", char: "-", vocal: "-", contador: "2", nextI: "Fin" }
    ]
  },
  burbuja: {
    titulo: "Pizarra: Ordenar Burbuja '321' (n = 3)",
    code: `for i := 1 to n - 1 do
  for j := i + 1 to n do
    if cad[i] > cad[j] then begin
      aux := cad[i]; cad[i] := cad[j]; cad[j] := aux;
    end;`,
    headers: ["Paso", "I", "J", "¿Cad[I] > Cad[J]?", "Aux", "Cadena Actual"],
    rows: [
      { step: 1, i: "1", j: "2", cond: "SÍ", aux: "3", cad: "231" },
      { step: 2, i: "1", j: "3", cond: "SÍ", aux: "2", cad: "132" },
      { step: 3, i: "2", j: "3", cond: "SÍ", aux: "3", cad: "123" }
    ]
  },
  invertir: {
    titulo: "Invertir Cadena 'sol' (n = 3, i := n downto 1)",
    code: `res := ''; i := n;
while i >= 1 do begin
  res := res + cad[i];
  i := i - 1;
end;`,
    headers: ["Paso", "i", "i >= 1", "cad[i]", "res", "i := i-1"],
    rows: [
      { step: 1, i: "3", cond: "SÍ", char: "l", res: "l", nextI: "2" },
      { step: 2, i: "2", cond: "SÍ", char: "o", res: "lo", nextI: "1" },
      { step: 3, i: "1", cond: "SÍ", char: "s", res: "los", nextI: "0" },
      { step: 4, i: "0", cond: "NO", char: "-", res: "los", nextI: "Fin" }
    ]
  },
  primos: {
    titulo: "Sumar Dígitos Primos de 352 (n = 352)",
    code: `suma := 0;
while n > 0 do begin
  d := n mod 10;
  if d in [2,3,5,7] then suma := suma + d;
  n := n div 10;
end;`,
    headers: ["Paso", "n", "n > 0", "d (n mod 10)", "¿Primo?", "suma", "n div 10"],
    rows: [
      { step: 1, n: "352", cond: "SÍ", d: "2", primo: "SÍ", suma: "2", nextN: "35" },
      { step: 2, n: "35", cond: "SÍ", d: "5", primo: "SÍ", suma: "7", nextN: "3" },
      { step: 3, n: "3", cond: "SÍ", d: "3", primo: "SÍ", suma: "10", nextN: "0" },
      { step: 4, n: "0", cond: "NO", d: "-", primo: "-", suma: "10", nextN: "Fin" }
    ]
  }
};

let trainExActual = 'vocales';

function trainCargarEjercicio() {
  const sel = document.getElementById('trainExSelect').value;
  trainExActual = sel;
  const ex = trainExercisesData[sel];

  document.getElementById('trainEnunciadoTitle').innerText = ex.titulo;
  document.getElementById('trainCodeSnippet').innerText = ex.code;
  document.getElementById('trainPuntajeBadge').innerText = 'Puntuación: Pendiente';
  document.getElementById('trainPuntajeBadge').style.color = '#94a3b8';
  document.getElementById('trainFeedbackBox').style.display = 'none';

  // Render headers
  let thHtml = '<tr>';
  ex.headers.forEach(h => {
    thHtml += '<th>' + h + '</th>';
  });
  thHtml += '</tr>';
  document.getElementById('trainThead').innerHTML = thHtml;

  // Render inputs rows
  let tbHtml = '';
  ex.rows.forEach((r, rIdx) => {
    tbHtml += '<tr>';
    tbHtml += '<td style="font-weight:bold; color:#38bdf8;">' + r.step + '</td>';
    
    // Obtenemos las claves ignorando 'step'
    const keys = Object.keys(r).filter(k => k !== 'step');
    keys.forEach(k => {
      tbHtml += '<td style="padding: 4px;">' +
                '<input type="text" class="train-input" data-row="' + rIdx + '" data-key="' + k + '" placeholder="?" style="width: 100%; text-align: center; font-family: \'Fira Code\', monospace; font-size: 0.85rem; padding: 4px 6px; background: #070a13; border: 1.5px solid #334155; border-radius: 4px; color: #ffffff;">' +
                '</td>';
    });
    tbHtml += '</tr>';
  });
  document.getElementById('trainTbody').innerHTML = tbHtml;
}

function trainCalificar() {
  const ex = trainExercisesData[trainExActual];
  const inputs = document.querySelectorAll('.train-input');
  let correctCount = 0;
  let totalCount = inputs.length;

  inputs.forEach(inp => {
    const rIdx = parseInt(inp.getAttribute('data-row'), 10);
    const key = inp.getAttribute('data-key');
    const expected = String(ex.rows[rIdx][key]).trim().toLowerCase();
    const userVal = String(inp.value || '').trim().toLowerCase();

    // Normalizar SÍ / SI / YES / V
    const isBoolTrue = (expected === 'sí' || expected === 'si' || expected === 'v' || expected === 'verdadero');
    const userBoolTrue = (userVal === 'sí' || userVal === 'si' || userVal === 'v' || userVal === 'verdadero');

    const isMatch = (userVal === expected) || (isBoolTrue && userBoolTrue);

    if (isMatch) {
      correctCount++;
      inp.style.background = 'rgba(16, 185, 129, 0.25)';
      inp.style.borderColor = '#10b981';
      inp.style.color = '#34d399';
      inp.title = '✓ Correcto';
    } else {
      inp.style.background = 'rgba(239, 68, 68, 0.25)';
      inp.style.borderColor = '#ef4444';
      inp.style.color = '#fca5a5';
      inp.title = 'Era: ' + ex.rows[rIdx][key];
    }
  });

  const pct = Math.round((correctCount / totalCount) * 100);
  const badge = document.getElementById('trainPuntajeBadge');
  badge.innerText = correctCount + ' / ' + totalCount + ' (' + pct + '%)';
  badge.style.color = (pct >= 80 ? '#34d399' : pct >= 50 ? '#fbbf24' : '#ef4444');

  const fbBox = document.getElementById('trainFeedbackBox');
  fbBox.style.display = 'block';
  if (pct >= 80) {
    document.getElementById('trainFeedbackTitle').innerText = '🎉 ¡Excelente Dominio de la Traza!';
    document.getElementById('trainFeedbackTitle').style.color = '#34d399';
    document.getElementById('trainFeedbackDesc').innerText = 'Has obtenido ' + pct + '%. Tu razonamiento paso a paso coincide plenamente con el estándar de evaluación de la docente.';
  } else {
    document.getElementById('trainFeedbackTitle').innerText = '⚠️ Ojo con los detalles del examen';
    document.getElementById('trainFeedbackTitle').style.color = '#fbbf24';
    document.getElementById('trainFeedbackDesc').innerText = 'Puntaje: ' + pct + '%. Pasa el mouse sobre las casillas en rojo para ver el valor exacto esperado o presiona «Ver Solución Oficial».';
  }
}

function trainRevelar() {
  const ex = trainExercisesData[trainExActual];
  const inputs = document.querySelectorAll('.train-input');
  inputs.forEach(inp => {
    const rIdx = parseInt(inp.getAttribute('data-row'), 10);
    const key = inp.getAttribute('data-key');
    inp.value = ex.rows[rIdx][key];
    inp.style.background = 'rgba(56, 189, 248, 0.2)';
    inp.style.borderColor = '#38bdf8';
    inp.style.color = '#7dd3fc';
  });
  document.getElementById('trainPuntajeBadge').innerText = 'Solución Oficial Cargada';
  document.getElementById('trainPuntajeBadge').style.color = '#38bdf8';
}

function trainLimpiar() {
  const inputs = document.querySelectorAll('.train-input');
  inputs.forEach(inp => {
    inp.value = '';
    inp.style.background = '#070a13';
    inp.style.borderColor = '#334155';
    inp.style.color = '#ffffff';
  });
  document.getElementById('trainPuntajeBadge').innerText = 'Puntuación: Pendiente';
  document.getElementById('trainPuntajeBadge').style.color = '#94a3b8';
  document.getElementById('trainFeedbackBox').style.display = 'none';
}

// =============================================================================
// HERRAMIENTA 4: BANCO MAESTRO DE 25 PREGUNTAS TRAMPA TEÓRICAS (QUIZ UAGRM)
// =============================================================================
const quizMasterQuestions = [
  // 1-6 DELPHI & SINTAXIS
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Por qué en Delphi una variable tipo String se indexa a partir de 1 y no de 0?",
    options: [
      "Porque en la arquitectura histórica de Pascal (ShortString), la posición 0 almacena la longitud de la cadena como un Byte (ord(cad[0]) = Length(cad)).",
      "Porque Delphi fue programado en Visual Basic.",
      "Porque el índice 0 está reservado exclusivamente para números negativos.",
      "Es falso, en Delphi se empieza siempre en 0 como en C y Python."
    ],
    correct: 0,
    exp: "En Turbo Pascal y Delphi tradicional (ShortString), cad[0] contiene el byte de longitud (hasta 255 caracteres). Por ello, los caracteres reales van de 1 a N. El compilador en Windows preserva esta convención para no romper código histórico."
  },
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Qué diferencia existe entre pasar un parámetro por VALOR vs por REFERENCIA (con palabra reservada 'var')?",
    options: [
      "Por valor es más rápido y por referencia ocupa toda la memoria RAM.",
      "Por valor se envía una copia local independiente; por referencia (var) se pasa la dirección de memoria real y cualquier cambio afecta a la variable original fuera del módulo.",
      "Por referencia no se permiten tipos numéricos.",
      "No hay diferencia, 'var' solo se usa para adornar la firma del procedimiento."
    ],
    correct: 1,
    exp: "Al usar 'var', el módulo recibe un puntero a la variable original del llamador (Caller). Es indispensable cuando un procedimiento debe retornar uno o múltiples valores modificados."
  },
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Por qué el tipo conjunto 'set of char' en Delphi solo admite hasta 256 elementos?",
    options: [
      "Porque se implementa internamente como un mapa de bits (bitmask) de 256 bits (32 Bytes), correspondiendo exactamente a la tabla ASCII estándar y extendida.",
      "Por una limitación del sistema operativo Windows de 32 bits.",
      "Porque la memoria caché no admite más de 256 números.",
      "Porque el alfabeto castellano solo tiene 256 letras."
    ],
    correct: 0,
    exp: "Un 'set' en Pascal es un bitset de 32 bytes (256 bits). La pertenencia 'ch in miSet' se evalúa en 1 ciclo de reloj de CPU con la instrucción assembly 'BT' (Bit Test), haciéndolo ultra veloz."
  },
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Cuál es la diferencia entre el operador 'div' y el operador '/' en Delphi?",
    options: [
      "'div' realiza división entera truncada retornando un Integer/Byte; '/' realiza división real de punto flotante retornando un tipo Real/Double.",
      "'div' divide por cero sin error y '/' lanza excepción.",
      "Son exactamente sinónimos intercambiables.",
      "'div' se usa para cadenas y '/' para enteros."
    ],
    correct: 0,
    exp: "Si intentas asignar 'n := n / 10;' a un entero, Delphi lanzará error de compilación: 'Incompatible types: Integer and Extended'. Siempre debe usarse 'div' para números naturales."
  },
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Por qué JAMÁS se coloca punto y coma (;) inmediatamente antes de la palabra 'else' en una estructura condicional?",
    options: [
      "Porque en la gramática BNF de Pascal el condicional completo 'if-then-else' es una sola sentencia compuesta; el punto y coma la daría por terminada antes de tiempo.",
      "Porque Delphi se confunde con el punto y coma de C++.",
      "Es mentira, sí se debe colocar punto y coma antes de else.",
      "Porque el teclado latino no lo permite."
    ],
    correct: 0,
    exp: "Poner ';' antes de else genera el error de compilación: '[Error] Statement expected, but ELSE found'. Es una de las trampas más cobradas en examen de pizarra."
  },
  {
    cat: "delphi",
    catLabel: "DELPHI & SINTAXIS",
    q: "¿Qué ocurre si una función no asigna ningún valor a 'Result' ni al nombre de la función antes de terminar?",
    options: [
      "El compilador da una advertencia (Warning: Return value may be undefined) y la función devuelve basura residual de los registros de CPU.",
      "El programa se apaga de inmediato.",
      "Retorna siempre una cadena vacía.",
      "El procesador se reinicia."
    ],
    correct: 0,
    exp: "En Delphi, 'Result' es una pseudo-variable local de retorno asignada al registro EAX. Si no la inicializas ni asignas, retornará lo que haya quedado en EAX en ese instante."
  },

  // 7-13 CADENAS
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "En la metodología de la Ing. Angélica Garzón, ¿cuáles son los 3 parámetros canónicos de una función de cadenas?",
    options: [
      "(cad: String; n, i: Byte) donde 'cad' es el texto, 'n' es Length(cad) e 'i' es el índice de control del recorrido.",
      "(cadena: PChar; puntero: Pointer; tam: Integer).",
      "(texto: String; bandera: Boolean; matriz: Array).",
      "(s: String) únicamente."
    ],
    correct: 0,
    exp: "La docente exige explícitamente recibir 'cad', 'n' e 'i' para verificar que el estudiante domine el recorrido posicional con bucle while i <= n."
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "Para recorrer una cadena buscando un carácter con salida anticipada (sin seguir buscando inútilmente), ¿cuál es la estructura correcta?",
    options: [
      "while (i <= n) and not encontrado do begin ... if cad[i] = car then encontrado := true; i := i + 1; end;",
      "for i := 1 to n do if cad[i] = car then break; (prohibido por la docente por mala práctica de modularidad).",
      "repeat until i = 1000;",
      "while true do begin cad := ''; end;"
    ],
    correct: 0,
    exp: "La docente enseña que las banderas booleanas 'encontrado' en la condición del while son la forma estructurada y limpia de detener el ciclo, sin usar instrucciones destructivas como 'break' o 'exit' dentro del for."
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "¿Qué devuelve la función Copy('Hola mundo', 6, 5) en Delphi?",
    options: [
      "'mundo'",
      "'Hola '",
      "'o'",
      "Error de índice."
    ],
    correct: 0,
    exp: "Copy(cad, index, count) extrae desde el índice 'index' la cantidad de caracteres 'count'. En 'Hola mundo', el índice 6 es la 'm', extrayendo 5 caracteres: 'mundo'."
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "Si la docente pide 'Invertir la segunda palabra de Hola mundo de Cadena', ¿cuál es la respuesta exacta?",
    options: [
      "'Hola odnum de Cadena'",
      "'Hola dmnou de Cadena'",
      "'anedaC ed odnum aloH'",
      "'Hola mundo de Cadena'"
    ],
    correct: 0,
    exp: "La segunda palabra es 'mundo'. Al invertirla de derecha a izquierda ('mundo' al revés) queda 'odnum'. ¡No confundir con ordenar ('dmnou')!"
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "Si la docente pide 'Ordenar alfabéticamente la segunda palabra de Hola mundo de Cadena', ¿cuál es la respuesta exacta?",
    options: [
      "'Hola dmnou de Cadena'",
      "'Hola odnum de Cadena'",
      "'Hola mundo de Cadena'",
      "'dmnou Hola de Cadena'"
    ],
    correct: 0,
    exp: "Las letras de 'mundo' son 'm', 'u', 'n', 'd', 'o'. Ordenadas alfabéticamente (A..Z): 'd' < 'm' < 'n' < 'o' < 'u' -> 'dmnou'."
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "¿Cómo se detecta que dos vocales contiguas están juntas en una cadena (ej: 'caoba')?",
    options: [
      "if (i < n) and (cad[i] in vocales) and (cad[i+1] in vocales) then ...",
      "if cad[i] = cad[i+1] then ...",
      "if Pos('aa', cad) > 0 then ...",
      "No se puede en Delphi."
    ],
    correct: 0,
    exp: "Se verifica que 'i < n' para que 'cad[i+1]' no desborde el final de la cadena, y se comprueba si ambos caracteres pertenecen al conjunto de vocales."
  },
  {
    cat: "cadenas",
    catLabel: "CADENAS & METODOLOGÍA",
    q: "¿Por qué se utiliza una bandera 'enPalabra: Boolean' para contar palabras en una cadena con espacios múltiples?",
    options: [
      "Porque evita contar espacios seguidos como palabras falsas (ej: 'Hola     mundo' tiene 2 palabras reales, no 6).",
      "Porque Delphi obliga a usar banderas en strings.",
      "Para que el código sea más largo.",
      "Porque los espacios no tienen código ASCII."
    ],
    correct: 0,
    exp: "Una palabra inicia cuando pasamos de un espacio a un no-espacio ('not enPalabra'). La bandera permite absorber múltiples espacios consecutivos sin incrementar erróneamente el contador."
  },

  // 14-19 ORDENAMIENTOS
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "En el algoritmo de Burbuja visto en la pizarra de la docente, ¿cuántas comparaciones se realizan exactamente para ordenar un vector de 5 elementos?",
    options: [
      "10 comparaciones (Fórmula: n*(n-1)/2 = 5*4/2 = 10).",
      "25 comparaciones.",
      "5 comparaciones.",
      "100 comparaciones."
    ],
    correct: 0,
    exp: "La pasada 1 hace 4 comparaciones, la pasada 2 hace 3, la 3 hace 2 y la 4 hace 1. Suma: 4+3+2+1 = 10 comparaciones."
  },
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "¿Cuáles son los 3 pasos estrictos del intercambio de valores (Swap) en la pizarra de la docente?",
    options: [
      "1) Aux := Cad[I];  2) Cad[I] := Cad[J];  3) Cad[J] := Aux;",
      "1) Cad[I] := Cad[J];  2) Cad[J] := Cad[I];",
      "1) Swap(Cad[I], Cad[J]);",
      "1) Delete(Cad, I, 1); 2) Insert(Cad, J, 1);"
    ],
    correct: 0,
    exp: "Primero se resguarda el primer elemento en Aux, luego se sobrescribe Cad[I] con Cad[J], y finalmente se deposita el valor guardado en Cad[J]."
  },
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "¿Cuál es la principal ventaja del método de Selección Directa frente a Burbuja?",
    options: [
      "Realiza exactamente O(n) intercambios (a lo sumo 1 intercambio por pasada), reduciendo escrituras en memoria.",
      "Tiene complejidad O(log n).",
      "No requiere bucles.",
      "Ordena sin comparar."
    ],
    correct: 0,
    exp: "Aunque ambos hacen O(n²) comparaciones, Selección busca el mínimo y hace a lo sumo N-1 intercambios en total, mientras Burbuja puede hacer hasta O(n²) intercambios."
  },
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "¿Por qué el algoritmo de Inserción Directa es el más recomendado para listas que ya están casi ordenadas?",
    options: [
      "Porque en el mejor caso solo realiza 1 comparación por elemento sin moverlo, logrando una complejidad casi lineal O(n).",
      "Porque usa recursividad de pila.",
      "Porque no usa variables auxiliares.",
      "Porque es el algoritmo creado por Alan Turing."
    ],
    correct: 0,
    exp: "Si el arreglo ya está ordenado, el bucle interior de inserción se detiene inmediatamente en la primera comparación, completando el proceso en tiempo O(n)."
  },
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "¿Qué concepto introdujo Donald Shell en el algoritmo 'Shell Sort' para mejorar la Inserción Directa?",
    options: [
      "Comparar elementos distantes mediante un intervalo decreciente (gap = n div 2) que se reduce a la mitad en cada fase.",
      "Particionar con un pivote central.",
      "Usar árboles binarios en disco duro.",
      "Ordenar primero los números pares y luego los impares."
    ],
    correct: 0,
    exp: "Shell Sort permite que elementos lejanos den 'grandes saltos' para acomodarse rápidamente cerca de su posición final, evitando los lentos desplazamientos paso a paso de la inserción simple."
  },
  {
    cat: "ordenamiento",
    catLabel: "MÉTODOS DE ORDENAMIENTO",
    q: "¿Cuál es el principio de diseño del algoritmo QuickSort (Ordenamiento Rápido)?",
    options: [
      "Divide y Vencerás: se elige un pivote, se particiona el vector (menores a la izquierda, mayores a la derecha) y se ordenan recursivamente los subvectores.",
      "Buscar el valor más grande y duplicarlo.",
      "Intercambiar aleatoriamente hasta que esté ordenado.",
      "Contar las frecuencias de cada carácter."
    ],
    correct: 0,
    exp: "Tony Hoare diseñó QuickSort bajo 'Divide y Vencerás'. Es el más utilizado en librerías estándar por su tiempo promedio O(n log n) y bajo consumo de memoria adicional."
  },

  // 20-25 MODULARIDAD & NÚMEROS
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "¿Cuándo es obligatorio implementar un módulo como PROCEDIMIENTO en lugar de FUNCIÓN?",
    options: [
      "Cuando el módulo debe devolver MÁS DE UN valor modificado al llamador (ej. mediante varios parámetros 'var') o cuando solo realiza una acción de interfaz gráfica sin retornar datos.",
      "Cuando se usan números mayores a 1000.",
      "Las funciones y procedimientos son idénticos y nunca hay diferencia obligatoria.",
      "Solo cuando el programa tiene formularios VCL."
    ],
    correct: 0,
    exp: "Una función formal solo puede retornar UN único valor mediante su tipo de resultado. Si requieres devolver 2, 3 o más variables modificadas (o modificar in-place una cadena sin crear nueva copia), se debe usar 'procedure ... (var a, b: Integer)'."
  },
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "En el examen de números naturales, ¿cómo se extrae el último dígito y cómo se elimina?",
    options: [
      "d := n mod 10; (extrae último dígito) y n := n div 10; (elimina el último dígito).",
      "d := n / 10; y n := n - 10;",
      "d := n * 10; y n := n + 10;",
      "d := StrToInt(n[1]);"
    ],
    correct: 0,
    exp: "'mod 10' obtiene el residuo en base 10 (último dígito). 'div 10' realiza el desplazamiento entero a la derecha, recortando ese dígito."
  },
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "¿Por qué un número de un solo dígito (ej: 0, 1, 2... 9) es Capicúa por definición?",
    options: [
      "Porque al tener una sola cifra, su lectura de izquierda a derecha y de derecha a izquierda es idéntica.",
      "Porque es divisible entre 1.",
      "Es falso, los números de 1 dígito no pueden ser capicúas.",
      "Porque es un número primo."
    ],
    correct: 0,
    exp: "Un número capicúa se lee igual al derecho y al revés. Cualquier dígito solitario cumple la definición trivialmente."
  },
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "¿Cuáles son los únicos 4 dígitos que pertenecen al conjunto de Dígitos Primos (0..9)?",
    options: [
      "[2, 3, 5, 7]",
      "[1, 3, 5, 7, 9]",
      "[2, 4, 6, 8]",
      "[0, 2, 3, 5]"
    ],
    correct: 0,
    exp: "El 0 y 1 NO son primos. El 4, 6, 8 y 9 son compuestos. Por tanto, los únicos dígitos primos en base 10 son: 2, 3, 5 y 7. ¡Pregunta clásica de la docente!"
  },
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "¿Qué sucede con las variables declaradas dentro de un módulo (locales) cuando el módulo termina su ejecución?",
    options: [
      "Se destruyen automáticamente liberando su espacio en el Stack (pila de memoria).",
      "Se guardan en el disco duro permanentemente.",
      "Se convierten en variables globales.",
      "Pasan a estar disponibles para el Formulario principal."
    ],
    correct: 0,
    exp: "Las variables locales tienen ámbito (scope) y tiempo de vida limitado a la ejecución del subprograma. Cuando llega al 'end;', el puntero del Stack retrocede y sus datos dejan de existir."
  },
  {
    cat: "modularidad",
    catLabel: "MODULARIDAD & NÚMEROS",
    q: "¿Por qué la docente prohíbe el uso de variables globales dentro de la lógica algorítmica de módulos reutilizables?",
    options: [
      "Porque rompen el principio de encapsulamiento e independencia modular, generando acoplamiento fuerte y efectos secundarios inesperados.",
      "Porque Delphi cobra licencia extra por usar variables globales.",
      "Porque hacen que el programa se ejecute al doble de velocidad.",
      "Porque no funcionan en Windows 11."
    ],
    correct: 0,
    exp: "La modularidad limpia exige que un módulo dependa únicamente de sus parámetros de entrada y salida, permitiendo probarlo, reutilizarlo y depurarlo sin depender del estado global de un Form."
  }
];

let quizFiltered = [...quizMasterQuestions];
let quizCurrentIdx = 0;
let quizUserScore = 0;
let quizAnswered = {};

function quizFiltrar(cat, btn) {
  document.querySelectorAll('#quizFilterButtons button').forEach(b => {
    b.style.background = '#1e293b';
    b.style.color = '#94a3b8';
  });
  if (btn) {
    btn.style.background = '#0284c7';
    btn.style.color = '#ffffff';
  }

  if (cat === 'todas') {
    quizFiltered = [...quizMasterQuestions];
  } else {
    quizFiltered = quizMasterQuestions.filter(q => q.cat === cat);
  }

  quizCurrentIdx = 0;
  quizRenderCurrent();
}

function quizRenderCurrent() {
  if (quizFiltered.length === 0) return;
  const q = quizFiltered[quizCurrentIdx];

  document.getElementById('quizBadgeCat').innerText = q.catLabel;
  document.getElementById('quizCounterText').innerText = 'Pregunta ' + (quizCurrentIdx + 1) + ' de ' + quizFiltered.length;
  document.getElementById('quizQuestionText').innerText = q.q;

  // Render opciones
  const container = document.getElementById('quizOptionsContainer');
  let html = '';
  const alreadyAnswered = quizAnswered.hasOwnProperty(q.q);

  q.options.forEach((opt, idx) => {
    let style = 'text-align: left; background: #0b1120; border: 1.5px solid #334155; color: #f8fafc; padding: 0.85rem 1.1rem; border-radius: 8px; font-size: 0.92rem; transition: all 0.2s; cursor: pointer;';
    
    if (alreadyAnswered) {
      if (idx === q.correct) {
        style = 'text-align: left; background: rgba(16, 185, 129, 0.25); border: 2px solid #10b981; color: #34d399; font-weight: bold; padding: 0.85rem 1.1rem; border-radius: 8px; font-size: 0.92rem;';
      } else if (idx === quizAnswered[q.q] && idx !== q.correct) {
        style = 'text-align: left; background: rgba(239, 68, 68, 0.25); border: 2px solid #ef4444; color: #f87171; padding: 0.85rem 1.1rem; border-radius: 8px; font-size: 0.92rem;';
      }
    }

    html += '<button class="delphi-btn-vcl quiz-opt-btn" id="qOptBtn-' + idx + '" onclick="quizElegirOpcion(' + idx + ')" style="' + style + '" ' + (alreadyAnswered ? 'disabled' : '') + '>' +
            '<strong style="color: #38bdf8; margin-right: 8px;">' + String.fromCharCode(65 + idx) + ')</strong> ' + htmlEscape(opt) +
            '</button>';
  });
  container.innerHTML = html;

  // Explicación
  const expBox = document.getElementById('quizExplanationBox');
  if (alreadyAnswered) {
    expBox.style.display = 'block';
    document.getElementById('quizExplanationText').innerHTML = q.exp;
  } else {
    expBox.style.display = 'none';
  }

  // Actualizar Score
  const totalResp = Object.keys(quizAnswered).length;
  document.getElementById('quizScoreText').innerText = quizUserScore + ' / ' + totalResp;
}

function quizElegirOpcion(chosenIdx) {
  const q = quizFiltered[quizCurrentIdx];
  if (quizAnswered.hasOwnProperty(q.q)) return;

  quizAnswered[q.q] = chosenIdx;
  const isCorrect = (chosenIdx === q.correct);
  if (isCorrect) quizUserScore++;

  quizRenderCurrent();
}

function quizSiguiente() {
  if (quizCurrentIdx < quizFiltered.length - 1) {
    quizCurrentIdx++;
    quizRenderCurrent();
  }
}

function quizAnterior() {
  if (quizCurrentIdx > 0) {
    quizCurrentIdx--;
    quizRenderCurrent();
  }
}

function quizReiniciar() {
  quizUserScore = 0;
  quizAnswered = {};
  quizCurrentIdx = 0;
  quizRenderCurrent();
}

