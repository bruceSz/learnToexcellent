class Solution:

    def minCut(self,s):
        cut = 0
        length = len(s)
        # the input can be zero length:
        
        if length<=1:
            return cut

        left,right = -1,-1

        #panLen = 0
        #while i < length:
        #    j=0
        #    while (i-j) >=0 and (i+j)<length:
        #        if self.isPalinDrome(s[i-j:i+j+1]):
        #            j+=1
        #        else:
        #            if j-1>panLen:
        #                pos = i
        #                panLen = j-1
        #            #left = i-j-1
        #            #right=i+j-1
        #            break
        #    i+=1
        pos,panLen = self.findMaxPalin(s)            

        left = s[:pos-panLen]
        right = s[pos+panLen+1:]
        leftcut = self.minCut(left)
        rightcut = self.minCut(right)
        if (pos-panLen)==0 and (pos+panLen+1)==length:
            return 0
        elif (pos-panLen)==0:
            return rightcut+1
        elif (pos+panLen+1)==length:
            return leftcut+1
        else:
            return leftcut+rightcut+2

    def findMaxPalinSmarter(self,s):
        length = len(s)
        matrix = [[ -1 for x in range(length)] for y in range(length)]
        for i in xrange(length):
            matrix[i][i] = 0
        #for i in xrange(1,length):
        #    if 
        for j in range(1,length):
            for i in range(j):

                if (j-1)<(i+1):
                    

                    if s[j]==s[i]:
                        
                        matrix[i][j]=0
                else:
                    if matrix[i+1][j-1]!=-1:
                        if s[j]==s[i]:
                            matrix[i][j]=matrix[i+1][j-1]+1

                    else:
                        matrix[i][j]=-1
                #print i,j,s[i],s[j],matrix[i][j],matrix[i+1][j-1]

        ##print matrix
        max = 0
        for i in range(1,length):
            for j in xrange(i+1):
                if matrix[j][i]>max:
                    max = matrix[j][i]

        return max




    def findMaxPalin(self,s):
        i=0
        length = len(s)
        pLen = 0
        while i< length:
            j=0
            # if length % 2 ==1
            while i-j>=0 and i+j<length:
                if self.isPalinDrome(s[i-j:i+j+1]):
                    j+=1
                else:
                    break
            if pLen<(j-1):
                pLen = j-1
                
            j=0
            if (i+1)<length:
                print s[i],s[i+1]
                if s[i]==s[i+1]:
                    while i-j>=0 and i+1+j <length:
                        if self.isPalinDrome(s[i-j:i+j+2]):
                            j+=1
                        else:
                            break
                    if pLen < (j-1):
                        pLen = j-1
                    print i,i+1,j-1

            i+=1

        return pLen


    def isPalinDrome(self,s):
        if len(s)%2==1:
            return s[:]==s[::-1]
        else:
            return s[len(s)/2:][::-1]==s[:len(s)/2]

    def max_palin_drome(self,s):
        reverse_s = s[::-1]
        s+='#'
        s+=reverse_s
        p_array = self.prefix_array(s)
        max_p = 0
        index = -1
        for i in range(len(p_array)-1):
            tmp = self.max_prefix(p_array[i],p_array[i+1])
            if tmp>max_p:
                max_p = tmp
                index=i

        return p_array[index][:max_p]

    def max_prefix(self,s1,s2):
        len1 = len(s1)
        len2 = len(s2)
        length = len1 if len1<len2 else len2
        p_len = 0 
        for i in range(length):
            if s1[i]!=s2[i]:
                break
            else:
                p_len+=1

        return p_len


    def prefix_array(self,s):
        length = len(s)
        array = []
        for i in range(0,length):
            array.append(s[i:])
        array.sort()
        return array

def test_prefix_array():
    s='aabaa';
    ss = Solution()
    print ss.prefix_array(s)

def test_max_palindrome():
    s='f'
    ss = Solution()
    print ss.max_palin_drome(s)

if __name__ == '__main__':
    s='b'
    #ss = Solution()
    #print ss.minCut(s)
    #print ss.findMaxPalinSmarter(s)
    #test_prefix_array()
    test_max_palindrome()