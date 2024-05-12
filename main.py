#1543
import sys

source = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

idx = 0
res = 0
slen = len(source)
plen = len(pattern)
while idx < slen :
    if source[idx] == pattern[0] and source[idx : idx + plen] == pattern:
        res += 1
        idx = idx + plen
    else :
        idx += 1

print(res)