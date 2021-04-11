# ConsoleGUI  
A Python Graphics Library for the Console. Contains several Widgets.  
**STILL VERY MUCH WORK IN PROGRESS**  

-------
# Widgets:  
Widgets can be added by using _add_widget(widget_type, name, x, y, width, height, [z])_.  
Widgets can be removed by using _remove_widget(name)_.  
Widgets can be customized by calling functions with _widgets[name].function()_.  

## Widget Types
**Rect**  
Draws a filled Rectangle.  
The Fill Character can be changed with set_fill(char)  
   
**Textbox**  
Draws an opaque Textbox.  
The Text can be changed with set_text(new_text)  
  
**Gradient**  
Like Rect, but filled with a Gradient.  
The Gradient Direction can be changed with set_direction({'up', 'right', 'down', 'left'})  
    
**Variable**  
Displays the Name of a Variable with a Value next to it.  
Variables can be added or set with set_variable(name, value) and removed with remove_variable(name)  
    

-------
# Additionaly
The z value controls the height of the Widget. Widgets with higher z values get drawn over those with low z values.  
Text will be cut off if the Widget is too small to display it. This applies to every Widget.  
The Values of Variables have to be updated continuosly with set_variable() or they will display old values.  
Widgets have a _transparent_ attribute that controls whether spaces get drawn over other widgets or not.
