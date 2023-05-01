import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] arr;
    static StringBuilder result = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        boolean[] check = new boolean[n];
        st = new StringTokenizer(br.readLine());
        for (int k = 0; k < n; k++) {
            arr[k] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        for (int i = 1; i <= n; i++) {
            dp(i, 1, arr[i - 1] + " ", check);
        }
        System.out.println(result);
    }

    public static void dp(int num, int count, String str, boolean[] check) {
        if (count == m) {
            result.append(str);
            result.append("\n");
            return;
        }
        check[num - 1] = true;
        count++;
        for (int i = 1; i <= n; i++) {
            if (!check[i - 1])
                dp(i, count, str + arr[i - 1] + " ", check);
        }
        check[num - 1] = false;
    }
}