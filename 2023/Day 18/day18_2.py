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
verts = [[0,0]]

dir_map = {3: (0, 1), 1: (0, -1), 2: (-1, 0), 0: (1, 0)}
pos = np.array((0,0))

boundary =0

for line in lines:
    splitted = line.split()

    hex_code = splitted[2][2:-1]
    direction = np.array(dir_map[int(hex_code[-1])])
    dist = int(hex_code[:5],16)
    # print(direction,dist)
    boundary += dist
    pos = (direction*dist + np.array(pos)).tolist()
    verts.append(pos)

# boundary += abs(verts[-1][0]-verts[0][0]) + abs(verts[-1][1]-verts[0][1])
#
# calculate area
verts.append(verts[0])
result = 0
for id in range(len(verts)):
    this_vert = verts[id]
    next_vert = verts[(id+1)%(len(verts))]

    result += (this_vert[0]*next_vert[1]) - (this_vert[1]*next_vert[0])
result = int(abs((boundary+result)/2)+1)
print(result + boundary)


