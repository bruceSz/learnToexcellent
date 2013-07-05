#include <stdio.h>
void swap(void * vp1,void * vp2,int size){
    char buff[size];
}
int main(){
    int a = 1;
    int b = 2;
    swap(&a,&b,sizeof(int));
}
