import numpy as np

input_data = open('input.txt').read()
test_data = r'''.|...L....
|.-.L.....
.....|-...
........|.
..........
.........L
..../.LL..
.-.-/..|..
.|....-|.L
..//.|....'''

data = np.array([[i for i in row] for row in input_data.split('\n')])
board_size = (data.shape[1], data.shape[0])  # x then y


def calc_energised(start_pos, start_dir):
    eng_array = np.array([['' for i in range(len(data[0]))] for j in range(len(data))])

    queue = [(start_pos, start_dir)]  # Start Queue with first position on the board
    dir_to_offset = {'E': (1, 0), 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0)}
    dir_mirror_table = {'E/': 'N', 'EL': 'S', 'W/': 'S', 'WL': 'N',
                        'N/': 'E', 'NL': 'W', 'SL': 'E', 'S/': 'W'}
    # print(data)
    while len(queue) > 0:
        look_at = queue.pop(0)
        position = np.array(look_at[0])
        direction = look_at[1]

        if direction not in eng_array[position[1]][position[0]]:
            if eng_array[position[1]][position[0]] == ' ':
                eng_array[position[1]][position[0]] = direction
            else:
                eng_array[position[1]][position[0]] += direction

        new_tile = data[position[1]][position[0]]
        if new_tile == 'L' or new_tile == '/':
            index = direction + new_tile
            direction = dir_mirror_table[index]

        if new_tile == '|' and direction in ['E', 'W']:
            queue.append((position, 'N'))
            queue.append((position, 'S'))
            continue

        if new_tile == '-' and direction in ['N', 'S']:
            queue.append((position, 'E'))
            queue.append((position, 'W'))
            continue

        while True:
            position += np.array(dir_to_offset[direction])

            if not (0 <= position[0] < board_size[0] and 0 <= position[1] < board_size[1]):
                # out of board
                break

            if direction not in eng_array[position[1]][position[0]]:
                if eng_array[position[1]][position[0]] == ' ':
                    eng_array[position[1]][position[0]] = direction
                else:
                    eng_array[position[1]][position[0]] += direction
            else:
                break

            new_tile = data[position[1]][position[0]]
            if new_tile == 'L' or new_tile == '/':
                index = direction + new_tile
                direction = dir_mirror_table[index]

            if new_tile == '|' and direction in ['E', 'W']:
                queue.append((position, 'N'))
                queue.append((position, 'S'))
                break

            if new_tile == '-' and direction in ['N', 'S']:
                queue.append((position, 'E'))
                queue.append((position, 'W'))
                break
    result = np.where(eng_array != '', 1, 0).sum()
    return result


# print(calc_energised((0, 0), 'E'))
max_result = 0
for x in range(board_size[0]):
    max_result = max(max_result, calc_energised((x, 0), 'S'))
    max_result = max(max_result, calc_energised((x, board_size[1] - 1), 'N'))

for y in range(board_size[0]):
    max_result = max(max_result, calc_energised((0, y), 'S'))
    max_result = max(max_result, calc_energised((board_size[0] - 1, y), 'N'))

print(max_result)
