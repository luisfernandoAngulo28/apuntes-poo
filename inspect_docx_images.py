# -*- coding: utf-8 -*-
import sys, os, zipfile
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

folder = r"D:\Introz2\practico07\modelos de pasados 2do examen"
for f in os.listdir(folder):
    if f.endswith('.docx'):
        path = os.path.join(folder, f)
        print(f"\n=================== {f} ===================")
        with zipfile.ZipFile(path, 'r') as z:
            media = [m for m in z.namelist() if m.startswith('word/media/')]
            print(f"Contains {len(media)} images:")
            for m in media:
                print("  ", m)

