class Solution:
    def atoi(self,str_):
        str_ = str_.strip()
        if len(str_) == 0:
            return 0
        sign_flag = 0
        if (lambda x: x.isdigit() or x=='+' or x=='-')(str_[0]):
            if str_[0]=='-':
                sign_flag = -1
            # as the flag is default to + ,actually we don't need
            # set flat to 1 if positive sign is given.
            # but to make it more clear, we will ...
            if str_[0] == '+':
                sign_flag = 1
        else:
            return 0

        if sign_flag !=0:
            str_ = str_[1:]
        else:
            sign_flag = 1
        ret = 0
        for char in str_:
            if (lambda x:x.isdigit())(char):
                ret += int(char)
                ret *= 10
            else :
                break
        ret/=10
        ret = ret*sign_flag
        if ret >= 2147483647 :
            return 2147483647
        if ret <= -2147483648:
            return -2147483648
        return ret
                

def test_atoi():
    ss = Solution()
    assert 0==ss.atoi("-")
    assert 0==ss.atoi('')
    assert 10==ss.atoi('10')
    assert -100 == ss.atoi('-100')
    assert 2147483647 == ss.atoi('2147483648')

if __name__ == '__main__':
    test_atoi()