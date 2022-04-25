package programmers.sorting;

import java.util.ArrayList;
import java.util.Arrays;

public class KthNumber {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> list = new ArrayList<>();

        int i, j, k;

        for (int[] command : commands) {
            i = command[0];
            j = command[1];
            k = command[2];

            int[] subArr = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(subArr);
            list.add(subArr[k - 1]);
        }

        int[] answer = new int[list.size()];
        for (int l = 0; l < list.size(); l++) {
            answer[l] = list.get(l);
        }

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