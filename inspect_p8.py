with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('id="solucion-practico8"')
p_end = text.find('</section>', p)
print("Start:", p, "End:", p_end)
print(text[p:p+1000].encode('ascii', errors='replace').decode('ascii'))
