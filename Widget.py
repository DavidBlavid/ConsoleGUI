from Color import *

class Widget:
    def __init__(self, width, height, x, y, z=0):
        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        self.z = z

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

    def __init__(self, new_text, width, height, x, y, z=0):
        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        self.z = z

        self.align = "left"
        #print(new_text)
        self.set_text(new_text)

    def set_text(self, new_text):
        self.text = ['' for i in range(self.height)]
        length = len(new_text)
        counter = 0
        for y in range(self.height):
            for x in range(self.width):
                if(counter < length):
                    #print(new_text[counter])
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
                    widget_print[y] += p_char(x/self.width)
                elif self.direction == 'left':
                    widget_print[y] += p_char((self.width-x)/self.width)
                elif self.direction == 'up':
                    widget_print[y] += p_char((self.height-y)/self.height)
                elif self.direction == 'down':
                    widget_print[y] += p_char(y/self.height)

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
                widget_print[w[0]] += ' ' * (self.width-len(w[1]))

        return widget_print
