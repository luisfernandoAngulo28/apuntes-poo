# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('id="examen-final-oficial"', 'Sección Examen Final Oficial'),
    ('id="series-y-herramientas"', 'Sección Series y Herramientas'),
    ('ef-p1', 'P1: Precedencia'),
    ('ef-p2', 'P2: Constantes'),
    ('ef-p3', 'P3: Tipos de Datos'),
    ('ef-p4', 'P4: Serie Triangular'),
    ('ef-p5', 'P5: Dígitos Pares'),
    ('ef-p6', 'P6: Valor Absoluto'),
    ('ef-p7', 'P7: Vacunación COVID-19'),
    ('lab-5pasos', 'Bloque 1: Metodología 5 Pasos'),
    ('lab-generador-traza', 'Bloque 2: Generador de Traza en Vivo'),
    ('lab-catalogo-series', 'Bloque 3: Catálogo de Series'),
    ('efProbarDigitosPares', 'JS efProbarDigitosPares'),
    ('efProbarValorAbsoluto', 'JS efProbarValorAbsoluto'),
    ('efCovidAgregarPersona', 'JS efCovidAgregarPersona'),
    ('generarTrazaEnVivo', 'JS generarTrazaEnVivo'),
    ('verSerie', 'JS verSerie'),
    ('switchTab(\'examen-final-oficial\')', 'Nav Tab Examen Final'),
    ('switchTab(\'series-y-herramientas\')', 'Nav Tab Series y Herramientas'),
]

all_ok = True
for target, label in checks:
    ok = target in text
    if not ok: all_ok = False
    print(f'{"✓" if ok else "✗"} {label}: {"ENCONTRADO" if ok else "FALTANTE"}')

print(f'\n{"✅ TODO CORRECTO AL 100%" if all_ok else "❌ SE DETECTARON PROBLEMAS"}')
print(f'HTML final: {len(text):,} bytes, {len(text.splitlines()):,} líneas')
