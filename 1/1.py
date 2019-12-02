import math
import sys

def get_fuel(m):
    return m//3 - 2

inp_file = sys.argv[1]
inp = open(inp_file, "r").read().splitlines()
print(sum([get_fuel(int(m)) for m in inp]))