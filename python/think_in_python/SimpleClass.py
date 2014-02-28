class Simple:
    def __init__(self,str):
	print "Inside the  Simple constructor"
	self.s = str

    #two methods
    def show(self):
	print self.s

    def showMsg(self,msg):
	print msg+":",
	self.show()

if __name__ == "__main__":
    x = Simple("constructor argument")
    # if there is no "()" behind show there is no error occured,which can confuse programmer.Maybe a error is better.
    # if there is no "()" the show function will be returned.
    x.show()
    x.showMsg("A message")
