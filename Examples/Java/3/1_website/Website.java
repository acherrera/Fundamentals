public class Website {
    //instance variables
    String webName;
    int webAge;

    //constructor
    Website(String name, int age) {
        this.webName = name;
        this.webAge = age;
    }

    public static void main(String args[]){
        //Create objects
        Website obj1 = new Website("beginnersbook", 5);
        Website obj2 = new Website("google", 18);

        //Accessing object data
        System.out.println(obj1.webName+" is "+obj1.webAge+" years old");
        System.out.println(obj2.webName+" is "+obj2.webAge+" years old");
    }
}
