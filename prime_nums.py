def generate_prime_nums(upper_limit):
    """
    Generate a list of prime numbers.
    """
    if type(upper_limit) is not int:
        raise TypeError("The Upper limit should be an integer.")
    else:
        primes = []
        for item in range(2, upper_limit+1):
            for num in range(2, item):
                if item % num == 0:
                    # The number is not prime.
                    break
            else:
                # The number is a prime number.
                primes.append(item)
        return primes
                
                