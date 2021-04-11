from Color import *


class Widget:
    def __init__(self, name, x, y, width, height, z=0, transparent=False):
        self.width = width
        self.height = height

        self.x = x
        self.y = y
        self.z = z

        self.name = name

        self.transparent = transparent

    def set_transparent(self, transparent):
        self.transparent = transparent

    def get_type(self):
        return self.__class__.__name__

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_scale(self, width, height):
        self.width = width
        self.height = height

    def get_printable(self):

        widget_print = []

        for x in range(self.width):
            widget_print.append('')
            for y in range(self.height):
                widget_print[x] += "?"
        return widget_print


class Rect(Widget):
    fill_char = '#'

    def set_fill(self, char):
        self.fill_char = char

    def get_printable(self):

        widget_print = []

        for y in range(self.height):
            widget_print.append('')
            for x in range(self.width):
                widget_print[y] += self.fill_char

        return widget_print


class Textbox(Widget):

    def set_text(self, new_text):
        self.text = ['' for i in range(self.height)]
        length = len(new_text)
        counter = 0
        for y in range(self.height):
            for x in range(self.width):
                if (counter < length):
                    # print(new_text[counter])
                    self.text[y] += new_text[counter]
                    counter += 1
                else:
                    self.text[y] += ' '

    def get_printable(self):

        return self.text


class Gradient(Widget):
    direction = 'right'

    def set_direction(self, new_direction):
        self.direction = new_direction

    def get_printable(self):

        widget_print = []

        for y in range(self.height):
            widget_print.append('')
            for x in range(self.width):
                if self.direction == 'right':
                    widget_print[y] += p_char(x / self.width)
                elif self.direction == 'left':
                    widget_print[y] += p_char((self.width - x) / self.width)
                elif self.direction == 'up':
                    widget_print[y] += p_char((self.height - y) / self.height)
                elif self.direction == 'down':
                    widget_print[y] += p_char(y / self.height)

        return widget_print


class Variable(Widget):
    values = {}

    def set_variable(self, name, value):
        self.values[name] = value

    def remove_variable(self, name):
        if name in self.values:
            del self.values[name]

    def get_printable(self):

        widget_print = ['' for i in range(self.height)]
        max_length = 0

        for v in self.values:
            max_length = max(len(v), max_length)

        for v in enumerate(self.values):
            current_v = v[1]

            widget_print[v[0]] = v[1] + ' ' * (max_length - len(v[1]) + 1) + str(round(self.values[v[1]], 2))

        for w in enumerate(widget_print):
            if len(w[1]) < self.width:
                widget_print[w[0]] += ' ' * (self.width - len(w[1]))

        return widget_print


class Diagram(Widget):
    min_value = 0
    max_value = 10
    fill_char = 'X'
    draw_axis = True

    def __init__(self, name, x, y, width, height, z=0, transparent=False):
        self.width = width
        self.height = height

        self.x = x
        self.y = y
        self.z = z

        self.name = name

        self.transparent = transparent

        self.values = [None] * width

    def set_draw_axis(self, visible):
        self.draw_axis = visible

    def set_min_max(self, new_min, new_max):
        min_value = new_min
        max_value = new_max

    def add_value(self, value):
        for i in range(self.width-3):
            self.values[i] = self.values[i+1]
        self.values[self.width-3] = value

    def set_fill(self, char):
        self.fill_char = char

    def set_scale(self, width, height):

        counter = 0

        if width > 2:
            next_values = [None] * (width - 2)

        if self.width > width:
            for i in range(self.width - width, self.width-2):
                next_values[counter] = self.values[i]
                counter += 1
            self.values = next_values

        elif self.width < width:
            for i in range(0, self.width - 2):
                next_values[width-self.width + counter] = self.values[i]
                counter += 1
            self.values = next_values

        self.width = width
        self.height = height

    def get_printable(self):

        widget_print = ['' for i in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                if x == y == 0 and self.draw_axis:
                    widget_print[y] += '⮝'
                elif x == 0 and y == self.height-1 and self.draw_axis:
                    widget_print[y] += '+'
                elif x == 0 and self.draw_axis:
                    widget_print[y] += '|'
                elif x == self.width-1 and y == self.height-1 and self.draw_axis:
                    widget_print[y] += '⮞'
                elif y == self.height-1 and self.draw_axis:
                    widget_print[y] += '-'
                else:
                    if self.values[x] is None:
                        widget_print[y] += ' '
                    else:
                        value_y = int((self.max_value - self.min_value) / self.height * (self.values[x] - self.min_value))
                        if value_y == self.height-1-y:
                            widget_print[y] += self.fill_char
                        else:
                            widget_print[y] += ' '

        return widget_print