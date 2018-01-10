def is_prime(n):
    divisor = 2
    while (n > divisor):
        if(n % divisor == 0):
            return False
        else:
            divisor += 1
    return True

# print is_prime(3)
# print is_prime(500)

def prime_factors(num):
    factors = []
    divisor = 2
    
    while (num > divisor):
        if (num % divisor == 0):
            factors.append(divisor)
            num = num/divisor
            
        divisor += 1
    
    return factors

# print prime_factors(63)
        

