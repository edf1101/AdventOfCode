from heapq import heappop, heappush

input_data = open('input.txt').read()
test_data = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

data = [[int(i) for i in line] for line in input_data.split('\n')]

seen = set()
# loss, pos x, pos y, dir x, dir y, moves in dir
queue = [(0, 0, 0, 0, 0, 0)]

while queue:

    loss, pos_x, pos_y, dir_x, dir_y, n = heappop(queue)

    if pos_x == len(data[0]) - 1 and pos_y == len(data) - 1 and n >= 4:
        # if in final position
        print(loss)
        break

    if (pos_x, pos_y, dir_x, dir_y, n) in seen:
        continue
    seen.add((pos_x, pos_y, dir_x, dir_y, n))

    if n < 10 :
        new_pos_x = pos_x + dir_x
        new_pos_y = pos_y + dir_y

        if 0 <= new_pos_x < len(data) and 0 <= new_pos_y < len(data[0]):
            heappush(queue, (loss + data[new_pos_x][new_pos_y], new_pos_x, new_pos_y,
                             dir_x, dir_y, n + 1))

    if n >= 4 or (dir_x, dir_y) == (0, 0):
        for new_dir_x, new_dir_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (new_dir_x, new_dir_y) != (dir_x, dir_y) and (new_dir_x, new_dir_y) != (-dir_x, -dir_y):
                new_pos_x = pos_x + new_dir_x
                new_pos_y = pos_y + new_dir_y
                if 0 <= new_pos_x < len(data) and 0 <= new_pos_y < len(data[0]):
                    heappush(queue, (loss + data[new_pos_x][new_pos_y], new_pos_x, new_pos_y,
                                     new_dir_x, new_dir_y, 1))
