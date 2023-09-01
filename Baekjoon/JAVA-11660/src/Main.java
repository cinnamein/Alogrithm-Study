import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n + 1][n + 1];
        for(int i = 0; i < n + 1; i++){
            arr[0][i] = 0;
            arr[i][0] = 0;
        }
        for(int r = 1; r < n + 1; r++){
            st = new StringTokenizer(br.readLine());
            for(int rr = 1; rr < n + 1; rr++){
                arr[r][rr] = Integer.parseInt(st.nextToken());
            }
        }
        for(int x = 1; x < n + 1; x++){
            for(int y = 1; y < n + 1; y++){
                arr[x][y] += arr[x - 1][y] + arr[x][y - 1] - arr[x - 1][y - 1];
            }
        }
        for(int k = 0; k < m; k++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            System.out.println(arr[c][d] + arr[a - 1][b - 1] - arr[c][b - 1] - arr[a - 1][d]);
        }
    }
}