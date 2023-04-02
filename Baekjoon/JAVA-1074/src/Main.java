import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int r, c, num;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken()) + 1;
        r = Integer.parseInt(st.nextToken()) + 1;
        if (n == 1) {
            if (c == 1 && r == 1) System.out.println(0);
            else if (r == 2 && c == 1) System.out.println(1);
            else if (r == 1 && c == 2) System.out.println(2);
            else System.out.println(3);
        }
        else {
            int tmp = (int) Math.pow(2, n);
            num = 0;
            dp(tmp);
            System.out.println(num);
        }
    }

    public static void dp(int size) {
        if (size == 1) return;
        int tmp = size * size / 4;
        if (r > size / 2 && c > size / 2) {
            num += tmp * 3;
            r = r - size / 2;
            c = c - size / 2;
        } else if (r > size / 2 && c <= size / 2) {
            num += tmp;
            r = r - size / 2;
        } else if (r <= size / 2 && c > size / 2) {
            num += tmp * 2;
            c = c - size / 2;
        }
        dp(size / 2);
    }
}