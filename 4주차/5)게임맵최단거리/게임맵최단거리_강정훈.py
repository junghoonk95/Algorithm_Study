def solution(maps):
    # visit=[]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    n=len(maps[0]) # 가로nx
    m=len(maps)    # 세로ny
    visit=maps.copy()
    cnt=1

    sol=[]

    def dfs(x,y):
        nonlocal cnt, sol
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=n or ny>=m or nx<0 or ny<0 or visit[ny][nx]==0 or maps[ny][nx]==0 :
                continue
            elif ny==m-1 and nx ==n-1:
                cnt=cnt+1
                sol.append(cnt)
                
            elif maps[ny][nx]==1 and visit[ny][nx]==1:
                visit[ny][nx]=0
                cnt=cnt+1
                dfs(nx,ny) 
                

    dfs(0,0)
    if sol==[]:
        return -1
    else:
        return min(sol)
    











