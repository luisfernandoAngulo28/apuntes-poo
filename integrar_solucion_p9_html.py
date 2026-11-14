# -*- coding: utf-8 -*-
"""
Script de integración final para insertar la solución completa del Práctico #9
(31 Ejercicios de Cadenas, Funciones y Procedimientos) en teoria_programacion_modular.html.
"""

import sys
import shutil
import generar_seccion_practico09_html as p9_gen

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def integrate():
    input_file = 'teoria_programacion_modular.html'
    backup_file = 'teoria_programacion_modular.html.bak_before_p9'
    
    print("Creando respaldo de seguridad...")
    shutil.copyfile(input_file, backup_file)
    print(f"✓ Respaldo creado: {backup_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Agregar botón en nav-tabs si no existe
    nav_btn_html = '    <button class="nav-btn" data-cat="practicos" onclick="switchTab(\'solucion-practico9\')">🎯 4. Práctico #9: Cadenas, Func. &amp; Proc. (31 Ej.)</button>\n'
    if "switchTab('solucion-practico9')" not in html:
        target_p8_btn = "switchTab('solucion-practico8')"
        pos_p8_btn = html.find(target_p8_btn)
        if pos_p8_btn != -1:
            pos_btn_end = html.find('</button>', pos_p8_btn) + len('</button>')
            html = html[:pos_btn_end] + '\n' + nav_btn_html + html[pos_btn_end:]
            print("✓ Botón añadido a nav-tabs.")
        else:
            print("⚠️ No se encontró botón p8 en nav-tabs.")
    else:
        print("ℹ️ El botón de nav-tabs ya estaba presente.")

    # 2. Agregar ítem en mobile drawer si no existe
    drawer_item_html = '''          <div class="drawer-item" onclick="selectDrawerTab('solucion-practico9')">
            <span>🎯 Práctico #9: Cadenas Func. &amp; Proc. (31 Ej.)</span>
            <span style="color: #f59e0b;">➜</span>
          </div>\n'''
    if "selectDrawerTab('solucion-practico9')" not in html:
        pos_p8_dr = html.find("selectDrawerTab('solucion-practico8')")
        if pos_p8_dr != -1:
            pos_dr_end = html.find('</div>', pos_p8_dr) + len('</div>')
            html = html[:pos_dr_end] + '\n' + drawer_item_html + html[pos_dr_end:]
            print("✓ Ítem añadido al menú drawer móvil.")
        else:
            print("⚠️ No se encontró drawer-item p8.")
    else:
        print("ℹ️ El ítem de drawer ya estaba presente.")

    # 3. Insertar o actualizar la sección solucion-practico9
    p9_html_content = p9_gen.build_p9_html()
    if 'id="solucion-practico9"' in html:
        sec_start = html.find('<section id="solucion-practico9"')
        marker_end = '<!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #9'
        sec_end = html.find(marker_end, sec_start)
        if sec_end != -1:
            sec_end = html.find('-->', sec_end) + len('-->')
        else:
            sec_end = html.find('</section>', sec_start) + len('</section>')
        html = html[:sec_start] + p9_html_content + html[sec_end:]
        print("✓ Sección solucion-practico9 REEMPLAZADA con datos actualizados.")
    else:
        # Insertar después de solucion-practico8
        pos_p8 = html.find('id="solucion-practico8"')
        if pos_p8 != -1:
            marker_end_p8 = '<!-- FIN SECCIÓN SOLUCIÓN COMPLETA PRÁCTICO #8'
            pos_p8_end = html.find(marker_end_p8, pos_p8)
            if pos_p8_end != -1:
                pos_insert = html.find('-->', pos_p8_end) + len('-->')
            else:
                pos_insert = html.find('</section>', pos_p8) + len('</section>')
            html = html[:pos_insert] + '\n\n' + p9_html_content + html[pos_insert:]
            print("✓ Sección solucion-practico9 insertada con los 31 ejercicios.")
        else:
            print("⚠️ No se encontró la sección solucion-practico8.")

    # 4. Insertar o actualizar el motor JavaScript
    p9_js_content = p9_gen.build_p9_js()
    js_marker = 'MOTOR JAVASCRIPT DEL SIMULADOR VCL Y PRÁCTICO #9'
    if js_marker in html:
        js_start = html.find('// ===========================================================================\n  //      ' + js_marker)
        if js_start == -1:
            js_start = html.find(js_marker)
            prev_line = html.rfind('// ===', 0, js_start)
            if prev_line != -1 and js_start - prev_line < 100:
                js_start = prev_line
        
        marker_end_p9_js = 'Mostrando \' + visible + \' de 31 ejercicios del Práctico #9.'
        pos_end_js = html.find(marker_end_p9_js, js_start)
        if pos_end_js != -1:
            pos_end_js = html.find('}', pos_end_js)
            pos_end_js = html.find('}', pos_end_js + 1) + 1
        else:
            pos_end_js = html.rfind('</script>')
        html = html[:js_start] + p9_js_content + '\n' + html[pos_end_js:]
        print("✓ Motor JavaScript de Práctico #9 REEMPLAZADO.")
    else:
        pos_last_script = html.rfind('</script>')
        if pos_last_script != -1:
            html = html[:pos_last_script] + '\n\n' + p9_js_content + '\n' + html[pos_last_script:]
            print("✓ Motor JavaScript y simulador VCL de Práctico #9 insertado.")
        else:
            print("⚠️ No se encontró </script>.")

    # Guardar archivo actualizado
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Integración completada con éxito. Tamaño final del HTML: {len(html)} bytes.")

if __name__ == '__main__':
    integrate()

