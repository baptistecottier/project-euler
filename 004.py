answer = 0
for p in range(999, 99, -1):
    for q in range(999, p, -1):
        a = str(p * q)
        if a == a[::-1]:
            answer = max(answer, p * q)
            break
print(answer)