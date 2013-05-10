import time
SLEEP = 0.5
class TC1:
    def run(self):
        print ('####in test 1####')
        time.sleep(SLEEP)
        print ('setting up')
        time.sleep(SLEEP)
        print('running test')
        time.sleep(SLEEP)
        print('tearing down')
        time.sleep(SLEEP)
        print ('test finished\n')

class TC2:
    
    def run(self):
        print ('####in test 2####')
        time.sleep(SLEEP)
        print ('setting up')
        time.sleep(SLEEP)
        print('running test')
        time.sleep(SLEEP)
        print('tearing down')
        time.sleep(SLEEP)
        print ('test finished\n')

class TC3:
    def run(self):
        print ('####in test 3####')
        time.sleep(SLEEP)
        print ('setting up')
        time.sleep(SLEEP)
        print('running test')
        time.sleep(SLEEP)
        print('tearing down')
        time.sleep(SLEEP)
        print ('test finished\n')

class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [i for i in (self.tc1,self.tc2,self.tc3)]
    def runAll(self):
        [i.run() for i in self.tests]

if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()
