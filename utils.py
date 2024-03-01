def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i*i < n:
        if n % i == 0:
            return False
        i += 2
    return True 

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
