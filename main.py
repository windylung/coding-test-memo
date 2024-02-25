N, M = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def move(i, j, d):
  if d == 0:
    i, j = i - 1, j
  elif d == 3:
    i, j = i, j - 1
  elif d == 2:
    i, j = i + 1, j
  elif d == 1:
    i, j = i, j + 1
  return i, j


def check_around(i, j, d):
  #direction 한 바퀴 돌려야 함.
  direction = [0, 3, 2, 1]
  init_idx = direction.index(d)
  idx = (init_idx + 1) % 4
  while (init_idx != idx):
    di, dj = move(i, j, direction[idx])  # 방향대로 이동한 좌표를 받음
    if arr[di][dj] == 0:  # 이동 가능한 경우 -> 리턴
      i, j = di, dj
      return direction[idx]
    idx = (idx + 1) % 4

  di, dj = move(i, j, direction[idx])  # 방향대로 이동한 좌표를 받음
  if arr[di][dj] == 0:  # 이동 가능한 경우 -> 리턴
    i, j = di, dj
    return direction[idx]
  return -1


def clean(i, j, d):
  res = 0
  while (1):
    if arr[i][j] == 0:
      arr[i][j] = 2  # 청소 완료한 경우
      res += 1
    check_d = check_around(i, j, d)
    if check_d != -1:  # 빈칸이 있는 경우 -> 해당 방향으로 전진
      d = check_d
      i, j = move(i, j, d)
    else:  #빈칸이 없는 경우
      di, dj = move(i, j, (d + 2) % 4)
      if arr[di][dj] != 1:  #후진할 수 있는 경우
        i, j, = di, dj
      else:
        print(res)
        return


clean(i, j, d)
