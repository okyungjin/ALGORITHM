// 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 여행경로
// https://programmers.co.kr/learn/courses/30/lessons/43164

package programmers.dfs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// class Solution
public class TravelRoute {
    static boolean[] isTicketsUsed;
    static List<String> list = new ArrayList<String>();
    static String[] answer = {};
    static int count = 0;

    public String[] solution(String[][] tickets) {
        isTicketsUsed = new boolean[tickets.length];

        // 1. 티켓을 정렬한다.
        sortTickets(tickets);

        // 2. 첫 출발지인 ICN 공항을 추가한다.
        list.add("ICN");

        // 3. DFS를 수행한다.
        dfs(count, "ICN", tickets);

        return answer;
    }

    public static void sortTickets(String[][] tickets) {
        Arrays.sort(tickets, (o1, o2) -> {
            if (o1[0].equals(o2[0])) {
                return o1[1].compareTo(o2[1]);
            } else {
                return o1[0].compareTo(o2[0]);
            }
        });
    }

    public static void dfs(int count, String start, String[][] tickets) {
        // 더 빠른 경로가 존재할 때
        if (answer.length > 0)
            return;

        // 모든 티켓 사용 완료
        if (count == isTicketsUsed.length) {
            answer = new String[list.size()];
            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }
            return;
        }

        for (int i = 0; i < tickets.length; i++) {
            if (!isTicketsUsed[i] && tickets[i][0].equals(start)) {
                // 티켓을 사용 처리한다.
                isTicketsUsed[i] = true;

                String destination = tickets[i][1];
                list.add(destination);

                // [destination]이 출발지가 된다.
                dfs(count + 1, destination, tickets);

                // for Back Tracking
                isTicketsUsed[i] = false;

                // [list]의 i번 째 [destination]을 제거한다.
                list.remove(list.size() - 1);
            }
        }
    }
}


class TravelRouteTester {
    public static void main(String[] args) {
        final String[][] tickets = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}};
        TravelRoute travelRoute = new TravelRoute();
        final String[] answer = travelRoute.solution(tickets);
        System.out.println(Arrays.toString(answer));
    }
}