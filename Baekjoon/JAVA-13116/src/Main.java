import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            LinkedList<Integer> listA = new LinkedList<>();
            LinkedList<Integer> listB = new LinkedList<>();
            while (a != 1) {
                listA.add(a);
                a /= 2;
            }
            listA.add(1);
            while (b != 1) {
                listB.add(b);
                b /= 2;
            }
            listB.add(1);
            Loop:
            for (int k = 0; k < listA.size(); k++) {
                for (int i = 0; i <listB.size(); i++) {
                    if (listA.get(k).equals(listB.get(i))) {
                        System.out.println(listA.get(k) + "0");
                        break Loop;
                    }
                }
            }
        }
    }
}
