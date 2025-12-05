test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


actual = open("input4.inp", 'r', encoding="utf-8").read()

data = actual.split('\n')

# pad it out
for ind in range(len( data)):
    data[ind] = '.'+data[ind]+'.'
w = len(data[0])
data.insert(0,'.'*w)
data.append('.'*w)

valids = 0
changesMade = []
while len(changesMade)!=0 or valids == 0:
    changesMade = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '@':
                # check sides
                count = 0
                for test_x in [-1,0,1]:
                    if count >= 4:
                        break
                    for test_y in [-1,0,1]:
                        if count>=4:
                            break
                        if test_x == 0 and test_y==0:
                            continue
                        if data[y+test_y][x+test_x] =='@':
                            count +=1

                if count<4:
                    valids+=1
                    changesMade +=[(x,y)]

    # populate changes
    for (x,y) in changesMade:
        data[y] = data[y][:x] + '.' + data[y][x + 1:]




print(valids)