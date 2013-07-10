#include<stdio.h>
#include<dlfcn.h>
#include<stdlib.h>
#include "test_module_dll.h"

int main(){

    void * dp;
    char * err;
    char temp[20];
    char fname[20];
    dll p;
    void (*init)(dll *p);
    printf("please input name of modle:");
    scanf("%s",temp);
    sprintf(fname,"./%s",temp);
    printf("your input is: %s\n",fname);
    dp = dlopen(fname,RTLD_LAZY);
    if (NULL == dp){
	printf("%s\n",dlerror());
	exit(1);
    }
    init = dlsym(dp,"init");
    init(&p);
    printf("%s\n",p.name);
}
