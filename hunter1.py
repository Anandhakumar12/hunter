a=int(input())
d=list(map(int,input().split()))
li=[]
li1=[]
for i in d:
    if i not in li:
        li.append(i)
    else:
        li1.append(i)
aa=set(li1)
s=list(aa)
print(*s)

