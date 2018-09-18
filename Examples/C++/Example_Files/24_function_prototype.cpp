#include <iostream>

using namespace std;

// function prototype for add - define at bottom
// This allow the function to compile even though we won't actually
// create the function till the bottom
int add (int x, int y);

int main()
{
    int result = add ( 1, 2 );
    cout << "This result is: " << result << "\n";
    cout << "Adding 3 and 4 gives us: " << add (3, 4) << endl;
}

int add (int x, int y)
{
    return x + y;
}

