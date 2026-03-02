#include <iostream>
using namespace std;
int main(){
int n = 1234;
int rem=0; int rev=0;
while(n!=0){
    rem=n%10;
    rev=rev*10+rem;
    n=n/10;
}
cout<<"The reverse order:"<<rev;
return 0;
}
