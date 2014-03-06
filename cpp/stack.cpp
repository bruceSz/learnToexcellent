#ifndef __StackClassH__
#define __StackClassH__

#include<assert.h>


template<class Elem>
class Stack
{
    public:
        Stack(int MaxSize=500);
        Stack(const Stack<Elem> &OtherStack);
        ~Stack(void);

        inline void Push(const Elem &Item);
        inline Elem Pop(void);
        inline const Elem &Peek(int Depth) const;

    protected:
        Elem * Data;
        int CurrElemNum;
        const int MAX_NUM;
};

template<class Elem>
Stack<Elem>::Stack(int MaxSize):
    MAX_NUM(MaxSize)
{
    Data = new Elem(MAX_NUM);
    CurrElemNum = 0;
}

template<class Elem>
Stack<Elem>::~Stack(void)
{
    delete[] Data;
}

template<class Elem>
inline void Stack<ELem>::push(const Elem &Item)
{
    assert(CurrElemNum < MAX_NUM);
    Data[CurrElemNum++] = Item;
}

template<class Elem>
inline Elem Stack<ELem>::Pop(void)
{
    assert(CurrElemNum > 0);
    return Data[--CurrElemNum];
}

template<class Elem>
incline const Elem &Stack<Elem>::Peek(int Depth) const
{
    assert(Depth<CurrElemNum);
    return Data[CurrElemNum - (Depth + 1)];
}
#endif
