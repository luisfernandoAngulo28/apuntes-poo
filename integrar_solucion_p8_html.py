# -*- coding: utf-8 -*-
"""
Script de integración final para insertar o actualizar la solución completa del Práctico #8
en teoria_programacion_modular.html.
"""

import sys
import shutil
import generar_seccion_practico08_html as p8_gen

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def integrate():
    input_file = 'teoria_programacion_modular.html'
    backup_file = 'teoria_programacion_modular.html.bak'
    
    print("Creando respaldo de seguridad...")
    shutil.copyfile(input_file, backup_file)

    with open(input_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Agregar botón en nav-tabs si no existe
    nav_btn_html = '    <button class="nav-btn" onclick="switchTab(\'solucion-practico8\')">🔤 Solución Práctico #8 (Cadenas & 40 Ejercicios)</button>\n'
    if 'switchTab(\'solucion-practico8\')' not in html:
        target_p7_btn = "switchTab('solucion-practico7')\">"
        pos_p7_btn = html.find(target_p7_btn)
        if pos_p7_btn != -1:
            pos_p7_btn_end = html.find('</button>', pos_p7_btn) + len('</button>')
            html = html[:pos_p7_btn_end] + '\n' + nav_btn_html + html[pos_p7_btn_end:]
            print("✓ Botón añadido a nav-tabs.")
        else:
            print("⚠️ No se encontró botón p7 en nav-tabs.")
    else:
        print("ℹ️ El botón de nav-tabs ya estaba presente.")

    # 2. Agregar ítem en mobile drawer si no existe
    drawer_item_html = '''      <div class="drawer-item" onclick="selectDrawerTab('solucion-practico8')">
        <span>🔤 Práctico #8: Cadenas (40 Ejercicios & Delphi Form)</span>
        <span style="color: var(--accent-emerald);">➜</span>
      </div>
'''
    if "selectDrawerTab('solucion-practico8')" not in html:
        pos_drawer = html.find('<div class="drawer-grid">')
        if pos_drawer != -1:
            insert_pos = pos_drawer + len('<div class="drawer-grid">\n')
            html = html[:insert_pos] + drawer_item_html + html[insert_pos:]
            print("✓ Ítem añadido al menú drawer móvil.")
        else:
            print("⚠️ No se encontró drawer-grid.")
    else:
        print("ℹ️ El ítem de drawer ya estaba presente.")

    # 3. Insertar o actualizar la sección solucion-practico8
    p8_html_content = p8_gen.build_p8_html()
    if 'id="solucion-practico8"' in html:
        # Reemplazar la sección existente
        sec_start = html.find('<section id="solucion-practico8"')
        marker_end = '<!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #8'
        sec_end = html.find(marker_end, sec_start)
        if sec_end != -1:
            sec_end = html.find('-->', sec_end) + len('-->')
        else:
            sec_end = html.find('</section>', sec_start) + len('</section>')
        html = html[:sec_start] + p8_html_content + html[sec_end:]
        print("✓ Sección solucion-practico8 REEMPLAZADA con datos corregidos.")
    else:
        pos_p7 = html.find('id="solucion-practico7"')
        if pos_p7 != -1:
            pos_p7_end = html.find('</section>', pos_p7) + len('</section>')
            html = html[:pos_p7_end] + '\n\n' + p8_html_content + html[pos_p7_end:]
            print("✓ Sección solucion-practico8 insertada con los 40 ejercicios.")
        else:
            print("⚠️ No se encontró la sección solucion-practico7.")

    # 4. Insertar o actualizar el motor JavaScript
    p8_js_content = p8_gen.build_p8_js()
    js_marker = 'MOTOR JAVASCRIPT DEL SIMULADOR VCL Y PRÁCTICO #8'
    if js_marker in html:
        js_start = html.find('// ===========================================================================\n  //      ' + js_marker)
        if js_start == -1:
            js_start = html.find(js_marker)
            prev_line = html.rfind('// ===', 0, js_start)
            if prev_line != -1 and js_start - prev_line < 100:
                js_start = prev_line
        
        pos_last_script = html.rfind('</script>')
        html = html[:js_start] + p8_js_content + '\n' + html[pos_last_script:]
        print("✓ Motor JavaScript REEMPLAZADO con funciones corregidas.")
    else:
        pos_last_script = html.rfind('</script>')
        if pos_last_script != -1:
            html = html[:pos_last_script] + '\n\n' + p8_js_content + '\n' + html[pos_last_script:]
            print("✓ Motor JavaScript y simulador VCL insertado.")
        else:
            print("⚠️ No se encontró </script>.")

    # Guardar archivo actualizado
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Integración completada con éxito. Tamaño final del HTML: {len(html)} bytes.")

if __name__ == '__main__':
    integrate()
