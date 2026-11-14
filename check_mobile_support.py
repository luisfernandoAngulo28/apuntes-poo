import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('<!-- GRUPO 2: TAREAS DE CLASE S2-2026 -->')
print(text[start:start+800])
