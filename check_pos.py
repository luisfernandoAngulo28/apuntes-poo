# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length of html:', len(text))
pos1 = text.find('id="cadenas-exam-kit"')
print('find id="cadenas-exam-kit":', pos1)
pos2 = text.find('<section id="cadenas-exam-kit"')
print('find <section id="cadenas-exam-kit":', pos2)
pos3 = text.find('id="solucion-practico8"')
print('find id="solucion-practico8":', pos3)
