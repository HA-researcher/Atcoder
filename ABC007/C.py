from collections import deque

def BFS(Row,Col,start_y,start_x,goal_y,goal_x):
    start_y-=1; start_x-=1; goal_y-=1; goal_x-=1
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    maze=[input() for _ in range(Row)]
    queue=deque([])
    visited=set()
    visited.add((start_y,start_x))
    distance=[[-1]*Col for _ in range(Row)]; distance[start_y][start_x]=0
    queue.append([start_y,start_x])
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]; nx=x+dx[i]
            if ((ny,nx) not in visited) and (0<=ny<Row) and (0<=nx<Col) and (maze[ny][nx]=="."):
                visited.add((ny,nx))
                queue.append([ny,nx])
                distance[ny][nx]=distance[y][x]+1
                if ny ==goal_y and nx == goal_x:
                    return(distance[ny][nx])

R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
print(BFS(R,C,sy,sx,gy,gx))

"""
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
        """
