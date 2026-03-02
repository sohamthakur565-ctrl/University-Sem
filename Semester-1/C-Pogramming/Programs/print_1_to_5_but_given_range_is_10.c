#include<stdio.h>
int main()
{
    int i = 1, n = 10;
    while(i != n)
    {
        printf("i=%d\n", i);
        if(i == 5)
            break;
        i++;
    }
return 0;
}
