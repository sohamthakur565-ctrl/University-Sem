 #include<stdio.h>
  void swap(int *x,int *y){
    printf("Before swapping  x is %d and y is %d\n",*x,*y);
    int temp=*x;
    *x=*y;
    *y=temp;
    printf("After swapping  x is %d and y is %d\n",*x,*y);
  }
int main(){
  int a,b;
  printf("Enter two numbers : \n");
  scanf("%d%d",&a,&b);
  printf("Before calling swap function a is %d and b is %d\n",a,b);
  swap(&a,&b);
  printf("After calling swap function a is %d and b is %d\n",a,b);
return 0;
}
