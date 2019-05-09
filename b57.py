a,b=map(int,input("enter value:").split())
sum=0
z=[int(i) for i in input().split()]
for i in range(0,a):
  if(b==z[i]):
    sum=sum+1
print(sum)
