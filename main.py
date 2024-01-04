#1789
def sum(S) :
  num = 0
  N = 1
  while num < S :
    num += N
    N += 1
  if num == S :
    print(N-1)
  else :
    print(N-2)
    
S = int(input())
sum(S)