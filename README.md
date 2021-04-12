# ConsoleGUI  
A Python Graphics Library for the Console. Contains several Widgets.  
**STILL VERY MUCH WORK IN PROGRESS**  


![Project Example](https://raw.githubusercontent.com/DavidBlavid/ConsoleGUI/main/ConsoleGUI.png)

---
# Usage
First import ConsoleGUI and create a CG Object
```
import ConsoleGUI

cg = ConsoleGUI.CG()
```

Once you have a CG Object you can customize it or add Widgets.

Widgets get saved in an internal Dict. You can adress specific Widgets  
by calling the Dict with the Widgets name.
```
cg1.add_widget('diagram', 'd1', 1, 1, 20, 20, 3)
cg1.widgets['d1'].set_transparent(True)
```

For a proper example check out Example.py  


### CG Functions
- **_add_widget(widget_type, name, x, y, width, height, [z])_**  
    Adds a Widget with specified type, name, position and scale.  
    Adding a Widget with an already existing name will overwrite the Widget.  
    Possible Values for widget_type can be found under **Widgets**


- **_remove_widget(name)_**  
    Removes the Widget with the specified Name


- **_get_size()_**  
    Returns the size of the Screen in Charater Width and Height as a Tuple


- **_resize(width, height)_**  
    Sets the size of the Screen in Charater Width and Height.  
    ```Default: width = 100, height = 30```  
    


- **_update()_**  
    Updates the Screen.


---
# Widgets:  
```
Widget Types:   - rect
                - textbox
                - gradient
                - variable
                - diagram
                - bar
```

Widgets with higher z values get draw over widgets with lower z values.

### Widget Functions
- **_set_transparent(transparent)_**  
    If a Widget is transparent its empty spaces do not get drawn,
    revealing the Widgets behind it.
    The default value ist false.  
    ```Default: transparent = False```  
    ```Values:  True, False```
  

- **_get_type()_**  
    Returns the Type of a Widget


- **_set_pos(x, y)_**   
    Sets the Position of a Widget


- **_set_scale(width, height)_**   
    Sets the Scale of a Widget

---

## Widget Types
### Rect 
Draws a filled Rectangle.  

- **_set_fill(char)_**   
    Sets the Character the Rectangle is filled with.  
    ```Default: fill_char = '#'```  
   
  
### Textbox
Draws a Textbox.

- **_set_text(new_text)_**  
  Changes the displayed Text.
  

### Gradient  
Like Rect, but filled with a Gradient.  

- **_set_direction(new_direction)_**  
    Sets the Direction of the Gradient.  
    ```Default: direction = 'right'```  
    ```Values:  'left', 'up', 'right', 'down'```
    
### Variable   
Displays the Name of a Variable with a Value next to it.  

- **_set_variable(self, name, value)_**  
    Adds a new Variable or sets the value of an existing one.  
    Values have to be continuosly updated or they will show old values.  
  
  
- **_remove_variable(self, name)_**  
    Removes a Variable from the list.
  
### Diagram
Displays a Diagram. Values get drawn at a specific Y between a specified Range

- **_set_draw_axis(visible)_**  
    Controls whether the Axis get drawn.  
    ```Default: draw_axis = True```  
  
  
- **_set_fill_bar(visible)_**  
    Controls whether the whole bar under the Value gets drawn, or only
    the Value itself.  
    ```Default: fill_bar = False```  
  
  
- **_set_min_max(new_min, new_max)_**  
    Sets the Range in which the Values get drawn.  
    ```Default: min = 0, max = 10```  
  

- **_add_value(value)_**  
    Adds a value to the right-most side of the Diagram.  
    All other values get shifted left.
  

- **_set_fill(char)_**  
    Sets the Character the Values (and Bars) get drawn with.  
    ```Default: fill_char = 'X'```  
  

### Bar
Similar to a loading bar, it displays a value in a range as a bar.  

- **_set_min_max(new_min, new_max)_**  
    Changes the Range in which the value gets interpolated.  
    ```Default: min = 0, max = 10```  
  

- **_set_fill(fill_char, empty_char)_**  
    fill_char controls the Character the Bar is filled with.  
    empty_char controls the Character the Background of the Bar is filled with.  
    ```Default: fill_char = '=', empty_char = ' '```
  

- **_set_value(value)_**  
    Sets the to be displayed Value.  
    ```Default: value = 0```  
  
  
- **_set_direction(direction)_**  
    Sets the direction the Bar fills in.  
    ```Default: direction = 'left'```  
    ```Values:  'left', 'up', 'right', 'down'```
  
