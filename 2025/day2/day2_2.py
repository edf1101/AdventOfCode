from time import perf_counter
from math import log10
test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

inps = open("input2.inp", 'r', encoding="utf-8").read().split(",")
# inps = test.split(",")
tot = 0

def check_num(candidate):
    """
    Check if a number is valid.
    ie any repeating patterns
    :param candidate:
    :return:
    """
    c = str(candidate)
    l = len(c)
    for i in range(1,int(l/2)+1):
        if l%i !=0:
            continue

        if c[:i]*int(l/i) == c:
            return True
    return False

def len_int(n):
    return 1+int(log10(n))

def first_digs(n,i):
    return n//(10**(len_int(n)-i))

def repeat_digs(n,i):
    t=0
    for x in range(i):
        t+= n* (10**(x*len_int(n)))
    return t

def check_num2(candidate:int):
    l = len_int(candidate)

    for i in range(1, int(l / 2) + 1):
        if l % i != 0:
            continue

        if repeat_digs(first_digs(candidate,i),int(l/i)) == candidate:
            return True



    return False


# --- SOLUTION 2: MATH (Fixed & Optimized) ---
def check_num_math(candidate):
    # Optimization: Use len(str()) because log10 is slow,
    # but stick to math for the rest to test the theory.
    s_len = len(str(candidate))

    for i in range(1, (s_len // 2) + 1):
        if s_len % i == 0:
            repeats = s_len // i

            # Extract first 'i' digits
            # divisor = 10^(total_len - chunk_len)
            divisor = 10 ** (s_len - i)
            chunk = candidate // divisor

            # Reconstruct the number mathematically
            reconstructed = 0
            chunk_len_pow = 10 ** i  # Pre-calculate power

            # Example: chunk 12, repeats 3 -> 12 * 10000 + 12 * 100 + 12
            for x in range(repeats):
                reconstructed = reconstructed * chunk_len_pow + chunk

            if reconstructed == candidate:
                return True
    return False


time_start = perf_counter()
#very ugly solution I apologise to anyone reading this
for inp in inps:
    low,high = map(int, inp.split("-"))
    # print(low, high)
    for candidate in range(low, high+1):
        if check_num_math(candidate):
            tot+=candidate

time_end = perf_counter()
dif = time_end-time_start
print(tot)
print(f'Time taken: {dif}')



