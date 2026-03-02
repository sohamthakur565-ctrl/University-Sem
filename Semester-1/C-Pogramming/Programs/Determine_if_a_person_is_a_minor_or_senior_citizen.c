// Program to determine if a person is a minor or senior citizen, check attendance and exam result
#include <stdio.h>
int main(){
    system("cls");
    int age,attendance,marks;
    printf("Enter your age: ");
    scanf("%d",&age);
    if(age>=18){
        printf("You are a senior citizen");
        printf("please enter your attendance: ");
        scanf("%d",&attendance);
        if(attendance>=75){
            printf("\nYou are an adult and your birth year is %d",attendance);
            printf("\nEnter your marks: ");
            scanf("%d",&marks);
            if(marks>=40){
                printf("\nYou have passed the exam");
            }
            else{
                printf("\nYou have failed the exam");
            }
        }
        else{
            printf("You are an adult but your attendance is below 75%");
        }
    }
    else{
        printf("You are a minor");
    }        
    return 0;
}
