import java.util.Scanner;

public class Demo {

    public static void main(String[] args) {
        // Reads input from user
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter any number: ");

        // Read in number 
        int num = scan.nextInt();

        // Close the scanner after using
        scan.close();

        // Show the number
        System.out.println("The number entered by user: "+num);
    }
}
