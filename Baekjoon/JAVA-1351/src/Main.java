import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static Map<Long, Long> a;
    static int result;
    static long n, p, q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());
        a = new HashMap<>();
        a.put((long) 0, (long) 1);
        a.put((long) 1, (long) 2);
        System.out.println(dp(n));
    }

    public static long dp(long num) {
        if (a.containsKey(num)) return a.get(num);
        long tmp = dp(num / p) + dp(num / q);
        a.put(num, tmp);
        return tmp;
    }
}