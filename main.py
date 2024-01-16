#14499
import sys

input = sys.stdin.readline

N, M, i, j, d = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]


def east(d):
  return [d[5], d[1], d[4], d[3], d[0], d[2]]


def west(d):
  return [d[4], d[1], d[5], d[3], d[2], d[0]]


def north(d):
  return [d[3]] + d[:3] + d[4:]


def south(d):
  result = d[1:]
  result.insert(3, d[0])
  return result


for n in arr:
  ic, jc = i, j

  if n == 1:
    if j + 1 < M:
      j += 1
      dice = east(dice)

  elif n == 2:
    if j - 1 >= 0:
      j -= 1
      dice = west(dice)

  elif n == 3:
    if i - 1 >= 0:
      i -= 1
      dice = north(dice)

  elif i + 1 < N:
    i += 1
    dice = south(dice)

  if ic != i or jc != j:
    if S[i][j] == 0 :
      S[i][j] = dice[0]
    else :
      dice[0] = S[i][j]
      S[i][j] = 0
    print(dice[2])
