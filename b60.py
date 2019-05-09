def seriessum(n):
  s=0
  for i in range(1,n+1):
    s+=i*(i+1)/2
  return s
  
n=int(input("enter value"))
print(seriessum(n))
