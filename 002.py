a = 1
b = 2
answer = 2
while b < 4_000_000:
    b, a = b + a, b
    if b % 2 == 0: answer += b
print(answer)