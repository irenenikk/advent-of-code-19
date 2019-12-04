import sys
import numpy as np

def manhattan_distance(vec1, vec2):
    return sum([np.abs(x-y) for x, y, in zip(vec1, vec2)])

def read_instruction(x, y, instruction):
    if instruction.startswith('R'):
        return x + 1, y
    if instruction.startswith('L'):
        return x - 1, y
    if instruction.startswith('U'):
        return x, y - 1
    if instruction.startswith('D'):
        return x, y + 1

def paint_grid(grid, instructions, centre, color):
    x, y = centre
    intersection_distances = []
    for instr in instructions:
        length = int(instr[1:])
        for i in range(length):
            x, y = read_instruction(x, y, instr)
            if grid[y][x] > -1 and grid[y][x] != color:
                # coordinates have already been painted
                # by someone else
                dist = manhattan_distance([x, y], centre)
                intersection_distances.append(dist)
            grid[y][x] = color
    return intersection_distances

if __name__ == '__main__':
    inp_file = sys.argv[1]
    inp = [l.strip().split(',') for l in open(inp_file, "r").readlines()]
    grid_side = 50000
    centre = [grid_side//2] * 2
    grid = -1*np.ones((grid_side, grid_side))
    distances = []
    for i, instr in enumerate(inp):
        distances += paint_grid(grid, instr, centre, color=i)
    closest_intersection = np.min(distances)
    print(closest_intersection)