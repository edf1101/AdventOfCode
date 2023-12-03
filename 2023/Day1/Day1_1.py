calibration_doc = open('input.txt').read()
#
alpha='qwertyuiopasdfghjklzxcvbnm'
sum=0
for line in calibration_doc.split('\n'):
    for char in alpha:
        line = line.replace(char,'')
    nums= int(str(line[0])+str(line[-1]))
    sum+=nums
print(sum)

