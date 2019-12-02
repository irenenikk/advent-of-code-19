import math
import sys

def is_opcode(code):
    return code == 1 or code == 2 or code == 9

def operate(val1, val2, opcode):
    result = None
    if opcode == 1:
        result = val1 + val2
    elif opcode == 2:
        result = val1 * val2
    else:
        raise ValueError('Something went wrong :(')
        exit()
    return result

def calculate_intcode(inp):
    i = 0
    while (i < len(inp)):
        opcode = inp[i]
        if opcode == 99:
            return inp
        val1 = inp[i+1]
        val2 = inp[i+2]
        target_index = inp[i+3]
        result = operate(inp[val1], inp[val2], opcode)
        inp[target_index] = result
        i += 4
    return inp

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