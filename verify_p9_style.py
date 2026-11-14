# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('teoria_programacion_modular.html','r',encoding='utf-8') as f:
    h = f.read()
start = h.find('id="solucion-practico9"')
end_marker = h.find('<!-- FIN', start + 1000)
if end_marker == -1:
    end_marker = start + 300000
section = h[start:end_marker]

# El HTML escapa el código, así que buscar con entities
count_ni_esc = section.count('n,i:Byte')
count_ni_esc2 = section.count('n,i:byte')
count_ni_html = section.count('n,i:Byte') + section.count('n, i: Byte')
count_while_loop = section.count('i:=1;')
count_while_loop2 = section.count('i:=i+1;')
count_inc_old = section.count('Inc(')
count_for_old = section.count('for i := 1')

print(f'Sección P9 longitud: {len(section)} chars')
print(f'--- Estilo NUEVO (docente) ---')
print(f'  "n,i:Byte": {count_ni_esc}')
print(f'  "n,i:byte": {count_ni_esc2}')
print(f'  "i:=1;": {count_while_loop}')
print(f'  "i:=i+1;": {count_while_loop2}')
print(f'--- Estilo VIEJO (a eliminar) ---')
print(f'  "Inc(": {count_inc_old}')
print(f'  "for i := 1": {count_for_old}')

# Verificar un bloque de codigo pascal real
import re
# Buscar primer pre/code con pascal
matches = re.findall(r'ContarPalabra\(cad:String', section)
matches2 = re.findall(r'ContarPalabra\(texto, palabra', section)
print(f'\n"ContarPalabra(cad:String" (NUEVO): {len(matches)}')
print(f'"ContarPalabra(texto, palabra" (VIEJO): {len(matches2)}')

# Buscar con HTML entities
matches3 = section.count('function ContarPalabra')
print(f'"function ContarPalabra" total: {matches3}')

# Buscar lo que realmente está en el HTML (con HTML escape)
idx = section.find('function ContarPalabra')
if idx >= 0:
    snippet = section[idx:idx+300]
    print(f'\nSnippet real:\n{snippet}')
