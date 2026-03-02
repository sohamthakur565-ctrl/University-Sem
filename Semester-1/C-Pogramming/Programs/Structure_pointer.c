#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct student {
    char name[50];
    int age;
    unsigned long mobile;
    };
    int main() {
    struct student *st2;
    st2 = (struct student *)malloc(sizeof(struct student));
    printf("Enter the student name: ");
    fgets(st2->name, 40, stdin);
    printf("Enter the student age: ");
    scanf("%d", &st2->age);
    printf("Enter the student mobile number: ");
    scanf("%lu", &st2->mobile);
    printf("\nStudent Details:\n");
    printf("Student Name: %s", st2->name);
    printf("Student Age: %d\n", st2->age);
    printf("The student Mobile: %lu\n", st2->mobile);
    return 0;
}
