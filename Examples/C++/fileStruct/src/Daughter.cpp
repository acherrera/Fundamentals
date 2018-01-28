#include <iostream>
#include "Mother.h"
#include "Daughter.h"

using namespace std;

Daughter::Daughter()
{
    // constructor goes here - blank for now
}

void Daughter::dosomething()
{
    publicv = 1; //just changes values showing it has access to these
    protectedv = 2;
    // privatev will not able to use
}
