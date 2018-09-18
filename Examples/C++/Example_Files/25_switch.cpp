// Showing how to use switch statements

#include <iostream>

using namespace std;

void playgame()
{
    cout << "Playing game" << endl;
}

void loadgame()
{
    cout << "Loading game" << endl;
}

void playmultiplayer()
{
    cout << "Multiplayer time" << endl;
}

int main()
{
    int input;

    cout << "1. Play game\n";
    cout << "2. Load game\n";
    cout << "3. Play play multiplayer\n";
    cout << "4. Exit\n";
    cout << "Selection: ";
    cin >> input;
    switch( input )
    {
        case 1: // semicolon here. Odd formatting
            playgame();
            break;
        case 2:
            loadgame();
            break;
        case 3:
            playmultiplayer();
            break;
        case 4:
            cout << "Thank you for playing!\n";
            break;
        default:
            cout << "Error, bad input, quitting\n";
            break;
    }
}

