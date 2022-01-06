package programmers.sorting;

import java.util.Arrays;

public class KthNumber {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {1,2,3};
        return answer;
    }
}

class KthNumberTester {
    public static void main(String[] args) {
        int[] array = {1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        KthNumber kthNumber = new KthNumber();
        int[] answer = kthNumber.solution(array, commands);

        System.out.println(Arrays.toString(answer));
    }
}