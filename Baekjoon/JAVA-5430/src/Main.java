import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int flag = 0;
            Deque<Integer> deque = new LinkedList<>();
            StringBuilder sb = new StringBuilder();
            String p = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String arr = br.readLine();
            StringTokenizer st = new StringTokenizer(arr.substring(1, arr.length() - 1), ",");
            for (int k = 0; k < n; k++) {
                deque.addLast(Integer.parseInt(st.nextToken()));
            }
            boolean reverse = true;
            for (int j = 0; j < p.length(); j++) {
                if (p.charAt(j) == 'R') {
                    reverse = !reverse;
                } else {
                    if (deque.isEmpty()) {
                        System.out.println("error");
                        flag = 1;
                        break;
                    }
                    if (reverse) {
                        deque.removeFirst();
                    } else {
                        deque.removeLast();
                    }
                }
            }
            if (flag == 0 && reverse) System.out.println(String.valueOf(deque).replace(" ", ""));
            else if (flag == 0 && !reverse){
                sb.append("[");
                while (!deque.isEmpty()){
                    sb.append(deque.pollLast());
                    sb.append(",");
                }
                if (sb.length() != 1) {
                    sb.deleteCharAt(sb.length() - 1);
                }
                sb.append("]");
                System.out.println(sb);
            }
        }
    }
}