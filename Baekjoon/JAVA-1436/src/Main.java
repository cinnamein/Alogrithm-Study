import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int num = 665;
        int count = 0;
        while (count < n) {
            num++;
            String numStr = String.valueOf(num);
            if (numStr.contains("666")) {
                count++;
            }
        }
        System.out.println(num);
    }
}