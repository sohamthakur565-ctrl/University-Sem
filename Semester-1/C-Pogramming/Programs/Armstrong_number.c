#include <stdio.h>

int main() {
    int n, rem, res = 0;
    int count = 0, temp, i;
    printf("Enter an integer: ");
    scanf("%d", &n);
    temp = n;
    while (temp != 0) {
        temp /= 10;
        count++;
    }
    temp = n;
    while (temp != 0) {
        rem = temp % 10;
        int power = 1;
        for (i = 0; i < count; i++) {
            power = power * rem;
        }
        res = res + power;
        temp /= 10;
    }
    if (res == n) {
        printf("%d is an Armstrong number.", n);
    } else {
        printf("%d is not an Armstrong number.", n);
    }
    return 0;
}
