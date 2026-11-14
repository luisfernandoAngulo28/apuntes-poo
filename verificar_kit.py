# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('cadenas-exam-kit', 'Sección del kit'),
    ('kit-patrones', 'Módulo 1 Patrones'),
    ('kit-ascii', 'Módulo 2 ASCII'),
    ('kit-trampas', 'Módulo 3 Trampas'),
    ('kit-traza', 'Módulo 4 Traza'),
    ('kit-simulacro', 'Módulo 5 Simulacro'),
    ('kitProbarPatron', 'JS Patrón'),
    ('kitOrdConvert', 'JS ASCII'),
    ('kitIniciarTraza', 'JS Traza'),
    ('simuIniciar', 'JS Simulacro'),
    ('SIMU_BANCO', 'Banco de ejercicios'),
    ('kitVerificarConjunto', 'JS Conjuntos'),
]

all_ok = True
for chk, label in checks:
    ok = chk in text
    if not ok: all_ok = False
    print(f'{"✓" if ok else "✗"} {label}: {"ENCONTRADO" if ok else "FALTANTE"}')

print(f'\n{"✅ TODO CORRECTO" if all_ok else "❌ HAY PROBLEMAS"}')
print(f'HTML: {len(text):,} bytes | {len(text.splitlines()):,} líneas')
