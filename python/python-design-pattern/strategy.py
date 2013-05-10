import types
class StrategyExample:
    def __init__(self,func = None):
        self.name = 'Strategy Example 0'
        if func:
            self.execute = types.MethodType(func,self)
    def execute(self):
        print(self.name)
def executeReplacement1(self):
    print(self.name+'from execute 1')
def executeReplacement2(self):
    print(self.name+'from execute 2')

if __name__ == '__main__':
    strat0 = StrategyExample()
    strat1 = StrategyExample(executeReplacement1)
    strat1.name = 'strategy example 1'

    strat2 = StrategyExample(executeReplacement2)
    strat2.name = "strategy example 2"

    strat0.execute()
    strat1.execute()
    strat2.execute()
