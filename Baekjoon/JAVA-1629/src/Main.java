import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Long a = Long.parseLong(st.nextToken());
        Long b = Long.parseLong(st.nextToken());
        Long c = Long.parseLong(st.nextToken());
        System.out.print(cal(a, b, c));
    }

    public static Long cal(Long a, Long b, Long c) {
        if (b == 1L) return (Long) (a % c);
        Long tmp = cal(a, b / 2, c);
        if (b % 2 == 0L) {
            return tmp % c * tmp % c;
        } else {
            return tmp % c * tmp % c * a % c;
        }
    }
}