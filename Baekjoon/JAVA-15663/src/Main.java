import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static String[] arr;
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        arr = br.readLine().split(" ");
        Arrays.sort(arr);
        sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            // 시작 지점 지정
            for (int k = 0; k < m; k++) {
                //갯수 카운트
                bt(i, k);
            }
        }
        System.out.println(sb);
    }

    public static void bt(int i, int k) {
        sb.append(arr[])
    }
}
