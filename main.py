#13458
import sys
import math

input = sys.stdin.readline

n = int(input())
student =list(map(int, input().split()))
c1, c2 = map(int, input().split())
res = 0

for s in student :
  c = math.ceil((s - c1) / c2)
  res += c if c >= 0 else 0

print(res + n)
