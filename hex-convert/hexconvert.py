def hex_convert(hex_in):
    """Convert a hexidecimal string, like '1A', into it's decimal equivalent.

        >>> hex_convert('6')
        6

        >>> hex_convert('10')
        16

        >>> hex_convert('FF')
        255

        >>> hex_convert('FFFF')
        65535
"""

    #make dictionary for hex conversions where key = num/letter and value is value
    #get length of input.
    #start at first and convert to dec using dictionary. and multiply by 16**(len-1) then next would be 16**(len-2). 
    #keep that power variable that is updated each loop
    #update sum to be + next

    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    total = 0

    power = (len(hex_in) - 1)

    for i in range(len(hex_in)):

        dec_val = hex_dict.get(hex_in[i])
            
        total += (dec_val * (16**power))

        power -= 1

    return total

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
