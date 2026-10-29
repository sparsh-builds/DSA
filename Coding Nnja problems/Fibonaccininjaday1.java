

public class Fibonaccininjaday1 {
    public static void main(String[] args) {
        int n = 6;
        System.out.println("Fibonacci of " + n + " is: " + nthFibonacci(n));
    }

    public static int nthFibonacci(int n) {
        if (n == 0) {
            return 0;
        } 
        else if (n == 1) {
            return 1;
        }
        return nthFibonacci(n - 1) + nthFibonacci(n - 2);
    }
}
