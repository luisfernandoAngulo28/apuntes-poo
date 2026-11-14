# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_pos = text.find('id="ejercicios-pizarra"')
end_pos = text.find('</section>', start_pos)
section_html = text[start_pos:end_pos+10]

with open('scratch_section_pizarra.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(section_html)

print("Length of section ejercicios-pizarra:", len(section_html))
