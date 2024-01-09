#14889
import sys

input = sys.stdin.readline

def get_sum(arr) :
  sum = 0
  for i in arr :
    for j in arr :
      sum += S[i][j]
  return sum 


def get_val(arr, val):
  if len(arr) == N / 2:
    other = list(set(range(N)) - set(arr))
    
    return (abs(get_sum(other) - val))
  res = []
  for i in range(arr[-1] + 1, int(N/2) + len(arr) + 1) :
    val2 = val
    for j in arr :
      val2 = val2 + S[i][j] + S[j][i]
    arr2 = arr + [i]
    res.append(get_val(arr2, val2))
  return min(res)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
arr = [0]
print(get_val(arr, 0))