import heapq

def solution(scoville, K):
    mix_count = 0
    while scoville:
        mildest = heapq.heappop(scoville)

        if mildest >= K:
            return mix_count

        sec_mildest = heapq.heappop(scoville)
        mixed = mix_scoville(mildest, sec_mildest)
        heapq.heappush(scoville, mixed)
        mix_count += 1
    
    return -1


def mix_scoville(mildest, sec_mildest):
    return mildest + sec_mildest * 2


print(solution([1, 2, 3, 9, 10, 12], 7))


# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)