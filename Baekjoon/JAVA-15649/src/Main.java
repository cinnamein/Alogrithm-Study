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
        dp(1, 0, sb);
        System.out.println(result);
    }

    public static void dp(int num, int count, StringBuilder sb) {
        System.out.println(num);
        if (count == m) {
            result.append(sb);
            result.append("\n");
            return;
        }
        for (int i = num + 1; i < n - count + 2; i++) {
            dp(i, count++, new StringBuilder(String.valueOf(sb) + i + " "));
        }
    }
}