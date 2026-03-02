#include<stdio.h>
int main(){
    system("cls");
    int a;
    printf("Enter a number : \n");
    scanf("%d",&a);
    if(a>0){
        printf("the number is positive ");
    }
    else if(a<0){
        printf("the number is negative ");
    }
    else{
        printf("the number is zero ");
    }
return 0;
}
