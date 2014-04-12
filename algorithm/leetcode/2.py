


def evalRPN(tokens):

    op_d={}
    op_d['+']=lambda x,y:x+y
    op_d['-']=lambda x,y:x-y
    op_d['*']=lambda x,y:x*y
    op_d['/']=lambda x,y:x/y

    def find_op(str_):
        try:
            op=op_d[str_]
        except KeyError:
            raise ValueError("invalid operator: "+str_)
        return op

    ll_optor=[]
    ll_opand=[]
    operator = set(['+','-','*','/'])
    for token in tokens:
        if token in operator:
            r_optor = ll_optor.pop()
            l_optor = ll_optor.pop()
            op=find_op(token)
            print token ,
            result = apply(op,[int(l_optor),int(r_optor)])
            ll_optor.append(result)
        else :
            ll_optor.append(token)
            
        print ll_optor


if __name__ == '__main__':
    #l=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    l=['1','2','+','4','*','5','+','3','-']
    evalRPN(l)
