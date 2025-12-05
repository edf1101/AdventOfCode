test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

inps = open("input2.inp", 'r', encoding="utf-8").read().split(",")

tot = 0

#very ugly solution I apologise to anyone reading this
for inp in inps:
    low,high = map(int, inp.split("-"))
    # print(low, high)
    for candidate in range(low, high+1):
        s = str(candidate)
        if len(s) %2 ==0 and s[:int(len(s)/2)]*2==s:
            # print(candidate)
            tot+=candidate

print(tot)

