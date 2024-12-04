from tools import is_prime
cnt = 1
n = 3
while cnt < 10_001:
    if is_prime(n): 
        cnt += 1
    n += 2
print(n - 2)