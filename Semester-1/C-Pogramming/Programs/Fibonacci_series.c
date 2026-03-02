#include<stdio.h>
int main(){
  int n1=0,n2=1,next,n,i;
  printf("Enter a number : ");
  scanf("%d",&n);
  printf("%d\n%d\n",n1,n2);
  for(i=2;i<n;i++){
    next=n1+n2;
    printf("%d\n",next);
    n1=n2;
    n2=next;
  }
  return 0;
}
