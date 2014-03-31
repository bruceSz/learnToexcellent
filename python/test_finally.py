def test_f():
    try:
        return 1
    finally:
        print 'execute the finally block of code.'

if __name__ == '__main__':
    print test_f()
