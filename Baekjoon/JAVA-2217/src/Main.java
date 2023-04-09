import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n == 1) {
            System.out.println(br.readLine());
        } else {
            Integer[] arr = new Integer[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(arr);
            int maxWeight = 0;
            for (int i = 0; i < n; i++) {
                int weight = arr[i] * (n - i);
                maxWeight = Math.max(maxWeight, weight);
            }
            System.out.println(maxWeight);
        }
    }
}