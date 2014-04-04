#include <stdio.h>

int * smart_sort(int * arr,int length){
    return NULL

}

void test_smart_sort(){
    int a[] = {2,3,1,2,1,2,3,2,1,3,2,1,2,2,2,3,1,1,1,2,1,2,3,2,1}; 
    int length = sizeof(a)/sizeof(int);
    int *b = smart_sort(a,length);
    for (int i=0;i<length;i++){
        printf("%d",b[i]);
    }

}
int main(){
    int a[] = {1,2,3};
    int *b = a;
    test_smart_sort();
}
