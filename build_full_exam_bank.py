# -*- coding: utf-8 -*-
"""
Full Generator for Banco Maestro de 7 Modelos de 2do Parcial (2022-2024)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Helper function to generate an exam card
def make_card(id_tag, title, date, points_info, img_path, summary_text, questions_html):
    return f'''
    <!-- TARJETA EXAMEN: {title} -->
    <div id="{id_tag}" style="background:rgba(15, 23, 42, 0.95); border:1px solid #334155; border-radius:12px; padding:1.6rem; margin-bottom:2.5rem; box-shadow:0 6px 24px rgba(0,0,0,0.4);">
      
      <!-- CABECERA EXAMEN -->
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem; border-bottom:1px solid #334155; padding-bottom:1.2rem; margin-bottom:1.4rem;">
        <div>
          <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.4rem;">
            <span style="font-size:1.5rem;">📄</span>
            <h3 style="color:#f8fafc; margin:0; font-size:1.35rem; font-weight:800;">{title}</h3>
          </div>
          <div style="font-size:0.88rem; color:#94a3b8; font-weight:500;">
            📅 Fecha / Semestre: <span style="color:#e2e8f0; font-weight:600;">{date}</span> • Docente: <span style="color:#38bdf8; font-weight:600;">M.Sc. Ing. Angélica Garzón C.</span>
          </div>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <span style="background:rgba(99, 102, 241, 0.2); color:#a5b4fc; border:1px solid rgba(99, 102, 241, 0.4); border-radius:6px; font-size:0.8rem; padding:0.35rem 0.75rem; font-weight:700;">
            {points_info}
          </span>
        </div>
      </div>

      <!-- FOTO DEL EXAMEN + RESUMEN -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.4rem; margin-bottom:1.8rem; background:rgba(30, 41, 59, 0.5); padding:1rem; border-radius:10px; border:1px solid rgba(255,255,255,0.06);">
        <div>
          <div style="font-size:0.85rem; color:#38bdf8; font-weight:700; margin-bottom:0.5rem; display:flex; align-items:center; gap:0.4rem;">
            📷 Fotografía Original del Examen Parcial:
          </div>
          <div style="border-radius:8px; overflow:hidden; border:1px solid #475569; max-height:260px; background:#000; text-align:center; position:relative;">
            <img src="{img_path}" alt="{title}" style="max-width:100%; max-height:260px; object-fit:contain; cursor:pointer;" onclick="window.open('{img_path}', '_blank')" title="Clic para abrir en grande">
          </div>
          <div style="font-size:0.75rem; color:#64748b; margin-top:0.3rem; text-align:center;">(Clic en la foto para ver en tamaño completo)</div>
        </div>
        <div style="display:flex; flex-direction:column; justify-content:center;">
          <div style="font-size:0.9rem; color:#f1f5f9; font-weight:700; margin-bottom:0.5rem;">📋 Estructura y Temas Evaluados:</div>
          <div style="font-size:0.88rem; color:#cbd5e1; line-height:1.6;">
            {summary_text}
          </div>
        </div>
      </div>

      <!-- PREGUNTAS RESUELTAS -->
      {questions_html}

    </div>
    '''

print("Card template ready.")

