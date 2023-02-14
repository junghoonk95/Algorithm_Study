N=int(input())
M=int(input())
arr=[]
com_arr=[i for i in range(N+1)]
for i in range(M):
    a,b,c= map(int,input().split())
    arr.append((a,b,c))
arr.sort(reverse=True,key=lambda x:(x[2]))
def lookup(x):
    if x !=com_arr[x]:
        com_arr[x]=lookup(com_arr[x])
    return com_arr[x]

def union(x,y):
    x,y =lookup(x),lookup(y)
    if x<y:
        com_arr[y]=x
    else:
        com_arr[x]=y

cnt=0
r=0
while cnt != N - 1:
    a,b,w = arr.pop()
    if lookup(a) == lookup(b):
        continue
    union(a, b)
    r += w
    cnt += 1

print(r)
