a=[41,2,3,443,21,24,656]
while a.count(41)>0:
    a.remove(41)
print(a)

b=[]
for i in range (0,len(a)):
    if a[i]!=41:
        b.append(a[i])
print(b)