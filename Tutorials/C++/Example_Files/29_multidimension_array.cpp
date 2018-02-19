#include <iostream>

using namespace std;

int main()
{
    int array [8][8]; //declare an 8x8 array

    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++ )
        {
            //set element values
            array[i][j] = i*j;
        }
    }

    cout << "Multiplication tables:\n";
    for (int i =0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++ )
        {
            cout << i << " * " << j << " = ";
            cout << array[i][j] << "\n";
        }
    }
}

