test = """987654321111111
811111111111119
234234234234278
818181911112111"""

actual = open('input3.inp', 'r', encoding="utf-8").read()

data = actual.split('\n')
tot = 0
for line in data:
    max_opt = 0
    nums = [i for i in line]
    item1= max(nums[:-1])
    pos1 = nums[:-1].index(item1)
    rest = nums[1+pos1:]
    item2=max(rest)

    tot+= 10*int(item1) +int(item2)
print(tot)
