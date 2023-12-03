input_data = open('input.txt').read()
test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

games = input_data.split('\n')
query = {'red': 12, 'green': 13, 'blue': 14}  # Red, green, blue

sum = 0
for game in games:
    game_id = game.split(':')[0].split(' ')[-1]
    hands = game.split(':')[1].split(';')
    valid = True
    for hand in hands:
        hand = hand.split(',')
        for i in hand:
            num, col = i.split()
            if int(num) > query[col]:
                valid = False
    if valid:
        sum += int(game_id)

print(sum)
