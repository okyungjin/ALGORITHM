package programmers.hash;

import java.util.HashMap;

public class Camouflage {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> hashMap = new HashMap<>();

        // 1. HashMap 생성
        for (String[] clothing: clothes) {
            hashMap.put(clothing[1], hashMap.getOrDefault(clothing[1], 0) + 1);
        }

        int answer = 1;

        // 2. 경우의 수 계산
        for (int value: hashMap.values())
            answer *= (value + 1);

        // 3. 모두 입지 않는 경우인 1을 빼준다.
        return answer - 1;
    }
}

class CamouflageTester {
    public static void main(String[] args) {
        String[][] clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
        Camouflage camouflage = new Camouflage();
        int answer = camouflage.solution(clothes);
        System.out.println(answer);
    }
}