class Test():
    title="class title"
    def __init__(self):
        self.__name="zs"
        self.title="instance title"
    def name(self):
        return self.__name
    def title(self):
        return self.title

t = Test()
print Test.title
print t.title
