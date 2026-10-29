public class gcdDay16 {
    public static void main(String[] args) {
        int a=6;
        int b=12;
        System.out.println(GCD(a,b));
    }
    public static int GCD(int n, int m){
        int max=Integer.MIN_VALUE;
        int loop = Math.min(n, m);
        for(int i=1;i<=loop;i++){
            if(n%i==0&&m%i==0){
                max=Math.max(max, i);
            }
        }
        return max;
    }
}
