# To solve this problem, i need figure out
# big algorithm first and separate interface between
# each modular.
# remember the way you solving the problem actualy
# make a dsl of the problme.
# let others deal with the concrete work of implementing
# concrete work.

def operation_on_numbers(operation,limit,condition):
    sum=0
    c=0
    for i in Fab():
        if i>=limit:
            break
        if condition(i):
            sum = operation(sum,i)

    return sum
            
def add(ret,sum):
    return ret+sum
    
def test_sum_of_numbers(condition):
    limit = 4000000
    print operation_on_numbers(add,limit,condition)

def Fab():
    a =1
    b =2
    yield a
    yield b
    while True:
        c=a+b
        yield c
        a=b
        b=c

def test_Fab():
    #for x in range(1,100):
    #    print "index: ",x,"fibo: ",f.next()

    for i in Fab():
        print i
        if i>100:
            break
    
    #for x in f:
    #    if x>100:
    #        break
    #    print x



def sum_of_even_fibonacci_numbers():
    sum =0
    a=1
    b=2
    c = a + b
    while c<4000000:
        print c
        if c%2==0:
            sum+=c

        a=b
        b=c
        c=a+b


    return sum+2

def test_sum_of_even_fibonacci_numbers():
    print sum_of_even_fibonacci_numbers()

def is_even(num):
    flag = False
    if num%2==0:
        flag = True
    return flag


if __name__ == "__main__":
    #test_sum_of_even_fibonacci_numbers()
    #test_Fab()
    test_sum_of_numbers(is_even)
