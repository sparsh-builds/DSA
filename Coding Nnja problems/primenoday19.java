public class primenoday19 {
    public static void main(String[] args) {
        int n=23;
        System.out.println(Prime(n));
    }
    public static String Prime(int n){
        for(int i=2;i<n;i++){
            if(n%i==0){
                return "yes";
            }

        }
        return "No";
    }
}
