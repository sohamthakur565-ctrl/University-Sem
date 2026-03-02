void swap(int *x, int *y) {
    printf("Inside swap: Before swapping *x is %d and *y is %d\n", *x, *y);
    int temp = *x; // temp holds the value at address x
    *x = *y;       // value at address x becomes the value at address y
    *y = temp;     // value at address y becomes temp
    printf("Inside swap: After swapping *x is %d and *y is %d\n", *x, *y);
}
int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Before calling swap: a is %d and b is %d\n", a, b);
    swap(&a, &b);
    printf("After calling swap in main: a is %d and b is %d\n", a, b);
    return 0;
}
