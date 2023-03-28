import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int len = Integer.valueOf(st.nextToken());
        int d = Integer.valueOf(st.nextToken());

        ArrayList<Integer> result = new ArrayList<Integer>();

        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i = 0; i < len; i++) arr.add(i + 1);

        int num = d - 1;

        while(arr.size() != 1) {
            result.add(arr.get(num));
            if (arr.size() > num + d) {
                arr.remove(num);
                num = num + d - 1;
            }else {
                arr.remove(num);
                num = (num + d - 1) % arr.size();
            }
        }

        result.add(arr.get(0));

        System.out.print("<");
        for(int i = 0; i < len; i++){
            System.out.print(result.get(i));
            if(i < len - 1) System.out.print(", ");
        }
        System.out.print(">");
    }
}