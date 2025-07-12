#include <iostream>
#include <exception>
using namespace std;

struct MyException : public exception
{
  const char * what () const throw ()
  {
    return "Exception trong C++";
  }
};
 
int main()
{
  try
  {
    throw MyException();
  }
  catch(MyException& e)
  {
    std::cout << "MyException da duoc bat!" << std::endl;
    std::cout << e.what() << std::endl;
  }
  catch(std::exception& e)
  {
    // phan nay danh cho cac error khac
  }
}