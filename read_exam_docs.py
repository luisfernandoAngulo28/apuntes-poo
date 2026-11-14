# -*- coding: utf-8 -*-
import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import docx
    print("python-docx is available!")
except ImportError:
    print("python-docx is NOT available, will install or use zipfile.")

folder = r"D:\Introz2\practico07\modelos de pasados 2do examen"
for f in os.listdir(folder):
    if f.endswith('.docx'):
        path = os.path.join(folder, f)
        print(f"\n=================== {f} ===================")
        try:
            doc = docx.Document(path)
            for p in doc.paragraphs:
                if p.text.strip():
                    print(p.text)
            for table in doc.tables:
                for row in table.rows:
                    print(" | ".join([c.text.strip().replace('\n', ' ') for c in row.cells]))
        except Exception as e:
            print(f"Error reading {f}: {e}")

