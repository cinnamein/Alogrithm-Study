import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] arr = new int[9];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            int tmp = Integer.parseInt(br.readLine());
            arr[i] = tmp;
            sum += tmp;
        }
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        Set<Integer> outputSet = new HashSet<>();
        while (flag) {
            for (int j = 0; j < 8; j++) {
                for (int k = j + 1; k < 9; k++) {
                    if (sum - arr[j] - arr[k] == 100) {
                        for (int r = 0; r < 9; r++) {
                            if (r != k && r != j) {
                                int num = arr[r];
                                if (!outputSet.contains(num)) {
                                    sb.append(num).append("\n");
                                    outputSet.add(num);
                                }
                            }
                        }
                        flag = false;
                        break; // exit the inner loop
                    }
                }
                if (!flag) {
                    break; // exit the outer loop
                }
            }
        }
        System.out.println(sb);
    }
}