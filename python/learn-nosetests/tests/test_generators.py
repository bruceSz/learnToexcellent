from nose import with_setup

def setup_func():
    print "set up test fixtures"

def teardown_func():
    print "tear down test fixtures"

@with_setup(setup_func,teardown_func)
def test_evens():
    for i in range(0,5):
        yield check_even, i, i*3

def check_even(n,nn):
    assert n%2 ==0 or nn%2 == 0
