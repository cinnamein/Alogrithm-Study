import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        n = 1000 - n;
        int result = 0;
        while(n != 0){
            if (n / 500 > 0){
                result += n / 500;
                n = n % 500;
            }else if (n / 100 > 0){
                result += n / 100;
                n = n % 100;
            }else if (n / 50 > 0){
                result += n / 50;
                n = n % 50;
            }else if (n / 10 > 0){
                result += n / 10;
                n = n % 10;
            }else if (n / 5 > 0){
                result += n / 5;
                n = n % 5;
            }
            else {
                result += n;
                n = 0;
            }
        }
        System.out.println(result);
    }
}