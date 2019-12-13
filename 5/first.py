import math
import sys
import numpy as np

def parse_instruction(instr, params):
    div = 100
    parsed = []
    for i in range(params):
        mode = (instr // div) % 10
        div *= 10
        parsed.append(mode)
    return parsed

def num_of_params(code):
    if code == 4:
        return 1
    if code == 3:
        return 1
    if code == 1 or code == 2:
        return 3
    return 0

def operate(opcode, i, inp, step, *args):
    argvs = [a for a in args[0]]
    if opcode == 1:
        return sum(argvs[:2]), argvs[-1]
    elif opcode == 2:
        return np.multiply(argvs[0], argvs[1]), argvs[-1]
    elif opcode == 3:
        inp = input('Please give input for opcode 3: ')
        return int(inp), argvs[0]
    elif opcode == 4:
        print(argvs[0])
        return None, None
    else:
        raise ValueError('Invalid opcode :(')

def operate_with_modes(opcode, i, inp, modes, step):
    args = []
    j = i+1
    # the last mode is always position and can be skipped
    for mode in modes:
        if mode == 0:
            args += [inp[inp[j]]]
        elif mode == 1:
            args += [inp[j]]
        j += 1
    # if the opcode is not 4
    # the last parameter should be interpreted as a value
    if opcode != 4:
        args[-1] = inp[j-1]
    return operate(opcode, i, inp, step, args)

def calculate_intcode(inp):
    i = 0
    while (i < len(inp)):
        opcode = inp[i] % 100
        params = num_of_params(opcode)
        step = params+1
        modes = parse_instruction(inp[i], params)
        if opcode == 99:
            return inp
        result, target_index = operate_with_modes(opcode, i, inp, modes, step)
        if result is not None:
            inp[target_index] = result
        i += step
    return inp

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = list(map(int, open(inp_file, "r").read().split(',')))
    calculate_intcode(inp)
