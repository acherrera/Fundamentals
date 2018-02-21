/* Code showing how to resize array using pointers. If the number entered would
 * cause the array to be larger than the current array, the array is doubled
 * to allow for more numbers to be entered
 */

#include <iostream>

using namespace std;

// prototyping
int *growArray(int* p_values, int *size); // Function returns a pointer
void printArray(int* p_values, int size, int elements_set); 

int main()
{
    int next_element = 0;       // starting element is 0
    int size = 10;              // starting size is 0
    int *p_values = new int[ size ]; //dynamic memory array using pointer. This is so it can change later
    int val;
    cout << "Please enter a number: ";
    cin >> val;
    
    // This loop runs until user tells it to stop
    while ( val > 0  )
    {
        if ( size == next_element+1 ) 
        {
            // If the size is as large as it can be. 
            // Need to implement the grow Array function
            // next_element is zero index. Size is one index
            p_values = growArray( p_values, &size );    // Notice that we pass address of size
        }
        p_values[ next_element ] = val;     // Set next element to value
        next_element++;                     // Increase next element value
        
        // Print the array values
        cout << "Current array values are: " << endl; 
        printArray( p_values, size, next_element );
        cout << "Please enter a number (or 0 to exit): ";
        cin >> val;
    }
    delete [] p_values;
}

void printArray ( int *p_values, int size, int elements_set )
{
    // elements set equals next element in implementation
    //
    cout << "The total size of the array is " << size << endl;
    cout << "Number of slots set so far: " << elements_set << endl;
    cout << "Values in the array: " << endl;
    for (int i = 0; i < elements_set; i++)  // print all values
    {
        cout << "p_values[" << i << "] = " << p_values[ i ] << endl;
    }
}

int *growArray(int* p_values, int *size)
{
    *size *= 2; //double the size of the value
    int *p_new_values = new int[ *size ]; //create new array of new size
    for ( int i = 0; i < *size; i++ )
    {
        p_new_values[ i ] = p_values[ i ];
    }
    delete [] p_values;
    return p_new_values;
}
