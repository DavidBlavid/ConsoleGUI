import ConsoleGUI as cg
import time
import math

# add a ConsoleGUI Object
cg1 = cg.CG()

tick = 0

width, height = cg1.get_size()

# cg1.set_font("Consolas", 10)

# Add some Widgets
cg1.add_widget('diagram', 'd1', 22, 0, width - 18, 9, 3)
cg1.add_widget('variable', 'v1', 1, 1, 28, 5, 4)
cg1.add_widget('bar', 'b1', 1, 2, 19, 1, 4)
cg1.add_widget('ellipse', 'c1', 1, 9, 98, 21, 19, True)

# Add Lines
cg1.add_widget('rect', 'l1', 21, 0, 1, 9, 4)
cg1.add_widget('rect', 'l2', 0, 9, width, 1, 4)

# Set Line Fill
cg1.widgets['l1'].set_fill('|')
cg1.widgets['l2'].set_fill('-')

# Set the Widget Parameters
cg1.widgets['d1'].set_min_max(0, 0.99)
cg1.widgets['d1'].set_fill('#')
cg1.widgets['d1'].set_transparent(True)
cg1.widgets['d1'].set_fill_bar(True)
cg1.widgets['d1'].set_draw_axis(False)

cg1.widgets['v1'].set_transparent(True)

cg1.widgets['b1'].set_min_max(0, 0.99)
cg1.widgets['b1'].set_direction('left')
cg1.widgets['b1'].set_fill('=', '.')

cg1.widgets['c1'].set_fill('O', ' ')

# update loop
while True:

    time.sleep(0.05)

    # update the widgets values
    cg1.widgets['d1'].add_value(abs(math.sin(tick / 30) * 1))
    cg1.widgets['v1'].set_variable('Scale', abs(math.sin(tick/30) * 1))
    cg1.widgets['b1'].set_value(abs(math.sin(tick / 30) * 1))

    cg1.widgets['c1'].set_scale(abs(math.sin(tick / 30) * 1))

    # update the screen
    cg1.update()

    tick += 1
