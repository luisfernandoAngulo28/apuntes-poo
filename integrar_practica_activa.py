# -*- coding: utf-8 -*-
"""
Script de integración para insertar el Módulo de Práctica Activa
(Simulador de Traza en Vivo, Flashcards 3D y Generador de Examen Parcial UAGRM)
en teoria_programacion_modular.html.
"""

import sys, shutil
from generar_herramientas_practica_activa import build_practica_activa_html

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def integrate():
    input_file = 'teoria_programacion_modular.html'
    backup_file = 'teoria_programacion_modular.html.bak_before_practica_activa'
    
    print("Creando respaldo de seguridad...")
    shutil.copyfile(input_file, backup_file)
    print(f"✓ Respaldo creado: {backup_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Insertar Estilos CSS si no existen
    css_marker = '/* ESTILOS PARA EL MÓDULO DE PRÁCTICA ACTIVA (EXAMEN UAGRM) */'
    if css_marker not in html:
        css_content = """
/* ESTILOS PARA EL MÓDULO DE PRÁCTICA ACTIVA (EXAMEN UAGRM) */
.tool-subpanel {
  transition: all 0.3s ease;
}

/* CINTA DE MEMORIA (CHARACTER TAPE) */
.tape-cell {
  flex: 0 0 54px;
  height: 68px;
  background: #0f172a;
  border: 2px solid #334155;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 4px 2px;
  position: relative;
  transition: all 0.25s ease;
  user-select: none;
}
.tape-cell .tape-idx {
  font-size: 0.7rem;
  color: #64748b;
  font-weight: 700;
  font-family: 'Fira Code', monospace;
}
.tape-cell .tape-char {
  font-size: 1.35rem;
  font-weight: 900;
  color: #f8fafc;
  font-family: 'Fira Code', monospace;
}
.tape-cell .tape-badge {
  font-size: 0.62rem;
  font-weight: 800;
  padding: 1px 4px;
  border-radius: 3px;
  background: #1e293b;
  color: #94a3b8;
}
.tape-cell.active {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.15);
  box-shadow: 0 0 15px rgba(16, 185, 129, 0.5);
  transform: translateY(-4px);
}
.tape-cell.active .tape-idx {
  color: #34d399;
}
.tape-cell.active .tape-char {
  color: #34d399;
}
.tape-cell.match {
  border-color: #f59e0b;
  background: rgba(245, 158, 11, 0.2);
}
.tape-pointer-arrow {
  position: absolute;
  top: -18px;
  left: 50%;
  transform: translateX(-50%);
  color: #10b981;
  font-size: 0.95rem;
  font-weight: 900;
  animation: bouncePointer 0.6s infinite alternate ease-in-out;
}
@keyframes bouncePointer {
  from { top: -20px; }
  to { top: -14px; }
}

/* TARJETAS DE VARIABLES RAM */
.var-ram-card {
  background: #0b1120;
  border: 1px solid #1e293b;
  border-radius: 4px;
  padding: 0.5rem 0.65rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.var-ram-name {
  font-family: 'Fira Code', monospace;
  font-size: 0.8rem;
  font-weight: 700;
  color: #94a3b8;
}
.var-ram-val {
  font-family: 'Fira Code', monospace;
  font-size: 0.95rem;
  font-weight: 800;
  color: #38bdf8;
  transition: color 0.2s;
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
        pos_style_end = html.rfind('</style>')
        if pos_style_end != -1:
            html = html[:pos_style_end] + '\n' + css_content + '\n' + html[pos_style_end:]
            print("✓ Estilos CSS de Práctica Activa insertados.")
        else:
            print("⚠️ No se encontró </style>.")

    # 2. Agregar botón en nav-tabs si no existe
    nav_btn_html = '    <button class="nav-btn" data-cat="practicos" onclick="switchTab(\'practica-activa-examenes\')">⚡ 5. Práctica Activa (Traza en Vivo, Flashcards &amp; Parcial Real)</button>\n'
    if "switchTab('practica-activa-examenes')" not in html:
        target_p9_btn = "switchTab('solucion-practico9')"
        pos_p9_btn = html.find(target_p9_btn)
        if pos_p9_btn != -1:
            pos_btn_end = html.find('</button>', pos_p9_btn) + len('</button>')
            html = html[:pos_btn_end] + '\n' + nav_btn_html + html[pos_btn_end:]
            print("✓ Botón añadido a nav-tabs.")
        else:
            print("⚠️ No se encontró botón p9 en nav-tabs.")
    else:
        print("ℹ️ El botón de nav-tabs ya estaba presente.")

    # 3. Agregar ítem en mobile drawer si no existe
    drawer_item_html = '''          <div class="drawer-item" onclick="selectDrawerTab('practica-activa-examenes')">
            <span>⚡ Práctica Activa (Traza, Flashcards &amp; Parcial)</span>
            <span style="color: #10b981;">➜</span>
          </div>\n'''
    if "selectDrawerTab('practica-activa-examenes')" not in html:
        pos_p9_dr = html.find("selectDrawerTab('solucion-practico9')")
        if pos_p9_dr != -1:
            pos_dr_end = html.find('</div>', pos_p9_dr) + len('</div>')
            html = html[:pos_dr_end] + '\n' + drawer_item_html + html[pos_dr_end:]
            print("✓ Ítem añadido al menú drawer móvil.")
        else:
            print("⚠️ No se encontró drawer-item p9.")
    else:
        print("ℹ️ El ítem de drawer ya estaba presente.")

    # 4. Insertar o reemplazar la sección practica-activa-examenes
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
        print("✓ Sección practica-activa-examenes REEMPLAZADA.")
    else:
        # Insertar después de solucion-practico9
        pos_p9 = html.find('id="solucion-practico9"')
        if pos_p9 != -1:
            marker_end_p9 = '<!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #9'
            pos_p9_end = html.find(marker_end_p9, pos_p9)
            if pos_p9_end != -1:
                pos_insert = html.find('-->', pos_p9_end) + len('-->')
            else:
                pos_insert = html.find('</section>', pos_p9) + len('</section>')
            html = html[:pos_insert] + '\n\n' + section_html + html[pos_insert:]
            print("✓ Sección practica-activa-examenes insertada después de Práctico #9.")
        else:
            print("⚠️ No se encontró la sección solucion-practico9.")

    # 5. Insertar o reemplazar el motor JavaScript
    with open('d:/Introz2/practico07/motor_practica_activa.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

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
        html = html[:js_start] + js_code + '\n' + html[pos_end_js:]
        print("✓ Motor JavaScript de Práctica Activa REEMPLAZADO.")
    else:
        pos_last_script = html.rfind('</script>')
        if pos_last_script != -1:
            html = html[:pos_last_script] + '\n\n' + js_code + '\n' + html[pos_last_script:]
            print("✓ Motor JavaScript de Práctica Activa insertado.")
        else:
            print("⚠️ No se encontró </script>.")

    # Guardar archivo actualizado
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Integración completada con éxito. Tamaño final del HTML: {len(html)} bytes.")

if __name__ == '__main__':
    integrate()

