import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int m, n, h;
    static int[][][] tomato;
    static int[] dm = {1, -1, 0, 0, 0, 0};
    static int[] dn = {0, 0, 1, -1, 0, 0};
    static int[] dh = {0, 0, 0, 0, 1, -1};
    static Queue<Pair> queue = new LinkedList<>();

    static class Pair {
        int x, y, z;
        Pair(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
        int getX() {
            return x;
        }
        int getY() {
            return y;
        }
        int getZ() {
            return z;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        tomato = new int[m + 1][n + 1][h + 1];
        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 1; k <= m; k++) {
                    int tmp = Integer.parseInt(st.nextToken());
                    if (tmp == 1) {
                        tomato[k][j][i] = tmp;
                        if (tmp == 1) queue.add(new Pair(k, j, i));
                    } else {
                        tomato[k][j][i] = tmp;
                    }
                }
            }
        }
        int result = bfs(1) - 1;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                for (int k = 1; k <= h; k++) {
                    if (tomato[i][j][k] == 0) result = -1;
                }
            }
        }
        System.out.println(result);
    }

    public static int bfs(int count) {
        int size = queue.size();
        for (int v = 0; v< size; v++) {
            Pair pair = queue.poll();
            int k = pair.getX();
            int j = pair.getY();
            int i = pair.getZ();
            for (int r = 0; r < 6; r++) {
                int a = k + dm[r];
                int b = j + dn[r];
                int c = i + dh[r];
                if ((0 < a && a < m + 1) && (0 < b && b < n + 1) && (0 < c && c < h + 1)) {
                    if (tomato[a][b][c] == 0) {
                        tomato[a][b][c] = 1;
                        queue.add(new Pair(a, b, c));
                    }
                }
            }
        }
        if (!queue.isEmpty()) return bfs(count + 1);
        return count;
    }
}
