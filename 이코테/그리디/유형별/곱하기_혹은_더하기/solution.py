#-*-coding:utf-8-*-

# 난이도 1
# 풀이 시간 30분
# 시간 제한 1초

testcase1 = '02984'
testcase2 = '567'

nums = []
for char in testcase2:
    nums.append(int(char))

def cal(res, index):
    global max_res
    if index == len(nums):
        if res > max_res:
            max_res = res
        return
    
    cal(res + nums[index], index + 1)
    cal(res * nums[index], index + 1)

max_res = -1
cal(0, 0)
print(max_res)