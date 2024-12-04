from tools import is_prime

n = 600_851_475_143
for k in range(int(n**0.5) + 1, 1, -2):
    if n % k == 0:
        if is_prime(k):
            print(k)
            break
        
        