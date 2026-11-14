# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('@media (max-width: 768px)')
while pos != -1:
    print('=== Snippet around media query ===')
    print(text[pos:pos+600])
    pos = text.find('@media (max-width: 768px)', pos+1)
