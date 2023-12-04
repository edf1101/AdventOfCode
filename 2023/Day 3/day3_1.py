input_data = open('input.txt').read()


def clamp(inp, ma, mi):
    return max(mi, min(ma, inp))


data = input_data.split('\n')
line_length = len(data[0])
sum = 0

for line_id, line in enumerate(data):
    look_at_num = False
    num = ''
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
                    if item not in '1234567890.':
                        found_symb = True

        if look_at_num is False and num != '':
            # just changed

            if found_symb:
                sum += int(num)
            num = ''
            found_symb = False
    if look_at_num:
        if found_symb:
            sum += int(num)
print(sum)
