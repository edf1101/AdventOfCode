test = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

data = open("input1.inp", 'r', encoding="utf-8").read()

input_clean = data.split("\n")
position =50
zero_count = 0
for command in input_clean:
    dir = command[0]
    steps = int(command[1:])
    if dir == "L":
        position  = (position - steps)%100
    else:
        position = (position + steps)%100

    if position ==0:
        zero_count += 1

print(zero_count)