    
    
def reverse_str(str_):
    
    l_=list(str_) 
    length = len(l_)
    i=0;
    j=length-1
    while i<j:
        l_[i],l_[j] = l_[j],l_[i]
        i+=1
        j-=1

    def op(x,y):
        return x+y

    return reduce(op,l_)
    

def reverse_words(str_):
    str_=str_.strip()
    if len(str_)==0 
        return ''

    str_=reverse_str(str_) 
    l_words = str_.split()
    l_words = map(reverse_str,l_words)
    def op(x,y):
        return x+' '+y

    return reduce(op,l_words)


if __name__ == "__main__":
    s='hello world , i love this world!'

    print reverse_words(s)

