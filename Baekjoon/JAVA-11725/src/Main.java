import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        map.put(1, null);
        for (int i = 1; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (map.containsKey(x)) {
                map.put(y, x);
            }else{
                map.put(x, y);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int j = 2; j <= n; j++) sb.append(map.get(j)).append("\n");
        System.out.println(sb);
    }
}
