from collections import deque

def solution(board):
    answer = 0
    n=len(board)
    visit=[[1000000 for _ in range(n)] for _ in range(n)] #0이 상하, 1이 좌우
    
    q=deque()
    q.append([0,0,1,0]) 
    visit[0][0]=0
    
    dir=[[0,1],[0,-1],[1,0],[-1,0]]
    while q:
        x,y,t_value,p=q.popleft() #t는 타입 1은 상하, 2는 좌우
        for a,b in dir:
            xa=x+a
            yb=y+b
            
            if 0<=xa<n and 0<=yb<n and board[xa][yb]==0:
                if t_value==0 or (t_value==1 and b==0) or (t_value==2 and a==0) : #직선, t==0일 경우는 첫 시작으로 전부다 직선     
                    
                    if visit[xa][yb]>=p+100:
                        if t_value==0 and b==0:
                            t=1
                        elif t_value==0 and a==0:
                            t=2
                        else:
                            t=t_value
                        q.append([xa,yb,t,p+100])
                        visit[xa][yb]=p+100
                        
                elif (t_value==1 and a==0) or (t_value==2 and b==0): #코너
                    if visit[xa][yb]>=p+600:
                        if t_value==1:
                            t=2
                        else:
                            t=1
                        q.append([xa,yb,t,p+600])
                        visit[xa][yb]=p+600
    

                        
    answer=visit[-1][-1]
    #answer=min(visit[0][-1][-1],visit[1][-1][-1])
    return answer

solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]])