class Solution:
    # @param s,a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self,s,dict_):
        if len(s) == 0:
            # this judgement is only used when input string s is empty string
            # assume there is no empty string '' in dict_
            if s in dict_:
                return True
            return False

        ret = []

        for i in xrange(1,len(s)+1):
            prefix = s[:i]
            if prefix in dict_:
                #print prefix
                if s[i:]=='':
                    ret.append(True)
                else:
                    ret.append(True&self.wordBreak(s[i:],dict_))
        if ret:
            return reduce(lambda x,y:x|y,ret)
        else:
            return False



def test_solution():
    ss = Solution()
    s='aaaaaaa'
    d = ['aaaa','aaa']
    set_ = set(d)
    print ss.wordBreak(s,d)
    
if __name__ == '__main__':
    test_solution()
    

