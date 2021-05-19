# Taken from http://paulbourke.net/dataformats/asciiart/
# <3
gradient_small = ' .:-=+*#%@'
gradient_large = " .'´\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def gradient_value_small(p):
    if 0. <= p <= 1.:
        return gradient_small[int(p / 0.1)]
    return ' '


def gradient_value(p):

    if 0. <= p <= 1.:
        return gradient_large[int(p * 68)]
    return ' '
