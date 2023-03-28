import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int test = Integer.valueOf(bf.readLine()); //테스트 케이스 입력
        ArrayList<Integer> tmp = new ArrayList<Integer>(); //리스트 생성, int 타입만 사용 가능
        for (int i = 0; i < test; i++) tmp.add(Integer.valueOf(bf.readLine())); //숫자 입력
        Collections.sort(tmp); //정렬
        for(int k = 0; k< test; k++) sb.append(tmp.get(k)).append("\n"); //sout에 비해 StringBuilder가 성능이 좋음
        System.out.println(sb);; //결과 출력
    }
}