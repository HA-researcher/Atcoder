dy=[1,-1,0,0]
dx=[0,0,1,-1]
R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())

sy-=1; sx-=1; gy-=1; gx-=1

maze=[-1]*R
dist=[[-1]*C for _ in range(R)]
dist[sy][sx]=0
for i in range(R):
    maze[i]=list(input())
visited=set()
from collections import deque

queue=deque([(sy,sx)])

while queue:
    y,x=queue.popleft()
    if y==gy and x==gx:
        print(dist[y][x])
        break
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ((ny,nx) not in visited) and maze[ny][nx]==".":
            visited.add((ny,nx))
            dist[ny][nx]=dist[y][x]+1
            queue.append((ny,nx))
        
    
    
    
