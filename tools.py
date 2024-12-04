
def is_prime(n):
    if n in [0, 1]: return False
    if n % 2 == 0: 
        return n == 2
    for i in range(3, 1 + int(n**0.5), 2): 
        if n % i == 0: 
            return False
    return True