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
        for (int k = 1; k < m; k++) {
            System.out.println("--------------------------------");
            dp(1, k, arr[1][k], 10);
        }
        System.out.println(sum);
    }

    public static void dp(int y, int x, int tmp, int des) {
        System.out.println("x: " + x + ", y: " + y + ", tmp: " + tmp + " arr[x][y] = " + arr[y][x]);
        if (y == n) {
            sum = Math.min(tmp, sum);
            System.out.println("sum: " + sum);
            return;
        }
        for (int i = 0; i < 3; i++) {
            if (i == des) continue;
            int mx = x + movement[i];
            if (y < n && 0 < mx && mx <= m) {
                tmp += arr[y + 1][mx];
                dp(y + 1, mx, tmp, i);
            }
        }
    }
}
//559154
//121211