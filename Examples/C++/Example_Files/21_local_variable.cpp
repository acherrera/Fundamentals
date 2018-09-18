// Showing variable's scope

#include <iostream>

using namespace std;

void changeArguement(int x)
{
    x += 5;
}

int main()
{
    int y = 4;
    changeArguement(y);
    // This does nothing to y. It is passed to the function but the
    // function variables is only valid in the funciton itself
    
    cout << y; //Still 4
}

