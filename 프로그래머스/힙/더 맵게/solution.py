import heapq

def solution(scoville, K):
    mix_count = 0 
    heapq.heapify(scoville)

    while scoville:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        if scoville[0] >= K:
            return mix_count

        mixed = mix_scoville(heapq.heappop(scoville), heapq.heappop(scoville))
        heapq.heappush(scoville, mixed)
        mix_count += 1
    
    return mix_count


def mix_scoville(mildest, sec_mildest):
    return mildest + sec_mildest * 2


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([3, 9, 1, 2, 12, 10], 7))

print(solution([1,2], 7))


# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)