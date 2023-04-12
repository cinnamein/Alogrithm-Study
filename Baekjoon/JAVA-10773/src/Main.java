import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++){
            int tmp = Integer.parseInt(br.readLine());
            if (tmp == 0) stack.pop();
            else stack.push(tmp);
        }
        int size = stack.size();
        int sum = 0;
        for (int j = 0; j < size; j++){
            sum += stack.pop();
        }
        System.out.println(sum);
    }
}
