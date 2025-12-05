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

def cmp(a,b):
    return a[0]<b[0]

fresh_data, availible_data = data[:data.index("")],data[1+data.index(""):]
fresh_data = [[int(i.split('-')[0]),int(i.split('-')[1])] for i in fresh_data]
fresh_data.sort(key=lambda x: x[0])

final_intervals = []

for fresh_interval in fresh_data:
    test_l,test_r = fresh_interval

    if len(final_intervals) ==0 or final_intervals[-1][1] < test_l:
        final_intervals.append(fresh_interval)
    else:
        final_intervals[-1][1] = max(final_intervals[-1][1],test_r)

count = 0
for fin in final_intervals:
    count+=fin[1]-fin[0]+1
print(count)

