inp = open('input9.inp',encoding='utf-8',mode='r').read()
test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

data = [tuple(map(int, line.split(','))) for line in inp.split('\n')]


max_a = 0
for i in range(len(data)):
    for t in range(i+1, len(data)):
        area = abs(data[i][0]-data[t][0]+1)* abs(data[i][1]-data[t][1]+1)
        # if (area > max_a):
        #     print(data[i],data[t])
        max_a = max(max_a,area)

print(max_a)