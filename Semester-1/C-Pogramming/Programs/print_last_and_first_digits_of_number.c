#include <stdio.h>
int main(){
    int n,fd,ld;
    printf("Enter a number : ");
    scanf("%d",&n);
    ld=n%10;
    while(n>=10){
      n=n/10;
    }
    fd=n;
    printf("First digit is %d and \n last digit is %d",fd,ld);
  return 0;
}
