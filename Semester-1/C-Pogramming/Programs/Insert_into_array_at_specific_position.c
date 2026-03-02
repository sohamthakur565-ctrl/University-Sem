 #include<stdio.h>
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
 int n,pas;
 printf("Enter the new element & position : ");
 scanf("%d %d",&n,&pas);
 if (pas>size||pas<=0){
  printf("Invalid position");
 }
 else{
   for(int i=size;i>=pas-1;i--){
    arr[i]=arr[i-1];
    // incomplete
   }

  }
   arr[pas-1]=n;
   size++;
   printf("The elements of array after insertion are : \n");     
      for(int i=0;i<size;i++){
        printf("%d\n",arr[i]);
      }
  return 0;
 }
