import Widget


# Like a smaller Canvas inside the Canvas
class Container(Widget.Widget):

    widgets = {}

    # The next three Methods are pretty much the exact same from ConsoleGUI
    def add_widget(self, widget_type, name, x, y, width, height, z=0, transparent=False):
        if width > 0 and height > 0:
            if widget_type in ('rect', 'Rect'):
                self.widgets[name] = Widget.Rect(name, x, y, width, height, z, transparent)
            elif widget_type in ('text', 'Text'):
                self.widgets[name] = Widget.Text(name, x, y, width, height, z, transparent)
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
            elif widget_type in ('container', 'Container'):
                self.widgets[name] = Container(name, x, y, width, height, z, transparent)
            else:
                raise ValueError("add_widget() called from Container with unknown widget_type: widget_type = " +
                                 widget_type)
        else:
            raise ValueError("[Warning] add_widget() called from Container with illegal width and height: (" +
                             str(width) + ", " + str(height) + ")")

    def remove_widget(self, name):
        if name in self.widgets:
            del self.widgets[name]
        else:
            print("[Warning] Widget ", name, " does not exist. Deletion will be skipped")

    def get_printable(self):

        drawboard = [[(' ', -10) for i in range(self.height)] for j in range(self.width)]
        widget_print = ['' for i in range(self.height)]

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

                    if 0 <= current_x + x < self.width and 0 <= current_y + y < self.height:

                        if drawboard[current_x + x][current_y + y][1] <= current_z:
                            # print("pos", current_x + x, current_y + y)
                            # print("x, y", x, y)

                            if not (current_text[y][x] == ' ' and current_transparent):

                                drawboard[current_x + x][current_y + y] = (current_text[y][x], current_z)
                                if drawboard[current_x + x][current_y + y][0] == '':
                                    drawboard[current_x + x][current_y + y] = (self.empty_char, current_z)

        # insert Text widget_print
        for y in range(self.height):
            word = ''
            for x in range(self.width):
                word += drawboard[x][y][0]
            widget_print[y] = word

        return widget_print
