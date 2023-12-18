import numpy as np

input_data = open("input.txt").read()
test_data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

data = [[char for char in line] for line in input_data.split("\n")]
print(np.array(data))
print()


# shift the O entries to the top
for row_id,row in enumerate(data):
    # print(row)
    if row_id==0:
        continue
    # Shift this row down as far as possible
    for cell_id,cell in enumerate(row):
        if cell == 'O':

            max_shift = 0
            for shifted_up in range(1, row_id+2):
                if data[row_id-shifted_up][cell_id] != '.' or (row_id-shifted_up == -1 and data[row_id-shifted_up][cell_id] == '.'):
                    max_shift = shifted_up - 1
                    if max_shift > 0:
                        data[row_id - max_shift][cell_id] = 'O'
                        data[row_id][cell_id] = '.'

                    break

result = 0
for row_id,row in enumerate(data):
    # Shift this row down as far as possible
    for cell_id,cell in enumerate(row):
        if cell == 'O':
            result += len(data)-row_id

print(result)




