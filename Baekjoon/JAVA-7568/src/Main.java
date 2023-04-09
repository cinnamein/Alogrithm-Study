import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        int[][] result = new int[n][2];
        for (int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int weight = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            arr[i][0] = weight;
            arr[i][1] = height;
            result[i][0] = weight;
            result[i][1] = height;
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return 0;
            }
        });
        for (int j = 0; j < n; j++){
            int num = 1;
            for (int k = 0; k < n; k++){
                //todo
                if (arr[j][0] > result[k][0] && arr[j][1] > result[k][1]){
                    num++;
                }else if (arr[j][0] < result[k][0] && arr[j][1] < result[k][1]){
                    sb.append(num + "\n");
                    continue;
                }
            }
        }
        System.out.println(sb);
    }
}
