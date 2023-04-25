import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] distance = new int[n - 1];
        long[] city = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n - 1; i++){
            distance[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < n; j++){
            city[j] = Long.parseLong(st.nextToken());
        }
        long tmp = city[0];
        long result = 0;
        for (int k = 0; k < n - 1; k++){
            tmp = Math.min(city[k], tmp);
            result += tmp * distance[k];
        }
        System.out.println(result);
    }
}