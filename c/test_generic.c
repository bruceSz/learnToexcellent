#include <stdio.h>
struct student {
    char *name;
    int number;
};
void * lsearch(void *key,
	    void * base,
	    int n,
	    int elementSize) {
    int i;

    for (i=0;i<n;i++) {
	void * elementAddr = base + i * elementSize;
	if (memcmp(key,elementAddr,elementSize)==0) {
	    return elementAddr;
	}
    }
    return NULL;
	    

}
int main() {
    //struct student stu;
    //printf("%lu\n",sizeof(stu.name));
    //printf("%lu\n",sizeof(stu.number));
    //printf("%lu\n",sizeof(int));
    int array[] = {4,2,3,7,11,6};
    int size = 6;
    int number = 8;
    int * found = lsearch(&number,array,6,sizeof(int));
    if(NULL != found) {
	printf("%d",*found);
    }
    else {
	printf("not found");
    }

}
