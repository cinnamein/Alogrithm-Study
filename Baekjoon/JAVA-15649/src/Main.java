import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static StringBuilder result = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        boolean[] arr = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            dp(i, 1, i + " ", arr);
        }
        System.out.println(result);
    }

    public static void dp(int num, int count, String str, boolean[] arr) {
        if (count == m) {
            result.append(str);
            result.append("\n");
            return;
        }
        arr[num] = true;
        count++;
        for (int i = 1; i <= n; i++) {
            if (!arr[i]) {
                arr[i] = true;
                dp(i, count, str + i + " ", arr);
            }        }
    }
}