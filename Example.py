import ConsoleGUI as cg
import time
import math

# add a ConsoleGUI Object
cg1 = cg.CG()

tick = 0

width, height = cg1.get_size()

# Add some Widgets
cg1.add_widget('diagram', 'd1', 0, 0, width, height, 3)
cg1.add_widget('variable', 'v1', 1, 1, 28, 5, 4)
cg1.add_widget('bar', 'b1', 1, 2, 20, 1, 4)

# Set the Widget Parameters
cg1.widgets['d1'].set_min_max(1, 29)
cg1.widgets['d1'].set_fill('#')
cg1.widgets['d1'].set_transparent(True)
cg1.widgets['d1'].set_fill_bar(True)
cg1.widgets['d1'].set_draw_axis(False)

cg1.widgets['v1'].set_transparent(True)

cg1.widgets['b1'].set_min_max(0, 29)
cg1.widgets['b1'].set_direction('left')
cg1.widgets['b1'].set_fill('=', '.')

# update loop
while True:

    time.sleep(0.05)

    # update the widgets values
    cg1.widgets['d1'].add_value(math.sin(tick/15) * 15 + 15)
    cg1.widgets['v1'].set_variable('Height', math.sin(tick/15) * 15 + 15)
    cg1.widgets['b1'].set_value(math.sin(tick/15) * 15 + 15)

    # update the screen
    cg1.update()

    tick += 1
