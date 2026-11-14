# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="series-y-herramientas"')
if pos != -1:
    print("Found series-y-herramientas at:", pos)
    print(text[pos:pos+2000])
else:
    print("Not found")

