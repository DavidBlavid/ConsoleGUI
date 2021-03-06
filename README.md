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
# Adds a Diagram Widget with the name 'd1'
cg.add_widget('diagram', 'd1', 1, 1, 20, 20, 3)

# Sets the transparency of 'd1' to True
cg.widgets['d1'].set_transparent(True)
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
# Color  
While colored Text is currently not implemented, a brightness value can be simulated
by drawing specific characters from a gradient.

Currently there are two types of Gradient, a small and a large one.
```
Small Gradient:  .:-=+*#%@
Large Gradient:  .'´\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
 ```

To get a Gradient Character for a brightness value between [0, 1],
call _either gradient_value(p)_ or _gradient_value_small(p)_ from Color.py.

---
# Widgets:  
```
Widget Types:   - rect
                - text
                - textbox
                - gradient
                - variable
                - diagram
                - bar
                - container
                - table
```

Widgets with higher z values get draw over widgets with lower z values.

### Widget Functions
- **_set_transparent(transparent)_**  
    If a Widget is transparent its empty spaces do not get drawn,
    revealing the Widgets behind it.  
    ```Default: transparent = False```  
    ```Values:  True, False```
  

- **_get_type()_**  
    Returns the Type of the Widget.
  

- **_get_name()_**  
    Returns the Name of the Widget.


- **_set_pos(x, y)_**   
    Sets the Position of the Widget.
  
  
- **_get_pos()_**  
    Returns a tuple of the X, Y and Z of the Widget.
  

- **_get_size()_**  
    Returns a tuple of the Width and Height of the Widget.


- **_resize(width, height)_**   
    Sets the Scale of a Widget.

---

## Widget Types
### Rect 
Draws a filled Rectangle.  

- **_set_fill(char)_**   
    Sets the Character the Rectangle is filled with.  
    ```Default: fill_char = '#'```

### Ellipse
Draws a filled Ellipse  

- **_set_fill(fill_char, empty_char)_**   
    fill_char controls the Character the Ellipse is filled with.  
    empty_char controls the Character the Background of the Ellipse is filled with.  
    ```Default: fill_char = 'O', empty_char = ' '```
  
  
- **_set_scale(scale)_**   
    Sets the scale the Ellipse is drawn with.  
    scale < 1.0: Ellipse is smaller than borders.  
    scale = 1.0: Ellipse touches borders.  
    scale > 1.0: Ellipse is bigger than borders.  
    ```Default: scale = 1.0```  

### Text
Displays text with simple wrapping.

- **_set_text(new_text)_**  
  Changes the displayed Text.

### Textbox
Displays characters like **Text**, but with more control over them.

- **_set_text(new_text)_**  
  Changes the displayed Text, similar to **Text**.


- **_set_char(char, x, y)_**  
    Sets a single Character in the Textbox. 
  
  
- **_add_pattern(pattern, x, y, [transparent])_**  
    Imprints the Textbox with a pattern. The Pattern has to be an Array of Strings.  
    Example: ```pattern = ['123', '456', '789']```  
    Will be displayed as:
  ```
  123
  456
  789
    ```
  If transparent is set to True, spaces will not override symbols behind them.  
    ```Default: transparent = False```  
  

- **_clear()_**  
    Clears the Textbox.



### Gradient  
Like **Rect**, but filled with a Gradient.  

- **_set_direction(new_direction)_**  
    Sets the Direction of the Gradient.  
    ```Default: direction = 'right'```  
    ```Values:  'left', 'up', 'right', 'down'```
    
### Variable   
Displays the Name of a Variable with a Value next to it.  

- **_set_variable(name, value)_**  
    Adds a new Variable or sets the value of an existing one.  
    Values have to be continuosly updated or they will show old values.  
  
  
- **_remove_variable(name)_**  
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
  
  
### Container
A smaller canvas that can contain its own Widgets (and even other Containers!).  
Widgets get saved in an internal Dict. You can adress specific Widgets  
by calling the Dict with the Widgets name.  

The Z Values of Widgets inside the Container only matters to other Widgets inside the Container.  
Widgets outside the Container only care about the Containers Z Value.  

- **_add_widget(widget_type, name, x, y, width, height, [z])_**  
    Adds a Widget with specified type, name, position and scale.  
    Adding a Widget with an already existing name will overwrite the Widget.  
    Possible Values for widget_type can be found under **Widgets**.


- **_remove_widget(name)_**  
    Removes the Widget with the specified Name.
  
Example:
```
# Creates a Container with the name 'c1'
cg1.add_widget('container', 'c1', 35, 5, 30, 20)

# Creates the Rectangle 'c1_t1' within the Container 'c1'
cg1.widgets['c1'].add_widget('rect', 'c1_t1', 0, 0, 30, 20)

# Changes the Fill Character of the Rectangle
# Notice the Recursive widgets[] Calls
cg1.widgets['c1'].widgets['c1_t1'].set_fill('X')
```

### Table
Similar to a Textbox, a Table is an array of values. The difference is that
Tables contain numerical values instead of characters. These values get interpolated
between the min and max value of the Table and finally assigned a gradient value.

- **_set_min_max(new_min, new_max)_**  
  Sets the min and max value of the Table. All Values get interpolated between these.


- **_set_value(self, value, x, y):_**  
    Sets a single Value at a specified Position.
  
  
- **_set_gradient_type(type)_**  
  Sets the Gradient Type the Table uses. Check the Chapter **Color** for more info.  
  ```Default: type = 'large'```  
  ```Values:  'large', 'small'```  
  

- **_add_pattern(pattern, x, y, [transparent])_**  
    Imprints the Table with a pattern. The Pattern has to be an Array of Digits.  
    Example: ```pattern = [123, 456, 789]```  
    with a min of 0 and a max of 10 will be displayed as:
  ```
   .:
  -=+
  *#%
    ```
  If transparent is set to True, spaces will not override symbols behind them.  
  Warning! Adding Patterns with a min and max outside of 0-9 could cause
  unexpected Behavior.
    ```Default: transparent = False```  
  

- **_clear()_**  
    Clears the Table. Every Value gets set to the min value.