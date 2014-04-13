import sys
class Point:
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b


def maxPoints(points):
    from functools import partial

    def pair(x,y):
        return (x,y)

    def compute_a_b(p1,p2):
        if p1.x==p2.x:
            return (p1.x,sys.maxint)

        a = (p1.y-p2.y)/(p1.x-p2.x)
        b = p1.y-a*p1.x
        return (a,b)

    pairs=[]
    for index,point in enumerate(points):
        l_pair = partial(pair,point) 
        pair_list=map(l_pair,points[index+1:])
        if pair_list :
            pairs.extend(pair_list)

    #for pair in pairs:
    #    print pair[0].x,pair[0].y,':',pair[1].x,pair[1].y

    map_line_count = {}
    for pair in pairs:
        line = compute_a_b(pair[0],pair[1])
        if line in map_line_count:
            map_line_count[line]+=1
        else:
            map_line_count[line]=1


    #for point in points:
    #    print point.x,point.y

    #for line,point_num in map_line_count.items():
    #    print line,point_num

    line,point_num=reduce(lambda x,y:x if x[1]>y[1] else y,map_line_count.items())

    #ret_points = filter(lambda point:(point.x*line[0]+line[1])==point.y,points )
    return point_num
if __name__ == "__main__":
   l=[]
   l.append(Point(1,2))
   l.append(Point(3,4))
   l.append(Point(2,5))
   l.append(Point(2,4))
   l.append(Point(3,6))
   print maxPoints(l)


