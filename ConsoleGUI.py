import tkinter as tk
import Widget


class CG:
    window_width = 100
    window_height = 30

    root = tk.Tk()

    caption = 'ConsoleGUI'

    t = tk.Text(root, bg="black", fg="white", height=window_height, width=window_width)
    t.pack()

    widgets = {}
    drawboard = []

    def add_widget(self, widget_type, name, x, y, width, height, z=0, transparent=False):
        if width > 0 and height > 0:
            if widget_type in ('rect', 'Rect'):
                self.widgets[name] = Widget.Rect(name, x, y, width, height, z, transparent)
            elif widget_type in ('textbox', 'Textbox'):
                self.widgets[name] = Widget.Textbox(name, x, y, width, height, z, transparent)
            elif widget_type in ('gradient', 'Gradient'):
                self.widgets[name] = Widget.Gradient(name, x, y, width, height, z, transparent)
            elif widget_type in ('variable', 'Variable'):
                self.widgets[name] = Widget.Variable(name, x, y, width, height, z, transparent)
            elif widget_type in ('diagram', 'Diagram'):
                self.widgets[name] = Widget.Diagram(name, x, y, width, height, z, transparent)
            elif widget_type in ('bar', 'Bar'):
                self.widgets[name] = Widget.Bar(name, x, y, width, height, z, transparent)
            elif widget_type in ('ellipse', 'Ellipse'):
                self.widgets[name] = Widget.Ellipse(name, x, y, width, height, z, transparent)
            else:
                print("[Warning] add_widget() called with unknown widget_type")
        else:
            print("[Warning] add_widget() called with illegal width and height: (" + str(width) + ", "
                  + str(height) + ")")

    def remove_widget(self, name):
        if name in self.widgets:
            del self.widgets[name]
        else:
            print("[Warning] Widget ", name, " does not exist. Deletion will be skipped")

    def get_size(self):
        return self.window_width, self.window_height

    def set_caption(self, caption):
        self.caption = caption
        self.root.title(caption)

    def get_caption(self):
        return self.caption

    def set_font(self, font, size):
        config = (font, size)
        self.t.configure(font = config)

    def resize(self, width, height):
        if width > 0 and height > 0:
            self.window_width = width
            self.window_height = height

            self.t.forget()

            self.t = tk.Text(self.root, bg="black", fg="white", height=height, width=width)
            self.t.pack()
        else:
            print("[Warning] resize() called with illegal width and height: (" + str(width) + ", " + str(height) + ")")

    def update(self):
        self.drawboard = [[(' ', -10) for i in range(self.window_height)] for j in range(self.window_width)]

        # insert widget text into drawboard array
        for current_widget in list(self.widgets.values()):

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

                    if 0 <= current_x + x < self.window_width and 0 <= current_y + y < self.window_height:

                        if self.drawboard[current_x + x][current_y + y][1] <= current_z:
                            # print("pos", current_x + x, current_y + y)
                            # print("x, y", x, y)

                            if not (current_text[y][x] == ' ' and current_transparent):

                                self.drawboard[current_x + x][current_y + y] = (current_text[y][x], current_z)
                                if self.drawboard[current_x + x][current_y + y][0] == '':
                                    self.drawboard[current_x + x][current_y + y] = (' ', current_z)

        self.t.delete("1.0", "end")

        # insert Text into TKinter
        for y in range(self.window_height):
            word = ''
            for x in range(self.window_width):
                word += self.drawboard[x][y][0]
            word += "\n"
            self.t.insert(tk.END, word)

        self.root.update()
