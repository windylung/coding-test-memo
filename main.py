#1504
import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
q = []
# 노드 별 간선, 가중치 리스트
data = list([] for _ in range(V + 1))
# 각 노드까지 거리 리스트

for i in range(E):
    u, v, w = map(int, input().split())
    data[u].append((w, v))
    data[v].append((w, u))
V1, V2 = map(int, input().split())

def dij(start, end):
    dist = list(float('inf') for _ in range(V + 1))
    if start == end :
        return 0
    heapq.heappush(q, (0, start))
    while q:
        cur_dist, cur = heapq.heappop(q)
        if cur_dist > dist[cur]:
            continue

        dist[cur] = cur_dist
        for l_dist, l_node in data[cur]:
            cmp = cur_dist + l_dist
            if dist[l_node] < 0 or cmp < dist[l_node]:
                dist[l_node] = cmp
                heapq.heappush(q, (cmp, l_node))
    return dist[end]

cal_list_1 = [(1, V1), (V1, V2), (V2, V)]
cal_list_2 = [(1, V2), (V2, V1), (V1, V)]

def cal(cal_list):
    res = 0
    for c1, c2 in cal_list:
        c = dij(c1, c2)
        if c == float('inf'):
            return -1
        res += c

    return res
res1 = cal(cal_list_1)
res2 = cal(cal_list_2)
if (res1 == -1 and res2 == -1):
    print(-1)
else :
    print(min(res1, res2))

