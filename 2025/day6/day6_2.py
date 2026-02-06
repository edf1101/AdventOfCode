import numpy as np

test ="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

actual = open('input6.inp', 'r').read()

lines = actual.split('\n')
# 1. Find the length of the longest line
max_len = max(len(line) for line in lines)

# 2. Pad shorter lines with spaces so they match the max_len
padded_lines = [line.ljust(max_len) for line in lines]

# 3. Create the array
data = np.array([[x for x in line] for line in padded_lines]).transpose()

total = 0
char = ''
nums = []
print(data)
for row in data:

    if row[-1] in['+','*']:
        print(nums)
        print(char)
        if char =='*':
            total+=np.prod(nums)
        elif char =='+':
            total+=np.sum(nums)
        nums = []
        char = row[-1]
    join = ''.join(row[:-1]).strip()
    if join !='':
        nums.append(int(join))

if char =='*':
    total+=np.prod(nums)
elif char =='+':
    total+=np.sum(nums)
print(total)