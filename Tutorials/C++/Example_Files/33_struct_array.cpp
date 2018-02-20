#include <iostream>

using namespace std;

struct PlayerInfo
{
    // simple structure so store player data
    int skill_level;
    string name;
};


int main()
{
    //can make arrays of structure like normal variables
    
    PlayerInfo players[ 5 ];
    for (int i = 0; i < 5; i++ )
    {
        cout << "Please enter the name for player " << i << "\n";
        cin >> players[ i ].name;
        cout << "Plesae enter the skill level for " << players[i].name
             << "\n";
        cin >> players[i].skill_level;
    }

    for ( int i = 0; i < 5; i++)
    {
        cout << players[i].name << " is at skill level "
             << players[i].skill_level << "\n";
    }
}

