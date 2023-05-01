import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static class Node {
        char mid;
        Node left;
        Node right;

        Node(char mid, Node left, Node right) {
            this.mid = mid;
            this.left = left;
            this.right = right;
        }
    }
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
        sb.append("\n");
        inorder(root);
        sb.append("\n");
        postorder(root);
        System.out.println(sb);
    }

    public static void insertNode(char mid, char left, char right, Node root) {
        if (root.mid == mid) {
            root.left = (left == '.' ? null : new Node(left, null, null));
            root.right = (right == '.' ? null : new Node(right, null, null));
        } else {
            if (root.left != null) insertNode(mid, left, right, root.left);
            if (root.right != null) insertNode(mid, left, right, root.right);
        }
    }

    public static void preorder(Node root) {
        if (root == null) return;
        sb.append(root.mid);
        preorder(root.left);
        preorder(root.right);
    }

    public static void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        sb.append(root.mid);
        inorder(root.right);
    }

    public static void postorder(Node root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        sb.append(root.mid);
    }
}