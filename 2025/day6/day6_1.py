import numpy as np

test ="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

actual = open('input6.inp', 'r', encoding="utf-8").read()

data =[i.split() for i in  actual.split('\n')]
nums = np.array(data[:-1],dtype=np.int64).transpose()
ops = data[-1]

total = 0
for ind,char in enumerate(ops):
    if char =='+':
        total+=np.sum(nums[ind])
    elif char =='*':
        total+=np.prod(nums[ind])

print(total)
