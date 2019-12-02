import math
import sys

def get_fuel(m):
    if m <= 0:
        return 0
    return m + get_fuel(m//3 - 2)

inp_file = sys.argv[1]
inp = open(inp_file, "r").read().splitlines()
print(sum([get_fuel(int(m)//3 - 2) for m in inp]))
