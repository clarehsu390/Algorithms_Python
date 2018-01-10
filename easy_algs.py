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
        
def fibonacci(n):
    fib_nums = [0, 1]
    if n <= 2:
        return fib_nums[0:n]
    i = 2
    while i < n:
        new_num = fib_nums[i-1] + fib_nums[i-2]
        fib_nums.append(new_num)
        i += 1
    
    return fib_nums

print fibonacci(5)
print fibonacci(10)

def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print fib_recursive(5)