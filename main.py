#14889
import sys

input = sys.stdin.readline


def get_max(arr):
  max_val = 0
  # arr 전체 탐색하며 max 값 리턴
  for i in range(N):
    for j in range(N):
      max_val = max(max_val, arr[i][j])
  return max_val


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def get_add(arr):
  for i in range(N):
    arr[i] = [num for num in arr[i] if num != 0]
    j = 0
    while j < len(arr[i]) - 1:
      if arr[i][j] == arr[i][j + 1]:
        arr[i][j] *= 2
        del arr[i][j + 1]
      j += 1

    while len(arr[i]) < N:
      arr[i].append(0)
  return arr


def move(arr, d):
  cp_arr = arr[:]
  res = arr[:]
  if d == 0:
    res = get_add(cp_arr)
  elif d == 1:
    for i in range(N):
      cp_arr[i] = cp_arr[i][::-1]
    res = get_add(cp_arr)
    for i in range(N):
      res[i] = res[i][::-1]
  elif d == 2:
    arr2 = list(zip(*cp_arr))
    res = list(zip(*get_add(arr2)))

  elif d == 3:
    arr2 = list(zip(*cp_arr[::-1]))
    res = list(zip(*get_add(arr2)))[::-1]
  return res


def get_val(arr, i):
  if (i == 5):
    return get_max(arr)
  res = []
  for d in range(4):
    arr2 = move(arr, d)
    # if i == 0  and d == 3:
    # print("i:", i , "d: ", d, arr2, "res", res)
    res.append(get_val(arr2, i + 1))
  return max(res)


print(get_val(arr, 0))
