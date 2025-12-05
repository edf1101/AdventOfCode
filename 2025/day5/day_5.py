test="""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

actual = open("input5.inp", 'r', encoding="utf-8").read()


data = actual.split('\n')
fresh_data, availible_data = data[:data.index("")],data[1+data.index(""):]

count = 0
for av in map(int,availible_data):
    # go through each fresh row check if in range
    for row in fresh_data:
        l,r = map(int,row.split('-'))
        if av<=r and av>=l:
            count+=1
            break
print(count)