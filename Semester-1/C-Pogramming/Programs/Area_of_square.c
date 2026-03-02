#include <stdio.h>
int main() {
    float side,area;
    printf("Enter side of the square: ");
    scanf("%f", &side);
    area = side * side;
    printf("Area of the square: %.2f\n", area);
return 0;
}
