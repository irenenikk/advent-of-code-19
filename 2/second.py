import math
import sys
from first import operate, calculate_intcode

def is_opcode(code):
    return code == 1 or code == 2 or code == 9

if __name__ == '__main__':
    inp_file = sys.argv[1]
    original_inp = list(map(int, open(inp_file, "r").read().split(',')))
    # replace values according to instructions
    for i in range(100):
        for j in range(100):
            inp = original_inp[:]
            inp[1] = i
            inp[2] = j
            inp = calculate_intcode(inp)
            if inp[0] == 19690720:
                print(100*inp[1] + inp[2])