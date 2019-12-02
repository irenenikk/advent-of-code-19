import math
import sys

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

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = list(map(int, open(inp_file, "r").read().split(',')))
    # replace values according to instructions
    inp[1] = 12
    inp[2] = 2
    inp = calculate_intcode(inp)
    print(inp[0])