import math
import time
import random
import tkinter as tk

import Widget

tick = 0

window_width = 100
window_height = 30

root = tk.Tk()

t = tk.Text(root, bg="black", fg="white", height=window_height, width=window_width)

widgets = {}
drawboard = [[(' ', -10) for i in range(30)] for j in range(100)]


def add_widget(widget_type, name, x, y, width, height, z=0):
    if widget_type in ('rect', 'Rect'):
        widgets[name] = Widget.Rect(name, x, y, width, height, z)
    elif widget_type in ('textbox', 'Textbox'):
        widgets[name] = Widget.Textbox(name, x, y, width, height, z)
    elif widget_type in ('gradient', 'Gradient'):
        widgets[name] = Widget.Gradient(name, x, y, width, height, z)
    elif widget_type in ('variable', 'Variable'):
        widgets[name] = Widget.Variable(name, x, y, width, height, z)
    elif widget_type in ('diagram', 'Diagram'):
        widgets[name] = Widget.Diagram(name, x, y, width, height, z)


def remove_widget(name):
    if name in widgets:
        del widgets[name]
    else:
        print("[Warning] Widget ", name, " does not exist. Deletion will be skipped")


def update_variables():
    pass


def update():

    update_variables()

    drawboard = [[(' ', -10) for i in range(30)] for j in range(100)]

    # insert widget text into drawboard array
    for current_widget in list(widgets.values()):

        current_text = current_widget.get_printable()

        current_width = current_widget.width
        current_height = current_widget.height

        current_x = current_widget.x
        current_y = current_widget.y
        current_z = current_widget.z

        current_transparent = current_widget.transparent

        for x in range(current_width):
            for y in range(current_height):
                # print(drawboard[current_x + x][current_y + y][1])
                # print(current_z)

                if 0 <= current_x + x < window_width and 0 <= current_y + y < window_height:

                    if drawboard[current_x + x][current_y + y][1] <= current_z:
                        # print("pos", current_x + x, current_y + y)
                        # print("x, y", x, y)

                        if not (current_text[y][x] == ' ' and current_transparent):

                            drawboard[current_x + x][current_y + y] = (current_text[y][x], current_z)
                            if drawboard[current_x + x][current_y + y][0] == '':
                                drawboard[current_x + x][current_y + y] = (' ', current_z)

    t.delete("1.0", "end")

    # insert Text into TKinter
    for y in range(window_height):
        word = ''
        for x in range(window_width):
            word += drawboard[x][y][0]
        word += "\n"
        t.insert(tk.END, word)

    root.update()


real_y = window_height - window_height // 3

# add_widget('gradient', 'grad', 0, window_height - window_height // 3, window_width, window_height // 3, 0)
# widgets['grad'].set_direction('down')
# widgets['grad'].set_transparent(True)

add_widget('diagram', 'd1', 0, 0, window_width + 2, window_height, 3)
add_widget('variable', 'v1', 70, 0, 28, 5, 4)

widgets['d1'].set_min_max(0, 29)
widgets['d1'].set_fill('#')
widgets['d1'].set_transparent(True)
widgets['d1'].set_fill_bar(True)
widgets['d1'].set_draw_axis(True)

widgets['v1'].set_transparent(True)

t.pack()

while True:
    time.sleep(0.05)
    update()

    # widgets['grad'].set_pos(0, real_y + int(math.sin(tick / 50) * 40))
    # widgets['grad'].height = window_height // 3 - int(math.sin(tick / 50) * 40)

    widgets['d1'].add_value(math.sin(tick/15) * 15 + 15)
    widgets['v1'].set_variable('Height', math.sin(tick/15) * 15 + 15)

    tick += 1
