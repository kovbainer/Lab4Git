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
<<<<<<< Updated upstream
=======

def is_power(n, k):
    while n >= k:
        n //= k
    return n == 1

def is_five_power(n):
    return is_power(n, 5)

def is_two_power(n):
    return is_power(n, 2)
>>>>>>> Stashed changes
