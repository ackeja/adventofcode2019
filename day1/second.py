import math

accumulated_fuel = 0
tmp_fuel0 = 0
tmp_fuel1 = 0
with open("input") as input:
    for mass in input:
        fuel = math.floor(int(mass) / 3) - 2
        tmp_fuel0 = fuel
        tmp_fuel1 = fuel
        while tmp_fuel0 >=6:
            tmp_fuel0 = math.floor(int(tmp_fuel0) / 3) - 2
            tmp_fuel1 = tmp_fuel1 + tmp_fuel0
        accumulated_fuel = accumulated_fuel + tmp_fuel1
    print(accumulated_fuel)