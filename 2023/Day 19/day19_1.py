from itertools import groupby

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

data = input_data.split('\n')
grouper = groupby(data, key=lambda x: x == '')
new_data = []
for i, j in grouper:
    if not i:
        new_data.append(list(j))
data = new_data

parts = []
for part in data[1]:
    part = part[1:-1]
    part = [int(i[2:]) for i in part.split(',')]
    parts.append(part)

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

# print(workflows)
accepted = []

for part in parts:
    workflow_id = 'in'
    while workflow_id not in ['R', 'A']:
        workflow = workflows[workflow_id]
        for trial in workflow:
            condition = trial[0]
            destination = trial[1]
            if condition is not None:
                var = part[condition[0]]
                operator = condition[1]
                operand = int(condition[2])
                if (operator == '<' and var < operand) or (operator == '>' and var > operand):
                    workflow_id = destination
                    break
                continue
            else:
                workflow_id = destination
                break

    if workflow_id == 'A':
        accepted.append(part)
# print(accepted)
result = sum([sum(i) for i in accepted])
print(result)