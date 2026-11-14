# -*- coding: utf-8 -*-
"""
Mejoras para optimizar la experiencia en dispositivos móviles (smartphones y tablets):
1. Meta tags de color de tema móvil (Android Chrome & iOS Safari).
2. Botón flotante 'Volver Arriba' optimizado para el pulgar en móviles.
3. Estilos táctiles (-webkit-overflow-scrolling: touch) para tablas y códigos.
"""

import sys, shutil
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HTML_FILE = 'teoria_programacion_modular.html'
BAK_FILE = 'teoria_programacion_modular.html.bak'

shutil.copyfile(HTML_FILE, BAK_FILE)

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Meta tags en <head>
meta_tags = '''  <meta name="theme-color" content="#0b1120">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="format-detection" content="telephone=no">
'''

if 'name="theme-color"' not in html:
    pos_vp = html.find('name="viewport"')
    if pos_vp != -1:
        end_vp = html.find('>', pos_vp) + 1
        html = html[:end_vp] + '\n' + meta_tags + html[end_vp:]
        print('✓ Meta tags móviles añadidos en <head>.')

# 2. CSS para el botón flotante y toques móviles
mobile_css = '''
    /* ==========================================================================
       OPTIMIZACIONES MÓVILES ADICIONALES (TOUCH & PWA READY)
       ========================================================================== */
    /* Botón flotante volver arriba */
    #btnVolverArriba {
      position: fixed;
      bottom: 24px;
      right: 20px;
      z-index: 999;
      background: linear-gradient(135deg, #38bdf8, #2563eb);
      color: #0b1120;
      border: none;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4), 0 0 12px rgba(56, 189, 248, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      font-weight: 900;
      cursor: pointer;
      opacity: 0;
      visibility: hidden;
      transform: translateY(15px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      touch-action: manipulation;
    }
    #btnVolverArriba.visible {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }
    #btnVolverArriba:active {
      transform: scale(0.92);
    }
    @media (max-width: 768px) {
      #btnVolverArriba {
        bottom: 20px;
        right: 16px;
        width: 44px;
        height: 44px;
        font-size: 1.25rem;
      }
    }
    /* Suavizado de desplazamiento táctil */
    .table-responsive, pre, code, .code-block, div[style*="overflow-x:auto"] {
      -webkit-overflow-scrolling: touch;
      overscroll-behavior-x: contain;
    }
'''

if '#btnVolverArriba' not in html:
    pos_style_end = html.find('</style>')
    if pos_style_end != -1:
        html = html[:pos_style_end] + mobile_css + html[pos_style_end:]
        print('✓ Estilos móviles y botón flotante añadidos en <style>.')

# 3. HTML del botón flotante antes de </body>
btn_html = '''
  <!-- BOTÓN FLOTANTE VOLVER ARRIBA (OPTIMIZADO PARA MÓVILES) -->
  <button id="btnVolverArriba" onclick="volverArribaMovil()" title="Volver al inicio" aria-label="Volver arriba">
    ▲
  </button>
'''

if 'id="btnVolverArriba"' not in html:
    pos_body_end = html.rfind('</body>')
    if pos_body_end != -1:
        html = html[:pos_body_end] + btn_html + html[pos_body_end:]
        print('✓ Elemento HTML del botón flotante añadido.')

# 4. JS para el botón flotante
js_script = '''
  // ===========================================================================
  //      CONTROL DEL BOTÓN FLOTANTE "VOLVER ARRIBA" PARA MÓVILES
  // ===========================================================================
  function volverArribaMovil() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.addEventListener('scroll', () => {
    const btn = document.getElementById('btnVolverArriba');
    if (!btn) return;
    if (window.scrollY > 350) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });
'''

if 'volverArribaMovil' not in html:
    pos_script_end = html.rfind('</script>')
    if pos_script_end != -1:
        html = html[:pos_script_end] + js_script + html[pos_script_end:]
        print('✓ Script de scroll volver arriba añadido.')

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Optimización móvil completada: {HTML_FILE} ({len(html):,} bytes, {len(html.splitlines()):,} líneas)")
