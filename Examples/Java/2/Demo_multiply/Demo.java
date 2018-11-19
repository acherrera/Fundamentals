import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        //Reading the input
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter first number: ");

        // Read number entered 
        int num1 = scan.nextInt();

        System.out.print("Enter second number: ");
        int num2 = scan.nextInt();

        // Close scanner
        scan.close();

        //Calculatin product of two numbers
        int product = num1*num2;

        //Show result
        System.out.println("Output: "+product);
    }
}
