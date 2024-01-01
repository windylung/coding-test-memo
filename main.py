N = int(input())
def divider(N) :
  if N == 1 :
    return

  for i in range(2, N+1) :
    while N % i == 0 :
      N = N // i
      print(i)
divider(N)