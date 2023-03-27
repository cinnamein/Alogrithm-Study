import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static boolean[][] arr;
    static boolean[] visit;
    static Queue<Integer> queue = new LinkedList<Integer>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        arr = new boolean[n + 1][n + 1];
        visit = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = true;
        }
        sb.append(v + " ");
        dfs(v);
        sb.append("\n");
        for (int i = 1; i <= n; i++) {
            visit[i] = false;
        }
        sb.append(v + " ");
        bfs(v);
        System.out.println(sb);
    }

    public static void dfs(int v) {
        visit[v] = true;
        for (int i = 1; i <= n; i++) {
            if (arr[v][i] && !visit[i]) {
                visit[i] = true;
                sb.append(i + " ");
                dfs(i);
            }
        }
    }

    public static void bfs(int v) {
        visit[v] = true;
        for (int i = 1; i <= n; i++) {
            if (arr[v][i] && !visit[i]) {
                visit[i] = true;
                queue.add(i);
                sb.append(i + " ");
            }
        }
        while (!queue.isEmpty()) {
            bfs(queue.poll());
        }
    }
}