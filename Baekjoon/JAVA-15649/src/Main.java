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
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < n - m + 2; i++)
            dp(i, 0, sb);
        System.out.println(result);
    }

    public static void dp(int num, int count, StringBuilder sb) {
        count++;
        if (count == m) {
            result.append(sb + "\n");
            return;
        }
        for (int i = num + 1; i <= n; i++) {
            dp(i, count, new StringBuilder(sb + num + " "));
        }
    }
}