public class VariableExample {
    // instance variable
    public String myVar="instance variable";

    public void myMethod(){
        // local variable
        String myVar = "Inside Method";
        System.out.println(myVar);
    }

    public static void main(String args[]){
        // Create object
        VariableExample obj = new VariableExample();

        System.out.println("Called Method");
        obj.myMethod();
        System.out.println(obj.myVar);
    }
}
