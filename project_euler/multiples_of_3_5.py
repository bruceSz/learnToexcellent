
DEBUG = True
def sum_of_multiples_of_3_5(limit):
    sum = 0
    for i in range(1,limit):
        if is_divided_exactly(i,3):
            sum+=i
        elif is_divided_exactly(i,5):
            sum+=i
        else:
            pass

    return sum

def test_sum_of_multiples_of_3_5():
    if DEBUG :
        print "this is the test"
    assert 23 == sum_of_multiples_of_3_5(10)
        
def is_divided_exactly(dividend,divisor):
    flag = False
    if dividend % divisor == 0:
        flag = True
    return flag

def test_is_divided_exactly():
    assert not is_divided_exactly(4,5)
    assert is_divided_exactly(15,5)

if __name__ == "__main__":
    test_is_divided_exactly()
    test_sum_of_multiples_of_3_5()
    print sum_of_multiples_of_3_5(1000)
    
    
