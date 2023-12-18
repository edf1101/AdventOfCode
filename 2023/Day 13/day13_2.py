from itertools import groupby


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

def find_mirror(group):
    for i in range(1, len(group)):
        above = group[:i][::-1]
        below = group[i:]
        if sum(sum(a != b for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return i

    return 0




groups = [tuple(group) for not_empty, group in groupby(data, bool) if not_empty]

res = 0
for group in groups:
    res += find_mirror(group) * 100
    res += find_mirror(tuple(zip(*group)))

print(res)