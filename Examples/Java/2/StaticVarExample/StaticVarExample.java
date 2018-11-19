public class StaticVarExample {
    public static String myClassVar="class or static variable";

    public static void main(String args[]){
        StaticVarExample obj = new StaticVarExample();
        StaticVarExample obj2 = new StaticVarExample();
        StaticVarExample obj3 = new StaticVarExample();

        //All three will show the same
        System.out.println(obj.myClassVar);
        System.out.println(obj2.myClassVar);
        System.out.println(obj3.myClassVar);


        //changing the value of static varialbe
        obj2.myClassVar = "Changed Text";

        // Now all three
        System.out.println(obj.myClassVar);
        System.out.println(obj2.myClassVar);
        System.out.println(obj3.myClassVar);
    }
}
