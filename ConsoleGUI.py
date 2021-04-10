import tkinter as tk
from Widget import *
import time, math

tick = 0

window_width = 100
window_height = 30

root = tk.Tk()

t = tk.Text(root, bg="black", fg="white", height=window_height, width=window_width)

widget_list = []
drawboard = [[(' ',-10) for i in range(30)] for j in range(100)]

w1 = Gradient(window_width, window_height//3, 0, window_height - window_height//3, 2)
w1.set_direction('down')
widget_list.append(w1)

w2 = Textbox("TEST-" * 500, 98, 20, 1, 1, -1)
widget_list.append(w2)

w3 = Variable(15, 10, 2, 2, 3)
widget_list.append(w3)

w4 = Rect(17, 12, 1, 1, 2)
w4.set_fill('*')
widget_list.append(w4)

w5 = Rect(19, 14, 0, 0, 1)
w5.set_fill(' ')
widget_list.append(w5)

t.pack()

def update_variables():
    widget_list[2].set_variable('Y', window_height - window_height//3 + int(math.sin(tick/15)*5))
    widget_list[2].set_variable('Height',window_height//3 - int(math.sin(tick/15)*5))
    widget_list[2].set_variable('Tick',tick)

def update():

    update_variables()

    drawboard = [[(' ',-10) for i in range(30)] for j in range(100)]

    #insert widget text into drawboard array
    for current_widget in widget_list:
        
        current_text = current_widget.get_printable()
        
        current_width  = current_widget.width
        current_height = current_widget.height
        
        current_x = current_widget.x
        current_y = current_widget.y
        current_z = current_widget.z
        
        for x in range(current_width):
            for y in range(current_height):
                #print(drawboard[current_x + x][current_y + y][1])
                #print(current_z)
                if drawboard[current_x + x][current_y + y][1] <= current_z:
                    #print("pos", current_x + x, current_y + y)
                    #print("x, y", x, y)
                    drawboard[current_x + x][current_y + y] = (current_text[y][x], current_z)
                    if drawboard[current_x + x][current_y + y][0] == '':
                        drawboard[current_x + x][current_y + y] = (' ', current_z)

    t.delete("1.0", "end")

    #insert Text into TKinter
    for y in range(window_height):
        word = ''
        for x in range(window_width):
            word += drawboard[x][y][0]
        word += "\n"
        t.insert(tk.END, word)

    root.update()

real_y =  window_height - window_height//3

while True:
    time.sleep(0.05)
    update()

    
    
    widget_list[0].y = real_y + int(math.sin(tick/15)*5)
    widget_list[0].height = window_height//3 - int(math.sin(tick/15)*5)

    tick += 1
