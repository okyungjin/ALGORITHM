// 코딩테스트 연습 > 해시 > 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576

package programmers.hash;

import java.util.Arrays;

//class Solution
public class PlayerNotFinishRace {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        int i = 0;

        for (i = 0; i < completion.length; i++) {
            if (participant[i].equals(completion[i])) continue;
            return participant[i];
        }
        return participant[i];
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
