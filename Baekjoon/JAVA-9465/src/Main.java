import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int m = Integer.parseInt(br.readLine());
            int[][] arr = new int[2][m + 1];
            int[][] result = new int[2][m + 1];
            for (int k = 0; k < 2; k++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 1; j <= m; j++) {
                    int tmp = Integer.parseInt(st.nextToken());
                    arr[k][j] = tmp;
                }
            }
            if (m == 1) System.out.println(Math.max(arr[0][1], arr[1][1]));
            else if (m == 2) System.out.println(Math.max(arr[0][1] + arr[1][2], arr[1][1] + arr[0][2]));
            else {
                result[0][1] = arr[0][1];
                result[1][1] = arr[1][1];
                for (int r = 2; r <= m; r++) {
                    result[0][r] = Math.max(result[1][r - 1], result[1][r - 2]) + arr[0][r];
                    result[1][r] = Math.max(result[0][r - 1], result[0][r - 2]) + arr[1][r];
                }
                System.out.println(Math.max(result[0][m], result[1][m]));
            }
        }
    }
}