from itertools import groupby

#  starting at 'in' go through the workflow each time theres a branch add it to the queue of places to investigate
#  The entry on said queue should be range restriction on all variables and what workflow it is.
#  A workflow only gets removed when you get to the default option of a workflow
# If the default option is A then add the restrictions to the accept list. To work out combinations
#  sum the number of combos for each accepted item. This is probs done by * the range of each var


input_data = open('input.txt').read()
test_data = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

data = test_data.split('\n')
grouper = groupby(data, key=lambda x: x == '')
new_data = []
for i, j in grouper:
    if not i:
        new_data.append(list(j))
data = new_data

workflows = {}

for workflow in data[0]:
    name = workflow.split('{')[0]
    outer_removed = workflow[workflow.index('{') + 1:-1]
    trials = outer_removed.split(',')
    trial_array = []
    for trial in trials:
        condition = None
        destination = trial
        if ':' in trial:
            destination = trial.split(':')[-1]
            condition = trial.split(':')[0]
            var = 'xmas'.index(condition[0])
            operator = condition[1]
            operand = condition[2:]
            condition = [var, operator, operand]
        trial_array.append([condition, destination])

    workflows[name] = trial_array

accepts = []
branches = [['in', (1, 4001), (1, 4001), (1, 4001), (1, 4001)]]
while branches:
    workflow, *part = branches.pop(0)
    for rule in workflows[workflow]:
        condition = rule[0]
        destination = rule[1]

        if condition is None:

            if destination == 'A':
                accepts.append(part)
            elif destination != 'R':
                branches.append([destination, *part])
            break

        category =condition[0]
        operator = condition[1]
        operand = int(condition[2])

        if operator == '>':
            filter_start = operand + 1
            filter_end = 4001
        else:
            filter_start = 0
            filter_end = operand

        part_start, part_end = part[category]

        start = max(part_start, filter_start)
        end = min(part_end, filter_end)

        if start < end:
            new_part = part.copy()
            new_part[category] = (start, end)
            if destination == 'A':
                accepts.append(new_part)
            elif destination != 'R':
                branches.append([destination, *new_part])

            if part_start < start:
                new_part = part.copy()
                new_part[category] = (part_start, start)
                branches.append([workflow, *new_part])
            if part_end > end:
                new_part = part.copy()
                new_part[category] = (end, part_end)
                branches.append([workflow, *new_part])
            break


distinct_combinations = 0
for accepted in accepts:
    combinations = 1
    for start, end in accepted:
        combinations *= end - start
    distinct_combinations += combinations

# 366876470872762
# 167409079868000
# 190898867611526
print(distinct_combinations)
