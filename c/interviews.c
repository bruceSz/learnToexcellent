#include <stdio.h>
#include "string.h"
void print_hello(){
    printf("hello world\n");
}
int cross_border_read(){
    char a;
    char *str=&a;
    strcpy(str,"hello");
    printf("%s",str);
    return 0;
}

int constant_write(){
    char * s ="AA";
    s[0]='B';
    printf("%s",s);
}
int main(){

}
