#include<stdio.h>
int main(){
    int ep,i,j,prime,sum=0;
    printf("Enter ending point : ");
    scanf("%d",&ep);
    for(i=0;i<=ep;i++){
        prime=0;
        for(j=2;j<=i/2;j++){
            if(i%j==0){
                prime=1;
                break;
            }
        }
        if(prime==0 && i!=1){
            sum=sum+i;
        }
    }
    printf("The sum of prime numbers till %d is %d",ep,sum);
return 0;
}
