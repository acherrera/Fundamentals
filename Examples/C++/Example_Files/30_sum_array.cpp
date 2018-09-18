#include <iostream>

using namespace std;

// showing how to pass arrays to a function. Need to pass both the array and
// the size of the array. 
int sumArray (int values[], int size)
{
    int sum = 0;
    for ( int i = 0; i < size; i++)
    {
        sum += values[i];
    }
    return sum;
}


int main()
{
    int arraySize = 10; //This was my change

    int values[ arraySize ];
    for (int i = 0; i < arraySize; i++)
    {
        cout << "Enter value " << i+1 << ": ";
        cin >> values [ i ];
    }
    int sumValue = sumArray(values, arraySize);
    cout << "Sum of values is: "<< sumValue << endl;
}

