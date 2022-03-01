import java.util.Scanner;
//1018
public class Main {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        String[] arr = new String[n];
        for(int i=0; i<n; i++){
                arr[i]=scanner.next();
        }
        String[] black = new String[8];
        String[] white = new String[8];
        for(int i=0; i<8; i+=2){
            black[i]="BWBWBWBW";
            black[i+1]="WBWBWBWB";
            white[i]="WBWBWBWB";
            white[i+1]="BWBWBWBW";
        }

        int countw;
        int countb;
        int min = 64;
        for(int i=0; i<n-7; i++){
            for(int j=0; j<m-7; j++){
                countw=0;
                countb=0;
                //다른부분찾기
                for(int k=0; k<8; k++){
                    for(int l=0; l<8; l++){
                        if(black[k].charAt(l)!=arr[k+i].charAt(l+j)){
                            countb++;
                        }
                        if(white[k].charAt(l)!=arr[k+i].charAt(l+j)){
                            countw++;
                        }
                    }
                }
                min=Math.min(min, countb);
                min=Math.min(min, countw);
            }
        }
        System.out.println(min);
    }
}
