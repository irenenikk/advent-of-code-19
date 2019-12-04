import sys
import numpy as np

def has_duplicate(digits):
    digit_str = str(digits)
    for i in range(1, len(digit_str)):
        if int(digit_str[i]) == int(digit_str[i-1]):
            return True
    return False

def is_increasing(digits):
    digit_str = str(digits)
    for i in range(1, len(digit_str)):
        if int(digit_str[i]) < int(digit_str[i-1]):
            return False
    return True

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = open(inp_file, "r").read()
    start, end = inp.split('-')
    start = int(start)
    end = int(end)
    valids = 0
    for i in range(start, end+1):
        if not is_increasing(i):
            continue
        if not has_duplicate(i):
            continue
        valids += 1
    print(valids)
