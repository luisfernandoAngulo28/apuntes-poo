# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pos_p8 = text.find('id="solucion-practico8"')
print('pos_p8:', pos_p8)
if pos_p8 != -1:
    pos_end_sec = text.find('</section>', pos_p8)
    print('pos_end_sec:', pos_end_sec)
    print('Context around end of p8 section:')
    print(text[pos_end_sec-100:pos_end_sec+120])
