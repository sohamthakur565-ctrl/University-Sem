#include <iostream>
namespace first{
 int x=1;
}
namespace second{
 int x=2;
}
int main(){
  using namespace first;
  //int x=0;
  std::cout<<x; //this prints the local x variable, if it is present, otherwise use first_x variable;
  return 0;
}
