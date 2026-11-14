# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from generar_modulo_series import build_modulo_series_html

def integrate_series():
    print("Iniciando integración del módulo de Series VCL en HTML...")
    html_file = 'teoria_programacion_modular.html'

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Verificar si ya existe
    if 'id="lab-delphi-series-oficial"' not in html:
        modulo_html = build_modulo_series_html()

        # Insertar antes de lab-5pasos
        target_marker = '<div id="lab-5pasos"'
        pos_target = html.find(target_marker)
        if pos_target != -1:
            html = html[:pos_target] + modulo_html + '\n      ' + html[pos_target:]
            print("✓ Módulo VCL de Series insertado antes de lab-5pasos.")
        else:
            print("⚠️ No se encontró lab-5pasos.")

        # Añadir botón en el índice de series-y-herramientas
        idx_target = '<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">'
        pos_idx = html.find(idx_target)
        if pos_idx != -1:
            pos_insert_btn = pos_idx + len(idx_target)
            new_btn = '\n        <a href="#lab-delphi-series-oficial" class="btn-print" style="text-decoration:none; font-size:0.82rem; background:#0284c7; color:#ffffff; font-weight:800; border:1px solid #38bdf8;">🖥️ Formulario Delphi VCL Series (Clase)</a>'
            html = html[:pos_insert_btn] + new_btn + html[pos_insert_btn:]
            print("✓ Botón añadido al índice de series-y-herramientas.")

    # 2. Agregar código JS si no está
    js_series_code = """
// =============================================================================
// SIMULADOR DEL FORMULARIO DELPHI VCL DE SERIES (CLASE ING. GARZÓN)
// =============================================================================
let vclSeriesRegistradoN = 5;

function vclRegistrarNumero() {
  const inp = document.getElementById('vclSeriesInput');
  const val = parseInt(inp.value, 10);
  if (isNaN(val) || val < 1) {
    alert('Ingrese un número natural válido mayor a 0');
    return;
  }
  vclSeriesRegistradoN = val;
  const badge = document.getElementById('vclRegistradoBadge');
  badge.innerText = '✓ Registrado n = ' + val;
  badge.style.display = 'inline-block';
  document.getElementById('vclSeriesOutput').value = 'Registrado n=' + val;
}

function vclEjecutarSerie(tipo) {
  const n = vclSeriesRegistradoN || 5;
  let res = 0;
  if (tipo === 'doble') {
    let sum = 0, doble = 1, c = 1;
    while (n >= c) {
      sum += doble;
      doble *= 2;
      c++;
    }
    res = sum;
  } else if (tipo === 'factorial') {
    let sum = 0, fact = 1, c = 1;
    while (n >= c) {
      fact *= c;
      sum += fact;
      c++;
    }
    res = sum;
  } else if (tipo === 'cuadratica') {
    let sum = 0, c = 1;
    while (n >= c) {
      let cuad = c * c;
      sum += cuad;
      c++;
    }
    res = sum;
  }
  document.getElementById('vclSeriesOutput').value = res;
}

function seriesResetForm() {
  document.getElementById('vclSeriesInput').value = '5';
  document.getElementById('vclSeriesOutput').value = 'Resultado aquí...';
  document.getElementById('vclRegistradoBadge').style.display = 'none';
  vclSeriesRegistradoN = 5;
}
"""

    if 'function vclEjecutarSerie' not in html:
        pos_last_script = html.rfind('</script>')
        if pos_last_script != -1:
            html = html[:pos_last_script] + '\n\n' + js_series_code + '\n' + html[pos_last_script:]
            print("✓ Funciones JS de Series VCL añadidas a script.")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"🎉 Integración completada con éxito. Tamaño final: {len(html)} bytes.")

if __name__ == '__main__':
    integrate_series()

