from contextlib import contextmanager
class Test:
    def __enter__(self):
        print('enter')
        return 1

    def __exit__(self,*args):
        print('exit')

def function():
    print 'function()'
    return 111



def test_with():

    with Test() as t:
        function()
        print 't is',t


@contextmanager
def tag(name):
    print "<%s>" %name
    yield 'haha'
    print "</%s>" % name


def test_contextlib():

    with tag("h1") as t:
        print t
        print 'foo'

if __name__ == '__main__':
    test_contextlib()

