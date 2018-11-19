//NOTE: Does not actually run


public abstract class Animal{
    public abstract void animalSound();
}

public class Lion extends Animal{
    @override
    public void animalSound(){
        Sysem.out.println("Roar");
    }
}

public class Dog extends Animal{
    @override
    public void animalSound(){
        Sysem.out.println("Woof");
    }
}

