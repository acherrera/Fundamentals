// Function example

#include <iostream>

using namespace std;

int add (int x, int y)
{
    return x + y;
}

int main()
{
    int result = add( 1, 2 );
    // call add and assign result to variable 
    
    cout << "The result is: " << result << "\n";
    cout << "Adding 3 and 4 gives us: " << add ( 3, 4 ) << '\n';
}

