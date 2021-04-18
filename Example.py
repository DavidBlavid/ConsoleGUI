import ConsoleGUI as cg
import time
import tkinter
import math

# add a ConsoleGUI Object
cg1 = cg.CG()

tick = 0

width, height = cg1.get_size()

# Add some Widgets

cg1.add_widget('diagram', 'd1', 0, 0, width-1, height-1, 0, True)
cg1.widgets['d1'].set_draw_axis(False)
cg1.widgets['d1'].set_min_max(0, 30)

cg1.add_widget('container', 'c1', 35, 5, 30, 20, 1, True)
cg1.widgets['c1'].add_widget('textbox', 'c1_t1', 0, 0, 30, 20, 1, True)

# Prepare some Patterns
pattern_cube = ['...', '...', '...']
pattern_square = ['OOO', 'OOO', 'OOO']
pattern_empty = ['  ', '  ']
pattern_empty_pre = ['******', '******', '******', '******', '******', '******']

# For convenience
textbox = cg1.widgets['c1'].widgets['c1_t1']

# update loop
while True:
    time.sleep(0.05)

    cg1.widgets['d1'].add_value(int(math.sin(tick/10) * 5 + 15))

    print(int(math.sin(tick/10) * 5 + 15))

    # Mouse Control
    if cg1.t.index(tkinter.INSERT) != '31.0' and tick != 0:

        mouse_y = int(cg1.t.index(tkinter.INSERT).split('.')[0])-1
        mouse_x = int(cg1.t.index(tkinter.INSERT).split('.')[1])

        cg1.widgets['c1'].set_pos(mouse_x, mouse_y)
        print(mouse_x, mouse_y)

    textbox.add_pattern(pattern_empty, (tick // 3) % 30, (tick // 4 - 6) % 20 % 20)

    textbox.add_pattern(pattern_cube, (tick // 5) % 30, (-tick // 3) % 20)
    textbox.add_pattern(pattern_square, (tick // 3) % 30, (tick // 4) % 20)

    # update the screen
    cg1.update()

    tick += 1
