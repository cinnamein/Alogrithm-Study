import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[1001];
        int result = 0;
        for (int i = 0; i < 10; i++){
            int tmp = Integer.parseInt(br.readLine());
            arr[tmp % 42]++;
        }
        for (int j = 0; j < 1001; j++){
            if (arr[j] != 0) result++;
        }
        System.out.println(result);
    }
}
