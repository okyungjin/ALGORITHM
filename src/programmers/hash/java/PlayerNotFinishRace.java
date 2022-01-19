// 코딩테스트 연습 > 해시 > 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576

package programmers.hash;

import java.util.Arrays;
import java.util.HashMap;

//class Solution
public class PlayerNotFinishRace {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String player: participant) hashMap.put(player, hashMap.getOrDefault(player, 0) + 1);
        for (String player: completion) hashMap.put(player, hashMap.get(player) - 1);

        for (String key: hashMap.keySet()) {
            if (hashMap.get(key) != 0) {
                answer = key;
            }
        }
        return answer;
    }
}

class PlayerNotFinishRaceTester {
    public static void main(String[] args) {
        PlayerNotFinishRace playerNotFinishRace = new PlayerNotFinishRace();
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};

        String answer = playerNotFinishRace.solution(participant, completion);
        System.out.println(answer);
    }
}
