// Recussion : A functoin calling itself is known as recussion function
#include<stdio.h>
void rev(int x);
int main(){
  rev(5);
  return 0;
}
 void rev(int x){
  if(x==0){
    printf("%d",x);
    rev(x-1);
  }
 }
