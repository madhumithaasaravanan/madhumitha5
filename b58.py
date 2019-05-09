a=int(input("-->"))
b=int(input("-->"))
l=[]
c=0
for i in range(a):
    num=int(input("-->"))
    l.append(num)
    for x in l:
        if(x==b):
            c=c+1
if(c==0):
    print("no")
else:
    print("yes")
