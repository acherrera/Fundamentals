# ifndef CLASSTEMPLATE_H // tells program to define this information
# define CLASSTEMPLATE_H // ALL CAPS HERE

// use #include "Parent.h" to import parent classes do not need to
// include parent functions in the delcarations below. It just assumes


// use ""class Classtemplate: public Parent"" to use a parent class

class ClassTemplate// same as file name
{
    // variables, functions, constructor, destructor names go here
    public:
        ClassTemplate();        // constructor
        void ExampleFunction(); // function in class
        ~ ClassTemplate();      // destructor
    protected:
    private:

};

// No idea of comment needs to be at end - leave for now

#endif          // CLASSTEMPLATE_H
