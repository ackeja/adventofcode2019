import math
accumulated_fuel = 0
with open("input") as input:
    for mass in input:
        fuel = math.floor(int(mass)/3)-2
        accumulated_fuel = accumulated_fuel + fuel

    print(accumulated_fuel)