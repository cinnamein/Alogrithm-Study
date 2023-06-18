import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (test-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int result = 0;
            HashMap<Integer, ArrayList<Integer>> city = new HashMap<>();
            while (m-- > 0) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (city.containsKey(a)) {
                    if (!city.get(a).contains(b)) {
                        ArrayList<Integer> tmp = city.get(a);
                        tmp.add(b);
                        city.put(a, tmp);
                        result++;
                    }
                } else if (city.containsKey(b)) {
                    if (!city.get(b).contains(a)) {
                        ArrayList<Integer> tmp = city.get(b);
                        tmp.add(a);
                        city.put(b, tmp);
                        result++;
                    }
                } else {
                    ArrayList<Integer> tmp = new ArrayList<>();
                    tmp.add(b);
                    city.put(a, tmp);
                    tmp.clear();
                    tmp.add(a);
                    result++;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}
