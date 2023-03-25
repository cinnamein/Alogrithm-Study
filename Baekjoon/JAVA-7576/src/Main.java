import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int a, b;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static int[][] tomato;
    static Queue<Pair> queue = new LinkedList<>();
    static class Pair {
        int x, y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int getKey() {
            return x;
        }

        int getValue() {
            return y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        tomato = new int[a + 2][b + 2];
        for (int y = 1; y <= b; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 1; x <= a; x++) {
                String tmp = st.nextToken();
                if (tmp.equals("1")) {
                    queue.add(new Pair(x, y));
                    tomato[x][y] = 1;
                }
                else if (tmp.equals("-1")) {
                    tomato[x][y] = -1;
                }
                else {
                    tomato[x][y] = 0;
                }
            }
        }
        int result = bfs(1) - 1;
        Loop1:
        for (int y = 1; y <= b; y++) {
            for (int x = 1; x <= a; x++) {
                if (tomato[x][y] == 0) {
                    result = -1;
                    break Loop1;
                }
            }
        }
        System.out.println(result);

    }

    public static int bfs(int n) {
        int size = queue.size();
        for (int i = 0; i < size; i++){
            Pair pair = queue.poll();
            int x = pair.getKey();
            int y = pair.getValue();
            for (int j = 0; j < 4; j++) {
                int tmpX = x + dx[j];
                int tmpY = y + dy[j];
                if (tmpX < 1 || tmpX > a || tmpY < 1 || tmpY > b) continue;
                if (tomato[tmpX][tmpY] == 0) {
                    tomato[tmpX][tmpY] = 1;
                    queue.add(new Pair(tmpX, tmpY));
                }
            }
        }
        if (!queue.isEmpty()) return bfs(n + 1);
        return n;
    }
}