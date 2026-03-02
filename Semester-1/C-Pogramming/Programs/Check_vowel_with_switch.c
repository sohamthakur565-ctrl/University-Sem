#include<stdio.h>
int main(){
    char ch;
    printf("enter an alphabet:");
    scanf("%c",&ch);
    switch(ch){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            printf("the given alphabet %c is a vowel",ch);
            break;
        default: 
        printf("the given alphabet %c is a consonent",ch);
    }
    return 0;
}
