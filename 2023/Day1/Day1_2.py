calibration_doc = open('input.txt').read()

words_to_nums = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,'nine': 9}

alpha = 'qwertyuiopasdfghjklzxcvbnm'
nums = '1234567890'
sum = 0
for line in calibration_doc.split('\n'):
    nums_found = []
    for i in range(len(line)):
        if line[i] in nums:
            nums_found.append(line[i])
        for k, v in words_to_nums.items():
            if line[i:i + len(k)] == k:
                nums_found.append(v)
    code = int(str(nums_found[0]) + str(nums_found[-1]))
    sum += code

print(sum)
