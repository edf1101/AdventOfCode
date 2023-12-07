input_data = open('input.txt').read()
test_data = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

data = input_data.split('\n')

order = 'AKQT98765432J'[::-1]
hashes = {}
scores = []
for line in data:
    hand = line.split()[0]
    print('\n', hand)
    bid = line.split()[1]
    hash = 0

    hand_unique = list(set(hand))
    hand_unique.sort()

    hand_unique_counts =[0 if i=='J' else hand.count(i) for i in hand_unique]

    highest = hand_unique[hand_unique_counts.index(sorted(hand_unique_counts)[-1])]
    new_hand = ''.join([highest if i=='J' else i for i in hand])
    hand_unique = list(set(new_hand))
    hand_unique.sort()

    if len(hand_unique) == 1:
        print('five of a kind')
        hash += 6000000
    elif len(hand_unique) == 2 and new_hand.count(hand_unique[0]) in [1, 4]:
        print('four of a kind')
        hash += 5000000

    elif len(hand_unique) == 2 and new_hand.count(hand_unique[0]) in [2, 3]:
        print('full house')
        hash += 4000000
    elif len(hand_unique) == 3 and 3 in [new_hand.count(hand_unique[0]), new_hand.count(hand_unique[1]),
                                         new_hand.count(hand_unique[2])]:
        print('three of a kind')
        hash += 3000000

    elif len(hand_unique) == 3:
        print('two pair')
        hash += 2000000

    elif len(hand_unique) == 4:
        print('one pair')
        hash += 1000000

    elif len(hand_unique) == 5:
        print('high card')
        hash += 0
    else:
        print('????')

    # rank the cards themselves
    hand_score = 0
    for idx,card in enumerate(hand):
        hand_score += (order.index(card) + 1) * (13 ** (4-idx))
    # print(hand_score)
    hash+=hand_score
    # print(hash)
    hashes[hand,bid] = hash
    scores.append(hash)
scores.sort()
print('\n')
hashes = {v:k for k,v in hashes.items()}
final_score = 0
for idx, score in enumerate(scores):
    print(hashes[score])
    final_score+= (idx+1)*int(hashes[score][1])
print(final_score)