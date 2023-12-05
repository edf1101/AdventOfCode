input_data = open('input.txt').read()
test_data = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
data = input_data.split('\n')

seed_data = data[0].split(':')[1].split()
seeds=[]
for i in range(0,len(seed_data),2):
    seeds.append(seed_data[i])
    seeds.append(str(int(seed_data[i])+int(seed_data[i+1])-1))
print(seeds)


# Create the maps as a dict
locations = ['']*len(seeds)
maps = []
map_data = []
writing =False
for line in data[1:]:
    if line=='':
        writing=False
    elif line[0].isalpha():
        writing=True

    if writing:
        map_data.append(line)
    else:
        if map_data!=[]:
            maps.append(map_data[1:])
            map_data=[]
maps.append(map_data[1:])

# print(maps)
found =False
check_i=0
while not found:
    # print('\n')
    # print(f'Trying {check_i}')
    value = check_i
    for step in reversed(maps):
        # print(step)
        # print(f'value = {value}')
        for option in step:
            option = option.split()
            if int(option[0]) <= value < int(option[0])+int(option[2]):
                # print(f'chosen {option}')
                value = int(option[1])-int(option[0])+value
                break

    # print(f'end value = {value}')
    for i in range(0, len(seed_data), 2):
        if value>=int(seeds[i]) and value<=int(seeds[i+1]):
            print(f'lowest is {check_i}')
            found = True
            break
    if found:
        break
    check_i+=1


