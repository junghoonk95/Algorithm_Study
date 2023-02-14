from collections import deque
n,m=map(int,input().split())
indegree=[0]*(n+1)
number=[[]for _ in range(n+1)]


for i in range(m):
    a,b=map(int,input().split())
    number[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    dq=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            dq.append(i)

    while dq:
        now=dq.popleft()
        result.append(now)
        for g in number[now]:
            indegree[g]-=1
            if indegree[g]==0:
                dq.append(g)

    for res in result:
        print(res, end=' ')

topology_sort()
