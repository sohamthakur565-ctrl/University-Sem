#include <stdio.h>
#include <stdlib.h>
#include <string.h>
union student
{
    char name[40];
    int age;
    unsigned long long mobile;
};
int main()
{
    union student st1;
    printf("enter student name: ");
    fgets(st1.name, 40, stdin);
    printf("enter student age: ");
    scanf("%d", &st1.age);
    printf("enter student mobile: ");
    scanf("%lu", &st1.mobile);
    printf("\nthe student name %s", st1.name);
    printf("the student age %d\n", st1.age);
    printf("the student mobile %lu\n", st1.mobile);
    return 0;
}
