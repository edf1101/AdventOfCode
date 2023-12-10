input_data = open('input.txt').read()
test_data = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''


def get_options(index):
    tile = data[index[1]][index[0]]
    options = []
    if index[0] != 0 and tile in ['S', '-', 'J', '7']:  # can check left
        if data[index[1]][index[0] - 1] in ['F', 'L', '-', 'S']:
            options.append((index[0] - 1, index[1]))
    if index[0] != len(data[0]) - 1 and tile in ['S', '-', 'F', 'L']:  # can check right
        if data[index[1]][index[0] + 1] in ['7', 'J', '-', 'S']:
            options.append((index[0] + 1, index[1]))
    if index[1] != 0 and tile in ['S', '|', 'J', 'L']:  # can check up
        if data[index[1] - 1][index[0]] in ['F', '7', '|', 'S']:
            options.append((index[0], index[1] - 1))
    if index[1] != len(data) - 1 and tile in ['S', '|', 'F', '7']:  # can check down
        if data[index[1] + 1][index[0]] in ['J', 'L', '|', 'S']:
            options.append((index[0], index[1] + 1))
    return options


data = input_data
# find the S
s_index = data.index('S')
data = data.split('\n')
s_index = (s_index % (len(data[0]) + 1), s_index // (len(data[0]) + 1))
current = get_options(s_index)[0]
history = [s_index]
possibles = get_options(current)
while not (possibles[0] in history and possibles[1] in history):
    possibles = get_options(current)

    history.append(current)
    if possibles[0] not in history:
        current = possibles[0]
    if possibles[1] not in history:
        current = possibles[1]

print(len(history)/2)