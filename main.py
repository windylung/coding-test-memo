#14501
import sys

input = sys.stdin.readline

N = int(input())
T = []
P = []
for i in range(N) :
  t, p = map(int, input().split())
  # 상담이 불가능한 경우
  # 등호 / -1 제거 가능성 따져보기
  if i + t -1 >= N :
    T.append(1)
    P.append(0)
  else : 
    T.append(t)
    P.append(p)

def get_max(i):
  if i >= N :
    return 0
  elif T[i] == 1 :
    return P[i] + get_max(i + 1)
  else :
    p1 = P[i] + get_max(i + T[i])
    p2 = get_max(i + 1)
    return max(p1, p2)
print(get_max(0))