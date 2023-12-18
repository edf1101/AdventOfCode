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


def get_row(mountain):
    for idx in range(1,len(mountain)):
        above_rows = mountain[:idx][::-1]  # reversed rows above
        below_rows = mountain[idx:]  # rows below
        sum_of_diffs = sum(sum(a != b for a, b in zip(x, y)) for x, y in zip(above_rows, below_rows))
        if sum_of_diffs == 1:
            return idx-1

    return -1


def check_cols(mountain):
    new_arr = [''.join(s) for s in zip(*mountain)]
    return (get_row(new_arr))


result = 0
for group in data:
    result += (get_row(group)+1) * 100
    result += get_row(tuple(zip(*group)))+1

print(result)
