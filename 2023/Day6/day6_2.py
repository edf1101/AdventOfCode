input_data = open('input.txt').read()
test_data = """Time:      7  15   30
Distance:  9  40  200"""

data = input_data.split('\n')

product = 1

time= int(''.join(data[0].split(':')[1].split()))
dist_record = int(''.join(data[1].split(':')[1].split()))


beat = 0
for i in range(1,time):
    charge = i
    race = time-i
    dist = race*charge
    # print(f'charge for {i} race for {time-i} dist is {dist}')
    if dist>dist_record:
        beat+=1

print(beat)