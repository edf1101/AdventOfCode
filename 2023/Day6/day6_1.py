input_data = open('input.txt').read()
test_data = """Time:      7  15   30
Distance:  9  40  200"""

data = input_data.split('\n')

product = 1
for time,dist_record in zip(data[0].split(':')[1].split(),data[1].split(':')[1].split()):

    time= int(time)
    dist_record = int(dist_record)

    beat = 0
    for i in range(1,time):
        charge = i
        race = time-i
        dist = race*charge
        # print(f'charge for {i} race for {time-i} dist is {dist}')
        if dist>dist_record:
            beat+=1

    product*= beat
print(product)