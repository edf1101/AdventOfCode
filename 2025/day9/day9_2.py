inp = open('input9.inp', encoding='utf-8', mode='r').read()

test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

lines = inp.strip().split('\n')

data = [tuple(map(int, line.split(','))) for line in lines]

def edges_of_polygon(points):
    for i in range(len(points)):
        yield points[i], points[(i + 1) % len(points)]


def is_edge_cutting_rect(p1, p2, r_min_x, r_max_x, r_min_y, r_max_y):
    # 1. Check if edge is Vertical
    if p1[0] == p2[0]:
        ex = p1[0]
        ey_min, ey_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        # A cut happens if the X is strictly inside Rect X bounds
        # AND the Y intervals overlap strictly
        if r_min_x < ex < r_max_x:
            # Check for interval overlap excluding simple touching
            if max(r_min_y, ey_min) < min(r_max_y, ey_max):
                return True

    # 2. Check if edge is Horizontal
    elif p1[1] == p2[1]:
        ey = p1[1]
        ex_min, ex_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        # A cut happens if the Y is strictly inside Rect Y bounds
        if r_min_y < ey < r_max_y:
            if max(r_min_x, ex_min) < min(r_max_x, ex_max):
                return True
    return False

max_a = 0
for i in range(len(data)):
    for t in range(i + 1, len(data)):

        minx = min(data[i][0], data[t][0])
        maxx = max(data[i][0], data[t][0])
        miny = min(data[i][1], data[t][1])
        maxy = max(data[i][1], data[t][1])

        valid = True

        for p1, p2 in edges_of_polygon(data):
            if is_edge_cutting_rect(p1, p2, minx, maxx, miny, maxy):
                valid = False
                break

        if valid: # Calculate Area if Valid
            max_a = max(max_a,(maxx - minx + 1) * (maxy - miny + 1))

print(max_a)