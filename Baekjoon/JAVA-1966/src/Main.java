import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Pair {
    Integer x;
    Integer y;

    public Pair(Integer x, Integer y) {
        this.x = x;
        this.y = y;
    }

    public Integer getX() {
        return x;
    }

    public Integer getY() {
        return y;
    }

    public void setX(Integer x) {
        this.x = x;
    }

    public void setY(Integer y) {
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < test; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
            Queue<Pair> queue = new LinkedList<>();
            for (int j = 0; j < n; j++) {
                int tmp = Integer.parseInt(st.nextToken());
                priorityQueue.add(tmp);
                queue.add(new Pair(j, tmp));
            }
            int result = 1;
            int tmp = priorityQueue.poll();
            while (true) {
                Pair pair = queue.poll();
                if (tmp == pair.getY()) {
                    result++;
                    tmp = priorityQueue.poll();
                } else if (tmp > pair.getY()) queue.add(pair);
                else if (tmp == pair.getY() && m != pair.getX()) queue.add(pair);
                else if (tmp == pair.getY() && m == pair.getX()) break;
                System.out.println("반복");
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}