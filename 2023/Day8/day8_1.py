input_data = open('input.txt').read()
test_data1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''
test_data2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

data = input_data.split('\n')
instructions = data[0]
# parse node data
nodes = {}
for node_raw in data[2:]:
    key = node_raw.split('=')[0].strip()
    data_raw = node_raw.split('=')[1][2:-1].split(',')
    value = (data_raw[0].strip(),data_raw[1].strip())
    nodes[key] = value

node_look = 'AAA'
steps = 0
instruction_index = 0

while node_look != 'ZZZ':
    steps += 1
    print(node_look)
    instruction = instructions[instruction_index]
    instruction_index = (instruction_index+1)%(len(instructions))
    node_look = nodes[node_look][0 if instruction == 'L' else 1]
print(steps)


