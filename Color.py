fill_types = [' ', '.', ',', ';', '-', '+', '%', 'X', '@', '#']

def p_char(p):
    if p >= 0. and p <= 1.:
        return fill_types[int(p//0.1)]
    return ' '
