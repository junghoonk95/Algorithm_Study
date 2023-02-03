import sys
import pprint
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
pprint.pprint(graph)
cnt = 0

ans = 0

def bfs():
    check = [[0]*M for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque()

    for n in range(N):
        for m in range(M):
            if graph[n][m] == 2:
                # print(n, m)
                q.append((n, m))
            # print(q)

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            # print('ori : ', now_r, now_c)
            new_r, new_c = dr[i] + now_r, dc[i] + now_c
            # print('after : ', new_r, new_c)

            if (new_c < 0 or new_r > N-1) or (new_c < 0 or new_c > M-1):
                continue
            if 0 <= new_c < N-1 and 0 <= new_c < M-1:
                if check[new_r][new_c] == 0 and graph[new_r][new_c] == 0:
                    check[new_r][new_c] = 1
                    q.append((new_r, new_c))
    print(check)



def check_zone(graph):
    temp = 0
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 0:
                temp += 1
    return temp


for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            graph[n][m] = 1
            cnt += 1

            if cnt == 3:
                bfs()

                # value = check_zone(graph)
                cnt = 0
                continue

        # if value > ans:
        #     ans = value
