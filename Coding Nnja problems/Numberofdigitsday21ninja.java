public class Numberofdigitsday21ninja {
    public static void main(String[] args) {
        int n=135;
        System.out.println(digits(n));
    }
    public static int digits(int n){
        int count =0;
        while (n>0) {
            n=n/10;
            count++;
        }
        return count;
    }
}
