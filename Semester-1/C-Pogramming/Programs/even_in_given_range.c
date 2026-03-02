#include<stdio.h>
int main(){
   int sp,ep,even;
   printf("Enter starting and ending point : ");
   scanf("%d%d",&sp,&ep);
   while(sp!=ep)
   {
      even = sp%2;
      if(even == 0)
      {
         printf("Even Number = %d",sp);
       }
      sp++;
    }
  return 0;
 }
