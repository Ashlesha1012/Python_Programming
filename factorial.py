l=[30,30,20,40,10]
n=len(l)
mx=max(l[0],l[1])
smx=min(l[0],l[1])
for i in range(2,n):
    if l[i]>mx:
        smx=mx
        mx=l[i]
    elif l[i]>smx and mx!=l[i]:
        smx=l[i]
    elif mx==smx and smx!=l[i]:
        smx=l[i]

print(str(smx))
