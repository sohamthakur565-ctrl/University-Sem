#include<stdio.h>
int main(){
  int n,i,sum=0;
  printf("Enter a number : ");
  scanf("%d",&n);
  while(n!=0){
    sum=sum+n;
    n--;
  }
  printf("The sum of first %d natural numbers is %d",n,sum);
  return 0;
}
