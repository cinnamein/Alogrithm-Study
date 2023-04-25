import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < test; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            HashMap<Integer, Integer> map = new HashMap<>();
            PriorityQueue<Integer> queue = new PriorityQueue<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                map.put(j, tmp);
                queue.add(tmp);
            }
            int result = n;
            m = map.get(m);
            while (true) {
                if (m == queue.poll()) {
                    break;
                } else {
                    result++;
                }
            }
            sb.append(result);
        }
        System.out.println(sb);
    }
}