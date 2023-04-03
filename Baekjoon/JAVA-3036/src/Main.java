import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        double a = Double.parseDouble(st.nextToken());
        for (int i = 1; i < n; i++) {
            double b = Double.parseDouble((st.nextToken()));
            if (a == b) System.out.println("1/1");
            else System.out.println(gcd(a, b));
        }
    }

    public static String gcd(double a, double b) {
        int num = 2;
        while (true) {
            if (num > a || num > b) break;
            if (a % num == 0 && b % num == 0) {
                a = a / num;
                b = b / num;
                num = 2;
            } else {
                num++;
            }
        }
        return (int) a + "/" + (int) b;
    }
}