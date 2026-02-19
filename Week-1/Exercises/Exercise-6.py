"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    if n % d == 0 :
        return True
    
    return False

def is_prime(n):
    """True iff n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    for d in range(2, n) :
        if is_factor(d, n) == True :
            return False
    return True


list_of_primes = []


for num in range(1, 10001) :
    if is_prime(num) == True :
        list_of_primes.append(num)



print(list_of_primes)