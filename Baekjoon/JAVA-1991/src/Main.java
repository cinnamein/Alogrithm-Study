import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static Node root = new Node('A', null, null);
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char mid = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);
            insertNode(mid, left, right, root);
        }
        preorder(root);
        inorder(root);
        postorder(root);
        System.out.println(sb);
    }

    public static void insertNode(char mid, char left, char right, Node root) {
//        Node node = new Node(mid, left, right, root);
        if (root.mid == mid) {
            root.left = ()
        }
    }

    public static void preorder(Node root) {
    }

    public static void inorder(Node root) {
    }

    public static void postorder(Node root) {
    }
}