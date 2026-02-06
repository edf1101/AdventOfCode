from time import  perf_counter

test = """987654321111111
811111111111119
234234234234278
818181911112111"""

actual = open('input3.inp', 'r', encoding="utf-8").read()

data = actual.split('\n')
st = perf_counter()
tot = 0

for line in data:
    max_opt = 0
    length= len(line)
    nums= [int(i) for i in line]

    l=0
    r = length-11 # not inclusive

    for i in range(12):
        # find biggest in the l:r range
        r = length-11 +i
        biggest = max(nums[l:r])
        biggest_pos = nums[l:r].index(biggest)
        max_opt += (10**(11-i))*biggest
        l += 1+biggest_pos

    tot+=max_opt

end = perf_counter()
print(f'Took {end-st}')
print(tot)

