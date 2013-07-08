#include "stdio.h"

int main() {
    int arr[5];
    struct student {
      int num;
      int numUnits;
    };
    struct student stu[4];
    printf("%d\n",&(arr[0]));
    printf("%d\n",&(arr[1]));
    printf("\n");

    printf("%d\n",&(stu[0].num));

    printf("%d\n",&(stu[0].numUnits));
}
