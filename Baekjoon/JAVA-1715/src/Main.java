import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Integer.parseInt(br.readLine());
        PriorityQueue<Long> queue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            queue.add(Long.parseLong(br.readLine()));
        }
        if (n == 1){
            System.out.println(0);
        }else {
            long sum = 0;
            while (true) {
                long tmp = queue.poll() + queue.poll();
                sum += tmp;
                queue.add(tmp);
                if (queue.size() == 1) break;
            }
            System.out.println(sum);
        }
    }
}