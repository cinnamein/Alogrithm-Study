import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(br.readLine());
        int left = 1;
        int right = m;
        int result = 0;
        for (int i = 0; i < j; i++){
            int apple = Integer.parseInt(br.readLine());
            if (apple < left){
                result += left - apple;
                left = apple;
                right = apple + m - 1;
            }else if (right < apple){
                result += apple - right;
                right = apple;
                left = apple - m + 1;
            }
        }
        System.out.println(result);
    }
}