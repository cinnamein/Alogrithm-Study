import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int j = 1; j <= n; j++) map.put(j, new ArrayList<>(null));
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            map.put(x, new ArrayList<>(map.get(x).add(y)));
            map.put(y, map.get(y));
        }
        StringBuilder sb = new StringBuilder();
        System.out.println(sb);
    }
}
