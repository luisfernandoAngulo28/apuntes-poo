import re

with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section\s+id=["\']([^"\']+)["\']', text)
print('Existing sections:', sections)

navs = re.findall(r'switchTab\(["\']([^"\']+)["\']\)', text)
print('Existing switchTab calls:', list(dict.fromkeys(navs)))

