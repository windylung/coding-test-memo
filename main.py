N = int(input())
def divider(N) :
  if N == 1 :
    return
  elif N % 2 :
    for i in range(1, int((N-1)/2) + 1) :
      j = 2*i + 1
      while N % j == 0 :
        N = N // j
        print (j)
      
  else :
    while N % 2 == 0 :
      N = N // 2
      print(2)
    divider(N)
divider(N)