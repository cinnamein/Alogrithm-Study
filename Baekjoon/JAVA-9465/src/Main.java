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
            int[][] arr = new int[2][m];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int k = 0; k < 2; k++) {
                for (int j = 0; j < m; j++) {
                    int tmp = Integer.parseInt(st.nextToken());
                    arr[k][j] = tmp;
                }
            }
            int result = 0;
            for (int r = 0; r < m; r++) {
                if (arr[0][r] + arr[1][r + 2] >= arr[0][r] + arr[1][r + 1] + arr[0][r + 2]) {
                    result += arr[0][r] + arr[1][r + 2];
                } else {
                    result += arr[0][r] + arr[1][r + 1] + arr[0][r + 2];
                }
            }
            System.out.println(result);
        }
    }
}
