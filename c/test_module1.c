#include<stdio.h>

#include<stdlib.h>
#include<string.h>
#include "test_module_dll.h"
void done() {
    printf("this is test module 1");
}

void init(dll *p){
    p->name = (char *)calloc(4,sizeof(char));
    strcpy(p->name,"so1");
    p->done = done;
}
