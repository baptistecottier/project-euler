for a in range(1_000):
    for b in range(1_000 - a):
        c = 1_000 - a - b
        if c**2 + b**2 == a**2: 
            print(a * b * c)