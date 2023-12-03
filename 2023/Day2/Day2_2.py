input_data = open('input.txt').read()
test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

games = input_data.split('\n')

sum = 0
for game in games:

    hands = game.split(':')[1].split(';')

    min_cols = {'red': 0, 'green': 0, 'blue': 0}
    for hand in hands:
        hand = hand.split(',')

        for i in hand:
            num, col = i.split()
            min_cols[col] = max(min_cols[col], int(num))

    min_cols = list(min_cols.values())
    power = min_cols[0] * min_cols[1] * min_cols[2]
    sum += power

print(sum)
