#14500
import sys

input = sys.stdin.readline

N, M =  map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
res = 0

def get_val(i, j, n, sum) :
  if (n==4) :
    return sum + S[i][j]

  sum += S[i][j] 
  if i+1 >= N and j+1 >= M :
    return -9999
  elif i+1 >= N :
    return get_val(i, j+1, n+1, sum)
  elif j+1 >= M :
    return get_val(i+1, j, n+1, sum)
  else :
    square = get_val(i+1, j+1, n+2, sum + S[i+1][j] + S[i][j])
    return max(get_val(i+1, j, n+1, sum), get_val(i, j+1, n+1, sum), square)

for i in range(N) :
  for j in range(M) :
    val = get_val(i, j, 1, 0)
    res = max(res, val)
print(res)