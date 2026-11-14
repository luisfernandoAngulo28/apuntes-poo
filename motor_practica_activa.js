
// =============================================================================
//      MOTOR DE PRÁCTICA ACTIVA: TRAZA EN VIVO, FLASHCARDS & EXAMEN UAGRM
// =============================================================================

// -----------------------------------------------------------------------------
// CONTROLADOR DE PESTAÑAS DEL MÓDULO (Sub-herramientas)
// -----------------------------------------------------------------------------
function switchToolActive(toolName, btn) {
  document.querySelectorAll('.tool-subpanel').forEach(p => p.style.display = 'none');
  const target = document.getElementById('toolSection-' + toolName);
  if (target) target.style.display = 'block';

  document.querySelectorAll('.active-herramienta').forEach(b => {
    b.classList.remove('active-herramienta');
    b.style.background = '#0f172a';
    b.style.color = '#cbd5e1';
  });

  btn.classList.add('active-herramienta');
  if (toolName === 'traza') {
    btn.style.background = '#10b981';
    btn.style.color = '#022c22';
  } else if (toolName === 'flashcards') {
    btn.style.background = '#0284c7';
    btn.style.color = '#ffffff';
  } else if (toolName === 'examen') {
    btn.style.background = '#f59e0b';
    btn.style.color = '#1e293b';
  } else if (toolName === 'entrenador') {
    btn.style.background = '#9333ea';
    btn.style.color = '#ffffff';
    if (typeof trainCargarEjercicio === 'function') trainCargarEjercicio();
  }
}

// =============================================================================
// 1. SIMULADOR DE TRAZA Y ANIMADOR DE MEMORIA EN VIVO
// =============================================================================

let animState = {
  alg: 'vocales',
  cad: 'hola mundo',
  extra: 'o',
  n: 10,
  i: 1,
  stepCount: 0,
  running: false,
  timer: null,
  vars: {},
  rows: [],
  completed: false,
  numVal: 12593
};

const ES_VOCAL_CHAR = (c) => ['A','E','I','O','U','Á','É','Í','Ó','Ú'].includes(c.toUpperCase());

function animCambiarAlgoritmo() {
  const sel = document.getElementById('animAlgSelect').value;
  animState.alg = sel;
  const extraCol = document.getElementById('animExtraCol');
  const inputLabel = document.getElementById('animInputLabel');
  const inputCad = document.getElementById('animInputCad');

  if (sel === 'buscarLetra') {
    extraCol.style.display = 'block';
  } else {
    extraCol.style.display = 'none';
  }

    if (sel === 'burbujaAsc') {
    inputLabel.innerText = 'Vector o Cadena a Ordenar:';
    inputCad.value = '45123';
  } else if (sel === 'numDigitos') {
    inputLabel.innerText = 'Número Natural (n):';
    inputCad.value = '12593';
  } else {
    inputLabel.innerText = 'Cadena de Entrada (cad):';
    if (inputCad.value === '12593') inputCad.value = 'hola mundo';
  }

  animReset();
}

function animReset() {
  if (animState.timer) {
    clearInterval(animState.timer);
    animState.timer = null;
  }
  animState.running = false;
  animState.completed = false;
  animState.stepCount = 0;
  animState.rows = [];

  const btnAuto = document.getElementById('btnAnimAuto');
  if (btnAuto) {
    btnAuto.innerText = '▶ Auto Ejecutar';
    btnAuto.style.background = '#0284c7';
  }

  const inp = document.getElementById('animInputCad').value || '';
  animState.cad = inp;
  animState.extra = (document.getElementById('animInputExtra').value || 'o')[0] || 'o';

  if (animState.alg === 'burbujaAsc') {
    animState.n = inp.length;
    animState.chars = inp.split('');
    animState.i = 1;
    animState.j = 2;
    animState.vars = { cad: inp, n: animState.n, i: 1, j: 2, 'cad[i]': "'" + (animState.chars[0] || '') + "'", 'cad[j]': "'" + (animState.chars[1] || '') + "'", aux: '-', '¿cad[i] > cad[j]?': '-' };
    document.getElementById('animTapeStatus').innerText = 'Vector longitud n = ' + animState.n;
  } else if (animState.alg === 'numDigitos') {
    animState.numVal = parseInt(inp, 10) || 0;
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { n: animState.numVal, dig: '-', '¿Es Primo?': '-', sumaPrimos: 0 };
    document.getElementById('animTapeStatus').innerText = 'Número: ' + animState.numVal;
  } else if (animState.alg === 'invertir') {
    animState.n = inp.length;
    animState.i = animState.n;
    animState.vars = { cad: inp, n: animState.n, i: animState.i, 'cad[i]': '-', res: "''" };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  } else if (animState.alg === 'contarPalabras') {
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { cad: inp, n: animState.n, i: 1, 'cad[i]': '-', enPalabra: false, cantPal: 0 };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  } else if (animState.alg === 'elimEspacios') {
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { cad: inp, n: animState.n, i: 1, 'cad[i]': '-', res: "''" };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  } else if (animState.alg === 'buscarLetra') {
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { cad: inp, n: animState.n, i: 1, buscarcar: "'" + animState.extra + "'", 'cad[i]': '-', posicion: 0, encontrado: false };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  } else if (animState.alg === 'paresVocales') {
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { cad: inp, n: animState.n, i: 1, 'cad[i..i+1]': '-', paresVocales: 0 };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  } else {
    // vocales
    animState.n = inp.length;
    animState.i = 1;
    animState.vars = { cad: inp, n: animState.n, i: 1, 'cad[i]': '-', '¿Es Vocal?': '-', contador: 0 };
    document.getElementById('animTapeStatus').innerText = 'Longitud n = ' + animState.n;
  }

  // Actualizar UI
  document.getElementById('animPasoCounter').innerText = 'Paso: 0';
  document.getElementById('animCondText').innerText = 'Inicialización: variables en memoria cargadas.';
  document.getElementById('animStepExplanation').innerHTML = 'Variables registradas. Presiona <strong>«Paso Siguiente»</strong> para evaluar la primera iteración.';
  
  animRenderTape(0);
  animRenderVars();
  animRenderTableHead();
  animRenderTableBody();
}

function animRenderTape(activeIdx, matchIdx) {
  const container = document.getElementById('animTapeContainer');
  if (!container) return;
  container.innerHTML = '';
  
  const text = (animState.alg === 'numDigitos') ? String(animState.numVal) : animState.cad;
  if (!text) {
    container.innerHTML = '<div style="color: #64748b; padding: 1rem;">Cinta de memoria vacía.</div>';
    return;
  }

  for (let idx = 1; idx <= text.length; idx++) {
    const ch = text[idx - 1];
    const cell = document.createElement('div');
    const isActive = (idx === activeIdx);
    const isMatch = (idx === matchIdx);

    cell.className = 'tape-cell' + (isActive ? ' active' : '') + (isMatch ? ' match' : '');
    cell.id = 'tapeCell-' + idx;

    let borderCol = isActive ? '#10b981' : (isMatch ? '#f59e0b' : '#334155');
    let bgCol = isActive ? 'rgba(16, 185, 129, 0.22)' : (isMatch ? 'rgba(245, 158, 11, 0.25)' : '#0f172a');
    let shadow = isActive ? '0 0 16px rgba(16, 185, 129, 0.6)' : '0 2px 5px rgba(0,0,0,0.4)';
    let transform = isActive ? 'transform: translateY(-6px);' : '';

    cell.style.cssText = 'flex: 0 0 58px; min-width: 58px; height: 74px; background: ' + bgCol + '; border: 2px solid ' + borderCol + '; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 6px 4px; position: relative; user-select: none; box-shadow: ' + shadow + '; transition: all 0.25s ease; ' + transform;

    if (isActive) {
      cell.innerHTML = '<div class="tape-pointer-arrow" style="position: absolute; top: -24px; left: 50%; transform: translateX(-50%); color: #10b981; font-size: 0.8rem; font-weight: 900; white-space: nowrap; background: #022c22; border: 1px solid #10b981; padding: 1px 6px; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.5);">▼ i=' + idx + '</div>';
    } else {
      cell.innerHTML = '';
    }

    const displayChar = (ch === ' ') ? '␣' : ch;
    const idxColor = isActive ? '#34d399' : '#94a3b8';
    const charColor = isActive ? '#34d399' : (isMatch ? '#fbbf24' : '#f8fafc');
    const badgeBg = isActive ? '#065f46' : '#1e293b';
    const badgeColor = isActive ? '#a7f3d0' : '#cbd5e1';

    cell.innerHTML += '<span class="tape-idx" style="font-size: 0.72rem; color: ' + idxColor + '; font-weight: 700; font-family: \'Fira Code\', monospace;">[' + idx + ']</span>' +
                      '<span class="tape-char" style="font-size: 1.45rem; font-weight: 900; color: ' + charColor + '; font-family: \'Fira Code\', monospace; line-height: 1;">' + displayChar + '</span>' +
                      '<span class="tape-badge" style="font-size: 0.62rem; font-weight: 800; padding: 2px 5px; border-radius: 3px; background: ' + badgeBg + '; color: ' + badgeColor + '; letter-spacing: 0.5px;">' + (ch === ' ' ? 'ESP' : 'CHAR') + '</span>';

    container.appendChild(cell);
  }

  if (activeIdx > 0) {
    const activeElem = document.getElementById('tapeCell-' + activeIdx);
    if (activeElem) {
      activeElem.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }
  }
}

function animRenderVars() {
  const grid = document.getElementById('animVarsGrid');
  if (!grid) return;
  grid.innerHTML = '';

  for (let key in animState.vars) {
    const card = document.createElement('div');
    card.className = 'var-ram-card';
    card.style.cssText = 'background: #0f172a; border: 1.5px solid #334155; border-radius: 6px; padding: 0.55rem 0.85rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3);';

    let val = animState.vars[key];
    let valStr = String(val);
    let isBoolTrue = (val === true || val === 'true');
    let isBoolFalse = (val === false || val === 'false');
    
    let valColor = '#38bdf8';
    let valBg = '#070a13';
    let valBorder = '#1e293b';

    if (isBoolTrue) {
      valColor = '#34d399';
      valBg = 'rgba(16, 185, 129, 0.15)';
      valBorder = '#059669';
    } else if (isBoolFalse) {
      valColor = '#f87171';
      valBg = 'rgba(239, 68, 68, 0.15)';
      valBorder = '#dc2626';
    }

    card.innerHTML = '<span class="var-ram-name" style="font-family: \'Fira Code\', monospace; font-size: 0.82rem; font-weight: 700; color: #94a3b8; margin-right: 0.5rem;">' + key + ':</span>' +
                     '<span class="var-ram-val" id="varVal-' + key + '" style="font-family: \'Fira Code\', monospace; font-size: 0.95rem; font-weight: 800; color: ' + valColor + '; background: ' + valBg + '; padding: 2px 8px; border-radius: 4px; border: 1px solid ' + valBorder + '; min-width: 28px; text-align: center;">' + valStr + '</span>';
    grid.appendChild(card);
  }
}

function animRenderTableHead() {
  const thead = document.getElementById('animTrazaThead');
  if (animState.alg === 'burbujaAsc') {
    thead.innerHTML = '<tr><th>Paso</th><th>I</th><th>J</th><th>¿Cad[I] &gt; Cad[J]?</th><th>Aux</th><th>Cadena / Vector</th><th>Acción</th></tr>';
  } else if (animState.alg === 'vocales') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>i &lt;= n</th><th>cad[i]</th><th>¿cad[i] in voc?</th><th>contador</th><th>i := i + 1</th></tr>';
  } else if (animState.alg === 'elimEspacios') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>i &lt;= n</th><th>cad[i]</th><th>¿cad[i] &lt;&gt; \' \'?</th><th>res</th><th>i := i + 1</th></tr>';
  } else if (animState.alg === 'contarPalabras') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>i &lt;= n</th><th>cad[i]</th><th>enPalabra</th><th>cantPal</th><th>i := i + 1</th></tr>';
  } else if (animState.alg === 'invertir') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>i &gt;= 1</th><th>cad[i]</th><th>res := res + cad[i]</th><th>i := i - 1</th></tr>';
  } else if (animState.alg === 'buscarLetra') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>Condición</th><th>cad[i]</th><th>buscarcar</th><th>posicion</th><th>encontrado</th></tr>';
  } else if (animState.alg === 'paresVocales') {
    thead.innerHTML = '<tr><th>Paso</th><th>i</th><th>cad[i]</th><th>cad[i+1]</th><th>¿Ambas Vocales?</th><th>paresVocales</th><th>i := i + 1</th></tr>';
  } else if (animState.alg === 'numDigitos') {
    thead.innerHTML = '<tr><th>Paso</th><th>n</th><th>n &gt; 0</th><th>dig := n mod 10</th><th>¿dig in Primos?</th><th>sumaPrimos</th><th>n := n div 10</th></tr>';
  }
}

function animRenderTableBody() {
  const tbody = document.getElementById('animTrazaTbody');
  if (animState.rows.length === 0) {
    tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: #64748b; padding: 1.5rem;">Presiona «Paso Siguiente» para construir la traza.</td></tr>';
    return;
  }
  let html = '';
  animState.rows.forEach(r => {
    html += '<tr>';
    r.forEach(col => {
      html += '<td>' + col + '</td>';
    });
    html += '</tr>';
  });
  tbody.innerHTML = html;
}

function animPasoSiguiente() {
  if (animState.completed) {
    if (typeof showMobileToast === 'function') {
      showMobileToast('El algoritmo ya ha finalizado su ejecución.');
    }
    return;
  }

  animState.stepCount++;
  document.getElementById('animPasoCounter').innerText = 'Paso: ' + animState.stepCount;

  const alg = animState.alg;
  const cad = animState.cad;
  const n = animState.n;

  if (alg === 'vocales') {
    if (animState.i <= n) {
      const idx = animState.i;
      const ch = cad[idx - 1];
      const isVocal = ES_VOCAL_CHAR(ch);

      if (isVocal) {
        animState.vars.contador++;
      }
      animState.vars.i = idx;
      animState.vars['cad[i]'] = "'" + ch + "'";
      animState.vars['¿Es Vocal?'] = isVocal ? 'VERDADERO' : 'FALSO';

      animRenderTape(idx, isVocal ? idx : null);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        '<span style="color:#34d399;">i &lt;= n (' + idx + ' &lt;= ' + n + ')</span> &rarr; ' +
        'cad[' + idx + '] = \'' + ch + '\' &rarr; ' +
        (isVocal ? '<strong style="color:#34d399;">ES VOCAL &rarr; contador = ' + animState.vars.contador + '</strong>' : '<span style="color:#f87171;">NO ES VOCAL</span>');

      document.getElementById('animStepExplanation').innerHTML = 
        'Posición <strong>' + idx + '</strong>: Carácter <code>\'' + ch + '\'</code>. ' +
        (isVocal ? 'Es vocal, se incrementa <code>contador := contador + 1</code>. Luego <code>i := ' + (idx + 1) + '</code>.' : 'No es vocal, el contador no cambia. Luego <code>i := ' + (idx + 1) + '</code>.');

      animState.rows.push([
        animState.stepCount,
        idx,
        'Verdadero (' + idx + ' &le; ' + n + ')',
        "'" + ch + "'",
        isVocal ? 'SÍ (contador=' + animState.vars.contador + ')' : 'NO',
        animState.vars.contador,
        idx + 1
      ]);
      animRenderTableBody();

      animState.i++;
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = 
        '<span style="color:#f87171;">i &lt;= n (' + animState.i + ' &lt;= ' + n + ') &rarr; FALSO. Fin del bucle while.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Algoritmo completado:</strong> Retorna <code>Result := ' + animState.vars.contador + '</code>.';
      animState.rows.push([
        animState.stepCount,
        animState.i,
        'FALSO (' + animState.i + ' > ' + n + ')',
        '-',
        '-',
        animState.vars.contador,
        'Retorna ' + animState.vars.contador
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'elimEspacios') {
    if (animState.i <= n) {
      const idx = animState.i;
      const ch = cad[idx - 1];
      const noEsEspacio = (ch !== ' ');

      if (noEsEspacio) {
        if (animState.vars.res === "''") animState.vars.res = "'" + ch + "'";
        else animState.vars.res = "'" + animState.vars.res.replace(/'/g, '') + ch + "'";
      }
      animState.vars.i = idx;
      animState.vars['cad[i]'] = (ch === ' ') ? "'␣'" : "'" + ch + "'";

      animRenderTape(idx, noEsEspacio ? idx : null);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        'cad[' + idx + '] &lt;&gt; \' \' &rarr; ' +
        (noEsEspacio ? '<strong style="color:#34d399;">SÍ, se añade \'' + ch + '\' a res</strong>' : '<span style="color:#f87171;">NO, es espacio (se omite)</span>');

      document.getElementById('animStepExplanation').innerHTML = 
        'Posición <strong>' + idx + '</strong>: Carácter <code>\'' + ch + '\'</code>. ' +
        (noEsEspacio ? 'No es espacio, se concatena al acumulador <code>res</code>.' : 'Es espacio, se ignora.');

      animState.rows.push([
        animState.stepCount,
        idx,
        'Verdadero (' + idx + ' &le; ' + n + ')',
        (ch === ' ') ? "'␣'" : "'" + ch + "'",
        noEsEspacio ? 'SÍ' : 'NO (espacio)',
        animState.vars.res,
        idx + 1
      ]);
      animRenderTableBody();

      animState.i++;
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = 
        '<span style="color:#f87171;">i &lt;= n (' + animState.i + ' &gt; ' + n + ') &rarr; FALSO. Fin.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Resultado final:</strong> Retorna <code>Result := ' + animState.vars.res + '</code>.';
      animState.rows.push([
        animState.stepCount, animState.i, 'FALSO', '-', '-', animState.vars.res, 'Retorna ' + animState.vars.res
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'contarPalabras') {
    if (animState.i <= n) {
      const idx = animState.i;
      const ch = cad[idx - 1];
      const noEsEspacio = (ch !== ' ');

      if (noEsEspacio) {
        if (!animState.vars.enPalabra) {
          animState.vars.cantPal++;
          animState.vars.enPalabra = true;
        }
      } else {
        animState.vars.enPalabra = false;
      }

      animState.vars.i = idx;
      animState.vars['cad[i]'] = (ch === ' ') ? "'␣'" : "'" + ch + "'";

      animRenderTape(idx, noEsEspacio ? idx : null);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        'cad[' + idx + '] = \'' + ch + '\' &rarr; enPalabra = ' + animState.vars.enPalabra + ' &rarr; cantPal = ' + animState.vars.cantPal;

      animState.rows.push([
        animState.stepCount,
        idx,
        'Verdadero',
        (ch === ' ') ? "'␣'" : "'" + ch + "'",
        animState.vars.enPalabra ? 'TRUE' : 'FALSE',
        animState.vars.cantPal,
        idx + 1
      ]);
      animRenderTableBody();

      animState.i++;
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = '<span style="color:#f87171;">Fin del recorrido.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Total de palabras:</strong> <code>Result := ' + animState.vars.cantPal + '</code>.';
      animState.rows.push([
        animState.stepCount, animState.i, 'FALSO', '-', animState.vars.enPalabra ? 'TRUE' : 'FALSE', animState.vars.cantPal, 'Retorna ' + animState.vars.cantPal
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'invertir') {
    if (animState.i >= 1) {
      const idx = animState.i;
      const ch = cad[idx - 1];

      if (animState.vars.res === "''") animState.vars.res = "'" + ch + "'";
      else animState.vars.res = "'" + animState.vars.res.replace(/'/g, '') + ch + "'";

      animState.vars.i = idx;
      animState.vars['cad[i]'] = "'" + ch + "'";

      animRenderTape(idx, idx);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        'i &gt;= 1 (' + idx + ' &ge; 1) &rarr; concatena \'' + ch + '\' a res';

      animState.rows.push([
        animState.stepCount,
        idx,
        'Verdadero (' + idx + ' &ge; 1)',
        "'" + ch + "'",
        animState.vars.res,
        idx - 1
      ]);
      animRenderTableBody();

      animState.i--;
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = '<span style="color:#f87171;">i = 0 &lt; 1 &rarr; Fin del bucle.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Cadena Invertida:</strong> <code>Result := ' + animState.vars.res + '</code>.';
      animState.rows.push([
        animState.stepCount, 0, 'FALSO (0 < 1)', '-', animState.vars.res, 'Retorna ' + animState.vars.res
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'buscarLetra') {
    if (animState.i <= n && !animState.vars.encontrado) {
      const idx = animState.i;
      const ch = cad[idx - 1];
      const match = (ch.toUpperCase() === animState.extra.toUpperCase());

      if (match) {
        animState.vars.posicion = idx;
        animState.vars.encontrado = true;
      }
      animState.vars.i = idx;
      animState.vars['cad[i]'] = "'" + ch + "'";

      animRenderTape(idx, match ? idx : null);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        '¿cad[' + idx + '] (\'' + ch + '\') = \'' + animState.extra + '\'? &rarr; ' +
        (match ? '<strong style="color:#34d399;">COINCIDENCIA ENCONTRADA EN POSICIÓN ' + idx + '</strong>' : '<span style="color:#94a3b8;">NO COINCIDE</span>');

      animState.rows.push([
        animState.stepCount,
        idx,
        '(i &le; n) Y (encontrado=F)',
        "'" + ch + "'",
        "'" + animState.extra + "'",
        animState.vars.posicion,
        animState.vars.encontrado ? 'TRUE (Exit)' : 'FALSE'
      ]);
      animRenderTableBody();

      animState.i++;
      if (match) {
        animState.completed = true;
        document.getElementById('animStepExplanation').innerHTML = 
          '🎯 <strong>¡Encontrado!</strong> Se activa salida anticipada: <code>Result := ' + idx + '</code>.';
        if (animState.timer) animToggleAuto();
      }
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = '<span style="color:#f87171;">Bucle terminado.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        'Resultado: <code>Result := ' + animState.vars.posicion + '</code> (0 si no se encontró).';
      animState.rows.push([
        animState.stepCount, animState.i, 'FALSO', '-', "'" + animState.extra + "'", animState.vars.posicion, animState.vars.encontrado ? 'TRUE' : 'FALSE'
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'paresVocales') {
    if (animState.i <= n) {
      const idx = animState.i;
      const ch1 = cad[idx - 1];
      const ch2 = (idx < n) ? cad[idx] : '';
      const ambasVocales = (idx < n) && ES_VOCAL_CHAR(ch1) && ES_VOCAL_CHAR(ch2);

      if (ambasVocales) {
        animState.vars.paresVocales++;
      }
      animState.vars.i = idx;
      animState.vars['cad[i..i+1]'] = "'" + ch1 + (ch2 || '') + "'";

      animRenderTape(idx, ambasVocales ? idx : null);
      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        'Par: \'' + ch1 + (ch2 || '') + '\' &rarr; ' +
        (ambasVocales ? '<strong style="color:#34d399;">2 VOCALES JUNTAS &rarr; Total: ' + animState.vars.paresVocales + '</strong>' : '<span style="color:#94a3b8;">No son vocales juntas</span>');

      animState.rows.push([
        animState.stepCount,
        idx,
        "'" + ch1 + "'",
        ch2 ? "'" + ch2 + "'" : '-',
        ambasVocales ? 'SÍ (+1)' : 'NO',
        animState.vars.paresVocales,
        idx + 1
      ]);
      animRenderTableBody();

      animState.i++;
    } else {
      animState.completed = true;
      animRenderTape(0);
      document.getElementById('animCondText').innerHTML = '<span style="color:#f87171;">Fin del bucle.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Total pares de vocales juntas:</strong> <code>Result := ' + animState.vars.paresVocales + '</code>.';
      animState.rows.push([
        animState.stepCount, animState.i, '-', '-', '-', animState.vars.paresVocales, 'Fin -> ' + animState.vars.paresVocales
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  } else if (alg === 'numDigitos') {
    if (animState.vars.n > 0) {
      const numActual = animState.vars.n;
      const dig = numActual % 10;
      const esPrimo = [2, 3, 5, 7].includes(dig);

      if (esPrimo) {
        animState.vars.sumaPrimos += dig;
      }
      const nuevoN = Math.floor(numActual / 10);
      animState.vars.dig = dig;
      animState.vars['¿Es Primo?'] = esPrimo ? 'SÍ (' + dig + ')' : 'NO';

      animRenderVars();

      document.getElementById('animCondText').innerHTML = 
        'n = ' + numActual + ' &rarr; dig := n mod 10 = ' + dig + ' &rarr; ' +
        (esPrimo ? '<strong style="color:#34d399;">ES PRIMO &rarr; Suma = ' + animState.vars.sumaPrimos + '</strong>' : '<span style="color:#94a3b8;">No primo</span>');

      document.getElementById('animStepExplanation').innerHTML = 
        'Dígito extraído: <strong>' + dig + '</strong>. ' +
        (esPrimo ? 'Es primo, se suma a <code>sumaPrimos</code>.' : 'No es primo.') +
        ' Luego <code>n := n div 10 = ' + nuevoN + '</code>.';

      animState.rows.push([
        animState.stepCount,
        numActual,
        'Verdadero (' + numActual + ' > 0)',
        dig,
        esPrimo ? 'SÍ (' + dig + ')' : 'NO',
        animState.vars.sumaPrimos,
        nuevoN
      ]);
      animRenderTableBody();

      animState.vars.n = nuevoN;
    } else {
      animState.completed = true;
      document.getElementById('animCondText').innerHTML = '<span style="color:#f87171;">n = 0 &rarr; n &gt; 0 es FALSO. Fin.</span>';
      document.getElementById('animStepExplanation').innerHTML = 
        '✅ <strong>Resultado final:</strong> Suma de dígitos primos = <code>Result := ' + animState.vars.sumaPrimos + '</code>.';
      animState.rows.push([
        animState.stepCount, 0, 'FALSO (0 > 0)', '-', '-', animState.vars.sumaPrimos, 'Retorna ' + animState.vars.sumaPrimos
      ]);
      animRenderTableBody();
      if (animState.timer) animToggleAuto();
    }
  }
}

function animToggleAuto() {
  const btn = document.getElementById('btnAnimAuto');
  if (animState.running) {
    clearInterval(animState.timer);
    animState.timer = null;
    animState.running = false;
    btn.innerText = '▶ Auto Ejecutar';
    btn.style.background = '#0284c7';
    btn.style.color = '#f0fdf4';
  } else {
    if (animState.completed) animReset();
    animState.running = true;
    btn.innerText = '⏸ Pausar';
    btn.style.background = '#eab308';
    btn.style.color = '#422006';

    const speed = parseInt(document.getElementById('animSpeedSelect').value, 10) || 600;
    animState.timer = setInterval(() => {
      animPasoSiguiente();
    }, speed);
  }
}

function animLimpiarTabla() {
  animState.rows = [];
  animRenderTableBody();
}

function animCopiarTabla() {
  const table = document.getElementById('animTrazaTable');
  let text = '';
  for (let r of table.rows) {
    let rowText = [];
    for (let c of r.cells) {
      rowText.push(c.innerText.trim());
    }
    text += rowText.join('\t') + '\n';
  }
  navigator.clipboard.writeText(text).then(() => {
    if (typeof showMobileToast === 'function') {
      showMobileToast('Tabla de traza copiada al portapapeles');
    } else {
      alert('Tabla copiada al portapapeles.');
    }
  });
}

// =============================================================================
// 2. FLASHCARDS DE REPASO RÁPIDO (ANKI PARA MÓVIL)
// =============================================================================

const FLASHCARDS_DATA = [
  {
    id: 1,
    cat: 'ascii',
    pregunta: "¿Cuál es el código ASCII del espacio en blanco ' '?",
    respuesta: "ASCII 32 (en Pascal: #32)",
    detalle: "Se evalúa con `cad[i] = ' '` o `Ord(cad[i]) = 32`. Es el delimitador universal de palabras."
  },
  {
    id: 2,
    cat: 'ascii',
    pregunta: "¿Cuál es el rango de códigos ASCII para los dígitos numéricos '0'..'9'?",
    respuesta: "De 48 a 57 ('0' = 48, '9' = 57)",
    detalle: "Para convertir un carácter numérico a número entero: `val := Ord(cad[i]) - 48;`."
  },
  {
    id: 3,
    cat: 'ascii',
    pregunta: "¿Cuáles son los códigos ASCII de las letras mayúsculas 'A'..'Z'?",
    respuesta: "De 65 a 90 ('A' = 65, 'Z' = 90)",
    detalle: "En conjuntos Pascal: `const may: set of char = ['A'..'Z'];`."
  },
  {
    id: 4,
    cat: 'ascii',
    pregunta: "¿Cuáles son los códigos ASCII de las letras minúsculas 'a'..'z'?",
    respuesta: "De 97 a 122 ('a' = 97, 'z' = 122)",
    detalle: "La diferencia con las mayúsculas es exactamente 32: `Ord('a') - Ord('A') = 32`."
  },
  {
    id: 5,
    cat: 'ascii',
    pregunta: "¿Cómo convertir una letra minúscula 'c' a mayúscula usando funciones aritméticas ASCII?",
    respuesta: "Chr(Ord(c) - 32)",
    detalle: "Si `c = 'b'` (98), `98 - 32 = 66`, que equivale al carácter `'B' = Chr(66)`."
  },
  {
    id: 6,
    cat: 'sintaxis',
    pregunta: "¿En qué índice inician las cadenas (String) en Delphi y Free Pascal?",
    respuesta: "En el índice 1 (Base 1)",
    detalle: "En Pascal el primer carácter es `cad[1]` y el último es `cad[Length(cad)]`. `cad[0]` almacena la longitud en shortstring antigua."
  },
  {
    id: 7,
    cat: 'sintaxis',
    pregunta: "¿Qué valores almacena el tipo de dato Byte y cuánta memoria ocupa?",
    respuesta: "De 0 a 255 (Entero sin signo de 1 Byte)",
    detalle: "La docente exige `n, i: Byte` porque las cadenas en sus ejercicios no superan 255 caracteres."
  },
  {
    id: 8,
    cat: 'sintaxis',
    pregunta: "¿Qué diferencia existe entre los operadores div y / en Pascal?",
    respuesta: "div = división entera; / = división real",
    detalle: "`10 div 3 = 3` (retorna Integer); `10 / 3 = 3.3333` (retorna Real/Double)."
  },
  {
    id: 9,
    cat: 'sintaxis',
    pregunta: "¿Cómo se define un conjunto constante de caracteres (set of char)?",
    respuesta: "const voc: set of char = ['A','E','I','O','U'];",
    detalle: "Se evalúa pertenencia con el operador `in`: `if cad[i] in voc then ...`."
  },
  {
    id: 10,
    cat: 'modular',
    pregunta: "¿Cuál es la diferencia fundamental entre una Función y un Procedimiento?",
    respuesta: "La Función retorna un único valor por su nombre; el Procedimiento ejecuta una acción.",
    detalle: "La función se invoca como expresión (`x := f(a);`), mientras que el procedimiento se invoca como instrucción (`p(a);`)."
  },
  {
    id: 11,
    cat: 'modular',
    pregunta: "¿Cómo retorna su valor una función en Delphi?",
    respuesta: "Asignando a 'Result := valor;' o 'NombreFuncion := valor;'",
    detalle: "En Delphi moderno se prefiere siempre `Result := ...;`."
  },
  {
    id: 12,
    cat: 'modular',
    pregunta: "¿Qué diferencia hay entre parámetro por Valor y parámetro por Referencia (var)?",
    respuesta: "Valor recibe una copia; var recibe la dirección de memoria de la variable original.",
    detalle: "Modificar un parámetro `var` altera la variable fuera del subprograma. Por valor no produce efecto secundario."
  },
  {
    id: 13,
    cat: 'trampas',
    pregunta: "¿Por qué la docente M.Sc. Angélica Garzón prohíbe el uso de ciclos for en cadenas?",
    respuesta: "Porque el for no permite saltos variables de índice requeridos al descomponer palabras.",
    detalle: "La docente exige estrictamente: `i := 1; while i <= n do begin ... i := i + 1; end;`."
  },
  {
    id: 14,
    cat: 'trampas',
    pregunta: "¿Qué error grave ocurre si olvidas escribir 'i := i + 1;' dentro del ciclo while?",
    respuesta: "Bucle infinito (el programa se congela y saca 0 en el examen)",
    detalle: "El índice `i` nunca alcanzará a `n`, consumiendo el 100% de CPU hasta que se cierre el proceso."
  },
  {
    id: 15,
    cat: 'trampas',
    pregunta: "¿Qué ocurre si intentas acceder a cad[n + 1] en tiempo de ejecución?",
    respuesta: "Error de desbordamiento (Range Check Error / Access Violation)",
    detalle: "Siempre valida `(i <= n)` antes de acceder a `cad[i]` o `cad[i + 1]`."
  },
  {
    id: 16,
    cat: 'sintaxis',
    pregunta: "¿Qué retorna la función Pos(subcad, cad) si la subcadena no existe?",
    respuesta: "Retorna 0",
    detalle: "Si existe, retorna el índice `1..n` de su primera aparición. Ejemplo: `Pos('z', 'hola') = 0`."
  },
  {
    id: 17,
    cat: 'sintaxis',
    pregunta: "¿Qué hace la función Copy(cad, inicio, cantidad)?",
    respuesta: "Extrae una subcadena a partir de 'inicio' con longitud 'cantidad'",
    detalle: "`Copy('Programacion', 1, 8)` retorna `'Programa'`."
  },
  {
    id: 18,
    cat: 'sintaxis',
    pregunta: "¿Qué hace la función Trim(cad)?",
    respuesta: "Elimina todos los espacios en blanco iniciales y finales de la cadena.",
    detalle: "`Trim('  hola  ')` retorna `'hola'`. No elimina los espacios intermedios."
  },
  {
    id: 19,
    cat: 'algoritmos',
    pregunta: "¿Cómo se extrae el último dígito de un número natural n?",
    respuesta: "dig := n mod 10;",
    detalle: "Ejemplo: `1259 mod 10 = 9`."
  },
  {
    id: 20,
    cat: 'algoritmos',
    pregunta: "¿Cómo se elimina el último dígito de un número natural n?",
    respuesta: "n := n div 10;",
    detalle: "Ejemplo: `1259 div 10 = 125`."
  },
  {
    id: 21,
    cat: 'algoritmos',
    pregunta: "¿Qué es una cadena Palíndroma o Capicúa?",
    respuesta: "Una cadena que se lee exactamente igual de izquierda a derecha que de derecha a izquierda.",
    detalle: "Ejemplos: 'anilina', 'reconocer', 'radar'. Se verifica con dos punteros: `i := 1; j := n;`."
  },
  {
    id: 22,
    cat: 'modular',
    pregunta: "¿Qué variables globales utiliza la docente en el formulario Delphi TForm1?",
    respuesta: "cad: String; n, i: Byte;",
    detalle: "Donde `cad` guarda el texto, `n` la longitud de Length(cad), e `i` el índice auxiliar."
  },
  {
    id: 23,
    cat: 'modular',
    pregunta: "¿Qué hace el botón Button2Click en el formulario de la docente?",
    respuesta: "n := Length(cad); Edit2.Text := IntToStr(n) + ' caracteres'; Label6.Caption := 'n=' + IntToStr(n);",
    detalle: "Precalcula la longitud para pasar `n` como parámetro a todos los subprogramas."
  },
  {
    id: 24,
    cat: 'algoritmos',
    pregunta: "¿Cómo se intercambian dos caracteres cad[j] y cad[j+1] en ordenamiento burbuja?",
    respuesta: "aux := cad[j]; cad[j] := cad[j+1]; cad[j+1] := aux;",
    detalle: "Se requiere obligatoriamente una variable auxiliar `aux: Char` para no perder el valor."
  },
  {
    id: 25,
    cat: 'trampas',
    pregunta: "¿Por qué 'a' = 'A' es falso en Pascal y cómo resolverlo?",
    respuesta: "Porque 'a' tiene ASCII 97 y 'A' tiene ASCII 65; se debe normalizar con UpCase o LowerCase.",
    detalle: "Solución: `if UpCase(cad[i]) = UpCase(buscarcar) then ...`."
  }
];

let fcCurrentIndex = 0;
let fcFilteredCards = [...FLASHCARDS_DATA];
let fcFlipped = false;
let fcMastery = {};

try {
  const saved = localStorage.getItem('inf110_fc_mastery');
  if (saved) fcMastery = JSON.parse(saved);
} catch(e) {}

function fcActualizarVista() {
  if (fcFilteredCards.length === 0) return;
  const card = fcFilteredCards[fcCurrentIndex];

  document.getElementById('fcBadgeCat').innerText = card.cat.toUpperCase();
  document.getElementById('fcCounter').innerText = (fcCurrentIndex + 1) + ' de ' + fcFilteredCards.length;
  document.getElementById('fcPreguntaText').innerText = card.pregunta;
  document.getElementById('fcRespuestaText').innerText = card.respuesta;
  document.getElementById('fcDetalleText').innerHTML = card.detalle.replace(/`([^`]+)`/g, '<code>$1</code>');

  const inner = document.getElementById('fcCardInner');
  if (inner) inner.classList.remove('flipped');
  fcFlipped = false;

  fcActualizarProgreso();
}

function fcToggleFlip() {
  const inner = document.getElementById('fcCardInner');
  fcFlipped = !fcFlipped;
  if (inner) {
    if (fcFlipped) inner.classList.add('flipped');
    else inner.classList.remove('flipped');
  }
}

function fcSiguiente() {
  if (fcCurrentIndex < fcFilteredCards.length - 1) {
    fcCurrentIndex++;
  } else {
    fcCurrentIndex = 0;
  }
  fcActualizarVista();
}

function fcAnterior() {
  if (fcCurrentIndex > 0) {
    fcCurrentIndex--;
  } else {
    fcCurrentIndex = fcFilteredCards.length - 1;
  }
  fcActualizarVista();
}

function fcAleatorio() {
  fcCurrentIndex = Math.floor(Math.random() * fcFilteredCards.length);
  fcActualizarVista();
}

function fcEvaluar(nivel) {
  const card = fcFilteredCards[fcCurrentIndex];
  fcMastery[card.id] = nivel;
  try {
    localStorage.setItem('inf110_fc_mastery', JSON.stringify(fcMastery));
  } catch(e) {}

  if (typeof showMobileToast === 'function') {
    const msg = (nivel === 'facil') ? '¡Dominado! Registrado en tu progreso.' : (nivel === 'dificil' ? 'Marcado para repasar.' : 'Registrado como duda.');
    showMobileToast(msg);
  }
  fcSiguiente();
}

function fcActualizarProgreso() {
  let dominadas = 0;
  FLASHCARDS_DATA.forEach(c => {
    if (fcMastery[c.id] === 'facil') dominadas++;
  });
  const pct = Math.round((dominadas / FLASHCARDS_DATA.length) * 100);
  const progText = document.getElementById('fcProgressText');
  const progBar = document.getElementById('fcProgressBar');
  if (progText) progText.innerText = dominadas + ' de ' + FLASHCARDS_DATA.length + ' dominadas (' + pct + '%)';
  if (progBar) progBar.style.width = pct + '%';
}

function fcFiltrarCategoria(cat, btn) {
  document.querySelectorAll('.active-fc-cat').forEach(b => b.classList.remove('active-fc-cat'));
  btn.classList.add('active-fc-cat');

  if (cat === 'todas') {
    fcFilteredCards = [...FLASHCARDS_DATA];
  } else {
    fcFilteredCards = FLASHCARDS_DATA.filter(c => c.cat === cat);
  }
  fcCurrentIndex = 0;
  fcActualizarVista();
}

// Atajo de teclado: Espacio para voltear, Flechas para navegar
document.addEventListener('keydown', function(e) {
  const toolFc = document.getElementById('toolSection-flashcards');
  if (toolFc && toolFc.style.display !== 'none') {
    if (e.code === 'Space') {
      e.preventDefault();
      fcToggleFlip();
    } else if (e.code === 'ArrowRight') {
      fcSiguiente();
    } else if (e.code === 'ArrowLeft') {
      fcAnterior();
    }
  }
});

// =============================================================================
// 3. GENERADOR DE EXÁMENES ALEATORIOS IMPRIMIBLES (SIMULADOR PARCIAL)
// =============================================================================

const REAL_BANCO_P1_NUMEROS = [
  {
    titulo: "Eliminar Dígitos Primos",
    enunciado: "Diseñar una función que reciba un número natural 'n' y retorne un nuevo número conformado únicamente por los dígitos que NO sean primos (descartar 2, 3, 5 y 7).",
    ejemplo: "Entrada: n = 12593 -> Salida: 19",
    pascal: "function EliminarPrimos(n: Cardinal): Cardinal;\nvar dig, pot, res: Cardinal;\nbegin\n  res := 0; pot := 1;\n  while n > 0 do begin\n    dig := n mod 10;\n    if not (dig in [2, 3, 5, 7]) then begin\n      res := res + dig * pot;\n      pot := pot * 10;\n    end;\n    n := n div 10;\n  end;\n  Result := res;\nend;"
  },
  {
    titulo: "Verificar si un Número es Capicúa",
    enunciado: "Diseñar una función booleana que determine si un número natural 'n' es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).",
    ejemplo: "Entrada: n = 13531 -> Salida: True; n = 1234 -> Salida: False",
    pascal: "function EsNumeroCapicua(n: Cardinal): Boolean;\nvar inv, aux, dig: Cardinal;\nbegin\n  aux := n; inv := 0;\n  while aux > 0 do begin\n    dig := aux mod 10;\n    inv := inv * 10 + dig;\n    aux := aux div 10;\n  end;\n  Result := (inv = n);\nend;"
  },
  {
    titulo: "Sumar Dígitos Múltiplos de 3",
    enunciado: "Crear una función que calcule y retorne la suma de todos los dígitos de 'n' que sean múltiplos de 3 (3, 6, 9). Descartar el cero.",
    ejemplo: "Entrada: n = 31695 -> Salida: 18 (3 + 6 + 9 = 18)",
    pascal: "function SumarMultiplos3(n: Cardinal): Cardinal;\nvar dig, suma: Cardinal;\nbegin\n  suma := 0;\n  while n > 0 do begin\n    dig := n mod 10;\n    if (dig in [3, 6, 9]) then\n      suma := suma + dig;\n    n := n div 10;\n  end;\n  Result := suma;\nend;"
  },
  {
    titulo: "Formar Número Solo con Dígitos Pares",
    enunciado: "Diseñar una función que tome los dígitos pares de 'n' y retorne un nuevo número preservando su orden posicional relativo.",
    ejemplo: "Entrada: n = 123456 -> Salida: 246",
    pascal: "function FormarSoloPares(n: Cardinal): Cardinal;\nvar dig, pot, res: Cardinal;\nbegin\n  res := 0; pot := 1;\n  while n > 0 do begin\n    dig := n mod 10;\n    if (dig mod 2 = 0) then begin\n      res := res + dig * pot;\n      pot := pot * 10;\n    end;\n    n := n div 10;\n  end;\n  Result := res;\nend;"
  }
];

const REAL_BANCO_P2_CADENAS = [
  {
    titulo: "Contar Palabras que Comienzan y Terminan en Vocal",
    enunciado: "Crear una función modular que reciba (cad: string; n, i: byte) y retorne cuántas palabras en la cadena inician y finalizan en vocal.",
    ejemplo: "Entrada: cad = 'ala este gol uno' -> Salida: 3 (ala, este, uno)",
    pascal: "function ContarPalabrasVocExtremos(cad: string; n, i: byte): byte;\nconst voc: set of char = ['A','E','I','O','U','a','e','i','o','u'];\nvar contador, nPal: byte; pal: string;\nbegin\n  contador := 0; i := 1;\n  while i <= n do begin\n    while (i <= n) and (cad[i] = ' ') do i := i + 1;\n    pal := '';\n    while (i <= n) and (cad[i] <> ' ') do begin\n      pal := pal + cad[i]; i := i + 1;\n    end;\n    if pal <> '' then begin\n      nPal := Length(pal);\n      if (pal[1] in voc) and (pal[nPal] in voc) then\n        contador := contador + 1;\n    end;\n  end;\n  Result := contador;\nend;"
  },
  {
    titulo: "Invertir la Segunda Palabra de una Cadena",
    enunciado: "Diseñar una función con firma (cad: string; n, i: byte) que invierta los caracteres de la segunda palabra preservando el resto del texto.",
    ejemplo: "Entrada: cad = 'Hola Mundo Cruel' -> Salida: 'Hola odnuM Cruel'",
    pascal: "function InvertirSegundaPalabra(cad: string; n, i: byte): string;\nvar pal, res, inv: string; totalP, j, k: byte;\n    palabras: array[1..100] of string;\nbegin\n  i := 1; totalP := 0;\n  while i <= n do begin\n    while (i <= n) and (cad[i] = ' ') do i := i + 1;\n    pal := '';\n    while (i <= n) and (cad[i] <> ' ') do begin\n      pal := pal + cad[i]; i := i + 1;\n    end;\n    if pal <> '' then begin totalP := totalP + 1; palabras[totalP] := pal; end;\n  end;\n  if totalP >= 2 then begin\n    inv := ''; j := Length(palabras[2]);\n    while j >= 1 do begin inv := inv + palabras[2][j]; j := j - 1; end;\n    palabras[2] := inv;\n  end;\n  res := ''; k := 1;\n  while k <= totalP do begin\n    if res <> '' then res := res + ' ';\n    res := res + palabras[k]; k := k + 1;\n  end;\n  Result := res;\nend;"
  },
  {
    titulo: "Eliminar Palabras Delante de una con Consonante 'c'",
    enunciado: "Crear una función (cad: string; n, i: byte) que elimine cualquier palabra que se encuentre inmediatamente después de una palabra que contenga la letra 'c' o 'C'.",
    ejemplo: "Entrada: cad = 'la casa bonita' -> Salida: 'la casa' (se elimina bonita)",
    pascal: "function EliminarPalDelanteDeC(cad: string; n, i: byte): string;\nvar pal, res: string; totalP, j, k: byte;\n    palabras: array[1..100] of string; teniaC: boolean;\nbegin\n  i := 1; totalP := 0;\n  while i <= n do begin\n    while (i <= n) and (cad[i] = ' ') do i := i + 1;\n    pal := '';\n    while (i <= n) and (cad[i] <> ' ') do begin\n      pal := pal + cad[i]; i := i + 1;\n    end;\n    if pal <> '' then begin totalP := totalP + 1; palabras[totalP] := pal; end;\n  end;\n  res := ''; j := 1;\n  while j <= totalP do begin\n    teniaC := false;\n    if j > 1 then begin\n      k := 1;\n      while k <= Length(palabras[j-1]) do begin\n        if UpCase(palabras[j-1][k]) = 'C' then teniaC := true;\n        k := k + 1;\n      end;\n    end;\n    if not teniaC then begin\n      if res <> '' then res := res + ' ';\n      res := res + palabras[j];\n    end;\n    j := j + 1;\n  end;\n  Result := res;\nend;"
  },
  {
    titulo: "Contar la Cantidad de Veces que Existen 2 Vocales Juntas",
    enunciado: "Diseñar una función (cad: string; n, i: byte): byte que cuente cuántas parejas de vocales contiguas consecutivas existen en la cadena.",
    ejemplo: "Entrada: cad = 'bueno aeiou' -> Salida: 5 ('ue', 'ae', 'ei', 'io', 'ou')",
    pascal: "function ContarDosVocalesJuntas(cad: string; n, i: byte): byte;\nconst voc: set of char = ['A','E','I','O','U','a','e','i','o','u'];\nvar contador, ayudante: byte;\nbegin\n  contador := 0; i := 1;\n  while i <= n do begin\n    ayudante := i + 1;\n    if ayudante <= n then begin\n      if (cad[i] in voc) and (cad[ayudante] in voc) then\n        contador := contador + 1;\n    end;\n    i := i + 1;\n  end;\n  Result := contador;\nend;"
  }
];

const REAL_BANCO_P3_TRAZAS = [
  {
    titulo: "Prueba de Escritorio: Contar Vocales con (cad, n, i)",
    cadenaPrueba: "UNIVERSIDAD",
    headers: ["Paso", "i", "i <= n", "cad[i]", "cad[i] in voc", "contador", "i := i + 1"],
    codigoSeguimiento: "function contarvocal(cad: string; n, i: byte): integer;\nconst voc: set of char = ['A','E','I','O','U'];\nvar c: integer;\nbegin\n  c := 0; i := 1;\n  while i <= n do begin\n    if UpCase(cad[i]) in voc then\n      c := c + 1;\n    i := i + 1;\n  end;\n  Result := c;\nend;"
  },
  {
    titulo: "Prueba de Escritorio: Eliminar Espacios en Blanco",
    cadenaPrueba: "H O L A",
    headers: ["Paso", "i", "i <= n", "cad[i]", "cad[i] <> ' '", "res", "i := i + 1"],
    codigoSeguimiento: "function EliminarEspacios(cad: string; n, i: byte): string;\nvar res: string;\nbegin\n  res := ''; i := 1;\n  while i <= n do begin\n    if cad[i] <> ' ' then\n      res := res + cad[i];\n    i := i + 1;\n  end;\n  Result := res;\nend;"
  },
  {
    titulo: "Prueba de Escritorio: Verificar Número Capicúa",
    cadenaPrueba: "n = 13531",
    headers: ["Paso", "aux", "aux > 0", "dig := aux mod 10", "inv := inv * 10 + dig", "aux := aux div 10"],
    codigoSeguimiento: "function EsCapicua(n: Cardinal): Boolean;\nvar inv, aux, dig: Cardinal;\nbegin\n  aux := n; inv := 0;\n  while aux > 0 do begin\n    dig := aux mod 10;\n    inv := inv * 10 + dig;\n    aux := aux div 10;\n  end;\n  Result := (inv = n);\nend;"
  }
];

let realExamCurrentSeed = 1;
let realExamTimerSeconds = 45 * 60;
let realExamTimerInterval = null;
let realExamSolucionVisible = false;

function realExamGenerarNuevo() {
  realExamCurrentSeed = Math.floor(Math.random() * 900) + 100;
  const badge = document.getElementById('realExamNumBadge');
  if (badge) badge.innerText = 'PARCIAL MODELO #' + realExamCurrentSeed;

  const p1 = REAL_BANCO_P1_NUMEROS[Math.floor(Math.random() * REAL_BANCO_P1_NUMEROS.length)];
  const p2 = REAL_BANCO_P2_CADENAS[Math.floor(Math.random() * REAL_BANCO_P2_CADENAS.length)];
  const p3 = REAL_BANCO_P3_TRAZAS[Math.floor(Math.random() * REAL_BANCO_P3_TRAZAS.length)];

  const container = document.getElementById('realExamQuestionsContainer');
  if (!container) return;

  let html = `
    <!-- PREGUNTA 1: NÚMEROS NATURALES (35 PUNTOS) -->
    <div style="margin-bottom: 2rem; border-bottom: 1px dashed #cbd5e1; padding-bottom: 1.5rem;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.05rem; font-weight: 800; color: #0f172a;">
          PREGUNTA 1 [35 PUNTOS]: ${p1.titulo}
        </h3>
        <span style="font-size: 0.8rem; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">Ponderación: 35%</span>
      </div>
      <p style="font-size: 0.95rem; color: #334155; line-height: 1.5; margin-bottom: 0.5rem;">
        ${p1.enunciado}
      </p>
      <div style="background: #f1f5f9; padding: 0.5rem 0.8rem; border-radius: 4px; font-size: 0.85rem; color: #475569; font-family: 'Fira Code', monospace; margin-bottom: 0.75rem;">
        💡 <strong>Caso de prueba:</strong> ${p1.ejemplo}
      </div>
      
      <div style="border: 1px solid #cbd5e1; border-radius: 4px; padding: 0.75rem; min-height: 160px; background: #fafafa; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #64748b;">
        // Espacio para solución en Pascal / Pseudocódigo del alumno:
      </div>

      <div class="exam-solution-box" style="display: none; margin-top: 1rem; background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px; padding: 1rem;">
        <div style="font-weight: 800; color: #166534; font-size: 0.85rem; margin-bottom: 0.5rem;">✅ SOLUCIÓN OFICIAL MODELO (Free Pascal / Delphi):</div>
        <pre style="margin: 0; font-family: 'Fira Code', monospace; font-size: 0.82rem; color: #064e3b; overflow-x: auto;">${htmlEscape(p1.pascal)}</pre>
        <div style="font-size: 0.8rem; color: #15803d; margin-top: 0.5rem;">
          📊 <strong>Criterio de Evaluación:</strong> Declaración de función (5 pts), control de ciclo while n > 0 (10 pts), descomposición mod/div (10 pts), acumulación y retorno (10 pts).
        </div>
      </div>
    </div>

    <!-- PREGUNTA 2: CADENAS CON METODOLOGÍA OFICIAL (40 PUNTOS) -->
    <div style="margin-bottom: 2rem; border-bottom: 1px dashed #cbd5e1; padding-bottom: 1.5rem;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.05rem; font-weight: 800; color: #0f172a;">
          PREGUNTA 2 [40 PUNTOS]: ${p2.titulo}
        </h3>
        <span style="font-size: 0.8rem; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">Ponderación: 40%</span>
      </div>
      <p style="font-size: 0.95rem; color: #334155; line-height: 1.5; margin-bottom: 0.5rem;">
        ${p2.enunciado} <em>(Requisito obligatorio: firma con <code>cad: string; n, i: byte</code> y recorrido estricto con ciclo <code>while i &lt;= n</code>)</em>.
      </p>
      <div style="background: #f1f5f9; padding: 0.5rem 0.8rem; border-radius: 4px; font-size: 0.85rem; color: #475569; font-family: 'Fira Code', monospace; margin-bottom: 0.75rem;">
        💡 <strong>Caso de prueba:</strong> ${p2.ejemplo}
      </div>

      <div style="border: 1px solid #cbd5e1; border-radius: 4px; padding: 0.75rem; min-height: 200px; background: #fafafa; font-family: 'Fira Code', monospace; font-size: 0.85rem; color: #64748b;">
        // Espacio para solución en Pascal / Delphi Form:
      </div>

      <div class="exam-solution-box" style="display: none; margin-top: 1rem; background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px; padding: 1rem;">
        <div style="font-weight: 800; color: #166534; font-size: 0.85rem; margin-bottom: 0.5rem;">✅ SOLUCIÓN OFICIAL MODELO:</div>
        <pre style="margin: 0; font-family: 'Fira Code', monospace; font-size: 0.82rem; color: #064e3b; overflow-x: auto;">${htmlEscape(p2.pascal)}</pre>
        <div style="font-size: 0.8rem; color: #15803d; margin-top: 0.5rem;">
          📊 <strong>Criterio de Evaluación:</strong> Firma correcta con n, i: byte (10 pts), control de while con i:=1 e i:=i+1 (10 pts), algoritmo de palabras/caracteres (15 pts), retorno en Result (5 pts).
        </div>
      </div>
    </div>

    <!-- PREGUNTA 3: PRUEBA DE ESCRITORIO / TRAZA FORMAL (25 PUNTOS) -->
    <div style="margin-bottom: 1rem;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.05rem; font-weight: 800; color: #0f172a;">
          PREGUNTA 3 [25 PUNTOS]: ${p3.titulo}
        </h3>
        <span style="font-size: 0.8rem; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">Ponderación: 25%</span>
      </div>
      <p style="font-size: 0.95rem; color: #334155; line-height: 1.5; margin-bottom: 0.5rem;">
        Dada la siguiente función, elabore la <strong>Prueba de Escritorio Formal</strong> completa para la entrada: <strong>${p3.cadenaPrueba}</strong>.
      </p>

      <div style="background: #0f172a; color: #f8fafc; border-radius: 4px; padding: 0.75rem; margin-bottom: 0.75rem; overflow-x: auto;">
        <pre style="margin: 0; font-family: 'Fira Code', monospace; font-size: 0.8rem;">${htmlEscape(p3.codigoSeguimiento)}</pre>
      </div>

      <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem; font-size: 0.85rem; border: 1px solid #cbd5e1;">
        <thead>
          <tr style="background: #f1f5f9;">
  `;

  p3.headers.forEach(h => {
    html += `<th style="border: 1px solid #cbd5e1; padding: 6px; text-align: center; color: #0f172a;">${h}</th>`;
  });

  html += `
          </tr>
        </thead>
        <tbody>
  `;

  for (let rowIdx = 1; rowIdx <= 6; rowIdx++) {
    html += `<tr>`;
    p3.headers.forEach(() => {
      html += `<td style="border: 1px solid #cbd5e1; height: 26px; text-align: center;">&nbsp;</td>`;
    });
    html += `</tr>`;
  }

  html += `
        </tbody>
      </table>

      <div class="exam-solution-box" style="display: none; margin-top: 1rem; background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px; padding: 1rem;">
        <div style="font-weight: 800; color: #166534; font-size: 0.85rem; margin-bottom: 0.5rem;">✅ CRITERIO DE EVALUACIÓN DE TRAZA:</div>
        <div style="font-size: 0.82rem; color: #15803d;">
          Columnas requeridas completas (5 pts), valores del puntero i secuenciales (5 pts), evaluación booleana exacta de condiciones (5 pts), actualización de variables de memoria (5 pts), determinación del valor de retorno final (5 pts).
        </div>
      </div>
    </div>
  `;

  container.innerHTML = html;
  realExamSolucionVisible = false;
  const btnSol = document.getElementById('btnToggleRealSolucion');
  if (btnSol) btnSol.innerText = '👁️ Revelar Solución & Criterios';
}

function realExamToggleSolucion() {
  realExamSolucionVisible = !realExamSolucionVisible;
  const boxes = document.querySelectorAll('.exam-solution-box');
  boxes.forEach(b => {
    b.style.display = realExamSolucionVisible ? 'block' : 'none';
  });
  const btnSol = document.getElementById('btnToggleRealSolucion');
  if (btnSol) btnSol.innerText = realExamSolucionVisible ? '🙈 Ocultar Solución Oficial' : '👁️ Revelar Solución & Criterios';
}

function realExamStartTimer() {
  if (realExamTimerInterval) return;
  realExamTimerInterval = setInterval(() => {
    if (realExamTimerSeconds > 0) {
      realExamTimerSeconds--;
      realExamUpdateTimerDisplay();
    } else {
      clearInterval(realExamTimerInterval);
      realExamTimerInterval = null;
      realExamPlaySoundAlarm();
      alert('⏰ ¡TIEMPO TERMINADO! Los 45 minutos del simulacro de examen han finalizado.');
    }
  }, 1000);
}

function realExamPauseTimer() {
  if (realExamTimerInterval) {
    clearInterval(realExamTimerInterval);
    realExamTimerInterval = null;
  }
}

function realExamResetTimer() {
  realExamPauseTimer();
  realExamTimerSeconds = 45 * 60;
  realExamUpdateTimerDisplay();
}

function realExamUpdateTimerDisplay() {
  const m = Math.floor(realExamTimerSeconds / 60);
  const s = realExamTimerSeconds % 60;
  const disp = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  const elem = document.getElementById('realExamTimerDisplay');
  if (elem) {
    elem.innerText = disp;
    if (realExamTimerSeconds <= 300) {
      elem.style.color = '#ef4444';
    } else {
      elem.style.color = '#f59e0b';
    }
  }
}

function realExamPlaySoundAlarm() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.frequency.setValueAtTime(440, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.5);
    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.8);
    osc.start();
    osc.stop(ctx.currentTime + 0.8);
  } catch(e) {}
}

function htmlEscape(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// Inicialización de componentes al cargar la página
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(() => {
    try {
      if (typeof animReset === 'function') animReset();
      if (typeof fcActualizarVista === 'function') fcActualizarVista();
      if (typeof realExamGenerarNuevo === 'function') realExamGenerarNuevo();
    } catch(e) {}
  }, 300);
});
