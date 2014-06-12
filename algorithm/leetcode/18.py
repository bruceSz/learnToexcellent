class Solution:
    def candy(self,ratings):
        l_low_points = []
        pre_ = None
        next_ = None
        length = len(ratings)
        if length == 1:
            return 1

        for index in xrange(length):
            if index == length-1:
                if ratings[index-1]> ratings[index]:
                    l_low_points.append(index)
                    
            elif index == 0:
                if ratings[1]>ratings[0]:
                    l_low_points.append(index)
            else:
                pass


                
            
        

