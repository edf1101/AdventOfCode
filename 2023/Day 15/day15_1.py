input_data = open('input.txt').read()
test_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

data = input_data.split(',')

def hash_func(inp):
    current_val = 0
    for char in inp:
        current_val += ord(char)
        current_val*=17
        current_val%=256
    return current_val

result = 0
for string in data:
    result += hash_func(string)

print(result)