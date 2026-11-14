# -*- coding: utf-8 -*-
"""
Integración limpia y robusta del Kit Completo de Examen de Cadenas.
Lee desde teoria_programacion_modular.html.bak y genera teoria_programacion_modular.html.
"""

import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import generar_kit_examen_cadenas as kit

BAK_FILE = 'teoria_programacion_modular.html.bak'
OUT_FILE = 'teoria_programacion_modular.html'

with open(BAK_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Leído {BAK_FILE}: {len(html):,} bytes")

# 1. Agregar botón en nav-tabs (después de solucion-practico8)
p8_btn = "onclick=\"switchTab('solucion-practico8')\">"
idx_p8_btn = html.find(p8_btn)
if idx_p8_btn != -1:
    idx_end_btn = html.find('</button>', idx_p8_btn) + len('</button>')
    nav_btn_html = '\n    <button class="nav-btn" onclick="switchTab(\'cadenas-exam-kit\')">🎯 Kit Examen Cadenas (5 Módulos)</button>'
    html = html[:idx_end_btn] + nav_btn_html + html[idx_end_btn:]
    print("✓ Botón añadido en nav-tabs.")
else:
    print("⚠ No se encontró el botón solucion-practico8 en nav-tabs.")

# 2. Agregar ítem en drawer móvil
drawer_marker = '<div class="drawer-grid">'
idx_drawer = html.find(drawer_marker)
if idx_drawer != -1:
    idx_ins_drawer = idx_drawer + len(drawer_marker) + 1
    drawer_item_html = '''      <div class="drawer-item" onclick="selectDrawerTab('cadenas-exam-kit')">
        <span>🎯 Kit Examen: 5 Módulos Cadenas</span>
        <span style="color: var(--accent-emerald);">➜</span>
      </div>\n'''
    html = html[:idx_ins_drawer] + drawer_item_html + html[idx_ins_drawer:]
    print("✓ Ítem añadido en drawer móvil.")
else:
    print("⚠ No se encontró drawer-grid.")

# 3. Insertar la sección HTML del Kit después del cierre de </section> de solucion-practico8
pos_p8_sec = html.find('id="solucion-practico8"')
if pos_p8_sec != -1:
    pos_end_sec = html.find('</section>', pos_p8_sec) + len('</section>')
    kit_html = kit.build_exam_kit_html()
    html = html[:pos_end_sec] + '\n\n' + kit_html.strip() + '\n' + html[pos_end_sec:]
    print("✓ Sección <section id=\"cadenas-exam-kit\"> insertada correctamente.")
else:
    print("⚠ No se encontró id=\"solucion-practico8\".")

# 4. Insertar el JavaScript del Kit justo antes del último </script>
pos_last_script = html.rfind('</script>')
if pos_last_script != -1:
    kit_js = kit.build_exam_kit_js()
    html = html[:pos_last_script] + '\n\n' + kit_js.strip() + '\n\n' + html[pos_last_script:]
    print("✓ JavaScript del Kit insertado antes de </script>.")
else:
    print("⚠ No se encontró </script>.")

# Guardar
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Archivo guardado: {OUT_FILE} ({len(html):,} bytes, {len(html.splitlines()):,} líneas)")
