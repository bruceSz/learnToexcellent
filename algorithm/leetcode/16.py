class Solution:
    def singleNumber(self,A):
        ss=set()
        for int_ in A:
            if int_ in ss:
                ss.discard(int_)
            else:
                ss.add(int_)

        return ss.pop()


def test_singleNumber():
    a=[1,2,4,76,4,3,2,3,76]
    sol = Solution()
    print sol.singleNumber(a)
if __name__=='__main__':
    test_singleNumber()