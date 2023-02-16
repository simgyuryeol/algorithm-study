n=int(input())
a=list(map(int,input().split()))

for i in range(1,max(a)+1):
    count=True
    for j in a:
        if j%i!=0:
            count=False
            break
    if count:
        print(i)