import numpy as np

input_data = open('input.txt').read()
test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

data = input_data.split('\n')
map = []

# space it out
for row in data:
    map.append([1 if i == '#' else 0 for i in row])

blank_rows = []
blank_cols = []
for idx, row in enumerate(map):
    if row == [0] * len(row):
        blank_rows.append(idx)

for idx, col in enumerate(np.array(map).transpose()):
    if col.sum() == 0:
        blank_cols.append(idx)
print(blank_rows, blank_cols)

positions = {}
count = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 1:
            positions[count] = (x, y)
            count += 1
permutations = set()
for k in list(positions.keys()):
    for other_key in positions.keys():
        if k != other_key:
            permutations.add(tuple(sorted([k, other_key])))

sum = 0
for path in permutations:
    start = positions[path[0]]
    end = positions[path[1]]
    # print(start,end)
    manhattan = abs(start[0] - end[0]) + abs(start[1] - end[1])
    for space in blank_rows:
        if start[1] < space < end[1] or end[1] < space < start[1]:
            manhattan += 1000000 - 1
    for space in blank_cols:
        if start[0] < space < end[0] or end[0] < space < start[0]:
            manhattan += 1000000 - 1
    sum += manhattan

print(sum)
