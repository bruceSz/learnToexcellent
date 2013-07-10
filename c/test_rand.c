#include<stdio.h>
#include<time.h>
int main(){
    srand((int)time(0));
    int i = 0;
    for(;i<10;i++){
	printf("%d\n",rand()%26);
    }
}
