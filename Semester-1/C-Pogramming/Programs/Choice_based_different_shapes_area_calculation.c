#include<stdio.h>
int main(){
int choice;
printf("Enter the choice \n 1. Area of Circle\n 2. Area of Sqaure\n 3. Area of Rectangle\n 4.Area of Triangle\n");
scanf("%d",&choice );
switch(choice){
  case 1: int area,radius;
          printf("FINDING THE AREA OF CIRCLE\n");
          printf("Enter the radius of the circle: ");
          scanf("%d",&radius);
          printf("The Area of Cirle with radius: %d is: %d",radius,2*3.14*radius);
          break;
  case 2:int area,side;
          printf("FINDING THE AREA OF SQUARE\n");
          printf("Enter the side of the square: ");
          scanf("%d",&side);
          printf("The Area of Square with side: %d is: %d",side,side*side);
          break;
  case 3:int area,length,breadth;
          printf("FINDING THE AREA OF RECTANGLE\n");
          printf("Enter the length of the rectangle: ");
          scanf("%d",&length);
          printf("Enter the breadth of the rectangle: ");
          scanf("%d",&breadth);
          printf("The Area of Rectangle with length: %d and breadth: %d is: %d",length,breadth,length*breadth);
          break;
  case 4:int area,base,height;
          printf("FINDING THE AREA OF TRIANGLE\n");
          printf("Enter the base of the triangle: ");
          scanf("%d",&base);
          printf("Enter the height of the triangle: ");
          scanf("%d",&height);
          printf("The Area of Triangle with base: %d and height: %d is: %d",base,height,0.5*(base*height));
          break;
}
return 0;
}
