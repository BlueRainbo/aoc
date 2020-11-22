def calculate_fuel(mass):
    """Fuel required to launch a given module is based on its mass.

    Specifically, to find the fuel required for a module, take its mass,
    divide by three, round down, and subtract 2.

    >>> calculate_fuel(12)
    2

    >>> calculate_fuel(14)
    2

    >>> calculate_fuel(1969)
    654

    >>> calculate_fuel(100756)
    33583
    """
    return mass // 3 - 2 

def main():
    total_fuel = 0

    f = open('1a-input.txt')
    for x in f:
        i = int(x)
        r = calculate_fuel (i)
        total_fuel += r

    print(total_fuel)

import sys
if sys.argv[1] == '--test':
    import doctest
    doctest.testmod()
else:
    main()
