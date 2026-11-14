# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import re
import subprocess

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
print(f'Total script tags found: {len(scripts)}')

for idx, sc in enumerate(scripts):
    with open(f'_temp_test_{idx}.js', 'w', encoding='utf-8') as tf:
        tf.write(sc)
    
    res = subprocess.run(['node', '--check', f'_temp_test_{idx}.js'], capture_output=True, text=True)
    if res.returncode == 0:
        print(f'✓ Script #{idx + 1} syntax is 100% VALID!')
    else:
        print(f'❌ Script #{idx + 1} ERROR:')
        print(res.stderr)

import os
for idx in range(len(scripts)):
    if os.path.exists(f'_temp_test_{idx}.js'):
        os.remove(f'_temp_test_{idx}.js')
