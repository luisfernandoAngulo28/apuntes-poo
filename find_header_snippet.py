# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_h = text.find('<header>')
if pos_h != -1:
    pos_end_h = text.find('</header>') + len('</header>')
    print("Header snippet:")
    print(text[pos_h:pos_end_h])
