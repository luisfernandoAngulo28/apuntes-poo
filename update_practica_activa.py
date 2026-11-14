# -*- coding: utf-8 -*-
"""
Script maestro para corregir completamente la visualización del
Animador de Traza de Escritorio en teoria_programacion_modular.html:
1. Elimina el </style> prematuro que dejaba todo el CSS huérfano fuera de las etiquetas de estilo.
2. Aplica estilos de alto contraste (texto blanco brillante sobre fondo oscuro) para:
   - animInputCad
   - animSpeedSelect
   - animInputExtra
   - animAlgSelect
3. Convierte las celdas de cinta de caracteres (.tape-cell) en cajas delimitadas de alta definición
   con borde, sombra, número de índice [i], carácter centrado destacado, badge y flecha activa superior.
4. Convierte las variables de memoria RAM (.var-ram-card) en tarjetas visualmente separadas tipo debugger,
   con separador ':' y valores en píldoras coloreadas.
5. Da formato estilizado a la tabla de traza de escritorio (.traza-table).
"""

import os, sys, re, shutil
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def main():
    print("Iniciando actualización y corrección de Práctica Activa...")

    # =========================================================================
    # PASO 1: Actualizar motor_practica_activa.js
    # =========================================================================
    js_file = 'motor_practica_activa.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        js_code = f.read()

    pos_tape = js_code.find('function animRenderTape(')
    pos_thead = js_code.find('function animRenderTableHead()')

    if pos_tape != -1 and pos_thead != -1:
        new_render_funcs = '''function animRenderTape(activeIdx, matchIdx) {
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

    cell.innerHTML += '<span class="tape-idx" style="font-size: 0.72rem; color: ' + idxColor + '; font-weight: 700; font-family: \\'Fira Code\\', monospace;">[' + idx + ']</span>' +
                      '<span class="tape-char" style="font-size: 1.45rem; font-weight: 900; color: ' + charColor + '; font-family: \\'Fira Code\\', monospace; line-height: 1;">' + displayChar + '</span>' +
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

    card.innerHTML = '<span class="var-ram-name" style="font-family: \\'Fira Code\\', monospace; font-size: 0.82rem; font-weight: 700; color: #94a3b8; margin-right: 0.5rem;">' + key + ':</span>' +
                     '<span class="var-ram-val" id="varVal-' + key + '" style="font-family: \\'Fira Code\\', monospace; font-size: 0.95rem; font-weight: 800; color: ' + valColor + '; background: ' + valBg + '; padding: 2px 8px; border-radius: 4px; border: 1px solid ' + valBorder + '; min-width: 28px; text-align: center;">' + valStr + '</span>';
    grid.appendChild(card);
  }
}

'''
        js_code = js_code[:pos_tape] + new_render_funcs + js_code[pos_thead:]
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_code)
        print("✓ motor_practica_activa.js actualizado con funciones de renderizado robustas.")
    else:
        print("⚠️ No se encontraron las funciones en motor_practica_activa.js")

    # =========================================================================
    # PASO 2: Actualizar CSS en integrar_practica_activa.py
    # =========================================================================
    enhanced_css = """/* ESTILOS PARA EL MÓDULO DE PRÁCTICA ACTIVA (EXAMEN UAGRM) */
.tool-subpanel {
  transition: all 0.3s ease;
}

/* ENTRADAS Y SELECTS DE PRÁCTICA ACTIVA (ALTO CONTRASTE) */
#animInputCad, #animInputExtra, #animAlgSelect, #animSpeedSelect {
  background: #0f172a !important;
  color: #f8fafc !important;
  border: 1.5px solid #38bdf8 !important;
  border-radius: 6px !important;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.3) !important;
}
#animInputCad {
  font-size: 1.15rem !important;
  font-weight: 700 !important;
  padding: 0.6rem 0.85rem !important;
  color: #ffffff !important;
}
#animInputCad:focus, #animInputExtra:focus, #animAlgSelect:focus {
  border-color: #38bdf8 !important;
  outline: none !important;
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.45) !important;
}
#animAlgSelect {
  color: #34d399 !important;
  font-weight: 700 !important;
  border-color: #059669 !important;
  padding: 0.6rem 0.85rem !important;
}
#animSpeedSelect {
  color: #f8fafc !important;
  border-color: #475569 !important;
  padding: 0.35rem 0.65rem !important;
}
#animInputExtra {
  border-color: #f59e0b !important;
  color: #fbbf24 !important;
  font-size: 1.15rem !important;
  font-weight: 900 !important;
}
select option {
  background: #0f172a !important;
  color: #f8fafc !important;
}

/* CINTA DE MEMORIA (CHARACTER TAPE) */
.tape-cell {
  flex: 0 0 58px;
  min-width: 58px;
  height: 74px;
  background: #0f172a;
  border: 2px solid #334155;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 6px 4px;
  position: relative;
  transition: all 0.25s ease;
  user-select: none;
  box-shadow: 0 2px 5px rgba(0,0,0,0.4);
}
.tape-cell .tape-idx {
  font-size: 0.72rem;
  color: #94a3b8;
  font-weight: 700;
  font-family: 'Fira Code', monospace;
}
.tape-cell .tape-char {
  font-size: 1.45rem;
  font-weight: 900;
  color: #f8fafc;
  font-family: 'Fira Code', monospace;
  line-height: 1;
}
.tape-cell .tape-badge {
  font-size: 0.62rem;
  font-weight: 800;
  padding: 2px 5px;
  border-radius: 3px;
  background: #1e293b;
  color: #cbd5e1;
  letter-spacing: 0.5px;
}
.tape-cell.active {
  border-color: #10b981 !important;
  background: rgba(16, 185, 129, 0.22) !important;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.6) !important;
  transform: translateY(-6px);
}
.tape-cell.active .tape-idx {
  color: #34d399 !important;
}
.tape-cell.active .tape-char {
  color: #34d399 !important;
}
.tape-cell.active .tape-badge {
  background: #065f46 !important;
  color: #a7f3d0 !important;
}
.tape-cell.match {
  border-color: #f59e0b !important;
  background: rgba(245, 158, 11, 0.25) !important;
}
.tape-cell.match .tape-char {
  color: #fbbf24 !important;
}
.tape-pointer-arrow {
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  color: #10b981;
  font-size: 0.8rem;
  font-weight: 900;
  white-space: nowrap;
  animation: bouncePointer 0.6s infinite alternate ease-in-out;
  background: #022c22;
  border: 1px solid #10b981;
  padding: 1px 6px;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.5);
}
@keyframes bouncePointer {
  from { top: -26px; }
  to { top: -20px; }
}

/* TARJETAS DE VARIABLES RAM */
.var-ram-card {
  background: #0f172a;
  border: 1.5px solid #334155;
  border-radius: 6px;
  padding: 0.55rem 0.85rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
  transition: all 0.2s ease;
}
.var-ram-name {
  font-family: 'Fira Code', monospace;
  font-size: 0.82rem;
  font-weight: 700;
  color: #94a3b8;
  margin-right: 0.5rem;
}
.var-ram-val {
  font-family: 'Fira Code', monospace;
  font-size: 0.95rem;
  font-weight: 800;
  color: #38bdf8;
  background: #070a13;
  padding: 2px 8px;
  border-radius: 4px;
  border: 1px solid #1e293b;
  min-width: 28px;
  text-align: center;
  transition: all 0.2s ease;
}

/* TABLA DE TRAZA EN TIEMPO REAL */
.traza-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Fira Code', monospace;
  font-size: 0.88rem;
  text-align: center;
}
.traza-table th {
  background: #1e293b;
  color: #38bdf8;
  padding: 0.6rem 0.75rem;
  border: 1px solid #334155;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.8rem;
}
.traza-table td {
  padding: 0.5rem 0.75rem;
  border: 1px solid #1e293b;
  color: #f1f5f9;
  background: #0b1120;
}
.traza-table tbody tr:nth-child(even) td {
  background: #0f172a;
}
.traza-table tbody tr:hover td {
  background: rgba(56, 189, 248, 0.12);
}

/* FLASHCARDS 3D */
.fc-card-scene {
  user-select: none;
}
.fc-card-inner.flipped {
  transform: rotateY(180deg);
}
.active-fc-cat {
  background: #0284c7 !important;
  color: #ffffff !important;
  font-weight: 800 !important;
}

/* HOJA DE EXAMEN IMPRIMIBLE */
@media print {
  body * {
    visibility: hidden;
  }
  #examSheetPrintable, #examSheetPrintable * {
    visibility: visible;
  }
  #examSheetPrintable {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    margin: 0;
    padding: 1.5cm;
    background: #ffffff !important;
    color: #000000 !important;
    box-shadow: none !important;
    border: none !important;
  }
}
"""

    # =========================================================================
    # PASO 3: Actualizar y limpiar directamente teoria_programacion_modular.html
    # =========================================================================
    html_file = 'teoria_programacion_modular.html'
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Identificar la sección <head>
    head_end = html.find('</head>')
    if head_end == -1:
        print("❌ Error: No se encontró </head> en el documento.")
        return

    head_content = html[:head_end]

    # Eliminar cualquier bloque previo de Práctica Activa en head
    marker = '/* ESTILOS PARA EL MÓDULO DE PRÁCTICA ACTIVA (EXAMEN UAGRM) */'
    if marker in head_content:
        # Encontrar el inicio de este bloque
        m_pos = head_content.find(marker)
        # Buscar hacia atrás el cierre de estilo o salto
        # Encontrar el </style> que cierra el bloque o la etiqueta
        end_style_after = head_content.find('</style>', m_pos)
        if end_style_after != -1:
            # Eliminar desde m_pos hasta end_style_after
            head_content = head_content[:m_pos] + head_content[end_style_after:]

    # Asegurarnos de que no haya </style> huérfanos antes del final del <head>
    # Dejamos solo UN </style> justo antes de </head>
    styles_close = [m.start() for m in re.finditer(r'</style>', head_content, re.IGNORECASE)]
    if len(styles_close) > 1:
        print(f"Detectados {len(styles_close)} cierres de estilo en <head>. Limpiando cierres prematuros...")
        # Eliminamos todos los </style> excepto el último
        cleaned_head = ""
        last_idx = 0
        for idx in styles_close[:-1]:
            cleaned_head += head_content[last_idx:idx]
            last_idx = idx + len('</style>')
        cleaned_head += head_content[last_idx:]
        head_content = cleaned_head

    # Ahora insertamos el enhanced_css justo antes del único </style>
    last_style_close = head_content.rfind('</style>')
    if last_style_close != -1:
        head_content = head_content[:last_style_close] + '\n' + enhanced_css + '\n' + head_content[last_style_close:]
        print("✓ CSS de Práctica Activa insertado correctamente DENTRO de <style>...</style>.")
    else:
        print("⚠️ No se encontró </style> en <head>. Insertando con nueva etiqueta <style>.")
        head_content += f"\n<style>\n{enhanced_css}\n</style>\n"

    # Reensamblar html con el head corregido
    html = head_content + html[head_end:]

    # =========================================================================
    # PASO 4: Reemplazar el motor JavaScript en el HTML con el nuevo código
    # =========================================================================
    with open('motor_practica_activa.js', 'r', encoding='utf-8') as f:
        latest_js = f.read()

    js_marker = 'MOTOR DE PRÁCTICA ACTIVA: TRAZA EN VIVO, FLASHCARDS & EXAMEN UAGRM'
    if js_marker in html:
        js_start = html.find('// =============================================================================\n//      ' + js_marker)
        if js_start == -1:
            js_start = html.find(js_marker)
            prev_line = html.rfind('// ===', 0, js_start)
            if prev_line != -1 and js_start - prev_line < 100:
                js_start = prev_line
        
        marker_end_js = 'examGenerarNuevo();'
        pos_end_js = html.find(marker_end_js, js_start)
        if pos_end_js != -1:
            pos_end_js = html.find('});', pos_end_js) + len('});')
        else:
            pos_end_js = html.rfind('</script>')
        html = html[:js_start] + latest_js + '\n' + html[pos_end_js:]
        print("✓ Motor JS actualizado en el HTML.")

    # =========================================================================
    # PASO 5: Actualizar la sección HTML de practica-activa-examenes
    # =========================================================================
    from generar_herramientas_practica_activa import build_practica_activa_html
    section_html = build_practica_activa_html()
    if 'id="practica-activa-examenes"' in html:
        sec_start = html.find('<section id="practica-activa-examenes"')
        marker_end = '<!-- FIN SECCIÓN PRÁCTICA ACTIVA -->'
        sec_end = html.find(marker_end, sec_start)
        if sec_end != -1:
            sec_end = html.find('-->', sec_end) + len('-->')
        else:
            sec_end = html.find('</section>', sec_start) + len('</section>')
        html = html[:sec_start] + section_html + html[sec_end:]
        print("✓ Sección practica-activa-examenes actualizada con inputs de alto contraste.")

    # Guardar archivo actualizado
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"🎉 Proceso finalizado exitosamente! Tamaño del HTML: {len(html)} bytes.")

if __name__ == '__main__':
    main()
