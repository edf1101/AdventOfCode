input_data = open('input.txt').read()

test_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

def clamp(inp, ma, mi):
    return max(mi, min(ma, inp))


data = input_data.split('\n')
line_length = len(data[0])
sum = 0
adjacent_to ={}

for line_id, line in enumerate(data):
    look_at_num = False
    num = ''
    adjacency = []
    found_symb = False
    for char_id, char in enumerate(line):
        look_at_num = char in '1234567890'
        if look_at_num:
            num += char
            # check around
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:

                    try_pos = (
                        clamp(char_id + x_offset, line_length - 1, 0), clamp(line_id + y_offset, len(data) - 1, 0))
                    item = data[try_pos[1]][try_pos[0]]
                    if item == '*':
                        # found gear
                        adjacency.append(try_pos)

        if look_at_num is False and num != '':
            # just changed

            if len(adjacency):
                adjacency=list(set(adjacency))
                for i in adjacency:
                    if i in adjacent_to:
                        adjacent_to[i].append(num)
                    else:
                        adjacent_to[i]=[num]
                print(num)
                print(adjacency)

            num = ''
            adjacency=[]
            found_symb = False
    if look_at_num:

        if len(adjacency):
            adjacency = list(set(adjacency))
            for i in adjacency:
                if i in adjacent_to:
                    adjacent_to[i].append(num)
                else:
                    adjacent_to[i] = [num]
print(adjacent_to)
for i in adjacent_to.values():
    if len(i)==2:
        sum+= int(i[0])*int(i[1])
print(sum)
