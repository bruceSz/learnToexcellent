class Solution:
    # @param s,a string
    # @param dict, a set of string
    # @return a boolean
    

    def wordBreak(self,s,dict_):
        # assume is is not None
        if len(s)== 0:
            if s in dict_:
                return True
            return False

        tmp_result = {}
        for i in xrange(len(s)-1,-1,-1):
            suffix = s[i:]
            tmp_result[suffix]=[]

            for j in xrange(1,len(suffix)+1):
                prefix = suffix[:j]
                if prefix in dict_:
                    print 'under:' ,suffix
                    print 'insert:' ,prefix,
                    if suffix[j:] in tmp_result:

                        print 'suffix is:' ,tmp_result[suffix[j:]]
                    else:
                        print '[]',
                    print
                    # The whole word is in dict_
                    if suffix[j:]=='':
                        tmp_result[suffix].append([prefix])

                    else:
                        result = tmp_result[suffix[j:]]

                        map(lambda x:x.insert(0,prefix),result)
                        
                        tmp_result[suffix].extend(result)

            

        return tmp_result[s]
                            
                            

def test_solution():
    ss = Solution()
    s='aaaaaaa'
    d = ['aaaa','aaa']
    set_ = set(d)
    print ss.wordBreak(s,d)
    
if __name__ == '__main__':
    test_solution()
    

