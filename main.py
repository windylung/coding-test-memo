import sys

input = sys.stdin.readline
A = int(input())
T = int(input())
X = int(input())



# T의 값을 보고 -> 중간에 끊기지 않고 온전히 도는 cycle의 개수 확인
cycle = 0 # 사이클의 개수
cnt = 0 # 번 또는 데기의 갯수
while (cnt < T) :
    cycle += 1
    cnt += cycle + 3

# 0 1 0 1 0 0 1 1

cnt -= cycle + 3
cycle -= 1

idx = 0
diff = T-cnt # 사이클 내 번 또는 데기의 개수
# print(cnt, cycle, diff)

if (diff == 1):
    idx = X + 1
elif (diff == 2):
    idx = X + 3
elif X == 0:
    idx = 2 + diff  # 앞에 기본적으로 1010 있음
else:
    idx = 2 + (cycle+2) + diff

res = cycle ** 2 + 7 * cycle + idx

# print(res)
print((res-1)%A)
