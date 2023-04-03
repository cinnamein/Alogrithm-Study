import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BigDecimal n = new BigDecimal(st.nextToken());
        BigDecimal m = new BigDecimal(st.nextToken());
        BigDecimal a = BigDecimal.ONE, b = BigDecimal.ONE, tmp = BigDecimal.ONE;
        for (int i = 0; i < m.intValue();i++){
            a = a.multiply(n.subtract(new BigDecimal(i)));
            b = b.multiply(tmp.add(new BigDecimal(i)));
            }
        System.out.println(a.divide(b).remainder(new BigDecimal(10007)));
    }
}
