import math

def prime_numbers(length):
    """ Calulate prime numbers in the range of length parameter. """
    primes = []
    for i in range(2,length): #string from number 3, not interested in p numbers 1 and 2
        for j in range(2,i): #start from 2 until the half of each nr to check divisibilty
            if i % j == 0:
                break
        else:        
            primes.append(i)
    return primes


def filter_primes(primes):
    """ Filter the prime number to be in format of p = 2*q + 1  """
    filtered_primes = []
    for i in primes:
        p = (2*i)+1
        if p in primes:
            filtered_primes.append(p)
    return filtered_primes


def primitive_root(prime_nr):
    """ calcualte the primitive roots of the prime_nr """
    prime_factors = []
    prim_roots = []
    division = [] 
    eu_phi =  prime_nr -1 # euler totient function (its a prime number so the answer is simply p-1)
    prime_nrs = prime_numbers(eu_phi) # find all primes in range of the prime nr -1
    
    for i in prime_nrs: # prime factors of the eu_phi
        if eu_phi % i == 0:
            prime_factors.append(i)

    for i in prime_factors: # calculating the prime factors devided by each prime factors of phi_n
        n_i = int(eu_phi/i)
        division.append(n_i)
        # dision contains all numbers that the prime factor are divisible with

    for i in prime_nrs: # looping thorugh all prime numbers again
        counter = 0 # set a counter, so if for each prime number p ==> p^(divisible_i nr) mod prime_nr != 1
        for j in division: 
            if pow(i, j, prime_nr) != 1:
                counter += 1
        if counter == len(division):
            prim_roots.append(i)
    return prim_roots


def public_numbers(interval=500):
    """ Calculate the publlic numbers of the Diffi-Hellman algorithm."""
    prime_nrs = prime_numbers(interval)
    filter_p = filter_primes(prime_nrs)
    q = filter_p.pop() # last index is the largest prime number in the interval
    primitves = primitive_root(q)
    generator = primitves[0] # pickup the first element that the generator of the cyclic group
    return q, generator

