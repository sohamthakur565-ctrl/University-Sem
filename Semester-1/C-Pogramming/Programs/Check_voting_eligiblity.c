#include <stdio.h>  
int main() {
    int b,age;
    printf("Enter 1 if you are an Indian citizen ");
    scanf(" %d", &b);
    if(b == 1) {
        printf("Enter your age: ");
        scanf("%d", &age);
        if(age >= 18) {
            printf("You are eligible to vote.\n");
        } else {
            printf("You are not eligible to vote.\n");
        }
    } else {
        printf("Only Indian citizens are eligible to vote.\n");
    }
    return 0;
}
