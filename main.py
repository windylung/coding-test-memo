import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# 출발지에서 지나온 칸 개수
dist = [[-1] * M for _ in range(N)]
q = deque()
q.append((0, 0))
dist[0][0] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while (q):
  i, j = q.popleft()
  d = dist[i][j]

  for n in range(4):
    di = i + dr[n]
    dj = j + dc[n]
    if (di < N and di >= 0 and dj < M and dj >= 0):
      # print("di dj", di, dj, data[di][dj], dist[di][dj])
      if (data[di][dj] == 1 and dist[di][dj] == -1):
        q.append((di, dj))
        dist[di][dj] = d + 1
        if (di == N - 1 and dj == M - 1):
          print(d + 1)
          break
