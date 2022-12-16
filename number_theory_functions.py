from random import randrange


def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if a == 0 :     # stop condition
        return b,0,1
             
    gcd,x1,y1 = extended_gcd(b%a,a)
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y



def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    if extended_gcd(a,n)[0] != 1: #checks if the inverse exists
        return None
    n0 = n
    y = 0
    x = 1
 
    if n == 1:
        return 0
 
    while a > 1:
 
        # q is quotient
        q = a // n
 
        t = n
 
        # n is remainder now, process
        # same as Euclid's algo
        n = a % n
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if x < 0:
        x = x + n0
 
    return x

def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    modular_exponent(2, 3, 5)
    """

    result = 1
    x = a
    d_new = str(bin(d))  # convert d to binary number
    length = len(d_new)  # find from how many digits d.bin is built (+2 str)
    d_new = d_new[2:length]
    length = length - 2
    last_i = length - 1
    for i in range(length-1, 0, -1):
        b_i = int(d_new[i])
        if b_i != 0:
            index_delta = i - last_i
            power_delta = 2 ** index_delta
            x = x ** power_delta
            x = x % n
            result *= x
            result = result % n
            last_i = i
    return result

      
def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None