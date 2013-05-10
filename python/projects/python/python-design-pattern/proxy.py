import time
class SalesManager:
    def work(self):
        print('sales manager working...')
    def talk(self):
        print('sales manager ready to talk')
class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None
    def work(self):
        print('proxy checking for sales manager availability')
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print('sales manager is busy')
if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = 'yes'
    p.work()
