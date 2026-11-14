# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="mobileDrawer"')
if pos == -1: pos = text.find('class="drawer')
if pos != -1:
    pos_end = text.find('</div>\n    </div>', pos)
    print("Drawer found at pos:", pos)
    print(text[pos:pos+2500])
