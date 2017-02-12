#include <iostream>
#include "Mother.h"
using namespace std;

// note - ONLY include what you need. Do not need to include the 
// child class in the parent class - get circular reference 

Mother::Mother()
{
    cout << "I am the mother constructor!" << endl;
}

Mother::~Mother()
{
    cout << "I am the mother destructor!" << endl;
}

void Mother::sayName(){
    cout << "I am a Herrera" << endl;
}

