# What is this

This is for helping with the differences between Python and C++.


# Big differences

## Pointers

Points only point at the address where a variables is stored rather than the
variabls itself is stored.

    int x = 5;
    int *p_x = &x;      // pointer (*) and address (&) 
    x = 10;             // set x to 10.
    *P_x = 10           // Does the same as the above
    cout << p_x << endl // This will only show the address of the variable


### References

References are like pointers but less so.

    int x = 5;
    int& ref = x; // This is just the addres of x

Example of references

    struct myBigStruct
    {
        int x[100]; //big struct
    };

    // This will take the 'myBigStruct' pointer passed to it.
    void takeStruct (myBigStruct& my_struct)
    {
        my_struct.x[0] = 23;
    }

