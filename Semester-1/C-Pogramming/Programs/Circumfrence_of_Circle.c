#include<stdio.h>
int main(){
   float circumfrence,radius,pi=3.14;
   printf("Enter the radius of circle : ");
   scanf("%f",&radius);
   circumfrence=2*pi*radius;
   printf("The circumfrence of circle is %f",circumfrence);
   return 0;
}
