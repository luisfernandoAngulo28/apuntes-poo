# -*- coding: utf-8 -*-
import os, zipfile

folder = r"D:\Introz2\practico07\modelos de pasados 2do examen"
with zipfile.ZipFile(os.path.join(folder, "2022-1.docx"), 'r') as z:
    z.extract('word/media/image1.png', folder)
    os.replace(os.path.join(folder, 'word', 'media', 'image1.png'), os.path.join(folder, '2022-1-exam.png'))

with zipfile.ZipFile(os.path.join(folder, "2023-1.docx"), 'r') as z:
    z.extract('word/media/image1.png', folder)
    os.replace(os.path.join(folder, 'word', 'media', 'image1.png'), os.path.join(folder, '2023-1-exam.png'))

if os.path.exists(os.path.join(folder, 'word')):
    import shutil
    shutil.rmtree(os.path.join(folder, 'word'))

print("Extracted 2022-1-exam.png and 2023-1-exam.png successfully!")

