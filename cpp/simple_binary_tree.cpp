#include<iostream>
using namespace std;

struct Tnode
{
    char value;
    struct Tnode* lChild;
    struct Tnode* rChild;
};

typedef Tnode * BiTree;

void InitBiTree(BiTree & T)
{
    char inChar = getchar();
    if(inChar == '#')
	T = 0;
    else
    {
	T = (BiTree)malloc(sizeof(Tnode));
	if(!T) throw "Invalid Address";
	else
	{
	    T->value = inChar;
	    InitBiTree(T->lChild);
	    InitBiTree(T->rChild);
	}
    }
}

void PreOrder(BiTree &T)
{
    if(T)
    {
	cout<<"node is"<<T->value<<endl;
	PreOrder(T->lChild);
	PreOrder(T->rChild);
    }
}

void InOrder(BiTree & T)
{
    if(T)
    {
	InOrder(T->lChild);
	cout<<"node is:"<<T->value<<endl;
	InOrder(T->rChild);
    }
}
void PostOrder(BiTree &T)
{
    if (T)
    {
	PostOrder(T->lChild);
	PostOrder(T->rChild);
	cout<<"node is"<<T->value<<endl;
    }
}

int main()
{
    BiTree t;
    cout<<"input node value:";
    InitBiTree(t);

    cout<<"pre order"<<endl;
    PreOrder(t);

    cout<<"in order"<<endl;
    InOrder(t);

    cout<<"post order"<<endl;
    PostOrder(t);
}
