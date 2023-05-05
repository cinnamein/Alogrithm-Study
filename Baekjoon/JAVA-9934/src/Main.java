import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
    static int n;
    static int[] arr;
    static String[] sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[(int) (Math.pow(2, n) - 1)];
        Queue<Integer> queue = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int i = 0;
        while (st.hasMoreTokens()) {
            int value = Integer.parseInt(st.nextToken());
            arr[i++] = value;
        }
        sb = new String[n];
        for (int j = 0; j < n; j++) sb[j] = "";
        order(0, arr.length - 1, 0);
        for (int k = 0; k < n; k++){
            System.out.println(sb[k]);
        }
    }

    static void order(int num, int length, int count) {
        if (count == n) return;
        int tmp = (num + length) / 2;
        sb[count] += arr[tmp] + " ";
        order(num, tmp - 1, count + 1);
        order(tmp + 1, length, count + 1);
    }
}
