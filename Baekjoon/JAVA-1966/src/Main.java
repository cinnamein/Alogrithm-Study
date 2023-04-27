import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
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
            System.out.println(queue.poll());
            int result = 0;
            int num = map.get(m);
            while (true) {
                int tmp = queue.poll();
                if (num < tmp) queue.add(tmp);
                else if (num == tmp) break;
                result++;
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}