#14888
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))


def get_idx(op):
  idx = []
  for i in range(4):
    if op[i]:
      idx.append(i)
  return idx


def cal(n1, n2, op):
  if op == 0:
    return n1 + n2
  elif op == 1:
    return n1 - n2
  elif op == 2:
    return n1 * n2
  elif op == 3 and n1 < 0 and n2 > 0:
    return (-1 * n1) // n2 * -1
  else:
    return n1 // n2


def get_max_val(num, op):
  # print("get_val" , num , op)
  if max(op) == 0:
    return num[0]
  val = []
  idx = get_idx(op)
  for i in idx:
    num2 = [cal(num[0], num[1], i)]
    if len(num) > 2:
      num2.extend(num[2:])
    op2 = op[:]
    op2[i] = op2[i] - 1
    val.append(get_max_val(num2, op2))
  return (max(val))


def get_min_val(num, op):
  # print("get_val" , num , op)
  if max(op) == 0:
    return num[0]
  val = []
  idx = get_idx(op)
  for i in idx:
    num2 = [cal(num[0], num[1], i)]
    if len(num) > 2:
      num2.extend(num[2:])
    op2 = op[:]
    op2[i] = op2[i] - 1
    val.append(get_min_val(num2, op2))
  return (min(val))


print(get_max_val(num, op))
print(get_min_val(num, op))
