input_data = open('input.txt').read()
test_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def does_perform(parts, contiguousness):
    acc = []
    count = 0
    found = False
    for i in parts:
        if i == '#':
            found = True
            count += 1
        if i == '.':
            found = False
            if count:
                acc.append(count)
                count = 0
    if count:
        acc.append(count)
        count = 0
    return acc == contiguousness


data = test_data.split('\n')
sum = 0
for line in data:
    contiguousness = [int(i) for i in line.split()[1].split(',')]*1
    parts = ((line.split()[0]+'?')*1)[:-1]
    # print(parts, contiguousness)
    combos = 0
    possible_reps = []
    for idx, cell in enumerate(line):
        if cell == '?':
            possible_reps.append(idx)
    # print(possible_reps)
    n = len(possible_reps)
    for i in range(2 ** n, 2 ** (n + 1)):
        option = (bin(i)[3:])
        test_line = [i for i in line]
        for j, op in enumerate(option):
            # print(op)
            test_line[possible_reps[j]] = '#' if op == '1' else '.'
        test_line = ''.join(test_line)

        if does_perform(test_line, contiguousness):
            # print(test_line)
            combos += 1

    sum += combos
print(sum)
