# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos_nav = text.find('class="nav-tabs"')
if pos_nav != -1:
    print('nav-tabs snippet:')
    print(text[pos_nav:pos_nav+800])
