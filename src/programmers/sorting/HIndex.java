package programmers.sorting;

import java.util.Arrays;

public class HIndex {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int hIndex = (citations.length - 1) / 2;
        return citations[hIndex];
    }
}

class HIndexTest {
    public static void main(String[] args) {
        int[] citations = {3, 0, 6, 1, 5};
        HIndex hIndex = new HIndex();
        int answer = hIndex.solution(citations);
        System.out.println(answer);
    }
}
