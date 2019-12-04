# this solution is super slow and probably not optimal
# it's essentially just simulating the problem
# ntohing fancy

import sys
import numpy as np
from first import read_instruction
from collections import defaultdict

def paint_grid_count_steps(grid, instructions, centre, color):
    """ Each wire traverses the grid and paints it with its own color. """
    x, y = centre
    steps_to_intersection = {}
    steps = 0
    for instr in instructions:
        length = int(instr[1:])
        for _ in range(length):
            x, y = read_instruction(x, y, instr)
            steps += 1
            if grid[y][x] > -1 and grid[y][x] != color:
                # coordinates have already been painted
                # by someone else
                steps_to_intersection[(x, y)] = steps
            grid[y][x] = color
    return steps_to_intersection

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = [l.strip().split(',') for l in open(inp_file, "r").readlines()]
    grid_side = 50000
    centre = [grid_side//2] * 2
    grid = -1*np.ones((grid_side, grid_side))
    steps = defaultdict(lambda: 0)
    # the painting needs to be run twice for the
    # first wire in order to be able to count all steps
    for i in list(range(len(inp))) + [0]:
        # use index of wire as the color
        step_dict = paint_grid_count_steps(grid, inp[i], centre, color=i)
        # both wires will find the same intersections
        # but necessarily in the same order
        # so we'll index them in a dict
        for k in step_dict.keys():
            steps[k] += step_dict[k]
    print(np.min(list(steps.values())))