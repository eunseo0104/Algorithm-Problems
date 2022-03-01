import java.util.Scanner;
//1149
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][3];
        for(int i=0; i<n; i++){
            for(int j=0; j<3; j++){
                arr[i][j]=sc.nextInt();
            }
        }
        int min;
        int[][] cache = new int[n][n];
        cache[0][0]=arr[0][0];
        cache[0][1]=arr[0][1];
        cache[0][2]=arr[0][2];

        for(int i=1; i<n; i++){
            for(int j=0; j<3; j++){
                cache[i][j] = Math.min(cache[i-1][(j+1)%3], cache[i-1][(j+2)%3])
                +arr[i][j];

            }
        }

        min = Math.min(cache[n-1][0], cache[n-1][1]);
        min = Math.min(min, cache[n-1][2]);

        System.out.println(min);
    }

}
