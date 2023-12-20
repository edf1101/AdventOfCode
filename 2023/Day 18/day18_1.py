import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

input_data = open('input.txt').read()
test_data = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

lines = input_data.split('\n')
verts = [np.array((0,0))]

max_y, max_x, min_y, min_x = 0, 0, 0, 0
dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
pos = np.array((0,0))

edge_dis = 0

for line in lines:
    splitted = line.split()

    direction = np.array(dir_map[splitted[0]])
    dist = int(splitted[1])
    colour = splitted[2][1:-1]
    pos = (direction*dist + np.array(pos)).tolist()
    verts.append(pos)
    edge_dis += dist
    max_x = max(pos[0],max_x)
    max_y = max(pos[1],max_y)
    min_x = min(pos[0], min_x)
    min_y = min(pos[1], min_y)


polygon = Polygon(verts)
count = 0

# print(min_x,min_y,)
for y in range(min_y-1,max_y+1):
    for x in range(min_x-1,max_x+1):
        point = Point(x,y)
        if polygon.contains(point):
            count+=1
print(count+edge_dis)




