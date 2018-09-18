// Note that this doesn't actually run. Only an example
#include <iostream>

using namespace std;

struct EnemySpaceShip 
{
    int x_coordinate;
    int y_coordinate;
    int weapon_power;
};


// This function will create an enemy ship struct
EnemySpaceShip getNewEnemy()
{
    EnemySpaceShip ship;
    ship.x_coordinate = 0;
    ship.y_coordinate = 0;
    ship.weapon_power = 20;
    return ship;
}

EnemySpaceShip upgradeWeapons (EnemySpaceShip ship)
{
    //Note that structures are copied on functions. See implementation
    ship.weapon_power += 10;
    return ship;
}

int main()
{
    EnemySpaceShip enemy = getNewEnemy(); //using function

    enemy = upgradeWeapons(enemy); //need to assigned to original struct
}

