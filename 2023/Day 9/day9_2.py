input_data = open('input.txt').read()
test_data = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

histories = input_data.split('\n')

sum = 0


def calc_diff(list_inp):
    diffs = []
    for i in range(len(list_inp) - 1):
        diffs.append(list_inp[i + 1] - list_inp[i])
    return diffs


for idx,history in enumerate(histories):
    history = [int(i) for i in history.split()]
    hierarchy = [history]

    while hierarchy[-1] != [0] * len(hierarchy[-1]):
        hierarchy.append(calc_diff(hierarchy[-1]))

    hierarchy[-1].append(0)
    for i in range(len(hierarchy) - 1, 0, -1):
        i = i - 1
        hierarchy[i].insert(0,hierarchy[i][0] - hierarchy[i + 1][0])
    sum += (hierarchy[0][0])


print(sum)
