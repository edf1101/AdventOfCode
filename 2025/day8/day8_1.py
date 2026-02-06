from math import sqrt,pow, inf
from functools import cache

inp = open('input8.inp',encoding='utf-8',mode='r').read()
test = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

all_boxes = [tuple(map(int, line.split(','))) for line in inp.split('\n')]

@cache
def dist(a,b):
    return sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2) + pow(a[2]-b[2],2))

edges = []

for i in range(len(all_boxes)):
    for j in range(i + 1, len(all_boxes)):
        d = dist(all_boxes[i], all_boxes[j])
        edges.append((d, all_boxes[i], all_boxes[j]))

edges.sort(key=lambda x: x[0])
circuits = []
connections_made = 0
last_b1, last_b2 = 0,0
for d, b1, b2 in edges:

    if  len(circuits)!=0 and len(circuits[0]) == len(all_boxes):
        print(last_b1[0]*last_b2[0])
        break

    sets_to_merge = []
    new_group = {b1, b2}

    for c in circuits:
        if not c.isdisjoint(new_group):
            sets_to_merge.append(c)
            new_group.update(c)


    for s in sets_to_merge:
        circuits.remove(s)


    circuits.append(new_group)

    connections_made += 1
    last_b1 = b1
    last_b2 = b2


print(circuits)
counts = [len(c) for c in circuits]
counts.sort()
print(counts)

print(counts[-1]*counts[-2]*counts[-3])