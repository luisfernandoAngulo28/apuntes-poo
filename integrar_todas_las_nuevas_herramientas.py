# -*- coding: utf-8 -*-
"""
Script maestro de integración de las 4 nuevas herramientas interactivas:
1. Carrera Visual de los 5 Métodos de Ordenamiento
2. Laboratorio «Detecta y Corrige el Bug de Examen»
3. Entrenador de Prueba de Escritorio («Modo Llenar Tabla»)
4. Banco Maestro de 25 Preguntas Trampa Teóricas (Quiz Rápido)
"""

import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from generar_carrera_ordenamiento import build_carrera_ordenamiento_html
from generar_laboratorio_bugs import build_laboratorio_bugs_html
from generar_entrenador_traza import build_entrenador_traza_html
from generar_quiz_trampas import build_quiz_trampas_html

def integrate_all():
    print("Iniciando integración de las 4 herramientas interactivas...")
    html_file = 'teoria_programacion_modular.html'

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # =========================================================================
    # 1. INTEGRAR CARRERA DE ORDENAMIENTOS en ordenamiento-cadenas
    # =========================================================================
    carrera_html = build_carrera_ordenamiento_html()
    if 'id="raceInputVector"' not in html:
        marker_race = '<!-- 5. CÓDIGO DELPHI VCL LISTO PARA PEGAR'
        pos_race = html.find(marker_race)
        if pos_race != -1:
            html = html[:pos_race] + carrera_html + '\n\n      ' + html[pos_race:]
            print("✓ Carrera de Ordenamientos integrada en ordenamiento-cadenas.")
        else:
            print("⚠️ No se encontró marcador para Carrera de Ordenamientos.")
    else:
        print("ℹ️ La Carrera de Ordenamientos ya estaba presente.")

    # =========================================================================
    # 2. INTEGRAR ENTRENADOR DE TRAZA (LLENAR TABLA) en practica-activa-examenes
    # =========================================================================
    entrenador_html = build_entrenador_traza_html()
    if 'id="toolSection-entrenador"' not in html:
        # Añadir el botón en la barra de herramientas activas
        btn_entrenador = """        <button class="btn-print" id="btnToolEntrenador" onclick="switchToolActive('entrenador', this)" style="font-size: 0.9rem; padding: 0.6rem 1.2rem; display: flex; align-items: center; gap: 0.5rem; background: #0f172a; color: #c084fc; font-weight: 700; border: 1px solid #9333ea;">
          <span>✏️ 4. Entrenador de Traza (Llenar Tabla)</span>
        </button>\n"""
        pos_btn_ex = html.find('id="btnToolExamen"')
        if pos_btn_ex != -1:
            pos_btn_end = html.find('</button>', pos_btn_ex) + len('</button>')
            html = html[:pos_btn_end] + '\n' + btn_entrenador + html[pos_btn_end:]
            print("✓ Botón Entrenador de Traza añadido a la botonera de Práctica Activa.")

        # Añadir la sección del entrenador antes del fin de practica-activa-examenes
        marker_activa_end = '<!-- FIN SECCIÓN PRÁCTICA ACTIVA -->'
        pos_act_end = html.find(marker_activa_end)
        if pos_act_end != -1:
            html = html[:pos_act_end] + entrenador_html + '\n  ' + html[pos_act_end:]
            print("✓ Subpanel Entrenador de Traza añadido a practica-activa-examenes.")
    else:
        print("ℹ️ El Entrenador de Traza ya estaba presente.")

    # =========================================================================
    # 3. INTEGRAR LABORATORIO DE BUGS DE EXAMEN
    # =========================================================================
    bugs_html = build_laboratorio_bugs_html()
    if 'id="laboratorio-bugs-examen"' not in html:
        # Añadir botón nav en 'examenes'
        nav_btn_bug = '    <button class="nav-btn" data-cat="examenes" onclick="switchTab(\'laboratorio-bugs-examen\')">🧪 Laboratorio: Detecta el Bug de Examen</button>\n'
        pos_trampas = html.find("switchTab('trampas-delphi')")
        if pos_trampas != -1:
            pos_tb_end = html.find('</button>', pos_trampas) + len('</button>')
            html = html[:pos_tb_end] + '\n' + nav_btn_bug + html[pos_tb_end:]
            print("✓ Botón Laboratorio Bugs añadido a nav-tabs.")

        # Añadir ítem al drawer
        drawer_bug = '''          <div class="drawer-item" onclick="selectDrawerTab('laboratorio-bugs-examen')">
            <span>🧪 Laboratorio: Detecta el Bug de Examen</span>
            <span style="color: #f87171;">➜</span>
          </div>\n'''
        pos_dr_tr = html.find("selectDrawerTab('practica-activa-examenes')")
        if pos_dr_tr != -1:
            pos_dr_end = html.find('</div>', pos_dr_tr) + len('</div>')
            html = html[:pos_dr_end] + '\n' + drawer_bug + html[pos_dr_end:]
            print("✓ Ítem Laboratorio Bugs añadido al mobile drawer.")

        # Añadir sección antes de practica-activa-examenes o al final
        pos_sec_target = html.find('id="practica-activa-examenes"')
        if pos_sec_target != -1:
            pos_sec_insert = html.rfind('<section', 0, pos_sec_target)
            html = html[:pos_sec_insert] + bugs_html + '\n\n  ' + html[pos_sec_insert:]
            print("✓ Sección laboratorio-bugs-examen insertada.")
    else:
        print("ℹ️ La sección de Laboratorio Bugs ya estaba presente.")

    # =========================================================================
    # 4. INTEGRAR BANCO MAESTRO DE 25 PREGUNTAS TRAMPA TEÓRICAS (QUIZ UAGRM)
    # =========================================================================
    quiz_html = build_quiz_trampas_html()
    if 'id="banco-quiz-teorico"' not in html:
        # Añadir botón nav en 'examenes'
        nav_btn_quiz = '    <button class="nav-btn" data-cat="examenes" onclick="switchTab(\'banco-quiz-teorico\')">🧠 Banco: 25 Preguntas Trampa Teóricas</button>\n'
        pos_sim = html.find("switchTab('simulacro-examen')")
        if pos_sim != -1:
            pos_sim_end = html.find('</button>', pos_sim) + len('</button>')
            html = html[:pos_sim_end] + '\n' + nav_btn_quiz + html[pos_sim_end:]
            print("✓ Botón Banco Quiz añadido a nav-tabs.")

        # Añadir ítem al drawer
        drawer_quiz = '''          <div class="drawer-item" onclick="selectDrawerTab('banco-quiz-teorico')">
            <span>🧠 Banco: 25 Preguntas Trampa Teóricas</span>
            <span style="color: #fbbf24;">➜</span>
          </div>\n'''
        pos_dr_quiz = html.find("selectDrawerTab('practica-activa-examenes')")
        if pos_dr_quiz != -1:
            pos_dr_end = html.find('</div>', pos_dr_quiz) + len('</div>')
            html = html[:pos_dr_end] + '\n' + drawer_quiz + html[pos_dr_end:]
            print("✓ Ítem Banco Quiz añadido al mobile drawer.")

        # Añadir sección
        pos_sec_target2 = html.find('id="practica-activa-examenes"')
        if pos_sec_target2 != -1:
            pos_sec_insert2 = html.rfind('<section', 0, pos_sec_target2)
            html = html[:pos_sec_insert2] + quiz_html + '\n\n  ' + html[pos_sec_insert2:]
            print("✓ Sección banco-quiz-teorico insertada.")
    else:
        print("ℹ️ La sección Banco Quiz ya estaba presente.")

    # =========================================================================
    # 5. INTEGRAR EL CÓDIGO JS DE LAS 4 HERRAMIENTAS
    # =========================================================================
    with open('motor_herramientas_nuevas.js', 'r', encoding='utf-8') as f:
        js_tools = f.read()

    marker_tools_js = 'MOTOR DE LAS 4 NUEVAS HERRAMIENTAS ACTIVAS (EXAMEN UAGRM - INF110-Z2)'
    if marker_tools_js not in html:
        pos_last_script = html.rfind('</script>')
        if pos_last_script != -1:
            # Init calls
            init_code = """
// Inicialización automática de las nuevas herramientas
window.addEventListener('DOMContentLoaded', () => {
  if (typeof raceRenderInitial === 'function') raceRenderInitial();
  if (typeof bugCargarCaso === 'function') bugCargarCaso(0);
  if (typeof trainCargarEjercicio === 'function') trainCargarEjercicio();
  if (typeof quizRenderCurrent === 'function') quizRenderCurrent();
});
"""
            html = html[:pos_last_script] + '\n\n' + js_tools + '\n' + init_code + '\n' + html[pos_last_script:]
            print("✓ Motor JavaScript de las 4 herramientas insertado en el HTML.")

    # Guardar HTML final
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"🎉 Integración completada al 100%! Tamaño final del HTML: {len(html)} bytes.")

if __name__ == '__main__':
    integrate_all()

