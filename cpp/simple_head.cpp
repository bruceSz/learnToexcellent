#include<iostream>
using namespace std;

void makeMinHeap(int *arr,int size)
{
    //assume the input array start from 0
    //assert(size>=0);
    int i;
    int j;
    int tmp;
    i = 0;
    for(j=2*i+1;j<size;j++)
    {
	tmp = arr[j];
	for(i=j;tmp<arr[(i-1)/2];)
	{
	    arr[i] = arr[(i-1)/2];
	    i = (i-1)/2;
	    //if 2*i+1<j,then 2*i+2=j
	    if (i==0)
		break;
	}
	arr[i]=tmp;
    }
    return;
}

int main()
{
    int i;
    int a[8]={9,7,5,6,8,4,10,13};
    cout<<"original array";
    for(i=0;i<7;i++)
    {
	cout<<i<<": "<<a[i]<<" "<<endl;
    }
    cout<<i<<": "<<a[i]<<" ";
    makeMinHeap(a,8);

    cout<<"after arrange"<<endl;
    for(i=0;i<7;i++)
    {
	cout<<i<<": "<<a[i]<<" "<<endl;
    }
    cout<<i<<": "<<a[i]<<" ";
}
