#include <iostream>
#include "Mother.h"
#include "Daughter.h"

using namespace std;

int main(){
    Daughter tina;
    tina.sayName(); // uses inherited method
    tina.dosomething(); // inherited method for private vs protected 

    return 0;
}
