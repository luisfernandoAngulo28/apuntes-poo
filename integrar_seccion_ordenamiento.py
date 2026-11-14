# -*- coding: utf-8 -*-
import sys, re
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from generar_seccion_ordenamiento import build_seccion_ordenamiento_html

def integrate_ordenamiento():
    print("Iniciando integración del Módulo de Ordenamiento en Cadenas...")
    html_file = 'teoria_programacion_modular.html'

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Agregar botón a nav-tabs si no existe
    nav_btn = '<button class="nav-btn" data-cat="tareas" onclick="switchTab(\'ordenamiento-cadenas\')">🔄 6. Pizarra: Ordenamiento (Burbuja, Selección, Shell &amp; QuickSort)</button>\n'
    if "switchTab('ordenamiento-cadenas')" not in html:
        target_tab = "switchTab('pizarra-cadenas-hoy')"
        pos_t = html.find(target_tab)
        if pos_t != -1:
            pos_end_btn = html.find('</button>', pos_t) + len('</button>')
            html = html[:pos_end_btn] + '\n    ' + nav_btn + html[pos_end_btn:]
            print("✓ Botón añadido a nav-tabs en categoría 'tareas'.")
        else:
            # Fallback en nav-tabs
            pos_nav = html.find('class="nav-tabs"')
            if pos_nav != -1:
                pos_first_btn = html.find('<button', pos_nav)
                html = html[:pos_first_btn] + nav_btn + html[pos_first_btn:]
                print("✓ Botón añadido al inicio de nav-tabs.")

    # 2. Agregar ítem en mobile drawer si no existe
    drawer_item = '''          <div class="drawer-item" onclick="selectDrawerTab('ordenamiento-cadenas')">
            <span>🔄 Pizarra: Métodos de Ordenamiento (Burbuja)</span>
            <span style="color: #38bdf8;">➜</span>
          </div>\n'''
    if "selectDrawerTab('ordenamiento-cadenas')" not in html:
        pos_dr = html.find("selectDrawerTab('pizarra-cadenas-hoy')")
        if pos_dr != -1:
            pos_dr_end = html.find('</div>', pos_dr) + len('</div>')
            html = html[:pos_dr_end] + '\n' + drawer_item + html[pos_dr_end:]
            print("✓ Ítem añadido al menú drawer móvil.")

    # 3. Insertar o actualizar la sección HTML
    seccion_html = build_seccion_ordenamiento_html()
    if 'id="ordenamiento-cadenas"' in html:
        start_sec = html.find('<section id="ordenamiento-cadenas"')
        end_marker = '<!-- FIN SECCIÓN ORDENAMIENTO CADENAS -->'
        end_sec = html.find(end_marker, start_sec)
        if end_sec != -1:
            end_sec += len(end_marker)
        else:
            end_sec = html.find('</section>', start_sec) + len('</section>')
        html = html[:start_sec] + seccion_html + html[end_sec:]
        print("✓ Sección ordenamiento-cadenas REEMPLAZADA/ACTUALIZADA.")
    else:
        # Insertar después de pizarra-cadenas-hoy
        pos_piz = html.find('id="pizarra-cadenas-hoy"')
        if pos_piz != -1:
            pos_piz_end = html.find('</section>', pos_piz) + len('</section>')
            html = html[:pos_piz_end] + '\n\n' + seccion_html + html[pos_piz_end:]
            print("✓ Sección ordenamiento-cadenas insertada después de pizarra-cadenas-hoy.")
        else:
            # Insertar antes de </main> o </body>
            pos_body = html.rfind('</body>')
            html = html[:pos_body] + '\n\n' + seccion_html + html[pos_body:]
            print("✓ Sección insertada antes de </body>.")

    # 4. Añadir la opción en el selector del Animador de Traza si no está
    opt_burbuja = '<option value="burbujaAsc">8. Pizarra: Ordenamiento Burbuja (Vector \'45123\' o \'mundo\')</option>'
    if 'value="burbujaAsc"' not in html:
        pos_opt = html.find('value="numDigitos"')
        if pos_opt != -1:
            pos_end_opt = html.find('</option>', pos_opt) + len('</option>')
            html = html[:pos_end_opt] + '\n                ' + opt_burbuja + html[pos_end_opt:]
            print("✓ Opción burbujaAsc añadida al selector del Animador de Traza en HTML.")

    # Guardar HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"🎉 HTML actualizado exitosamente ({len(html)} bytes).")

if __name__ == '__main__':
    integrate_ordenamiento()

