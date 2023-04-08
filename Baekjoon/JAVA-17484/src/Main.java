import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr;
    static int[] movement = {-1, 0, 1};
    static int n, m, sum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        sum = 600;
        arr = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int k = 1; k <= m; k++) {
            dp(k, 1, arr[1][k], 10);
        }
        System.out.println(sum);
    }

    public static void dp(int x, int y, int tmp, int des) {
        if (y == n) {
            sum = Math.min(tmp, sum);
            return;
        }
        for (int i = 0; i < 3; i++) {
            if (i == des) continue;
            int mx = x + movement[i];
            if (y < n && 0 < mx && mx <= m) {
                dp(mx, y + 1, tmp + arr[y + 1][mx], i);
            }
        }
    }
}