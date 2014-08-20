import abc
class Base(object):
    __metaclass__ = abc.ABCMeta

    def value_getter(self):
        return 'should never see this'

    def value_setter(self,newv):
        return
    value = abc.abstractproperty(value_getter,value_setter)

class PartialImplementation(Base):
    @property
    def value(self):
        return 'read only'


class Implementation(Base):
    _value = 'default value'

    def value_getter(self):
        return self._value

    def value_setter(self,newv):
        self._value = newv

    value = property(value_getter,value_setter)

try:
    b = Base()
except Exception,err:
    print str(err)

try:
    p = PartialImplementation()
    print p.value
    p.value=1
except Exception,err:
    print str(err)

i = Implementation()
i.value = 'new value'

print 'new value:',i.value
