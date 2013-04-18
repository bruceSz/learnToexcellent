__author__ = "zs:copied from andand b pihhai"
__maintainer__ = 'zs'
__version__ = '1.0'

def normalize(val):
    ""
    if val.find('-') != -1:
        val = val.replace('-','_')
    return val

def denormalize(val):
    
    if val.find('_') != -1:
        val = val.replace('_','-')
    return val
class SpecialDict(dict):
    def __getattr__(self,name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                raise AttributeError('no attribute named %s' %name)
    def __setattr__(self,name,value):
        if name in self.__dict__:
            self.__dict__[name] = value
        elif name in self:
            self[name] = value
        else:
            name2 = denormalize(name)
            if name2 in self:
                self[name2] = value
            else:
                self[name] = value
class CompositeDict(SpecialDict):
    ID = 0
    def __init__(self,name=''):
        if name:
            self._name = name
        else:
            self._name = ''.join(('id#',str(self.__class__.ID)))
            self.__class__.ID +=1
        self._children = []
        self._father = None
        self[self._name] = SpecialDict()
    
    def __getattr__(self,name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            name = denormalize(name)
            if name in self:
                return self.get(name)
            else:
                child = self.findChild(name)
                if child:
                    return child
                else:
                    attr = getattr(self[self._name],name)
                    if attr: return attr
                    raise AttributeError('no attribute named %s'%name)
    def isRoot(self):
        return not self._father
    
    def isLeaf(self):
        return not self._children
    
    def getName(self):
        return self._name
    
    def getIndex(self,child):
        if child in self._children:
            return self._children.index(child)
        else:
            return -1
    def getDict(self):
        return self[self._name]

    def getProperty(self,child,key):
        childDict = self.getInfoDict(child)
        if childDict:
            return childDict.get(key,None)

    def setProperty(self,child,key,value):
        childDict = self.getInfoDict(child)
        if childDict:
            childDict[key] = value

    def getChildren(self):
        return self._children


    def getAllChildren(self):
        l = []
        for child in self._children:
            l.append(child)
            l.extend(child.getAllChildren())
        return l

    def getChild(self,name):
        for child in self._children:
            if child.getName() == name:
                return child
    def findChild(self,name):
        for child in self.getAllChildren():
            if child.getName() == name:
                return child
    def findChildren(self,name):
        children = []
        for child in self.getAllChildren():
            if child.getName() == name:
                children.append(child)
    def getPropertyDict(self):
        d = self.getChild('__properties')
        if d:
            return d.getDict()
        else:
            return {}
    def getParent(self):
        return self._father

    def __setChildDict(self,child):
        d = self[self._name]
        d[child.getName()] = child.getDict()
    
    def setParent(self,father):
        self._father = father
    
    def setName(self,name):
        self._name = name
    def setDict(self,d):
        self[self._name] = d.copy()
    def setAttribute(self,name,value):
        self[self._name][name] = value
    def getAttribute(self,name):
        return self[self._name][name]

    def addChild(self,name,force=False):
        if type(name) != str:
            raise ValueError('argument should be a string')
        child = self.getChild(name)
        if child:
            if force:
                index = self.getIndex(child)
                if index != -1:
                    child = self.__class__(name)
                    self._children[index] = child
                    child.setParent(self)
                    self.__setChildDict(child)
            return child
        else:
            child = self.__class__(name)
            child.setParent(self)
            self._children.append(child)
            self.__setChildDict(child)
            return child
    def addChild2(self,child):
        currChild = self.getChild(child.getName())
        if currChild:
            index = self.getIndex(currChild)
            if index != -1:
                self._children[index] = child
                child.setParent(self)
                currChild.setParent(None)
                del currChild
                self.__setChildDict(child)
        else:
            child.setParent(self)
            self._children.append(child)
            self.__setChildDict(child)
if __name__ == '__main__':
    window = CompositeDict('windows')
    frame = window.addChild('Frame')
    tfield = frame.addChild('text field')
    tfield.setAttribute('size','20')

    btn = frame.addChild('Button1')
    btn.setAttribute('label','submit')
    btn = frame.addChild('Button2')
    btn.setAttribute('label','browse')
    print (window.Frame.Button1.label)
    print (window.Frame.Button2.label)
