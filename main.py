import sys
from collections import deque

n = int(sys.stdin.readline())
# 일단 한 줄 읽음
input = [list(sys.stdin.readline()) for _ in range(n)]

for i in range(n) :
  arr = input[i]
  q = deque()
  for m in arr : 
    if m == '(' :
      q.append(m)
    elif m == ')' :
      if len(q) == 0 :
        q.append(m)
      else :
        tmp = q.pop()
        if tmp != '(' :
          q.append(tmp)
          q.append(m)
        
  if len(q) != 0 :
    print("NO", end = "")
  else :
    print("YES", end = "")

  if i != n - 1 :
    print()
    