import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split("");
        int b = 0, r = 0;
        String tmp = arr[0];
        for (int i = 1; i < n; i++){
            if (!arr[i].equals(arr[i - 1])) {
                if (arr[i].equals("B")) b++;
                else r++;
            }
        }
        if (b > r){
            System.out.println(1 + b);
        }else System.out.println(1 + r);
    }
}
