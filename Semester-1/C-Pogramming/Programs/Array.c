#include<stdio.h>
# define MAXSIZE 100
int main(){    
     int size;
     printf("Enter the size of array : ");
     scanf("%d",&size); 
      int arr[size];
     printf("Enter %d elements in array : \n",size);
     for(int i=0;i<size;i++){
     scanf("%d",&arr[i]);
     }
     printf("The elements of array are : \n");     
      for(int i=0;i<size;i++){
        printf("%d\n",arr[i]);
      }
  return 0;
}
