import ConsoleGUI as cg
import time
import math

# add a ConsoleGUI Object
cg1 = cg.CG()

tick = 0

width, height = cg1.get_size()

# Add some Widgets
cg1.add_widget('textbox', 'tb1', 0, 0, width - 1, height - 1)

#prepare some patterns
pattern_cube = ['...', '...', '...']
pattern_square = ['OOO', 'OOO', 'OOO']
pattern_empty = ['      ', '      ', '      ', '      ', '      ', '      ']
pattern_empty_pre = ['******', '******', '******', '******', '******', '******']

# update loop
while True:
    time.sleep(0.05)

    cg1.widgets['tb1'].add_pattern(pattern_cube, int((tick + math.sin(tick / 9) * 3) % (width - 1)),
                                   int((tick - math.cos(tick / 10 + 5) * 4) % (height - 1)))

    cg1.widgets['tb1'].add_pattern(pattern_square, int((tick + math.sin(tick / 11) * 6) % (width - 1)),
                                   int((tick + math.cos(tick / 8) * 5) % (height - 1)), True)

    # cg1.widgets['tb1'].add_pattern(pattern_cube, int(tick % (width - 1)),
    #                                int(tick % (height - 1)))

    # cg1.widgets['tb1'].add_pattern(pattern_square, int((tick+7) % (width - 1)),
    #                               int((tick) % (height - 1)))

    cg1.widgets['tb1'].add_pattern(pattern_empty_pre, int((- tick - 2) % (width - 1)),
                                   int((tick + 2) % (height - 1)))

    cg1.widgets['tb1'].add_pattern(pattern_empty, int(-tick % (width - 1)),
                                   int(tick % (height - 1)))

    # update the screen
    cg1.update()

    tick += 1
