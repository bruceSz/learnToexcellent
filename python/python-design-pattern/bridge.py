class DrawingAPI1:
    def drawCircle(self,x,y,radius):
        print ('API.circle at {}:{} radius {}'.format(x,y,radius))

class DrawingAPI2:
    def drawCircle(self,x,y,radius):
        print ('API.circle at {}:{} radius {}'.format(x,y,radius))

class CircleShape:
    def __init__(self,x,y,radius,drawingAPI):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__drawingAPI = drawingAPI
    def draw(self):
        self.__drawingAPI.drawCircle(self.__x,self.__y,self.__radius)

    def resizeByPercentage(self,pct):
        self.__radius *= pct
        
def main():
    shapes = (
        CircleShape(1,2,3,DrawingAPI1()),
        CircleShape(5,7,8,DrawingAPI2())
    )
    for shape in shapes:
        shape.resizeByPercentage(2.5)
        shape.draw()
if __name__ == "__main__":
    main()
