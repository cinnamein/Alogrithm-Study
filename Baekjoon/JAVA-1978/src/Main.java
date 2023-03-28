import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(bf.readLine());
        String[] tmp = bf.readLine().split(" ");
        int[] arr = 
        int result = 0;

        for (int i = 0; i < test; i++) {
            for (int k = 2; k < arr[i]; k++) {
                if (arr[i] % k == 0) result++;
            }
        }

        System.out.println(result);
    }
}