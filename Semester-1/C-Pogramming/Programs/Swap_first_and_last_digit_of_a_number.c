#include<stdio.h>
int main(){
   int n,l,f,s;
    printf("Enter a number : ");
    scanf("%d",&n);
    l=n%10;
   while(n>=10){
    n=n/10;
   }
   f=n;
  s=n;
  n=f;
  f=s;
  printf("The swap of first and last digit is %d and %d",f,l);
  return 0;
}
