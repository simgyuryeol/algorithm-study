import sys
input = lambda : sys.stdin.readline().rstrip()

N=list(map(int,input().split())) #N[0]가 세로 N[1] 가로


m=[[]*N[1] for i in range(N[0])]
index=[]
for i in range(N[0]):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==2:
            index.append(j)
            index.append(i)
        m[i].append(a[j])

q=[]
q.append(index[0]) #가로줄 먼저
q.append(index[1])

visit=[[0]*N[1] for i in range(N[0])] #0이면 방문 x

out=[[-1]*N[1] for i in range(N[0])] #출력값
xx=[0,1,0,-1]
yy=[1,0,-1,0]

out[index[1]][index[0]]=0 #2의 값 0값

while q:   
    a=q.pop(0)
    b=q.pop(0)
    visit[b][a]=1
    
    for i in range(4): 
        x=a+xx[i] #하
        y=b+yy[i]
        
        if (0<=x<N[0])and (0<=y<N[1]): 
            if visit[y][x]==0 and m[y][x]==1:
                
                visit[y][x]=1 #방문 표시
                q.append(x)
                q.append(y)
                if out[b][a]==0:
                    visit[y][x]=0
                    
                out[y][x]=out[b][a]+1

            elif a!=index[0] and b!=index[1] and (m[b][a]==0 or out[b][a]==-1):
                if visit[y][x]==0 and out[y][x]==-1:
                    q.append(x)
                    q.append(y)
                    out[y][x]=-1
for i in range(N[0]):
    for j in range(N[1]):   
        if m[i][j]==0:
            out[i][j]=0
            

for i in range(N[0]):
    for j in range(N[1]):
        #if i!=index[0]+0 and j!=index[1]+1 and i!=index[0]+1 and j!=index[1]+0 and i!=index[0]+0 and j!=index[1]-1 and i!=index[0]-1 and j!=index[1]+0 and out[i][j]==1:    
         #   print(-1,end=' ')
        #else:
            print(out[i][j],end=' ')
    
    print()