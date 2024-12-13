def is_prime(n):
    '''Checks whether given number n is prime or not and returns True/False'''
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True
