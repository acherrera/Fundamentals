/* Switch the values of the two variables. Only the second method 
* works without making a copy of the variables
*
* Note that this is a typical example
*
* Creating a pointer
* varb = 5;
* int *p_name = NULL;       instantiate as NULL to avoid issues
* int *p_name2 = &varb;     Create pointer and assign address
* cout << p_name2 << endl;  Will print address
* cout << *p_name2 << endl; Will print value at address
*/


#include <iostream>

using namespace std;


void swap1(int left, int right)
{
    int temp = left;
    left = right;
    right = temp;
    // This does not return a value. Values are not changed.
}


void swap2 (int *p_left, int *p_right)
{
    int temp = *p_left;
    *p_left = *p_right;
    *p_right = temp;
    // This also does not return. But this taken in an address and
    // changes the value AT THAT ADDRESS. Therefore, values changes
} 


int main()
{
    int x=1, y=2;
    swap1(x ,y);
    cout << x << " " << y << '\n';
    swap2(&x, &y);      // Pass the address to the function
    cout << x << " " << y << '\n';
}
