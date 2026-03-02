#include <iostream>
int main(){
//Typedef is the alias name;
//Using is the replacement for Typedef keyword (works better w/ templates);
using text_t=std::string;
  text_t name = "Krishna";
  std::cout<<name;
  return 0;
}
