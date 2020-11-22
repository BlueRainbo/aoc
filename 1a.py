# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

def calculate_fuel(mass):
    return mass // 3 - 2 

total_fuel = 0

f = open('1a-input.txt')
for x in f:
    i = int(x)
    r = calculate_fuel (i)
    total_fuel += r

print(total_fuel)