import java.util.Scanner;
//1912
public class Main {
    static int[] cache;
    static int[] arr;
    static int n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        cache = new int[n];

        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();
        }

        cache[0]=arr[0];

        for(int i=1;  i<n; i++){
            cache[i] = Math.max(cache[i-1]+arr[i], arr[i]);
        }

        int max=cache[0];
        for(int i=0; i<n; i++){
            max = Math.max(cache[i], max);
        }
        System.out.println(max);
    }

}
