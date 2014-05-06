class Solution:
    # @param s,a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak1(self,s,dict_):
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

    def wordBreak(self,s,dict_):
        # assume is is not None
        if len(s)== 0:
            if s in dict_:
                return True
            return False

        tmp_result = {}
        for i in xrange(len(s)-1,-1,-1):
            suffix = s[i:]
            for j in xrange(1,len(suffix)+1):
                prefix = suffix[:j]
                if prefix in dict_:
                    # The whole word is in dict_
                    if suffix[j:]=='':
                        tmp_result[suffix]=True
                        break

                    else:
                        result = tmp_result[suffix[j:]]
                        if result:
                            tmp_result[suffix]=True
                            break

            if not suffix in tmp_result:
                tmp_result[suffix] = False

        return tmp_result[s]
                            
                            
                        
                        
            





def test_solution():
    ss = Solution()
    s='aaaaaaa'
    d = ['aaaa','aaa']
    set_ = set(d)
    print ss.wordBreak(s,d)
    
if __name__ == '__main__':
    test_solution()
    

