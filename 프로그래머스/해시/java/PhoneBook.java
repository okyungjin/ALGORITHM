// 코딩테스트 연습 > 해시 > 전화번호 목록
// https://programmers.co.kr/learn/courses/30/lessons/42577

package programmers.hash;

import java.util.HashMap;

public class PhoneBook {
    public static void main(String[] args) {
        String[] phoneBook = {"119", "97674223", "1195524421"};

        Solution solution = new Solution();
        boolean answer = solution.solution(phoneBook);
        System.out.println(answer);
    }
}

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < phone_book.length; i++) {
            hashMap.put(phone_book[i], i);
        }

        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < phone_book[i].length(); j++) {
                if (hashMap.containsKey(phone_book[i].substring(0, j)))
                    return false;
            }
        }
        return true;
    }
}