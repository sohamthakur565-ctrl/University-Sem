#include <stdio.h>
int main(){
   int  n=0,i,next=0,n1=1,m;
   printf("Enter a number : ");
   scanf("%d",&m);
   while(n<=m){
    n=n1;
    n1=next;
    next=n+n1;
    printf("%d\n",next);
   }
  return 0;
}
