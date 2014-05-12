class Solution:
    def singleNumber(self,A):
        d={}
        for int_ in A:
            if int_ in d:
                if d[int_] ==2:
                    d.pop(int_)
                else:
                    d[int_]+=1
            else:
                d[int_]=1
        return d.keys().pop()


def test_singleNumber():
    a=[1,2,4,3,76,76,4,2,3,4,2,3,76]
    sol = Solution()
    print sol.singleNumber(a)

if __name__=='__main__':
    test_singleNumber()
