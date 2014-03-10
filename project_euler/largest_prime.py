import math

def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def factors(num):
    # Assume minmum num is 1
    if num <=1:
        yield 1

    for i in range(2,int(math.sqrt(num))+1):
        if num % i==0:
            yield i

def select_with(iterator,condition):
    for i in iterator:
        if condition(i):
            yield i

def print_iterator(iterator):
    for i in iterator:
        print i

def find_max(iterator):
    # Assume the -1 is the minmum of all iterator.
    max = 0
    for i in iterator:
        #print i
        if max == 0:
            max = i

        elif i>max:
            max = i

    return max
    
    
def print_factors():
    f = factors(13195)
    print_iterator(f)

def print_condition_factors(condition):
    f = factors(13195)
    filtered = select_with(f,condition)
    print_iterator(filtered)
    
def find_largest_prime_factors():
    f = factors(600851475143)
    filtered = select_with(f,isPrime)
    print find_max(filtered)
    
    
if __name__ == "__main__":
    #print_factors()
    #print_condition_factors(isPrime)
    find_largest_prime_factors()
    
        



