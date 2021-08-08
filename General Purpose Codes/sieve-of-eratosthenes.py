'''This code below uses the sieve of eratosthenes which is an effective algorithm
to 'sieve' prime numbers.

The code has been modified a little bit to return a list of all prime numbers upto n.

NOTE: The count of prime numbers start from 1, i.e. index position of 2 is 1 and 
3 is 2 and so on... '''

def sieve_of_eratosthenes(n):
 
    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is not a prime, else true.
    
    prime = [True for i in range(n+1)]
    p = 2
    
    while (p * p <= n):
 
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    # Primes generally are counted from 1
    prime_list = ['#']
 
    # Append primes to a list
    for p in range(2, n+1):
        if prime[p]:
            prime_list.append(p)
            
    return prime_list