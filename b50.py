def div(n,m):
    if(n&((1<< m)-1))==0:
        return True
    return False
n=8
m=2
if div(n,m):
    print("yes")
else:
    print("no")
    
