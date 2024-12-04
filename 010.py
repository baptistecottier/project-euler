from tools import is_prime

answer = 0
for n in range(2_000_000):
    if is_prime(n): answer += n

print(answer)