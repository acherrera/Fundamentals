/* Here we are trying to sort a list of one hundred numbers
* Note that function 'findSmallestRemainingElement' and 
* 'swap' wre ipmlemented after they were first called in the sort 
* function
*/

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;


// prototyping time!

int findSmallestRemainingElement(int array[], int size, int index);
void swap (int array[], int first_index, int second_index);

// Defining Functions - may want to put this under main 

void sort (int array[], int size)
{
    // function just implements 'findSmallest...' and 'swap'
    for ( int i = 0; i < 100; i++ )
    {
        int index = findSmallestRemainingElement ( array , size, i);
        swap (array, i, index);
    }
}



int findSmallestRemainingElement (int array[], int size, int index)
{
    /* Given an array and an index value, This loops through the array from the
     * given index and checks if the value is smallest than the next value. If
     * the value is smaller, the new index is saved. 
     */

    int index_of_smallest_value = index;
    for (int i = index + 1; i < size;  i++)
    {
        // Starts at the next value of the index
        if ( array[ i ] < array[ index_of_smallest_value ] )
        {
            index_of_smallest_value = i;
        }
    }
    return index_of_smallest_value;
}


void swap(int array[], int first_index,  int second_index)
{
    int temp = array[ first_index ];
    array[ first_index ] = array[ second_index ];
    array[ second_index ] = temp;
}


// helper function to display the before adn after arrays
void displayArray (int array[], int size)
{
    cout << "{";
    for ( int i = 0; i < size; i++)
    {
        //You'll see this a lot for formatting lists. If we are psat the first
        //element, append a comma
        if ( i != 0 )
        {
            cout << ", ";
        }
        cout << array[ i ];
    }
    cout << "}";
}


int main()
{
   int array[ 10 ];
   srand( time ( NULL ) );
   for ( int i = 0; i < 10; i++ )
   {
        //Keep numbers small so that they are easy to read
        array[ i ] = rand() % 100;
   }
   cout << "Original array: ";
   displayArray( array, 10 );
   cout << '\n';

   sort( array, 10 );
   cout << "Sorted array: ";
   displayArray( array, 10);
   cout << '\n';
}

