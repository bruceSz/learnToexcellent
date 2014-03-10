#include <stdio.h>
int main(void){
    char * str="this is a test str";
    void * vstr=str;


    printf("this is c world\n");
    printf("%c",*(char *)vstr);
    return 0;
}
