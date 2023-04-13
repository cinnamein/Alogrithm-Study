import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<String> stack = new Stack<>();
        String result = "yes";
        while (true) {
            String[] arr = br.readLine().split("");
            if (arr[0].equals(".")) break;
            try {
                for (String s : arr) {
                    if (s.equals(".")) break;
                    switch (s) {
                        case "(":
                        case "[":
                            stack.add(s);
                            break;
                        case ")":
                            if (stack.peek().equals("(")) stack.pop();
                            else result = "no";
                            break;
                        case "]":
                            if (stack.peek().equals("[")) stack.pop();
                            else result = "no";
                            break;
                    }
                }
            } catch (Exception e) {
                result = "no";
            }
            if (!stack.isEmpty()) result = "no";
            System.out.println(result);
            result = "yes";
            stack.clear();
        }
    }
}
