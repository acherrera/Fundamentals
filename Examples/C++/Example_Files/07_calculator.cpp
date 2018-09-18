# include <iostream>

using namespace std;

int main()
{
    int first_argument;
    int second_arguement;
    cout << "Enter first argument: ";
    cin >> first_argument;
    cout << "Enter second argument: ";
    cin >> second_arguement;
    cout << first_argument << " * " << second_arguement 
         << " = " << first_argument * second_arguement 
         << endl;
    cout << first_argument << " + " << second_arguement 
         << " = " << first_argument + second_arguement 
         << endl;
    cout << first_argument << " - " << second_arguement 
         << " = " << first_argument - second_arguement 
         << endl;
    cout << first_argument << " / " << second_arguement 
         << " = " << first_argument / second_arguement 
         << endl;
}
