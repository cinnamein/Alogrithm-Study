import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= n; i++){
            dp(i);
        }
    }

    public static void dp(int num){
        StringBuilder sb = new StringBuilder();
        sb.append(num + " ");
        for (int i = num + 1; i <= n; i++){
            sb.append(i + " ");
            dp(i);
        }
        return;
    }
}
