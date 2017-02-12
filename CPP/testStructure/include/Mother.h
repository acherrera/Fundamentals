# ifndef MOTHER_H // tells program to define this information
# define MOTHER_H 

class Mother
{
    public:
        Mother();
        ~Mother();
        void sayName();
        int publicv;
    protected:
        int protectedv; //protected and private variables
    private:
        int privatev;

};

#endif // MOTHER_H
