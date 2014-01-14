from nose import with_setup
def setup_func():
    "set up test fixtures"

def teardown_func():
    "tear down test fixtures"

@with_setup(setup_func,teardown_func)
def test():
    'test ...'
