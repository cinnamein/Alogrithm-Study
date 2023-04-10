import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        boolean flag = true;
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split("");
            set.add(str[0]);
            for (int j = 1; j < str.length; j++){
                if (!str[j].equals(str[j - 1])){
                    if (set.contains(str[j])) {
                        flag = false;
                        break;
                    }
                    set.add(str[j]);
                }
            }
            if (flag) count++;
            flag = true;
            set.clear();
        }
        System.out.println(count);
    }
}
