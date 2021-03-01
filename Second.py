def is_prime(input):
    for i in range(2, input):
        if input % i == 0:
            return False
    return True

def primes(n):
    for j in range(2, n+1):
        if is_prime(j):
            print(j, end=' ')

        
    # figure out which numbers are primes between 1 and n
    # call is_prime(1), is_prime(2)... is_prime(n)
        # print i if is_prime(i) is True

primes(10)
