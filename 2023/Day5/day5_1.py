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
data = test_data.split('\n')
seeds = data[0].split(':')[1].split()
locations = ['']*len(seeds)
# Create the maps as a dict
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
for seed_idx,seed in enumerate(seeds): # Go through each seed

    print('\n\n')
    value = int(seed)
    print(value)

    for step in maps: # Go through each map
        # print(value)
        for options in step:
            options = options.split()
            # print(options)

            if int(options[1])+int(options[2]) > value >= int(options[1]):
                # print('^ chosen')
                value = value+(int(options[0])-int(options[1]))

                break
    print(value)
    locations[seed_idx] = value

print(seeds,locations)
print(min(locations))

