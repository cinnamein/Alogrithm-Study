import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node {
    int num;
    Node left;
    Node right;

    public Node(int num, Node left, Node right) {
        this.num = num;
        this.left = left;
        this.right = right;
    }
}

public class Main {
    static int n;
    static int[] arr;
    static String[] sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[(int) (Math.pow(2, n) - 1)];
        Queue<Integer> queue = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) queue.add(Integer.parseInt(st.nextToken()));
        sb = new String[n];
        for (int j = 0; j < n; j++) sb[j] = new String();
        order(0, arr.length - 1, 0);
        for (int k = 0; k < n; k++){
            System.out.println(sb);
        }
    }

    static void order(int num, int length, int count) {
        if (count == n) return;
        int tmp = (num + length) / 2;
        sb[count] += arr[tmp] + " ";
        order(num, tmp - 1, count + 1);
        order(tmp + 1, length, count + 1);
    }
}
