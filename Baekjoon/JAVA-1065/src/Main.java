import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        if (n < 10) System.out.println(n);
        else {
            for (int i = 10; i <= n; i++) {
                String[] str = String.valueOf(i).split("");
                int tmp = Integer.parseInt(str[1]) - Integer.parseInt(str[0]);
                for (int j = 2; j < str.length; j++) {
                    if (Integer.parseInt(str[j]) - Integer.parseInt(str[j - 1]) != tmp) {
                        count++;
                        break;
                    }
                }
            }
            count = n - count;
            System.out.println(count);
        }
    }
}