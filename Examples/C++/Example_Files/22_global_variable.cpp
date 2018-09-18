#include <iostream>

using namespace std;


int doStuff() 
{
    // just demonstrating scope
    // not used? 
    return 2 + 3;
}

// Global variables can be initialized like other variables
// This is available everywhere to use because it was called 
// outside of all the functions. Usually not a good idea to use
int count_of_function_calls = 0;

void fun ()
{
    // global variable is avialable here
    count_of_function_calls++;
}

int main()
{
    fun();
    fun();
    fun();

    cout << "Function fun was called " << count_of_function_calls
          << " times\n";
}
