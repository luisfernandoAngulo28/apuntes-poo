# -*- coding: utf-8 -*-
with open('teoria_programacion_modular.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_nav = text.find('<nav')
pos_nav_end = text.find('</nav>', pos_nav)
print('<nav> starts at:', pos_nav, 'ends at:', pos_nav_end)
print(text[pos_nav:pos_nav_end+6])

pos_drawer = text.find('<div class="drawer-grid">')
pos_drawer_end = text.find('</div>', pos_drawer)
print('\ndrawer-grid starts at:', pos_drawer)
print(text[pos_drawer:pos_drawer+500])
