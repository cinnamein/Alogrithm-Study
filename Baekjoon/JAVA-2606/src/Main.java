import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] arr;
    static boolean[] visit;
    static int num, count, result;
    static void dfs(int n) {
        result++;
        visit[n] = true;
        for(int i = 1; i <= num; i++){
            if (!visit[i] && arr[n][i]) dfs(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        num = Integer.parseInt(br.readLine());
        count = Integer.parseInt(br.readLine());
        arr = new boolean[num + 1][num + 1];
        visit = new boolean[num + 1];
        for (int i = 0; i < count; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = true;
        }
        dfs(1);
        System.out.println(result - 1);
    }
}