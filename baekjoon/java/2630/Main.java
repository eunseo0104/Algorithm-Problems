import java.util.Scanner;
//2630
public class Main {
    private static int N;
    private static int[][] arr;
    private static int cntB;
    private static int cntW;
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        cntB=0;
        cntW=0;
        N = scan.nextInt();
        arr = new int[N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr[i][j] = scan.nextInt();
            }
        }
        f(0,0,N);
        System.out.println(cntW);
        System.out.println(cntB);
    }
    private static void f(int x, int y, int m){
        if(m == 1) {
            if(arr[y][x]==1){
                cntB++;
            }
            else cntW++;
            return;
        }
        int num = arr[y][x];
        for(int i=0; i<m; i++){
            for(int j=0; j<m; j++){
                if(arr[y+i][x+j] != num){
                    f(x, y, m/2);
                    f(x+m/2, y, m/2);
                    f(x, y+m/2, m/2);
                    f(x+m/2, y+m/2, m/2);

                    return;

                }
            }
        }
        if(arr[y][x]==1){
            cntB++;
        }
        else cntW++;
    }
}
