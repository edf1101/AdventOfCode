from itertools import groupby
import numpy
import numpy as np

input_data = open('input.txt').read()
test_data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

data = input_data.split('\n')
grouper = groupby(data, key=lambda x: x == '')
new_data = []
for i, j in grouper:
    if not i:
        new_data.append(list(j))
data = new_data


def check_rows(mountain):
    for idx, row in enumerate(mountain):
        if  idx == len(mountain) - 1:
            continue
        # print(idx, row)

        mirror = True
        for i in range(0, min(idx + 1, len(mountain) - 1 - idx)):
            below = mountain[idx - i]
            above = mountain[idx + 1 + i]
            mirror = mirror and (below == above)
            # print(f'  below {below}  above {above}')
        if mirror:
            return idx
    return -1


def check_cols(mountain):
    new_arr = [''.join(s) for s in zip(*mountain)]
    return (check_rows(new_arr))


sum = 0
for idx, mountain in enumerate(data):
    # print(idx)
    # print(f'{idx},{check_rows(mountain)},{(check_cols(mountain))}')
    sum += (check_rows(mountain) + 1) * 100
    sum += check_cols(mountain)+1

print(sum)
