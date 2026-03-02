#include<stdio.h>
int main(){
 float x,y,z;
    printf("Enter marks of C Programming :");
    scanf("%f",&x);
    printf("Enter marks of Data Structure :");
    scanf("%f",&y);
    z= x*0.3/100 + y*0.7/100;
    printf("the result is : %f",z);
return 0;
}
