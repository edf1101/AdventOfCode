input_data = open('input.txt').read()
test_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

data = input_data.split(',')

def hash_func(inp):
    current_val = 0
    for char in inp:
        current_val += ord(char)
        current_val*=17
        current_val%=256
    return current_val

boxes ={i:[] for i in range(256)}
for string in data:
    operation = '-' if '-' in string else '='
    label = string.split(operation)[0]
    box = hash_func(label)
    focal_length = None if operation== '-' else string.split(operation)[1]
    print(label,box,operation,focal_length)

    if operation == '-':
        for i in boxes[box]:
            if i[:len(label)] == label:
                boxes[box].remove(i)

    if operation =='=':
        # check if any with same name
        changed = False
        for index, lens in enumerate(boxes[box]):
            if lens[:len(label)] == label:
                boxes[box][index] = label+' '+focal_length
                changed= True
                break
        if not changed:
            boxes[box].append(label+' '+focal_length)

result = 0
for box_num, box in boxes.items():
    for lens_num,lens in enumerate(box):
        focal_length = int(lens.split()[1])
        focusing_power = (box_num+1) * (lens_num+1) * focal_length
        result+= focusing_power

print(result)



