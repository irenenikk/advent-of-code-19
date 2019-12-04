import sys
import numpy as np
from first import is_increasing

def has_one_duplicate(digits):
    digit_str = str(digits)
    for i in range(len(digit_str)-1):
        if int(digit_str[i]) == int(digit_str[i+1]):
            if len(digit_str) == 2:
                # special case
                return True
            if i-1 < 0 and digit_str[i+2] != digit_str[i]:
                # duplicate in the beginning
                return True
            if i+2 >= len(digit_str) and digit_str[i-1] != digit_str[i]:
                # duplicate in the end
                return True
            if i-1 >= 0 and digit_str[i-1] != digit_str[i] and i+2 < len(digit_str) and digit_str[i+2] != digit_str[i]:
                # duplicate in the middle
                return True
    return False

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
        if not has_one_duplicate(i):
            continue
        valids += 1
    print(valids)
