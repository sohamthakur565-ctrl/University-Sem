#include<stdio.h>
int main()
{
    int y,x,temp;
    printf("Enter two numbers:");
    scanf("%d%d",&x,&y);
    printf("Before swapping a=%d b=%d\n",x,y);
    x=x+y;
    y=x-y;
    x=x-y;
    printf("After swapping a=%d b=%d\n",x,y);
    return 0;
}
