import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        if (n == 1 || n == 3) System.out.println(-1);
        else {
            while (n != 0) {
                if (n % 5 == 0) {
                    result += n / 5;
                    n = 0;
                } else {
                    n -= 2;
                    result++;
                }
            }
            System.out.println(result);
        }
    }
}
