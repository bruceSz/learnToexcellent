#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "test_module_dll.h"
void done() {
    printf("tis is test module 2\n");
}

void init(dll *p) {
    p->name = (char *)calloc(4,sizeof(char));
    strcpy(p->name,"so2");
    p->done = done;
}
