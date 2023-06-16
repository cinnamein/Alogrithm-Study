import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static class Node {
        Integer mid;
        Node left;
        Node right;

        Node(Integer mid, Node left, Node right) {
            this.mid = mid;
            this.left = left;
            this.right = right;
        }
    }

    static Node root = new Node(1, null, null);
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        while (test-- > 0) {
            
        }
    }
}
