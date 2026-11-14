# -*- coding: utf-8 -*-

def update_responsive_css():
    with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Enhanced responsive CSS block
    new_css = '''
    /* ==========================================================================
       RESPONSIVE MOBILE & TOUCH DESIGN SYSTEM (INF110-Z2)
       ========================================================================== */

    /* Touch-friendly Horizontal Navigation Tabs */
    .nav-tabs {
      display: flex;
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: thin;
      scrollbar-color: var(--accent-blue) rgba(255, 255, 255, 0.05);
      gap: 0.5rem;
      margin-bottom: 1.5rem;
      position: sticky;
      top: 0.5rem;
      z-index: 100;
      background: rgba(11, 17, 32, 0.95);
      padding: 0.6rem;
      border-radius: var(--radius-md);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
    }

    .nav-tabs::-webkit-scrollbar {
      height: 4px;
    }

    .nav-tabs::-webkit-scrollbar-track {
      background: rgba(255, 255, 255, 0.03);
      border-radius: 4px;
    }

    .nav-tabs::-webkit-scrollbar-thumb {
      background: var(--accent-blue);
      border-radius: 4px;
    }

    .nav-btn {
      flex: 0 0 auto;
      white-space: nowrap;
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 0.65rem 1.15rem;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    .nav-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.1);
    }

    .nav-btn.active {
      background: linear-gradient(135deg, var(--accent-blue), #0284c7);
      color: #ffffff;
      font-weight: 700;
      border-color: transparent;
      box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4);
    }

    /* Floating Scroll-to-Top FAB */
    .fab-scroll-top {
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent-blue), #0284c7);
      color: #ffffff;
      border: none;
      box-shadow: 0 6px 20px rgba(56, 189, 248, 0.4);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      font-weight: bold;
      z-index: 999;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      pointer-events: none;
    }

    .fab-scroll-top.visible {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    .fab-scroll-top:active {
      transform: scale(0.92);
    }

    /* Code block touch optimizations */
    .code-wrapper {
      position: relative;
      margin: 1rem 0;
      max-width: 100%;
    }

    .code-block {
      background: var(--code-bg);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.88rem;
      color: #e2e8f0;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      line-height: 1.65;
    }

    /* Table touch scroll indicators */
    .table-container {
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 1.25rem 0;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: rgba(11, 17, 32, 0.6);
    }

    .table-container table {
      min-width: 500px;
    }

    /* ==========================================================================
       MEDIA QUERIES ESPECÍFICAS PARA MÓVILES Y TABLETS
       ========================================================================== */

    @media (max-width: 1024px) {
      .container {
        padding: 1.5rem 1rem;
      }
      .delphi-buttons-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 768px) {
      .container {
        padding: 0.75rem 0.5rem;
      }

      header {
        padding: 1.5rem 1.2rem;
        border-radius: var(--radius-md);
        margin-bottom: 1.25rem;
      }

      h1 {
        font-size: 1.5rem;
        line-height: 1.25;
      }

      .subtitle {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
        font-size: 0.9rem;
      }

      .header-top-actions {
        flex-direction: column;
        align-items: stretch;
      }

      .btn-print {
        width: 100%;
        justify-content: center;
        padding: 0.6rem;
      }

      .card {
        padding: 1.25rem 1rem;
        border-radius: var(--radius-sm);
        margin-bottom: 1.25rem;
      }

      .card-title {
        font-size: 1.15rem;
        flex-direction: column;
        align-items: flex-start;
      }

      /* Formulario Delphi en Celular */
      .delphi-window {
        margin: 1rem 0;
        width: 100%;
        border-radius: 4px;
      }

      .delphi-body {
        padding: 1rem 0.75rem;
        gap: 1rem;
      }

      .delphi-header-label {
        font-size: 1.1rem;
      }

      .delphi-form-row {
        flex-direction: column;
        align-items: stretch;
        gap: 0.4rem;
      }

      .delphi-form-label {
        width: 100%;
        font-size: 0.82rem;
      }

      .delphi-form-edit {
        width: 100%;
        font-size: 1rem;
        padding: 0.65rem 0.75rem;
      }

      .delphi-btn-vcl {
        width: 100%;
        padding: 0.75rem 0.5rem;
        font-size: 0.9rem;
        min-height: 44px; /* Touch friendly standard */
      }

      .delphi-buttons-grid {
        grid-template-columns: 1fr;
        gap: 0.5rem;
      }

      .delphi-console-log {
        font-size: 0.78rem;
        padding: 0.75rem;
        word-break: break-word;
      }

      /* Acordeones y preguntas */
      .qa-header {
        padding: 0.9rem 1rem;
        font-size: 0.95rem;
        gap: 0.5rem;
      }

      .qa-body {
        padding: 0.75rem 1rem 1rem 1rem;
      }

      .qa-number {
        font-size: 0.75rem;
        padding: 0.15rem 0.45rem;
      }

      /* Grid de tarjetas */
      .tag-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
      }

      .tag-card {
        padding: 1rem;
      }

      /* Tablas */
      th, td {
        padding: 0.6rem 0.7rem;
        font-size: 0.82rem;
      }

      /* Bloques de código */
      .code-block {
        font-size: 0.8rem;
        padding: 1rem 0.75rem;
      }

      .copy-btn {
        top: 0.4rem;
        right: 0.4rem;
        padding: 0.25rem 0.5rem;
        font-size: 0.7rem;
      }

      /* Buscador */
      .qa-search-box input {
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
      }
    }

    @media (max-width: 480px) {
      h1 {
        font-size: 1.35rem;
      }

      .nav-btn {
        padding: 0.55rem 0.9rem;
        font-size: 0.82rem;
      }

      .card {
        padding: 1rem 0.75rem;
      }

      .fab-scroll-top {
        bottom: 1rem;
        right: 1rem;
        width: 42px;
        height: 42px;
        font-size: 1.1rem;
      }
    }
'''

    # Replace the existing media query at the end of style block
    media_start = html.find('@media (max-width: 768px)')
    if media_start != -1:
        style_end = html.find('</style>', media_start)
        html = html[:media_start] + new_css.strip() + "\n  " + html[style_end:]
    else:
        # insert before </style>
        style_end = html.rfind('</style>')
        html = html[:style_end] + "\n" + new_css.strip() + "\n" + html[style_end:]

    # Add Floating Action Button before </body> if not present
    if 'fab-scroll-top' not in html:
        fab_html = '''
  <!-- Botón flotante para volver arriba en celulares -->
  <button class="fab-scroll-top" id="fabScrollTop" onclick="scrollToNav()" title="Volver al menú de navegación">
    ↑
  </button>
'''
        body_end = html.rfind('</body>')
        html = html[:body_end] + fab_html + "\n" + html[body_end:]

    # Add JS helper for smooth scrolling and active tab centering
    js_responsive = '''
  // --- RESPONSIVIDAD Y NAVEGACIÓN EN MÓVILES ---
  function scrollToNav() {
    const nav = document.querySelector('.nav-tabs');
    if (nav) {
      nav.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  window.addEventListener('scroll', function() {
    const fab = document.getElementById('fabScrollTop');
    if (fab) {
      if (window.scrollY > 300) {
        fab.classList.add('visible');
      } else {
        fab.classList.remove('visible');
      }
    }
  });

  // Asegurar que la pestaña activa se centre en la barra horizontal táctil
  const origSwitchTab = window.switchTab;
  window.switchTab = function(tabId) {
    if (typeof origSwitchTab === 'function') {
      origSwitchTab(tabId);
    } else {
      document.querySelectorAll('.section-content').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      const targetSec = document.getElementById(tabId);
      if (targetSec) targetSec.classList.add('active');
    }
    // Centrar botón activo en celulares
    setTimeout(() => {
      const activeBtn = document.querySelector(`.nav-btn[onclick*="${tabId}"]`);
      if (activeBtn) {
        activeBtn.classList.add('active');
        activeBtn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      }
    }, 50);
  };
'''

    if 'fabScrollTop' not in html or 'scrollToNav' not in html:
        script_end = html.rfind('</script>')
        html = html[:script_end] + js_responsive + "\n" + html[script_end:]

    with open('teoria_programacion_modular.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("teoria_programacion_modular.html updated with complete mobile responsive design!")

if __name__ == '__main__':
    update_responsive_css()
