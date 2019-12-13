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
    if code >= 1 and code <= 2:
        return 3
    elif code >= 3 and code <= 4:
        return 1
    elif code >= 5 and code <= 6:
        return 2
    elif code >= 7 and code <= 8:
        return 3
    return 0

def operate(opcode, i, inp, step, *args):
    """ Returns the result, index it should be stored to, and the index to jump to if necessary. """
    argvs = [a for a in args[0]]
    if opcode == 1:
        return sum(argvs[:2]), argvs[-1], None
    elif opcode == 2:
        return np.multiply(argvs[0], argvs[1]), argvs[-1], None
    elif opcode == 3:
        inp = input('Please give input for opcode 3: ')
        return int(inp), argvs[0], None
    elif opcode == 4:
        print(argvs[0])
        return None, None, None
    elif opcode == 5:
        if argvs[0] != 0:
            return None, None, argvs[1]
        return None, None, None
    elif opcode == 6:
        if argvs[0] == 0:
            return None, None, argvs[1]
        return None, None, None
    elif opcode == 7:
        if argvs[0] < argvs[1]:
            return 1, argvs[2], None
        return 0, argvs[2], None
    elif opcode == 8:
        if argvs[0] == argvs[1]:
            return 1, argvs[2], None
        return 0, argvs[2], None
    else:
        raise ValueError('Invalid opcode :(')

def operate_with_modes(opcode, i, inp, modes, step):
    args = []
    j = i+1
    # the last mode is always position and can be skipped
    for mode in modes:
        #print('j', j)
        #print('inp[j]', inp[j])
        if mode == 0:
            args += [inp[inp[j]]]
        elif mode == 1:
            args += [inp[j]]
        j += 1
    # if the opcode is not 4
    # the last parameter should be interpreted as a value
    #print('args', args)
    if opcode < 4 or opcode > 6:
        args[-1] = inp[j-1]
    return operate(opcode, i, inp, step, args)

def calculate_intcode(inp):
    i = 0
    while (i < len(inp)):
        #print('i', i)
        opcode = inp[i] % 100
        #print('inp[i]', inp[i])
        #print('opcode', opcode)
        params = num_of_params(opcode)
        #print('params', params)
        step = params+1
        modes = parse_instruction(inp[i], params)
        #print('modes', modes)
        if opcode == 99:
            return inp
        result, target_index, new_i = operate_with_modes(opcode, i, inp, modes, step)
        if result is not None:
            #print('storing', result, 'to', target_index)
            inp[target_index] = result
        if new_i is not None:
            i = new_i
        else:
            i += step
    return inp

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = list(map(int, open(inp_file, "r").read().split(',')))
    calculate_intcode(inp)
