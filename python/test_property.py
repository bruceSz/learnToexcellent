import json

class SomeModel(object):
    _foo = 'this is the data'

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self,new_val):
        self._foo = new_val


class SomeModel(object):
    _foo = 'this is the data'

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self,new_val):
        self._foo = new_val


if __name__ == '__main__':

    sm = SomeModel()
    print sm.foo
    sm.foo='new data'
    print sm.foo
