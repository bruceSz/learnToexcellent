a = [23,4,6,8,34,76]

i = len(a)
j=0
while True:
    if i<=0:
        break
    for j in range(1,i):
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
    i -=1

print (a)
    
    
