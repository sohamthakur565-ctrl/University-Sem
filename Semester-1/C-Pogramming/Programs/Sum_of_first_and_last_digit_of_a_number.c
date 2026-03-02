#include<stdio.h>
int main(){
   int n,l,f,sum;
    printf("Enter a number : ");
    scanf("%d",&n);
    l=n%10;
   while(n>=10){
    n=n/10;
   }
   f=n;
   sum=f+l;
  printf("The sum of first and last digit is %d",sum);
  return 0;
}
