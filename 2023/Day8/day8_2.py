import math
input_data = open('input.txt').read()
test_data = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

data = input_data.split('\n')
instructions = data[0]
# parse node data
starting_nodes = []
nodes = {}
for node_raw in data[2:]:
    key = node_raw.split('=')[0].strip()
    data_raw = node_raw.split('=')[1][2:-1].split(',')
    value = (data_raw[0].strip(),data_raw[1].strip())
    nodes[key] = value
    if key[-1] == "A":
        starting_nodes.append(key)
print(starting_nodes)

ends_after = []
for node_look in starting_nodes:
    steps = 0
    instruction_index = 0

    while node_look[-1] != 'Z':
        steps += 1
        # print(node_look)
        instruction = instructions[instruction_index]
        instruction_index = (instruction_index+1)%(len(instructions))
        node_look = nodes[node_look][0 if instruction == 'L' else 1]
    ends_after.append(steps)

print(ends_after)
print(math.lcm(* ends_after))

