# -*- coding: utf-8 -*-
"""
Integración del Examen Final Oficial 2-2020 y del Laboratorio de Series/Traza en teoria_programacion_modular.html
"""

import sys, os, shutil
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import generar_seccion_examen_final_y_herramientas as mod

HTML_FILE = 'teoria_programacion_modular.html'
BAK_FILE = 'teoria_programacion_modular.html.bak'

# 1. Crear respaldo
shutil.copyfile(HTML_FILE, BAK_FILE)
print(f"Respaldo creado: {BAK_FILE}")

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Leído {HTML_FILE}: {len(html):,} bytes, {len(html.splitlines()):,} líneas")

# 2. Agregar botones en nav-tabs (después de cadenas-exam-kit)
target_btn = "switchTab('cadenas-exam-kit')"
idx_btn = html.find(target_btn)
if idx_btn != -1:
    idx_end_btn = html.find('</button>', idx_btn) + len('</button>')
    nav_btns = '''
    <button class="nav-btn" onclick="switchTab('examen-final-oficial')">🏆 Examen Final Oficial (40 Ptos)</button>
    <button class="nav-btn" onclick="switchTab('series-y-herramientas')">📈 Series, Traza &amp; 5 Pasos</button>'''
    html = html[:idx_end_btn] + nav_btns + html[idx_end_btn:]
    print("✓ Botones de navegación añadidos en nav-tabs.")
else:
    print("⚠ No se encontró el botón de cadenas-exam-kit en nav-tabs.")

# 3. Agregar ítems en drawer móvil
drawer_target = "selectDrawerTab('cadenas-exam-kit')"
idx_drw = html.find(drawer_target)
if idx_drw != -1:
    idx_end_drw = html.find('</div>', idx_drw) + len('</div>')
    drawer_items = '''
      <div class="drawer-item" onclick="selectDrawerTab('examen-final-oficial')">
        <span>🏆 Examen Final Oficial 2-2020 (40 Ptos)</span>
        <span style="color: var(--accent-rose);">➜</span>
      </div>
      <div class="drawer-item" onclick="selectDrawerTab('series-y-herramientas')">
        <span>📈 Series, Traza &amp; 5 Pasos</span>
        <span style="color: var(--accent-emerald);">➜</span>
      </div>'''
    html = html[:idx_end_drw] + drawer_items + html[idx_end_drw:]
    print("✓ Ítems añadidos en drawer móvil.")
else:
    print("⚠ No se encontró el ítem cadenas-exam-kit en drawer.")

# 4. Insertar las 2 secciones HTML después de la sección cadenas-exam-kit
target_sec = 'id="cadenas-exam-kit"'
idx_sec = html.find(target_sec)
if idx_sec != -1:
    idx_end_sec = html.find('</section>', idx_sec) + len('</section>')
    sec1_html = mod.build_examen_final_html()
    sec2_html = mod.build_series_y_herramientas_html()
    nuevas_secciones = '\n\n' + sec1_html.strip() + '\n\n' + sec2_html.strip() + '\n'
    html = html[:idx_end_sec] + nuevas_secciones + html[idx_end_sec:]
    print("✓ Secciones <section id=\"examen-final-oficial\"> y <section id=\"series-y-herramientas\"> insertadas.")
else:
    print("⚠ No se encontró id=\"cadenas-exam-kit\".")

# 5. Insertar el motor JS antes del último </script>
idx_script = html.rfind('</script>')
if idx_script != -1:
    js_code = mod.build_exam_y_herramientas_js()
    html = html[:idx_script] + '\n\n' + js_code.strip() + '\n\n' + html[idx_script:]
    print("✓ Motor JavaScript insertado antes de </script>.")
else:
    print("⚠ No se encontró </script>.")

# Guardar
with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Integración completada: {HTML_FILE} ({len(html):,} bytes, {len(html.splitlines()):,} líneas)")
