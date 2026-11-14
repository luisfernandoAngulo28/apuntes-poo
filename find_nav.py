# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('solucion-practico7')
print("Position:", pos)
print("Context around position:")
print(text[pos-200:pos+200])
