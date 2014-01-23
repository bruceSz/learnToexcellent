# meta class need more work.
class UpperAttrMetaClass(type):
    def __new__(cls,name,bases,attr_dict):
        attrs = ((name,value) for name,value in attr_dict.items() if not name.startswith('__'))
        for name,value in attrs:
            print name
        upperclass_attr = dict((name.upper(),value) for name,value in attrs)
        #return type(future_class_name,future_class_parents,upperclass_attr)
        #return type.__new__(upperattr_metaclass,future_class_name,future_class_parents,future_class_attr)
        return super(UpperAttrMetaClass,cls).__new__(cls,name,bases,upperclass_attr)



class Foo(object):
    __metaclass__ = UpperAttrMetaClass
    def _test(self):
        pass

    bar = 'bip';

print hasattr(Foo,'bar')
print hasattr(Foo,'BAR')
f=Foo()
print dir(f)
print f.BAR


